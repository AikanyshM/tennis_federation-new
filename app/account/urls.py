from django.urls import path
from .views import DestroyProfileView, RegisterView, ChangePasswordView, UpdateProfileView, LogoutView, LogoutAllView, RetrieveProfileView, AdminCreateAPIView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('admin/create/', AdminCreateAPIView.as_view(), name="admin_create"),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('logout_all/', LogoutAllView.as_view(), name='auth_logout_all'),
    path('delete/<int:pk>/', DestroyProfileView.as_view(), name='delete_profile'),
    path('<int:pk>/', RetrieveProfileView.as_view(), name='retrieve_profile'),


]