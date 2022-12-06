from django.urls import path
from . import views

app_name = 'stretches'
urlpatterns = [
    # path('', views.Home.as_view(), name='home'),
    path('', views.stretches, name='home')
]