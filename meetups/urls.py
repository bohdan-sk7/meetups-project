from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('meetups/<slug:slug>', views.meetup_details, name='meetup-detail')
]