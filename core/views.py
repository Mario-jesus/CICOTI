from django.shortcuts import render
from .models import Home

# Create your views here.
def home(request):
    home = Home.objects.latest("updated")
    return render(request, "core/index.html", {'home': home})
