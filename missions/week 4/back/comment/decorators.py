from django.http import HttpResponseForbidden

from comment.models import Comment


def comment_owner(func):
    def decorated(request, *args, **kwargs):
        comment = Comment.objects.get(pk=kwargs['pk'])
        if not comment.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated
