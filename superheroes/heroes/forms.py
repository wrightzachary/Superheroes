from django.forms import ModelForm
from .models import Heroes


class HeroesForm(ModelForm):
    class Meta:
        model = Heroes
        fields = '__all__'
