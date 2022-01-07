from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from comment.forms import CommentCreationForm
from comment.models import Comment
from product.models import Product


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'comment/create.html'

    def form_vaile(self, form):
        temp_comment = form.save(commit=False)
        temp_comment.product = Product.objects.get(pk=self.request.POST['product_pk'])
        temp_comment.writer = self.request.user
        temp_comment.save()
        return super().form_valid(form)


    def get_success_url(self):
        return reverse('product:detail', kwargs={'pk': self.object.article.pk})

