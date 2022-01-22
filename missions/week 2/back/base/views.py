from django.shortcuts import render, redirect
from .forms import *
from .models import *


# Create your views here.
def base(request):
    return render(request, 'base.html')

# Create your views here.
def main(request):
    if request.method == 'POST':
        return redirect('main_page')
    else:
        malllistForm = MallslistForm
        mlists = MallsList.objects.all()
        context = {
            'malllistForm': malllistForm,
            'mlists': mlists,
        }
        return render(request, 'main.html', context)



# ---------------------------------------------------------------------
def shop(request, id=id):
    malllistForm = MallslistForm
    mlists = MallsList.objects.get(id=id)
    itemlistForm = MallsitemForm
    ilists = MallsItem.objects.filter(id=id)
    context = {
        'malllistForm': malllistForm,
        'mlists': mlists,
        'itemlistForm': itemlistForm,
        'ilists': ilists,
    }

    return render(request, 'shop.html', context)


def item(request, id, num):
    questionform = MallsquestionForm
    question = MallsQuestion.objects.all()
    items = MallsItem.objects.filter(id=id, num=num)
    return render(request, 'item.html', {'context' : items, 'questionform': questionform,'question': question})





def search(request):
    if request.method == 'POST':
        query = request.POST.get('query')

    else:
        query = request.GET['q']

    item_name_search = MallsItem.objects.filter(name__contains =query)
    item_d_search = MallsItem.objects.filter(description__contains =query)
    item_search = item_name_search.union(item_d_search, all=True)
    return render(request, 'search.html', {'query' : query, 'item_search': item_search} )
