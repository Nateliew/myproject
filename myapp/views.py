from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Feature
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def index(request):
    # feature1 = Feature()
    # feature1.id = 0 
    # feature1.name = 'Fast'
    # feature1.details = 'Our service is quick'

    # feature2 = Feature()
    # feature2.id = 1
    # feature2.name = 'Cheap'
    # feature2.details = 'Our service is cheap'

    # feature3 = Feature()
    # feature3.id = 3
    # feature3.name = 'omg'
    # feature3.details = 'Our service is cheap'

    features = Feature.objects.all()


    # features = [feature1, feature2, feature3]
    return render(request, 'index.html', {'features': features})


def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password, password2=password2)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passord not the same')
            return redirect('register')
        
    return render(request, 'register.html')


def login(request):
    if request.method == "POST":
        username = request.POST('username')
        password = request.POST('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials invalid')
            return redirect('login')
    
    else: 
        return render(request, 'login.html')
    return render(request, 'login')
