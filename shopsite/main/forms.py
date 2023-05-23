from django import forms
from .models import Users,Product,Business

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['phone','email','name','account','password']
        widgets = {
            'account':forms.TextInput(attrs = {'class': 'form-control','placeholder': '使用者帳號'}),
            'phone': forms.TextInput(attrs = {'class': 'form-control','placeholder': '手機'}),
            'email': forms.EmailInput(attrs = {'class': 'form-control','placehold': '電子信箱'}),
            'password': forms.PasswordInput(attrs = {'class': 'form-control','placehold': '密碼'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '姓名'})
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'money', 'stock', 'srcset']
        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control','placeholder': '商品標題'}),
            'money':forms.NumberInput(attrs={'class': 'form-control','placeholder': '商品售價'}),
            'stock':forms.TextInput(attrs={'class': 'form-control','placeholder':'庫存數量'}),
            'srcset': forms.TextInput(attrs={'type': "file", 'placeholder': '商品圖片'})
        }

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['buyer', 'seller', 'total_price', 'amount', 'product_id', 'order_number']
        widgets={
            'buyer':forms.TextInput(),
            'seller': forms.TextInput(),
            'amount':forms.NumberInput(),
            'product_id':forms.NumberInput(),
            'total_price':forms.NumberInput(),
            'order_number':forms.TextInput()
        }        