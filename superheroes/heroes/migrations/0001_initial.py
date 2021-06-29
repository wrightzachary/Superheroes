# Generated by Django 3.1.8 on 2021-06-29 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Heroes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('alter_ego', models.CharField(max_length=50)),
                ('primary_superhero_ability', models.CharField(max_length=50)),
                ('secondary_superhero_ability', models.CharField(max_length=50)),
                ('catchphrase', models.CharField(max_length=50)),
            ],
        ),
    ]
