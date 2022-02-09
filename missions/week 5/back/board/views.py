from django.shortcuts import render, redirect

# Create your views here.
from board.forms import BoardCreateForm
from board.models import Board


def index(request):
    board_list = Board.objects.all()
    context={'board_list': board_list}
    return render(request, 'board/board_list.html', context)

def detail(request, board_id):
    context = {'board': board_id}
    return render(request, 'board/board_detail.html', context)


def write(request):
    if request.method == 'POST':
        form = BoardCreateForm(request.POST)
        if form.is_valid():
            cleand_data = form.clean()
            Board.objects.create(type=cleand_data['type'], title=cleand_data['title'], content=cleand_data['content'])
            return redirect('/board/')
    return render(request, 'board/board_write.html', {'form' : BoardCreateForm})