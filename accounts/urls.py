from rest_framework_simplejwt.views import TokenRefreshView
from accounts.views import (
    LoginView, ListAccountsView, LogoutView, RegisterView,)
from django.urls import path


urlpatterns = [
    path('api/token/', LoginView.as_view(), name='access-token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh-token'),
    path('api/users/', ListAccountsView.as_view(), name='users'),
    path('api/register/', RegisterView.as_view(), name='registeration'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
]
