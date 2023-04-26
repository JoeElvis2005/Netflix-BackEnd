from django.shortcuts import render
from main.models import *
from main.forms import *
from django.contrib.auth.models import User



# Create your views here.

def dashboard(request):
    return render(request,"dashboard.html")
def home(request):

# this view is too count the number of rows in each table
    movies=Movie.objects.all().order_by('-created_at')
    categories=Category.objects.all().order_by('-created_at')
    users=User.objects.all().order_by('-date_joined')

    # the order by allows you to add a field in which you want to order a certain objects
    # EG If you were to loop movies it would print according to date created
    # If u add - it starts form down to up
    # its like the order by in your phine that allows you to to arrange your files according to alphabetical 0r numbers
    # After it arranges if u slice it uses the order of the field you add but if u do not use order by and slice u get according to id
    context={
        "movies":movies,
        "users": users,
        "categories":categories
    }


    return render(request,"home.html",context)
def movielist(request):
    movies=Movie.objects.all()
    context={
        "movies":movies,
    }
    return render(request,"movielist.html",context)

def moviedetails(request,movie_id):
    # The parameteR movie_id recieves the argument via the sent url 
    # The id passed as the functions parameter will be the movie selected id so it can be used to get the details.
    selected_movie=Movie.objects.filter(id=movie_id).first()
    # the var selected_movie now holds the fmovie being searched for after being filtered via the recieved id
    context = {
        "selected_movie":selected_movie
    }
    return render(request,"moviedetails.html",context)# this line of code then sends the functions answer to the template
  
def categorylist(request):
    categories=Category.objects.all()

    context={
        "category":categories
    }
    
    return render(request,"categorylist.html",context)

def adminsettings(request):

    return render(request,"settings.html",)

def userlist(request):
    return render(request,"userlist.html")