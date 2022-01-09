from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import FormView
from django.views.generic import DetailView, ListView
from .forms import RegisterForm, LoginForm
from .models import Product
from django.core.paginator import Paginator
from django.db.models import Q

def index(request):
	page = request.GET.get('page','1')
	kw = request.GET.get('kw','')

	product_list = Product.objects.order_by('-add_date')
	if kw:
		product_list = product_list.filter(
			Q(subject__icontains=kw) | Q(content__icontains=kw)
		).distinct()

	paginator = Paginator(product_list, 3)
	page_obj = paginator.get_page(page)
	context = {'product_list' : page_obj, 'page' : page, 'kw' : kw}
	return render(request, 'index.html', context)

def detail(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	context = {'detail':detail}
	return render(request, 'product_detail.html', context)


class RegisterView(FormView):
	template_name = 'register.html'
	form_class = RegisterForm
	success_url = '/'


class LoginView(FormView):
	template_name = 'login.html'
	form_class = LoginForm
	success_url = '/'

	def form_valid(self, form):
		self.request.session['user'] = form.email
		return super().form_valid(form)

class ProductListView(ListView):
	model = Product
	template_name = 'index.html'
	form_class = RegisterForm
	success_url = '/'

class ProductDetailView(DetailView):
	template_name = 'product_detail.html'
	queryset = Product.objects.all()
	context_object_name = 'product'

