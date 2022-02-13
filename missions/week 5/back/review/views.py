from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Review, ReviewBot
from shop.models import Product, Category, Inventory
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .classifier import mespredict
from .repeat import is_reapeated
from django.contrib import messages


@login_required(login_url='login')
def review_list(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    categories = Category.objects.all()
    inventories = Inventory.objects.filter(product=product.id)

    # 상품 문의 페이지네이터
    page = request.GET.get('page')
    reviews = Review.objects.filter(product=product.id)
    paginator = Paginator(reviews, 7)
    page_obj = paginator.get_page(page)

    context = {'product': product, 'categories': categories,
               'reviews': reviews, 'inventories': inventories,
               'page_obj': page_obj}
    return render(request, 'review/list.html', context)


# 리뷰 등록 -------
@login_required(login_url='login')
def review_create(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {'product': product}
    if request.method == 'POST':
        comment = request.POST['body']
        predict = mespredict(comment)
        repeated = is_reapeated(comment)
        if predict == 0 and repeated == False:
            current_user = request.user
            title = request.POST['title']
            Review.objects.create(user_id=current_user.id,
                                    product_id=product_id,
                                    title=title,
                                    comment=comment,
                                    violation=False,
                                    )
            return redirect(reverse('review:review_list', kwargs={'product_id':product.id}))
        else:
            current_user = request.user
            title = request.POST['title']
            Review.objects.create(user_id=current_user.id,
                                    product_id=product_id,
                                    title=title,
                                    comment=comment,
                                    violation=True,
                                    )
            messages.warning(request, "해당 리뷰는 리뷰봇에 의해 필터링될 수 있습니다.")
            return redirect(reverse('review:review_list', kwargs={'product_id': product.id}))
    return render(request, 'review/create.html', context)


# 리뷰 디테일 -------
@login_required(login_url='login')
def review_detail(request, review_id):
    current_user = request.user
    bot_status = ReviewBot.objects.filter(user_id=current_user.id).exists()
    if bot_status == True:
        is_use_bot = ReviewBot.objects.get(user_id=current_user.id).use_bot
    else:
        is_use_bot = False
    review = get_object_or_404(Review, pk=review_id)
    product = get_object_or_404(Product, id=review.product_id)
    context = {'review': review, 'product': product, 'is_use_bot':is_use_bot}
    return render(request, 'review/detail.html', context)


# 리뷰 수정 -------
@login_required(login_url='login')
def review_modify(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    product = get_object_or_404(Product, id=review.product_id)
    context = {'product': product, 'review':review}

    if request.method == 'POST':
            review = get_object_or_404(Review, pk=review_id)
            title = request.POST['title']
            comment = request.POST['body']
            predict = mespredict(comment)
            repeat = is_reapeated(comment)
            if predict == 0 and repeat == False:
                review.user_id=review.user.id
                review.product_id=product.id
                review.title=title
                review.comment=comment
                review.violation = False
                review.save()
                return redirect(reverse('review:review_list', kwargs={'product_id':product.id}))
            else:
                review.user_id=review.user.id
                review.product_id=product.id
                review.title=title
                review.comment=comment
                review.violation = True
                review.save()
                messages.warning(request, "해당 리뷰는 리뷰봇에 의해 필터링될 수 있습니다.")
                return redirect(reverse('review:review_list', kwargs={'product_id':product.id}))
    return render(request, 'review/modify.html', context)



# 리뷰 삭제 -------
def review_delete(request, review_id):
    review = get_object_or_404(Review, pk=review_id)

    if request.user != review.user:
        # messages.warning(request, '삭제 권한이 없습니다.')
        return redirect((request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found')))
    else:
        review.delete()
        return redirect((request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found')))


# 봇 사용 상태 변경 -----
@login_required(login_url='login')
def use_reviewbot(request):
    usebot_exist = ReviewBot.objects.filter(user_id=request.user.id).exists()
    if usebot_exist ==True:
        bot_status = ReviewBot.objects.get(user_id=request.user.id)
    else:
        bot_status = False

    if request.method == 'POST':
        # 봇 사용 처음 등록할 시---
        if usebot_exist == False:
            select = False
            if request.POST['choice'] == "1":
                select = True
            ReviewBot.objects.create(user_id=request.user.id,
                                       use_bot=select
                                     )
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        else:
            reviewbot = ReviewBot.objects.get(user_id=request.user.id)
            if request.POST['choice'] == "1":
                reviewbot.use_bot = True
                reviewbot.save()
                return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
            else:
                reviewbot.use_bot = False
                reviewbot.save()
                return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

    return render(request, 'review/reviewbot.html', {'bot_status':bot_status})




