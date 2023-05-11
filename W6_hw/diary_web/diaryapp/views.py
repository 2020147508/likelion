from django.shortcuts import render, redirect, get_object_or_404
from .models import diary
from django.utils import timezone

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
    new_diary = diary()
    new_diary.title = request.POST['title']
    new_diary.location = request.POST['location']
    new_diary.body = request.POST['body']
    new_diary.pub_date = timezone.now()
    new_diary.save()
    return redirect('detail', new_diary.id)