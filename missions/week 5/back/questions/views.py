from django import forms
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Question
from products.models import Product


def question(request, object_id):
    obj = get_object_or_404(Product, pk=object_id)

    class QuestionForm(forms.ModelForm):
        class Meta:
            model = Question
            fields = ['title', 'private', 'content']
            labels = {
                'title': '제목',
                'private': '비밀글',
                'content': '문의 내용'
            }

    return render(request, 'questions/question.html', {
        'obj': obj,
        'form': QuestionForm()
    })


def question_submit(request, object_id):
    product = get_object_or_404(Product, pk=object_id)
    title = request.POST['title']
    content = request.POST['content']
    product_question = Question(content_type=ContentType.objects.get_for_model(product), object_id=object_id,
                                user=request.user, title=title, content=content)
    product_question.save()
    return render(request, 'questions/question_submit.html', {
        'product': product,
        'question': product_question
    })
