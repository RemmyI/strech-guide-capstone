# from django.shortcuts import render
import requests, json
from django.views.generic import ListView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import exercises
# from django.contrib.auth.models import User
from users_app.models import CustomUser
from django.contrib.auth.hashers import make_password

# Create your views here.
# class Home(ListView):
#     model = exercises
#     template_name = 'home.html'


def stretches(request):
    type = 'stretching'
    muscle = 'neck'
    api_url = f'https://api.api-ninjas.com/v1/exercises?muscle={muscle}&type={type}'
    response = requests.get(api_url, headers={'X-Api-Key': '/eC7c8Yhpc3WiypBjxYKZg==bbWEvsg9V9HO5HKv'})
    data = json.loads(response.text)

    muscles = exercises.objects.all()

    if response.status_code == requests.codes.ok:
        context = {
            "exc_list": data[0],
            "exc_name":data[0]['name'],
            "exc_equ":data[0]['equipment'],
            "exc_inst":data[0]['instructions'],
            'muscles':muscles
        }
        # print('!!!!!!!!!!!!!!!!!!!!!!!!!', data[0]['name'])
    else:
        print("Error:", response.status_code, data)
    
    return render(request, 'home.html', context)
