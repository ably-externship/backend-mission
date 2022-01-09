from django.db import models


class Help(models.Model):
    title = models.CharField(max_length=64, verbose_name="제목")
    contents = models.TextField(verbose_name="내용")
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name="등록 시간")
    writer = models.ForeignKey('users.Users', verbose_name="작성자", on_delete=models.CASCADE)

    class Meta:
        db_table = 'help'
        app_label = 'api.help'
        verbose_name = "게시물"
        verbose_name_plural = "게시물"

    def __str__(self):
        return self.title