from django.shortcuts import render
from .models import CommentSection
from .forms import Comment_Section

def HomeView(request):
     comments = CommentSection.objects.all().order_by('date_added')
     context = {
          'comments':comments
     }
     return render(request, 'home.html', context)