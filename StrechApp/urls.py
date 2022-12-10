from django.urls import path
from . import views

app_name = 'stretches'
urlpatterns = [
path('', views.stretches, name='home'),
path('edit/<int:pk/',views.edit.as_view(), name='edit'),
path('add/',views.add.as_view(), name='add'),
]