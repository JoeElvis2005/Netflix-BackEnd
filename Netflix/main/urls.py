from django.urls import path
from .views import * 

urlpatterns=[
    path('',home,name='home'),
    path('netflixlogin/',login, name='login'),
    path('movies/',movie,name="movies"),
    path('addmovie/',add_movie,name="add_movie"),
    path('payment/',payment,name="subscription"),
]