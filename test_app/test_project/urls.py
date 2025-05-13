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
from . import views

urlpatterns = [
    #path('', views.car_review_list1, name='home'),  # Сопоставляет пустой URL с функцией представления home
    #path('car/<int:car_id>/reviews/', views.car_review_list1, name='car_review_list'),
    path('cars/', views.car_list_view, name='car_list'),
    path('delete/<int:car_id>/', views.delete_car, name='delete_car'), # URL для удаления автомобиля
    path('add/', views.add_car, name='add_car'),  # URL для добавления автомобиля
    path('adds/', views.add_reviews, name='add_review'),
    path('reviews/<int:car_id>/', views.car_review_list, name='car_review_list'),
    path('', views.car_list, name='car_list'),  # Главная страница (список автомобилей)
    path('login_choice/', views.login_choice, name='login_choice'),  # Страница выбора
    path('login/', views.login_view, name='login'),  # Страница входа
    path('signup/', views.signup, name='signup'),  # Страница регистрации
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('admin/', admin.site.urls)
]



