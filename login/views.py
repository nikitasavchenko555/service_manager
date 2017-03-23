from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user.is_authenticated:
                if user:
                    if user.is_active:
                         login(request, user)
                         return HttpResponseRedirect('/index')
            else:
                     print("Пользователя не существует")
        else:
                 print("Имя или пароль неверны")
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form})

@login_required
def user_logout(request):
    # Поскольку мы знаем, что только вошедшие в систему пользователи имеют доступ к этому представлению, можно осуществить выход из системы
    logout(request)

    # Перенаправляем пользователя обратно на главную страницу.
    return HttpResponseRedirect('/login/')




	
    
    



