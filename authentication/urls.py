from django.contrib import admin
from django.urls import path, include

from authentication import views

urlpatterns = [

    # path('login/', views.login.as_view(), name='loginUser'), #Considerando que el login es una CLASE
    path('login/', views.loginUser, name='loginUser'),
    # path('register/', views.createUser.as_view(), name='registerUser'), #Considerando que el login es una CLASE
    path('register/', views.createUser, name='registerUser'),
    path('home/', views.home, name='home'),
]
