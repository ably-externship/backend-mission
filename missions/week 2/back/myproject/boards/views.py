from django.shortcuts import render, redirect

# Create your views here.
from .forms import *
from .models import *


def board(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        writer = request.POST["writer"]

        board = Board(
            title=title,
            content=content,
            writer=writer,
        )
        board.save()
        return redirect("detail")
    else:
        boardForm = BoardForm
        board = Board.objects.all()
        context = {
            "boardForm": boardForm,
            "board": board,
        }
        return render(request, "detail.html", context)
