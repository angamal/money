from django.contrib.auth import login
from django.forms import Form
from django.shortcuts import render, redirect
from django.http import HttpResponse

from.models import Formss


# Create your views here.
def demo(request):
    obj = Formss.objects.all()
    return  render(request,"index.html",{'result':obj})












