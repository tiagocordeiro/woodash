from django.shortcuts import render

# Create your views here.
from core.facade import get_orders


def index(request):
    return render(request, "index.html")


def dashboard(request):
    orders = get_orders()
    return render(request, "dashboard.html", {"orders": orders})
