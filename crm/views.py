from django.shortcuts import render,redirect
from .models import Profile,Todo
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.   

def signup(request):
    if request.method=="POST":
        username=request.POST.get('username','')
        email=request.POST.get('email','')
        password=request.POST.get('password','')
        u=User.objects.filter(username=username,email=email)
        if not username or not email:
            messages.info(request,"Please enter all your fields")
        elif u:
            messages.info(request,"Username Already exists")
        else:
            user=User.objects.create_user(username=username,email=email,password=password)
            user.save()
            messages.info(request,"Successfully created user")
            return redirect('signin')
    return render(request,'signup.html')
def signin(request):
    if request.method=="POST":
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,"INVALID credentials")
            return redirect('signin')
            
    return render(request,'signin.html')

@login_required(login_url='signin')
def index(request):
    print(request.user)
    if request.method == "POST":
        task = request.POST.get('task', '')
        if not task:
            messages.info(request, "Enter a task")
        else:
            Todo.objects.create(task=task, user=request.user)
        return redirect('index')
    items = Todo.objects.filter(user=request.user)
    return render(request, 'index.html', {'items': items})



@login_required(login_url='signin')
def logout(request):
    j=auth.logout(request)
    if j is None:
        messages.info(request,"LOGOUT SUCCESSFUL")
    return redirect('signin')

@login_required(login_url='signin')
def delete(request, task_id):
    task = Todo.objects.get(id=task_id)
    task.delete()
    return redirect('index')
@login_required(login_url='signin')
def update(request, task_id):
    task = Todo.objects.get(id=task_id)
    if request.method == 'POST':
        task.task = request.POST.get('task')
        task.save()
        return redirect('index')
    return render(request, 'update.html', {'task': task})
