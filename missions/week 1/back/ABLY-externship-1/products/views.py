from django.http import request
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import redirect, render
from .forms import QuestionLoadForm, QuestionSaveForm, CommentForm
from .models import MainCategory, SubCategory, Merchandise


# Create your views here.


class MerchandiseALL(ListView):
    
    model = Merchandise
    template_name = 'core/home.html'
    context_object_name = 'merchandises'
    paginate_by = 8
    merchandise_list = Merchandise.objects.all()
    user = None
    
    def __init__(self, **kwargs):
        try:
            self.user = self.request.user
        except:
            pass
        super().__init__(**kwargs)
    
    def get_queryset(self):
        if self.request.method == 'GET':
            q = self.request.GET.get('search', '')
            self.merchandise_list = Merchandise.objects.filter(name__icontains=q)
        return self.merchandise_list


class MerchandiseDetail(DetailView):
    
    model = Merchandise
    template_name = 'products/merchandise_detail.html'
    context_object_name = 'merchandise'
    user = None
    
    def __init__(self, **kwargs):
        try:
            self.user = request.user
        except:
            pass
        super().__init__(**kwargs)
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context['user'] = self.user
        return self.render_to_response(context)


class QuestionNew(View):
    
    def get(self, request, *args, **kwargs):
        
        if not request.user:
            pk = request.GET.get('merchandise')
            return redirect(f'/products/detail/{pk}')
        
        form = QuestionLoadForm()
        
        context = {
            'form': form
        }
        return render(request, 'products/question_new.html', context)
    
    def post(self, request, *args, **kwargs):
        form = QuestionSaveForm(request.POST)
        form.data = form.data.copy()
        user = request.user
        merchandise = request.GET.get('merchandise')
        form.data['user'] = user
        form.data['merchandise'] = merchandise
        
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return redirect(f'/products/detail/{merchandise}')
