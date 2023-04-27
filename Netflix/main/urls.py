from django.urls import path
from .views import * 

urlpatterns=[
    path('',home,name='home'),
    # path('netflixlogin/',login, name='login'),
    path('movies/',movie,name="movies"),
    path('addmovie/',add_movie,name="add_movie"),
    path('payment/',payment,name="subscription"),
    # the anme of a path can be used anywhere in the project to access this view unlike context that takes only to specified html in view
]