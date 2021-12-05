from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User


def gallery(request):
    #selecting what photos to show based on category
    category=request.GET.get('category')
    if category==None:
        photos = Photo.objects.all()
    else :
        photos = Photo.objects.filter(category__name=category)    

    categories = Category.objects.all()

    context = {'categories': categories, 'photos': photos}
    return render(request, 'photos/gallery.html', context)

def viewPhoto(request, pk):
    photo = Photo.objects.get(id = pk)
    return render(request, 'photos/photo.html', {'photo': photo})

def addPhoto(request):
    categories = Category.objects.all()

    if request.method == "POST":
        data=request.POST
        image = request.FILES.get('image')
     #setting the category value  
        #if selected a category
        if data['category'] !='none' :
            category= Category.objects.get(id=data['category'])
        #if selected category new, then creating a new category and giving it the name     
        elif data['category_new'] !='': 
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else : #when theres no specific cat
            category= None    

        # creating photo
        photo = Photo.objects.create(
            category= category,
            description= data['description'] ,
            image=image,
        )

        return redirect('gallery')  #redirecting to gallery page after uploading photo  

    context = {'categories': categories}
    return render(request, 'photos/add.html',context)

def aboutUs(request):
    return render(request, 'photos/aboutUs.html')

def sign(request):
    return render(request, 'photos/sign.html')

@csrf_exempt
def signsub(request):
    
    if request.method == 'POST':
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')
        user = authenticate(request,username=username1, password=password1)
        if user :
            login(request, user)
            return redirect('gallery')      
        else:  
            messages.info(request, 'Your password or username is incorrect')
            return redirect('sign')
    else:
        return render(request, 'photos/gallery.html', {})

@csrf_exempt
def registersub(request):
    if request.method=='POST':
        username1=request.POST.get("username")
        mail=request.POST.get("email")
        password1=request.POST.get("password")
        obj=User.objects.create_user(username=username1,email=mail,password=password1)
        obj.save()
        user = authenticate(request,username=username1, password=password1)
        login(request, user)
        
    return redirect('gallery') 

def register(request):
    return render(request, 'photos/register.html')


@csrf_exempt
def feedbacksub(request):
    if request.method=='POST':
        fname=request.POST.get("firstName")
        lname=request.POST.get("lastName")
        num=request.POST.get("phone")
        mail=request.POST.get("email")
        message=request.POST.get("message")
        obj=Feedback(First_Name=fname,Last_Name=lname,Phone_Number=num,Email=mail,Help=message)
        obj.save()
        
    return redirect('gallery') 

def feedback(request):
    return render(request, 'photos/feedback.html')  

def logout_view(request):
    logout(request)
    return redirect ("gallery")


