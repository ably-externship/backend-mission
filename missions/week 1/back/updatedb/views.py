from django.shortcuts import render

# Create your views here.
def updatedb(request):
    return render(request, 'updatedb.html')