from django.shortcuts import render, redirect
from .models import Tour
from .forms import TourForm
import requests


def schedule_tour(request):
    return render (request, "schedule-tour.html")