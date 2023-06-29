from django.shortcuts import render, get_object_or_404, redirect
from .models import clubs

# Create your views here.
def home(request):
    clubs_ = clubs.objects.all()
    return render(request, 'home.html', {'clubs' : clubs_})

def detail(request, id):
    club = get_object_or_404(clubs, pk=id)
    return render(request, 'detail.html', {'club':club})

def new(request):
    return render(request, 'new.html')

def create(request):
    '''
    if request.method == 'GET':
        return render(request, 'new.html')
    '''
    if request.method == 'POST':
        club = clubs()
        club.title = request.POST['title']
        club.description = request.POST['description']
        club.numpeople = float(request.POST['numpeople'])
        club.save()
        return redirect('detail', club.id)
    return render(request, 'new.html')