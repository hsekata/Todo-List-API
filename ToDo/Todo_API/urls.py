from django.urls import path, include
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns=[
    # path('get_token/', obtain_auth_token),
    path('todos', CreateToDo.as_view()),
    path('register', RegisterUser.as_view()),
    path('login', LoginUser),
    path('todos/<int:pk>/',GetToDos.as_view()),
    # path('todos/', todos_list, name='todos_list'),
    # path('api/token/', TokenGenerator.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]