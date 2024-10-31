from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from . import forms
from .forms import CalculatorForm
from django.contrib.auth import login, authenticate
from .forms import SignUpForm 
from django.contrib.auth.decorators import login_required

def index(request): 
    return HttpResponse("Hello, world. This is the index view of app_test_1.") 

def home(request):
    content = "<html><body><h1>It's my bad</h1></body></html>"
    return HttpResponse(content)

def display_date(request):
    date_joined = datetime.today()
    return HttpResponse(date_joined)

@login_required
def home_view(request):
    return render(request, 'home.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Lưu người dùng vào cơ sở dữ liệu
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)  # Đăng nhập ngay sau khi đăng ký
            return redirect('home')  # Chuyển hướng về trang chủ sau khi đăng ký thành công
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def calculator_view(request):
    result = None
    error = None
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            operation = form.cleaned_data['operation']
            
            try:
                if operation == '+':
                    result = round(num1 + num2, 2)
                elif operation == '-':
                    result = round(num1 - num2, 2)
                elif operation == '*':
                    result = round(num1 * num2, 2)
                elif operation == '/':
                    result = round(num1 / num2, 2) if num2 != 0 else None
                    if result is None:
                        error = "Cannot divide by zero."
            except Exception as e:
                error = str(e)
        else:
            error = "Invalid input."
    else:
        form = CalculatorForm()
    
    return render(request, 'calculator.html', {'form': form, 'result': result, 'error': error})




