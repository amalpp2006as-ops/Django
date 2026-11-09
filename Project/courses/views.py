from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm

def RegisterView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid():
            user_data = form.save(commit=False)
            user_data.set_password(form.cleaned_data['password'])
            user_data.save()
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})
