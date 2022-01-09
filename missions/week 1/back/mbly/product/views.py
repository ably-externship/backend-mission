from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
# Create your views here.
from .models import Product
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from product.forms import ProductSearchForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import QuestionForm,AnswerForm


class ProductList(ListView):
    model = Product
    paginate_by = 3
    queryset = Product.objects.all()



class ProductDetail(DetailView):
    model = Product


class SearchFormView(FormView):
    form_class = ProductSearchForm
    template_name= 'blog/post_search.html'

    # POST 요청의 search_word 파라미터 값을 추출하여 schWord 변수에 지정, search_wrod 파라미터는 ProductSearchForm 클래스에서 정의한 id
    def form_valid(self,form):
        schWord = "%s" %self.request.POST['search_word']
        # icontains = 대소문 구분안하고 조사, distinct() 중복 제거
        post_list = Product.objects.filter(Q(title__icontains=schWord)|Q(description__icontains=schWord)|Q(content__icontains=schWord)).distinct()

        context ={}
        context['form'] = form
        context['search_term'] = schWord
        context['object_list']=post_list
        return render(self.request,self.template_name,context)


@login_required(login_url = 'account:login')
def question_create(request,product_id):
    """
     질문등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit= False)
            question.author = request.user
            question.save()
            return redirect('product:detail',product_id= product_id)
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request,'pybo/question_form.html',context)