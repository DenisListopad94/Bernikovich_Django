from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from forms import CustomUserCreationForm, CustomAuthenticationForm


@login_required
def some_view(request):
    #  только для аутентифицированных пользователей
    pass


@permission_required('your_app.view_hotel', raise_exception=True)
def hotel_view():
    #  только для пользователей с правом просмотра отелей
    pass


@permission_required('your_app.view_user', raise_exception=True)
def user_view():
    # только для пользователей с правом просмотра пользователей
    pass


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


def custom_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})


def home_view(request):
    return render(request, 'home.html')


def your_view(request):
    return redirect('home')  # Перенаправление на домашнюю страницу
