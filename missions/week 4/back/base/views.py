from django.shortcuts import render

# Create your views here.
from django.views import View


class CustomHandler404(View):
    def get(self, request):
        return render(request, 'error/404.html')

class CustomHandler500(View):
    def get(self, request):
        return render(request, 'error/500.html')
