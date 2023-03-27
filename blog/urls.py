from . import views
from django.urls import path
from .views import user_login, register, comment_delete
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('password-change/', PasswordChangeView.as_view(), name='password-change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/<slug:slug>/comment/<int:comment_id>/delete/', views.comment_delete, name='comment_delete')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
