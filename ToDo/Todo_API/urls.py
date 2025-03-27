from django.urls import path, include
from .views import *

urlpatterns=[
    
    path('todos', ListCreateToDo.as_view()),
    path('register', RegisterUser.as_view()),
    path('login', LoginUser),
    path('todos/<int:pk>/',GetToDos.as_view()),
    
]