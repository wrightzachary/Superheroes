from . import views
from django.urls import path, include


app_name = 'heroes'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.create, name='new_hero'),
    path('detail/<int:hero_id>/', views.detail, name='detail'),
    path('change/<int:specific_superhero_id>/', views.change, name='change_hero'),
    path('delete/<int:specific_superhero_id>/', views.delete, name='delete_hero')
]
