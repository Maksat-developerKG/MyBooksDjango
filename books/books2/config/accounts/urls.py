from django.urls import path 
from .views import register_view, activate_account, login_view, logout_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('activate/<uidb64>/<token>/', activate_account, name='activate'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
