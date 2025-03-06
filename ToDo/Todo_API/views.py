from rest_framework import mixins, generics, response
from rest_framework.decorators import api_view
from .models import ToDos,UserToDo
from rest_framework.permissions import IsAuthenticated
from .serializers import RegistrationUserSerializer, ToDoSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
from rest_framework_simplejwt.tokens import RefreshToken

# class ToDo(mixins.ListModelMixin,
# mixins.RetrieveModelMixin, 
# mixins.DestroyModelMixin,
# mixins.CreateModelMixin,
# mixins.UpdateModelMixin,
# generics.GenericAPIView

# ):
#     serializer_class = ""
#     queryset = ""
#     def get(self, request, id=None):
#         if id:
#             return self.get(request, id)
#         return list(request)

#     def delete(self, request, id):
#         return self.destroy(request, id)

#     def put(self, request, id):
#         return self.update(request, id)
#     def patch(self, request, id):
#         return self.partial_update(request, id)
        
class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'limit'

class CreateToDo(generics.ListCreateAPIView):
    
    permission_classes = [IsAuthenticated]
    
    serializer_class = ToDoSerializer
    queryset = ToDos.objects.all()
    def create(self, request,*args, **kwargs):
        usr = request.user
     
        user_todo = get_object_or_404(UserToDo, email=usr)
        request.data['UserToDo'] = user_todo.id  
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response_data = serializer.data
        response_data.pop("UserToDo", None)
        headers = self.get_success_headers(serializer.data)
        return response.Response(response_data, status=201, headers=headers)
    def list(self, request,*args, **kwargs):

        # permission_classes = [IsAuthenticated]
        todos = ToDos.objects.all()
        paginator = CustomPageNumberPagination()
        result_page = paginator.paginate_queryset(todos, request)
        print(f"result page {result_page}")
        serializer = ToDoSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class RegisterUser(generics.CreateAPIView):
    serializer_class = RegistrationUserSerializer
    queryset = UserToDo.objects.all()

    def create(self,request, *args, **kwargs):
        data = request.data
        
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return  response.Response({"mssg":"registration success"})

        return response.Response({"mssg:User exists"}, status=400)
class GetToDos(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ToDoSerializer
    queryset = ToDos.objects.all()




@api_view(['POST'])
def LoginUser(request):
    data = request.data
    print(f"data {data}")
    email = data['email']
    password = data['password']

    user = authenticate(request, email=email, password=password)

    if user:
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return response.Response({
            "message": "Login successful",
            "access_token": access_token,
            "refresh_token": str(refresh)
        })
    
    return response.Response({"error": "Invalid credentials"}, status=401)
# @api_view(['GET'])
# def todos_list(request):

