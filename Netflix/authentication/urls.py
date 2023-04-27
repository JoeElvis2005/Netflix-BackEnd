from django.urls import path
from .views import *
# Never forget to import views to connect urls.py with views

urlpatterns=[
    path('signup/',sign_up,name="sign_up"),
    
]