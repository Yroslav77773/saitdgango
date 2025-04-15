"""
URL configuration for test_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from . import viewscar

urlpatterns = [
    path('', views.car_list, name='car_list'),  # Главная страница (список автомобилей)
    path('login_choice/', views.login_choice, name='login_choice'),  # Страница выбора
    path('login/', views.login_view, name='login'),  # Страница входа
    path('signup/', views.signup, name='signup'),  # Страница регистрации
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('car_reviews/', views.car_review_list, name='car_reviews'),
    path('admin/', admin.site.urls),

]



