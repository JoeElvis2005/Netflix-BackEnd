from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    # first_name=forms.CharField(max_length=30 , required=True),
    # second_name=forms.CharField(max_length=30,required=True)
    # email=forms.EmailField(max_length=254, required=True)

    class Meta:
        model=User
        # fields='__all__'
        fields=('username','first_name','email','last_name','password1','password2',)

            # The meta class fields var is the one that holds the fields to be shown to the user if the form is displayed.
            # Therefore this includes the ones you made up using  yourself.
