from . import views
from django.urls import path
from .views import user_login, register
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('login/', LoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('register/', register, name = 'register'),
    path('password-change/', PasswordChangeView.as_view(), name = 'password-change'),
    path('password-change/done', PasswordChangeDoneView.as_view(), name = 'password_change_done'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]