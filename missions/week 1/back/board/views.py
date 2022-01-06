from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'board/board_list.html')

def detail(request, board_id):
    context = {'board': board_id}
    return render(request, 'board/board_detail.html', context)


