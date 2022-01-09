from django.shortcuts import render, redirect
from .models import Item, Quantity, Question
from django.core.paginator import Paginator
# from .models import Post




def index(request):
  if request.method == 'GET':
    # items = Item.objects.all()
    
    p = Paginator(Item.objects.all(),3)
    page = request.GET.get('page')
    print(page)
    items = p.get_page(page)
    

  return render(request, 'mutbly/index.html', {'items' : items})

def show(request, id):
  item = Item.objects.get(id=id)
  item_choices = Quantity.objects.filter(item_id = id)
  item_questions = Question.objects.filter(item_id = id)
  print(item_questions)
  return render(request, 'mutbly/show_item.html', {'item' : item, 'item_choices' : item_choices, 'item_questions' : item_questions})


def search(request) :
  if request.method == "POST":
    searched = request.POST['searched']
    items = Item.objects.filter(name__contains = searched)
    return render(request, 'mutbly/search.html', {'searched': searched, 'items': items})
  else :
    return render(request, 'mutbly/search.html')


class QuestionView:
  def create(request, id):
    content = request.POST['asked']
    Question.objects.create(item_id=id, content=content, author=request.user)
    return redirect(f'/items/{id}')
  
  def delete(request, id, cid):
    question = Question.objects.get(id = cid)
    question.delete()
    return redirect(f'/items/{id}')