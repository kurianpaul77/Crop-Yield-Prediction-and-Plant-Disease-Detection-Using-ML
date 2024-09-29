from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request,'home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_home')
            elif user.is_farmer:
                return redirect('farmerviewprofile')
            elif user.is_officer:
                return redirect('officer_home')
        else:
            return render(request, 'login.html', {'invalid_credentials': True})
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')