from django import forms
from django.forms import widgets
# from .models import Board
# from django_summernote.fields import SummernoteTextField
# from django_summernote.widgets import SummernoteWidget

# class BoardWriteForm(forms.ModelForm):
#     title = forms.CharField(
#         label = '글 제목',
#         widget = forms.TextInput(
#             attrs={
#                 'placeholder': '게시글 제목'
#             }),
#         required=True,
#     )

#     contents = SummernoteTextField()

#     options = (
#         ('상품문의'),
#         ('반품문의'),
#         ('배송문의'),
#         ('기타')
#     )

#     board_name = forms.ChoiceField(
#         label = '선택',
#         widget = forms.Select(),
#         choices = options
#     )

#     field_order = [
#         'title',
#         'board_name',
#         'contents'
#     ]

#     class Meta:
#         model = Board
#         exclude = [
#             'title',
#             'contents',
#             'board_name'
#         ] 
#         widgets = {
#             'contents' : SummernoteWidget()
#         }
    
#     def clean(self):
#         cleaned_data = super().clean()

#         title = cleaned_data.get('title','')
#         contents = cleaned_data.get('contents','')
#         board_name = cleaned_data.get('board_name','')

#         if title =='':
#             self.add_error('title', '글 제목을 입력하세요.')
#         elif contents == '':
#             self.add_error('contents', '글 내용을 입력하세요.')
#         else:
#             self.title = title
#             self.contents = contents
#             self.board_name = board_name

from django.forms import ModelForm
from .models import *

class BoardForm(ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'content']

