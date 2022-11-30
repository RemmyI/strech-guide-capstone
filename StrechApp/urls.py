from django.urls import path
from . import views

app_name = 'streches'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
]