from django.shortcuts import render
from .models import CommentSection
from .forms import Comment_Section

def HomeView(request):
     form = Comment_Section(request.POST or None)
     if form.is_valid() and 'comment' in request.data:
          name = form.cleaned_data['name'].capitalize()
          CommentSection.objects.create(name=name, email=form.cleaned_data['email'],
                                        comment=form.cleaned_data['comment'])
          form = Comment_Section()
          
     comments = CommentSection.objects.all().order_by('-date_added')
     count= CommentSection.objects.all().count()
     context = {
          'count':count,
          'comments':comments,
          'form':form
     }
     return render(request, 'home.html', context)