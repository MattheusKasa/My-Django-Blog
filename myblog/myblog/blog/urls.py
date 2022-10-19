from . import views
from django.urls import path
from .views import user_login, register

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('login/', user_login, name = 'login'),
    path('register/', register, name = 'register'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]