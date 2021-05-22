from django.shortcuts import render
from .utils import Commments, ViewGenerator


def HomeView(request):
     return ViewGenerator(request, 'home.html')

def FontStyleView(request):
     return ViewGenerator(request, 'fonts.html')

def BorderStyleView(request):
     return ViewGenerator(request, 'border.html')

def FlexStyleView(request):
     return ViewGenerator(request, 'flex.html')

def ShadowStyleView(request):
     return ViewGenerator(request, 'shadow.html')

def TransformStyleView(request):
     return ViewGenerator(request, 'transform.html')