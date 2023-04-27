from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render (request,"Netflix_home.html")

# def login(request):
#     return render(request,"netflix_login.html")


@login_required #This is a decorator
def movie(request):

   all_categories=Category.objects.all()

   background_playing={
        'source':'<iframe width="560" height="315" src="https://www.youtube.com/embed/SD3dT_kFKBM?controls=0&autoplay=1&mute=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>',
        'title':'BLACK CLOVER',
        'description':'''
              ► For Better Experience watch  HD 1080p<br>
              ► Like, Comment, and Subscribe!<br>
              Black Clover Episode 167 English Subbed<br>
              Black Clover Episode 167 English Subbed<br>
              Black Clover Episode 167 English Subbed<br>
              '''

    }

   context = {
        "title":"Stranger things",
        "background": background_playing,
        "all_categories": all_categories,
    }

   return render(request,"movies.html",context)

def add_movie(request):
    print(f"Request method = {request.method}")
    form=MovieForm()#MovieForm() is the imported form's name
    message=""
    form_valid=False

    if request.method== "POST":
        print(f"FORM DATA {request.POST}")
        form=MovieForm(request.POST) # This parameter is added to allow the user data sent to the views (from the action in the frontend) to be added to the form thus changing the var form in preparation for being added to the dataabse
        print(f"FORM {form}") # This prints out a html form very similar to that when you inspect this html file only that the value is the users values added
        if form.is_valid:
            form.save()
            form_valid=True
            message="Movie created"
        else :
            message = f"Invalid input " 
            form_valid = False

            
    context={
        "movie_form": form,
        "message": message,
        "form_valid": form_valid,

    }
    # The context is needed to display anything in views.py in the frontend

    return render(request,"create_movie.html",context)

def payment(request):
    form=PaymentForm()
    context={
        "Pay":form
    }

    return render(request,"payment.html",context)