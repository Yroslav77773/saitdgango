from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Car, CarReview
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CarForm



# Функция для отображения списка автомобилей
def car_list(request):  # Получает HTTP-запрос
    cars = Car.objects.all()  # Получает все объекты Car из базы данных
    context = {'cars': cars}  # Создаёт словарь данных для передачи в шаблон
    return render(request, 'car_list.html', context)  # Отображает шаблон car_list.html с данными

# Функция для отображения страницы выбора способа входа (Войти или Зарегистрироваться)
def login_choice(request): #Получает HTTP-запрос
    return render(request, 'login_choice.html')  # Отображает страницу выбора (login_choice.html)

# Функция для обработки входа пользователя
def login_view(request):  # Получает HTTP-запрос
    if request.method == 'POST':  # Если это отправка формы (POST-запрос)
        form = AuthenticationForm(request, data=request.POST)  # Создаёт форму с данными из запроса
        if form.is_valid():  # Если форма заполнена правильно
            user = form.get_user()  # Получает объект пользователя из формы
            auth_login(request, user)  # Выполняет вход пользователя
            return redirect('car_list')  # Перенаправляет на страницу car_list
        else:  # Если форма заполнена с ошибками
            return render(request, 'login.html', {'form': form})  # Отображает форму входа с ошибками
    else:  # Если это просто запрос страницы (GET-запрос)
        form = AuthenticationForm()  # Создаёт пустую форму
        return render(request, 'login.html', {'form': form})  # Отображает пустую форму входа

# Функция для обработки регистрации пользователя
def signup(request):  # Получает HTTP-запрос
     if request.method == 'POST':  # Если это отправка формы (POST-запрос)
        form = UserCreationForm(request.POST)  # Создаёт форму с данными из запроса
        if form.is_valid():  # Если форма заполнена правильно
            user = form.save()  # Создаёт нового пользователя в базе данных
            auth_login(request, user)  # Выполняет вход пользователя
            return redirect('car_list')  # Перенаправляет на страницу car_list
        else:  # Если форма заполнена с ошибками
           return render(request, "signup.html", {  # Отображает форму регистрации с ошибками
                "form": form,  # Передаёт форму в шаблон
                "title": "Sign Up",  # Передаёт заголовок в шаблон
                "errors": form.errors,  # Передаёт ошибки в шаблон
            })
     else:  # Если это просто запрос страницы (GET-запрос)
        return render(request, "signup.html", {  # Отображает пустую форму регистрации
            "form": UserCreationForm(),  # Создаёт пустую форму
            "title": "Sign Up",  # Передаёт заголовок в шаблон
        })

# Функция для обработки выхода пользователя
def logout_view(request):  # Получает HTTP-запрос
    auth_logout(request)  # Выполняет выход пользователя
    return redirect('car_list')  # Перенаправляет на страницу car_list

# Функция для отображения профиля пользователя
def profile(request):  # Получает HTTP-запрос
    return render(request, 'profile.html')  # Отображает шаблон profile.html

# Функция для отображения списка отзывов
def car_review_list(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    review = CarReview.objects.filter(car=car).first()  # Получаем только ОДИН отзыв
    context = {'review': review, 'car': car}
    return render(request, 'car_review_list.html', context)


def car_list(request):
    search_query = request.GET.get('search_query', '')
    cars = Car.objects.all()

    if search_query:
        cars = cars.filter(car_brand__icontains=search_query)  # Ищем только по car_brand

    context = {'cars': cars, 'search_query': search_query}
    return render(request, 'car_list.html', context)



@login_required
def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            description = form.cleaned_data['description']
            car_brand = form.cleaned_data['car_brand']
            car_model = form.cleaned_data['car_model']
            car_body = form.cleaned_data['car_body']
            horse_power = form.cleaned_data['horse_power']
            car_drive = form.cleaned_data['car_drive']
            tax = form.cleaned_data['tax']


            car = Car(
                description=description,
                car_brand=car_brand,
                car_body=car_body,
                horse_power=horse_power,
                car_drive=car_drive,
                tax=tax,
                user=request.user.username,  # Извлекаем имя пользователя
                car_model=car_model,  # ADD THE MODEL
            )
            car.save()
            return redirect('car_list')
    else:
        form = CarForm()
    return render(request, 'add_car.html', {'form': form})


@login_required
def delete_car(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    car.delete()
    return redirect('car_list')