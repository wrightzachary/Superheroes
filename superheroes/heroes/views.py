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


def change(request, hero_id):
    specific_superhero = Heroes.objects.get(pk=hero_id)
    context = {
        'change_specific_superhero': specific_superhero
    }
    if request.method == 'POST':
        specific_superhero.change_name = request.POST.get('change_name')
        specific_superhero.change_alter_ego = request.POST.get('change_alter_ego')
        specific_superhero.change_primary_superhero_ability = request.POST.get('change_primary_superhero_ability')
        specific_superhero.change_secondary_superhero_ability = request.POST.get('change_secondary_superhero_ability')
        specific_superhero.change_catchphrase = request.POST.get('change_catchphrase')
        specific_superhero = Heroes(name=specific_superhero.name, alter_ego=specific_superhero.alter_ego, primary_superhero_ability=specific_superhero.primary_superhero_ability,secondary_superhero_ability=specific_superhero.secondary_superhero_ability, catchphrase=specific_superhero.catchphrase)
        specific_superhero.save()
        return HttpResponseRedirect(reverse('heroes:index', context))
    else:
        return render(request, 'heroes/change.html', context)


def delete(request, hero_id):
    delete_superhero = Heroes.objects.get(pk=hero_id)
    Heroes.delete(delete_superhero)
    return HttpResponseRedirect(reverse('heroes:index'))
