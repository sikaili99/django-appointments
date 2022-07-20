from rest_framework_simplejwt.views import TokenRefreshView
from accounts.views import (
    LoginView, ListAccountsView, LogoutView, RegisterView,)
from django.urls import path


urlpatterns = [
    path('api/token/', LoginView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/users/', ListAccountsView.as_view()),
    path('api/register/', RegisterView.as_view()),
    path('api/logout/', LogoutView.as_view()),
]
