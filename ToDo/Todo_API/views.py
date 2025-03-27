from rest_framework import generics, response, status
from rest_framework.decorators import api_view, permission_classes
from .models import ToDos, UserToDo
from .serializers import RegistrationUserSerializer, ToDoSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken


class ListCreateToDo(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ToDoSerializer

    def get_queryset(self):
        return ToDos.objects.filter(usertodo=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usertodo=self.request.user)

class RegisterUser(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegistrationUserSerializer
    queryset = UserToDo.objects.all()
class GetToDos(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ToDoSerializer

    def get_queryset(self):
        return ToDos.objects.filter(usertodo=self.request.user)

class ListTodos(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ToDoSerializer

    def get_queryset(self):
        return ToDos.objects.filter(usertodo=self.request.user)

@api_view(['POST'])
@permission_classes([AllowAny])
def LoginUser(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    if not email or not password:
        return response.Response(
            {"error": "Both email and password are required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        user = UserToDo.objects.get(email=email)
        if user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return response.Response({
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            })
        return response.Response(
            {"error": "Invalid credentials"},
            status=status.HTTP_401_UNAUTHORIZED
        )
    except UserToDo.DoesNotExist:
        return response.Response(
            {"error": "User not found"},
            status=status.HTTP_404_NOT_FOUND
        )