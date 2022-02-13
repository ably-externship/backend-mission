# from board.forms import BoardWriteForm
# from accounts.models import AuthUser
# from .models import Board
# from django.shortcuts import redirect, render
# def board_list(request):
#     return render(request, 'board.html')

# def board_write(request):
#     login_session = request.session.get('login_session','')
#     context = {'login_session':login_session}
#     if request.method =='GET':
#         write_form = BoardWriteForm()
#         print(dir(write_form))
#         context['forms'] = write_form
#         print(dir(context['forms']))
#         return render(request, 'board_write.html', context)
    
#     elif request.method == 'POST':
#         write_form = BoardWriteForm(request.POST)

#         if write_form.is_vaild():
#             writer = AuthUser.objects.get(username = login_session)
#             board = Board(
#                 title = write_form.title,
#                 contents = write_form.contents,
#                 writer = writer,
#                 board_name = write_form.board_name
#             )
#             board.save()
#             return redirect('/board')
#         else:
#             context['forms'] = write_form
#             if write_form.erros:
#                 for value in write_form.errors.values():
#                     context['error'] = value
#             return render(request, 'board_write.html', context)

from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render, redirect

# # Create your views here.
from .forms import *
from .models import *

def board(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        user = request.user
        board = Board(
            title=title,
            content=content,
            user=user,
        )
        board.save()

        return redirect('board')
    else:
        boardForm = BoardForm
        board = Board.objects.all()
        context = {
            'boardForm': boardForm,
            'board': board,
        }
        return render(request, 'board.html', context)

def boardEdit(request, pk):
    board = Board.objects.get(id=pk)
    if request.method == "POST":
        board.title = request.POST['title']
        board.content = request.POST['content']
        board.user = request.user

        board.save()
        return redirect('board')

    else:
        boardForm = BoardForm
        return render(request, 'update.html', {'boardForm':boardForm})

def boardDelete(request, pk):
    board = Board.objects.get(id=pk)
    board.delete()
    return redirect('board')

