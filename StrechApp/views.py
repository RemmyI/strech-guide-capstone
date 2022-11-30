# from django.shortcuts import render
from django.views.generic import ListView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from .models import exercises
# from django.contrib.auth.models import User
from users_app.models import CustomUser
from django.contrib.auth.hashers import make_password

# Create your views here.
class Home(ListView):
    model = exercises
    template_name = 'home.html'
