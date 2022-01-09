from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,DetailView
# Create your views here.
from .models import Product,Question,Answer
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from product.forms import ProductSearchForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import QuestionForm,AnswerForm
from django.contrib import messages

class ProductList(ListView):
    # 한 화면당 4개로 pagination
    model = Product
    paginate_by = 4
    queryset = Product.objects.all()



class ProductDetail(DetailView):
    model = Product


class SearchFormView(FormView):
    form_class = ProductSearchForm
    template_name= 'product/product_list.html'

    # POST 요청의 search_word 파라미터 값을 추출하여 schWord 변수에 지정, search_wrod 파라미터는 ProductSearchForm 클래스에서 정의한 id
    def form_valid(self,form):
        schWord = "%s" %self.request.POST['search_word']
        # icontains = 대소문 구분안하고 조사, distinct() 중복 제거
        post_list = Product.objects.filter(Q(name__icontains=schWord)|Q(description__icontains=schWord)).distinct()
        context ={}
        context['form'] = form
        context['search_term'] = schWord
        context['object_list']= post_list
        return render(self.request,self.template_name,context)


def question_detail(request,question_id,*args,**kwargs):
    """
    question 상세 출력
    """
    question = get_object_or_404(Question, pk = question_id)
    context = {'question':question}
    return render(request,'product/question_detail.html',context)

@login_required(login_url = 'account:login')
def question_create(request,product_id):
    """
     질문등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            product = Product.objects.get(pk=product_id)
            question = form.save(commit= False)
            question.author = request.user
            question.product = product
            question.save()
            return redirect('product:detail',product_id)
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request,'product/question_form.html',context)


@login_required(login_url = 'common:url')
def question_modify(request,question_id):
    """
    질문 수정

    """
    question = get_object_or_404(Question,pk = question_id)
    print(question)
    if request.user != question.author:
        messages.error(request,'수정권한이 없습니다.')
        return redirect('product:detail',question.product.id)
    
    if request.method == "POST":
        form = QuestionForm(request.POST,instance= question)
        if form.is_valid():
            question = form.save(commit = False)
            question.save()
            return redirect('product:detail',question.product.id)
        
    else:
        form = QuestionForm(instance = question)
    context = {'form': form}
    return render(request,'product/question_form.html',context)

@login_required(login_url='common:login')
def question_delete(request, question_id):
    """
    질문삭제
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('product:detail', question.product.id)
    question.delete()
    return redirect('product:index')



def answer_detail(request,answer_id,*args,**kwargs):
    """
    answer 상세 출력
    """
    answer = get_object_or_404(Answer, pk = answer_id)
    context = {'answer':answer}
    return render(request,'product/answer_detail.html',context)

@login_required(login_url = 'account:login')
def answer_create(request,question_id):
    """
     답변등록
    """
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            question = Question.objects.get(pk=question_id)
            answer = form.save(commit= False)
            answer.author = request.user
            answer.question = question
            answer.save()
            return redirect('product:question_detail',question_id)
    else:
        form = AnswerForm()
    context = {'form': form}
    return render(request,'product/answer_form.html',context)


@login_required(login_url = 'common:url')
def answer_modify(request,answer_id):
    """
    답변 수정

    """
    answer = get_object_or_404(Answer,pk = answer_id)
    if request.user != answer.author:
        messages.error(request,'수정권한이 없습니다.')
        return redirect('product:detail',answer.question.id)
    
    if request.method == "POST":
        form = AnswerForm(request.POST,instance= answer)
        if form.is_valid():
           
            answer = form.save(commit = False)
            answer.save()
            return redirect('product:detail',answer.question.product.id)
        
    else:
        form = AnswerForm(instance = answer)
    context = {'form': form}
    return render(request,'product/answer_form.html',context)

@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    """
    답변삭제
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('product:detail', answer.product.id)
    answer.delete()
    return redirect('product:question_detail',answer.question.id)