from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import *
# Create your views here.

def Login(request):
    if request.user.is_authenticated:
        return redirect('shop:home')
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("shop:login_phone")
        else:
            context = {
                "username": username,
                "errormessage": "User not found"
            }
            return render(request, "shop/login/login.html", context)
    else:
        return render(request, 'shop/login/login.html', {})


def Register(request):
    if request.user.is_authenticated:
        return redirect('shop:profile')
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        username = form['username'].value()
        email = form['email'].value()
        if MyUser.objects.filter(username=username).exists():
            messages.error(request, 'یوزرنیم شما تکراری است.')
            return redirect('shop:register')
        if MyUser.objects.filter(email=email).exists():
            messages.error(request, 'ایمیل شما تکراری است.')
            return redirect('shop:register')
        if form.is_valid():
            data = form.cleaned_data
            user = MyUser.objects.create_user(email=data['email'], username=data['username'], password=data['password'])
            user.save()
            return redirect('shop:profile')
        else:
            messages.error(request, 'Something is wrong! Please try again', 'danger')
    else:
        form = UserCreateForm()
    context = {'form': form}
    return render(request, 'shop/register/register.html')

@login_required(login_url='/login/')
def Logout_view(request):
    logout(request)
    return redirect('hair_style:home')

