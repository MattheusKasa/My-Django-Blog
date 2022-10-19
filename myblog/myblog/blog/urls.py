from . import views
from django.urls import path
from .views import user_login

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('login/', user_login, name = 'login'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]