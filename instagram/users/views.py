from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from home.models import Details



# Create your views here.

def LoginAdmin(request):

    if request.user.is_authenticated:
        return redirect('view')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            print('username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('view')
        else:
            print('wrong info')

    return render(request, 'users/login.html')

def logoutUser(request):
    logout(request)
    # messages.error(request, 'Logout Sucessful')
    return redirect('login')

@login_required(login_url="login")
def ViewDetails(request):
  
    details = Details.objects.all()
    context = {'details': details}
  

    return render(request, 'users/view.html', context)