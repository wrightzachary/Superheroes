from django.shortcuts import render
from .models import Heroes
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    all_heroes = Heroes.objects.all()
    context = {
        'all_heroes': all_heroes
    }
    return render(request, 'heroes/index.html', context)


def detail(request, hero_id):
    specific_superhero = Heroes.objects.get(pk=hero_id)
    context = {
        'specific_superhero': specific_superhero
    }
    return render(request, 'heroes/detail.html', context)


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_superhero_ability = request.POST.get('primary_superhero_ability')
        secondary_superhero_ability = request.POST.get('secondary_superhero_ability')
        catchphrase = request.POST.get('catchphrase')
        new_hero = Heroes(name=name, alter_ego=alter_ego, primary_superhero_ability=primary_superhero_ability, secondary_superhero_ability=secondary_superhero_ability, catchphrase=catchphrase)
        new_hero.save()
        return HttpResponseRedirect(reverse('heroes:index'))
    else:
        return render(request, 'heroes/create.html')


def change(request, superhero_id):
    specific_superhero = Heroes.objects.filter(pk=superhero_id)
    context = {
        'specific_superhero': specific_superhero
    }
    if request.method == 'POST':
        change_name = request.POST.get('change_name')
        change_alter_ego = request.POST.get('change_alter_ego')
        change_primary_superhero_ability = request.POST.get('change_primary_ability')
        change_secondary__superhero_ability = request.POST.get('change_secondary_ability')
        change_catchphrase = request.POST.get('change_catchphrase')
        superhero_id = Heroes(name=change_name, alter_ego=change_alter_ego, primary_ability=change_primary_superhero_ability, secondary_ability=change_secondary__superhero_ability, catchphrase=change_catchphrase)
        superhero_id.save()
        return HttpResponseRedirect(reverse('heroes:detail'))
    else:
        return render(request, 'superheroes/change.html', context)
