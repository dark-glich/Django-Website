from django.shortcuts import render
from .utils import Commments


def HomeView(request):
     comment_section = Commments(request)
     return render(request, 'home.html', comment_section)

def FontStyleView(request):
     comment_section = Commments(request)
     return render(request, 'fonts.html', comment_section)

