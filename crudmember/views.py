from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def signup(request):
    if request.method == 'POST':
         #POST 요청이 들어온다면
        if request.POST['password1'] == request.POST['password2']:#pw1과 pw2가 같아야 회원가입 진행
            user = User.objects.create_user(#새로운 회원을 추가한다.
                request.POST['username'], password=request.POST['password1'])
            auth.login(request, user) #성공적으로 추가되면 바로 로그인시켜주고
            return redirect('home')#홈으로 돌아가기.
    return render(request, 'signup.html')
    


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')