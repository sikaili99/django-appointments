from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework import generics, views
from accounts.models import User
from accounts.serializers import (
    Accountserializer,
    CustomTokenObtainPairSerializer,
    RefreshTokenSerializer,
    RegisterSerializer,)


class ListAccountsView(views.APIView):

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            users = User.objects.all()
            serializer = Accountserializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "success", "error": "You have not been authorized accesss"}, status=status.HTTP_200_OK)


class LoginView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = CustomTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        
        return super().create(request, *args, **kwargs)

class LogoutView(generics.GenericAPIView):
    serializer_class = RefreshTokenSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request, *args):
        sz = self.get_serializer(data=request.data)
        sz.is_valid(raise_exception=True)
        sz.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
