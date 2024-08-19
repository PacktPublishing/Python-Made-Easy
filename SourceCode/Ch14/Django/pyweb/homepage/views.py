from django.shortcuts import render
from datetime import datetime


def home(request):
   today = datetime.now().date()
   return render(request, "homepage/home.html", {"today" : today})
