from . import views
from django.urls import path


app_name = 'heroes'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:hero_id>/', views.detail, name='detail'),
    path('new/', views.create, name='create_new_hero'),
    path('change/<int:hero_id>/', views.change, name='change_hero'),
    path('delete/<int:hero_id>/', views.delete, name='delete_hero')
]