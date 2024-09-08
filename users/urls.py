from django.contrib.auth.views import LogoutView
from django.urls import path

from users import views
from users.apps import UsersConfig
from users.views import UserRegisterView, LoginUser, PasswordResetView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginUser.as_view(template_name='users/login.html'), name='login'),
    path('activate/<int:user_id>/<str:email>/', views.activate, name='activate'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
]
