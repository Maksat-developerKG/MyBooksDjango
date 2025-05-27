from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),        # Главная страница и статьи
    path('accounts/', include('accounts.urls')),  # Регистрация и вход
]
