from typing import ContextManager
from django.db import models
from accounts.models import AuthUser

# Create your models here.

# class Board(models.Model):
#     title = models.CharField(max_length=64, verbose_name='글 제목')
#     contents = models.TextField(verbose_name='글 내용')
#     writer = models.ForeignKey('accounts.AuthUser', on_delete=models.CASCADE, verbose_name='작성자')
#     write_dt = models.DateTimeField(auto_now_add=True, verbose_name='작성일')

#     board_name = models.CharField(max_length=32)
#     hits = models.PositiveIntegerField(default=0, verbose_name='조회수')

#     def __str__(self):
#         return self.title
    
#     class Meta:
#         db_table = 'board'

class Board(models.Model):
    title = models.CharField(max_length=20, null=True)
    content = models.TextField()
    user = models.ForeignKey('accounts.AuthUser', on_delete=models.DO_NOTHING, null=True)
    class Meta:
        db_table = 'board'