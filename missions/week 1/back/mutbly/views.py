from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import FormView
from django.views.generic import DetailView, ListView
from .forms import RegisterForm, LoginForm
from .models import Product

def index(request):
	product_list = Product.objects.order_by('-add_date')
	context = {'product_list' : product_list}
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

