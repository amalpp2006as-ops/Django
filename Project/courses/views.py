from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import Profile
from django.contrib.auth.models import User

def RegisterView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            Profile.objects.create(
                user=user,
                age=form.cleaned_data['age'],
                file=form.cleaned_data['file']
            )

            login(request, user)

            return redirect('home')

    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

def LoginView(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user_data = User.objects.get(email=email)
            user = authenticate(
                request,
                username=user_data.username,
                password=password
            )

            if user is not None:
                login(request, user)
                return redirect('home')

        except User.DoesNotExist:
            pass

        return render(request, 'login.html', {
            'error': 'Invalid email or password'
        })

    return render(request, 'login.html')

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

def LogoutView(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

    return redirect('home')