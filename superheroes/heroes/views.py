from django.shortcuts import render
from .models import Heroes
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import HeroesForm


# Create your views here.
def index(request):
    all_heroes = Heroes.objects.all()
    context = {
        'all_heroes': all_heroes
    }
    return render(request, 'heroes/index.html', context)


def detail(request, hero_id):
    specific_superhero = Heroes.objects.get(id=hero_id)
    context = {
        'specific_superhero': specific_superhero
    }
    return render(request, 'heroes/detail.html', context)


def create(request):
    form = HeroesForm()
    if request.method == 'POST':
        form = HeroesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('heroes:index'))
    context = {'form': form}
    return render(request, 'heroes/create.html', context)


def change(request, specific_superhero_id):
    change_specific_superhero = Heroes.objects.get(id=specific_superhero_id)
    form = HeroesForm(instance=change_specific_superhero)
    if request.method == 'POST':
        form = HeroesForm(request.POST or None, instance=change_specific_superhero)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('heroes:index'))
    context = {'form': form, 'specific_superhero': change_specific_superhero}
    return render(request, 'heroes/change.html', context)


def delete(request, specific_superhero_id):
    delete_superhero = Heroes.objects.get(pk=specific_superhero_id)
    Heroes.delete(delete_superhero)
    return HttpResponseRedirect(reverse('heroes:index'))
