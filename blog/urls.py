from . import views
from django.urls import path
from .views import user_login, register
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    #path('login/', user_login, name = 'login'),
    path('login/', LoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('register/', register, name = 'register'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]