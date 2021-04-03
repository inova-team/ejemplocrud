from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import CreateView
# Create your views here.


def createUser(request):

    if request.POST:
        email = request.POST['email']
        print(type(email))
        name = request.POST['name']
        password =request.POST['password']

        if User.objects.filter(email=email).count() == 0 :
            User.objects.create_user(email=email, first_name=name, password=password, username=email)
            return render(request, 'authentication/login.html')



    return render(request, 'authentication/register.html')


# class CreateUser(CreateView):
#     template_name = 'authentication/register.html'
#     def get_context_data(self, **kwargs):
#         return render()
#
#     def post(self, request, *args, **kwargs):
#         return render()


def loginUser(request):

    if request.POST:
        username = request.POST['email']
        password = request.POST['password']
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            print("SE LOGEO")
            return redirect(home)
        else:
            print("NO SE LOGEO")
            context = {
                    'error' : 'Error al iniciar sesión'
            }
            return render(request, 'authentication/login.html', context)

    context = {

    }

    return render(request, 'authentication/login.html', context)


def home(request):

    context = {
        'user' : request.user
    }

    return render(request, 'home.html',context)