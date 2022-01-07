from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView

from comment.decorators import comment_owner
from comment.forms import CommentCreationForm
from comment.models import Comment
from product.models import Product


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'comment/create.html'

    def form_valid(self, form):
        temp_comment = form.save(commit=False)
        temp_comment.product = Product.objects.get(pk=self.request.POST['product_pk'])
        temp_comment.writer = self.request.user
        temp_comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('product:detail', kwargs={'pk': self.object.product.pk})


@method_decorator(comment_owner, 'get')
@method_decorator(comment_owner, 'post')
class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'comment/delete.html'

    def get_success_url(self):
        return reverse('product:detail', kwargs={'pk': self.object.product.pk})
