from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from .forms import *
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.
def index(request):
    return render(request, 'index.html')


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



#  로그인 로그아웃 회원가입
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('login_page')
            
        else:
            return render(request, 'login.html', {'error' : 'username or password is incorrect'})
    else:
        return render(request, 'login.html')



def logout(request):
    auth.logout(request)
    return redirect('main_page')



# def signup(request):
#     if request.method == "POST":
#         form = CreateUserForm()
#         if form.is_valid():
#             form.save()
#             username = request.POST.get('username')
#             messages.success(request, f'Hi {username} 가입이 완료되었습니다.')
#             return redirect('login.html')
                
#         else : 
#             return render(request, 'signup.html', {'error' : '가입에 실패하였습니다'})

#     else : 
#         form = CreateUserForm()
#         return render(request, 'signup.html', {'form':form} )




def signup(request):
    if request.method == "POST":
        if request.POST.get("password1") == request.POST.get("password2"):
            user = User.objects.create_user(
                username=request.POST.get("username"), 
                email=request.POST.get("email"),
                password=request.POST.get("password1")
            )
            user.save()

            username=request.POST.get("username")
            auth.login(request, user)
            messages.success(request, f'반갑습니다, {username} 가입이 완료되었습니다.')
            return redirect('login_page')            
        else : 
            return render(request, 'signup.html', {'error' : '가입에 실패하였습니다'})
    return render(request, 'signup.html')


# ---------------------------------------------------------------------
def shops(request, id=id):
    malllistForm = MallslistForm
    mlists = MallsList.objects.get(id=id)
    itemlistForm = MallsitemForm
    ilists = MallsItems.objects.filter(id=id)
    context = {
        'malllistForm': malllistForm,
        'mlists': mlists,
        'itemlistForm': itemlistForm,
        'ilists': ilists,
    }

    return render(request, 'shops.html', context)


def item_page(request, id, num):
    questionform = MallsquestionForm
    question = MallsQuestion.objects.all()
    items = MallsItems.objects.filter(num=num)
    return render(request, 'item.html', {'context' : items, 'questionform': questionform,'question': question})

def search_page(request):
    if request.method == 'POST':
        query = request.POST.get('query')

    else:
        query = request.GET['q']

    item_name_search = MallsItems.objects.filter(name__contains =query)
    item_d_search = MallsItems.objects.filter(description__contains =query)
    item_search = item_name_search.union(item_d_search, all=True)
    return render(request, 'search.html', {'query' : 1, 'item_search': item_search} )


def board_page(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        content = request.POST['content']
        user = request.POST['user']
        date = request.POST['date']
        rep =  request.POST['rep']
        question = MallsQuestion(
            subject=subject,
            content=content,
            date=date,
            rep=rep)
        question.save()
        messages.success(request, f'{subject}등록이 완료되었습니다.')
        return redirect('board_page')
        
    else :   
        questionform = MallsquestionForm
        question = MallsQuestion.objects.all()
        return render(request, 'board.html', {'questionform': questionform,'question': question})


def board_page_num(request, num):
    q_num = num
    question_num = MallsQuestion.objects.filter(q_num=q_num)
    question = MallsQuestion.objects.all()
    return render(request, 'board.html', {'question_num': question_num, 'question': question})