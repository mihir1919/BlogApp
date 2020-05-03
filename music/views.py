from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
from django.shortcuts import render, get_object_or_404
from .forms import MusicForm,SearchForm
from .models import Music
from django.forms import ModelForm
from django.utils import timezone
from django.contrib.auth.models import User
# Create your views here.
def weather(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&APPID=2edc88045665cd7d7e9ce52053e0948a'
    city = "Las Vegas"
    r = requests.get(url.format(city)).json()

    city_weather = {
        'city' : city,
        'temperature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
    }
    
    print(city_weather)
    context = {'city_weather' : city_weather}
    return render(request, 'music/weather.html',context)

def index(request):
    
    t = Music.objects.order_by('-added')
    return render(request, 'music/index.html', {'t':t})

def profile(request):
    t = Music.objects.filter(author=str(request.user))
    return render(request, 'music/profile.html', {'t':t})

def details(request, pk):
    r = get_object_or_404(Music, pk=pk)
    return render(request, 'music/details.html', {'r':r})

def add(request):
    form = MusicForm(request.POST)
    if form.is_valid():
        music = form.save(commit=False)
        music.author = request.user
        music.added = timezone.now()
        form.save()
        return redirect('index')
    return render(request, 'music/add.html', {'form':form})
    
def delete(request, pk):
    f = Music.objects.get(pk=pk)
    f.delete()
    return redirect('index')

def edit(request, pk):
    f = get_object_or_404(Music, pk=pk)
    form = MusicForm(request.POST,instance=f)
    if request == "POST":
        if form.is_valid():
            f.save()
            return redirect('index')
    else:
        form = MusicForm(instance=f)
    return render(request, 'music/add.html', {'form':form})


def search(request):
    form = Music.objects.filter(author=str(request.GET))
    if form == None:
        return HttpResponse ("NOT FOUND")
    return render(request, 'music/profile.html', {'form':form})