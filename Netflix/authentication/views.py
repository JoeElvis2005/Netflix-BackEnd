from django.shortcuts import render,redirect #redirect allows moving to another page
from django.http import HttpResponse
# the above allows you to access a page even without a self made page
from .forms import *
from django.contrib.auth import authenticate,login
# the above are neccessary when authenticating thus are imported
# these are functions used in authentication


# Create your views here.

def sign_up(request):

    form=SignUpForm()


    if (request.method=="POST"):
        form=SignUpForm(request.POST)
        # the request.post parameter saves the data given by the user and holds it as cache
        if form.is_valid():
            form.save()
            raw_username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # the above .cleaned_data allows you to take specific data from a specific field of a form(changes data into a dict)

            # Now for the authentication with a authenticate function that we will call the proccess is as below

            user_valid = authenticate(username=raw_username , password=raw_password)
            # the above function authenticate goes to your usermodel by default and cross refrences if you are valid plus password
            # the password= and username= are constant names used as aunthenicate arguments.
            login(request,user_valid)
            # the login function is called to take in the validated variable as an argument and give it access thus the request parameter...
            # It opens the page specified at the end of the view at return

            # it now redirects you to the right page
             
            redirect("movies") 
            #it takes in the name of the url that accesses a view to open the template or u can use the path

    context={
        "signup_form":form
    }

    return render(request,"signup.html",context)
