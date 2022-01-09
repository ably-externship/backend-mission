from django import forms
from .models import Product
from inquiry.models import Inquiry


class RegisterForm(forms.Form):
    name = forms.CharField(
        error_messages={
            'required': '상품명을 입력해주세요.'
        }, label="상품명", max_length=64)

    price = forms.IntegerField(
        error_messages={
            'required': "상품 가격을 입력해주세요."
        }, label="상품 가격",
    )
    description = forms.CharField(
        error_messages={
            'required': "상품 설명을 입력해주세요."
        }, label="상품 설명"
    )
    quantity = forms.IntegerField(
        error_messages={
            'required': "재고를 입력해주세요."
        }, label="재고"
    )

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        price = cleaned_data.get('price')
        description = cleaned_data.get('description')
        quantity = cleaned_data.get('quantity')

        if not (name and price and description and quantity):
            self.add_error('quantity', '모든 값을 입력해야 합니다.')


class ProductSearchForm(forms.Form):
    kw = forms.CharField(label='keyword')


class InquiryForm(forms.ModelForm):

    class Meta:
        model = Inquiry
        fields = ['content']
