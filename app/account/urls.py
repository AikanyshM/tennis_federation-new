from django.urls import path, include
from .views import RegisterView, ChangePasswordView, LogoutView, LogoutAllView, UserProfile, AdminUserCreateAPIView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('create-admin/', AdminUserCreateAPIView.as_view()),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('logout_all/', LogoutAllView.as_view(), name='auth_logout_all'),
    path('profile/<int:pk>/', UserProfile.as_view(), name='profile'),

]