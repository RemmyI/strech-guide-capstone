# Generated by Django 4.1.3 on 2022-12-09 04:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('StrechApp', '0002_alter_exercises_options_exercises_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercises',
            name='Person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to=settings.AUTH_USER_MODEL),
        ),
    ]
