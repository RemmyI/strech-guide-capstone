# from django.shortcuts import render
import requests
import json
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import exercises
# from django.contrib.auth.models import User
from users_app.models import CustomUser
from django.contrib.auth.hashers import make_password
from django.db.models import Q

# Create your views here.
# class Home(ListView):
#     model = exercises
#     template_name = 'home.html'


def stretches(request):
    # if request.method == "POST":
    #     bodypart = request.POST.get()

    type = 'stretching'
    muscle = 'neck'
    api_url = f'https://api.api-ninjas.com/v1/exercises?muscle={muscle}&type={type}'
    response = requests.get(
        api_url, headers={'X-Api-Key': '/eC7c8Yhpc3WiypBjxYKZg==bbWEvsg9V9HO5HKv'})
    data = json.loads(response.text)
    q = request.GET.get('q')if request.GET.get('q') != None else ''

    # muscles = exercises.objects.all()
    muscles = exercises.objects.filter(
        Q(Bodypart__icontains = q)
        )

    if response.status_code == requests.codes.ok:
        context = {
            "exc_list": data[0],
            "exc_name": data[0]['name'],
            "exc_equ": data[0]['equipment'],
            "exc_inst": data[0]['instructions'],
            'muscles': muscles
            # graph context and calculate aray that holds demo, send to front end (graph js)
        }
    return render(request, 'home.html', context)

class add(CreateView, LoginRequiredMixin):
    model = exercises
    template_name = 'add.html'
    fields = ['Bodypart', 'Duration', 'Person']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class edit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = exercises
    template_name = 'edit.html'
    fields = ['Bodypart', 'Duration']

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.user
