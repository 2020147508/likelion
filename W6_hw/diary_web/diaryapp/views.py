from django.shortcuts import render, redirect, get_object_or_404
from .models import diary
from django.utils import timezone
from django.contrib import auth # auth app 가져오기
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    diaries = diary.objects.all()
    diary_count = 0
    for diary_ in diaries:
        diary_count += 1
    return render(request, 'home.html', {'diaries' : diaries, 'diary_count' : diary_count})

def detail(request, id):
    diary_ = get_object_or_404(diary, pk = id)
    return render(request, 'details.html', {'diary': diary_})

def new(request):
    return render(request, 'new.html')

def create(request):
    if request.method == 'GET':
        return render(request, 'new.html')
    else:
        new_diary = diary()
        new_diary.title = request.POST['title']
        new_diary.location = request.POST['location']
        new_diary.body = request.POST['body']
        new_diary.pub_date = timezone.now()
        new_diary.writer = request.user
        new_diary.save()
        return redirect('detail', new_diary.id)

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    if request.method == 'POST':
        userid = request.POST['username']
        userpw = request.POST['password']

        user = auth.authenticate(request, username=userid, password=userpw)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')
        
def logout(request):
    auth.logout(request)
    return redirect('home')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    
    else:
        userid = request.POST['username']
        userpw = request.POST['password']
        new_user = User.objects.create_user(username=userid, password=userpw)
        auth.login(request, new_user)
        return redirect('home')
    
def edit(request, id):
    edit_diary = diary.objects.get(id=id)
    return render(request, 'edit.html', {'diary':edit_diary})

def update(request, id):
    update_diary = diary.objects.get(id=id)
    update_diary.title = request.POST['title']
    update_diary.location = request.POST['location']
    update_diary.body = request.POST['body']
    update_diary.pub_date = timezone.now()
    update_diary.save()
    return redirect('detail', update_diary.id)

def delete(request, id):
    delete_diary = diary.objects.get(id=id)
    delete_diary.delete()
    return redirect('home')