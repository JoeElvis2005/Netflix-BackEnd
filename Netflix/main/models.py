from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='media/images/',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural="Categories"

class Package(models.Model):
    name=models.TextField()
    description=models.TextField()

    def __str__(self):
        return self.name        
    

class Movie(models.Model):
    MOVIE=1
    SERIES=2
    TRAILER=3
    SPECIALISATION_CHOICES=(
        (MOVIE,"Movies"),
        (SERIES,"Series"),
        (TRAILER,"Trailers"),
    )

    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='media/images/',null=True,blank=True)
    descriptions=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True, null=True)
    source=models.TextField()
    category=models.ForeignKey(Category, on_delete=models.SET_NULL , null=True)
    specification=models.IntegerField(choices=SPECIALISATION_CHOICES, default=MOVIE)

    def __str__(self):
        return self.title

class UserModel(models.Model):
    first_name= models.CharField(max_length=30)
    last_name= models.CharField(max_length=30)
    age= models.IntegerField()
    profile_image= models.ImageField( null=True,blank=True )
    email= models.EmailField()
    phone_number=models.CharField(max_length=12)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Settings(models.Model):
    cover_url= models.TextField()
    cover_description= models.TextField()
    cover_title = models.CharField(max_length=100)

    def __str__(self):
        return "Settings"
    class Meta:
        verbose_name_plural="Settings"

class Payment(models.Model):
    
    PHONENUMBER=1
    VISACARD=2
    PAYPAL=3
    VENMO=4

    PAYMENT_CATEGORIES=(
        (PHONENUMBER,"Phone number"),
        (VISACARD,"Visa Card"),
        (PAYPAL,"Paypal"),
        (VENMO,"Venmo"),
    )
    
    user=models.ForeignKey(UserModel,on_delete=models.SET_NULL , null=True)  
    payed_via=models.IntegerField(choices=PAYMENT_CATEGORIES, default=PHONENUMBER)
    amount=models.FloatField()
    payed_at=models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return "Payment Option"

class UserMovie(models.Model):
    MYLIST=1
    DOWNLOADS=2
    INTERESTEDIN=3

    SPECIFICATION_CATEGORY=(
        (MYLIST,"My list"),
        (DOWNLOADS,"Downloads"),
        (INTERESTEDIN,"Intrested In"),
    )

    user=models.ForeignKey(UserModel,on_delete=models.SET_NULL, null= True)
    movie=models.ForeignKey(Movie,on_delete=models.SET_NULL,null=True)
    specification=models.IntegerField(choices=SPECIFICATION_CATEGORY,default=INTERESTEDIN)

    def __str__(self):
        return self.specification

class Notification(models.Model):
    notif_title=models.TextField()
    notification=models.TextField()
    created_at=models.DateTimeField()

    def __str__(self):
        return "Notification"



        




