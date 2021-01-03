from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
import re


def log_in(request):
    form = LoginForm()
    if request.method == 'POST':
        if request.is_ajax() == True:
            form_send_login = request.POST.get('data')
            usern = re.findall(r'(username=[0-9A-Za-zА-Яа-я_]+)', form_send_login)
            usern = re.sub("username=", '', str(usern))
            usern = re.sub("(\['|\'])", '', str(usern))
            passw = re.findall(r'(password=[0-9A-Za-z]+)', form_send_login)
            passw = re.sub("password=", '', str(passw))
            passw = re.sub("(\['|'\])", '', str(passw))
            print(usern, passw)
            # return HttpResponse(passw)
            user = authenticate(username=usern, password=passw)
            print(user.is_authenticated)
            if user and user.is_authenticated:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Успешно')
            else:
                return HttpResponse('Логин или пароль неверны!')

    return render(request, 'login/login.html', {'form': form})


@login_required
def user_logout(request):
    # Поскольку мы знаем, что только вошедшие в систему пользователи имеют доступ к этому представлению, можно осуществить выход из системы
    logout(request)

    # Перенаправляем пользователя обратно на главную страницу.
    return HttpResponseRedirect('/login/')
