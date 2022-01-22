from django.shortcuts import render, redirect
from .models import *
from base.forms import *
from django.contrib import messages

# Create your views here.
def qna_page(request):
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
        return redirect('qna_page')
        
    else :   
        questionform = MallsquestionForm
        question = MallsQuestion.objects.all()
        return render(request, 'qna.html', {'questionform': questionform,'question': question})


def qna_page_num(request, num):
    q_num = num
    question_num = MallsQuestion.objects.filter(q_num=q_num)
    question = MallsQuestion.objects.all()

    answer = MallsAnswer.objects.filter(q_num=q_num)
    if answer is not None:
        return render(request, 'board.html', {'question_num': question_num, 'answer':answer, 'question': question})
    return render(request, 'board.html', {'question_num': question_num, 'question': question})