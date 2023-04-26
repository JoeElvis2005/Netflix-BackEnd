from django import forms
from .models import *

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields='__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model=UserModel
        fields='__all__'

class PaymentForm(forms.ModelForm):
    class Meta:
        model=Payment
        fields=("payed_via","amount")

class MethodForm(forms.ModelForm):
    class Meta:
        model=UserModel
        fields=("phone_number",)    

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'

