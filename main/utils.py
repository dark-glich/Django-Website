from .models import CommentSection
from .forms import Comment_Section
from django.shortcuts import render

def Commments(request):
     form = Comment_Section(request.POST or None)
     if form.is_valid() :
          name = form.cleaned_data['name'].capitalize()
          CommentSection.objects.create(name=name, email=form.cleaned_data['email'],comment=form.cleaned_data['comment'])
          form = Comment_Section()
          
     comments = CommentSection.objects.all().order_by('-date_added')[:15]
     count= CommentSection.objects.all().count()
     
     return {'count':count,'comments':comments,'form':form}

def ViewGenerator(request, file):
     comment_section = Commments(request)
     return render(request, file, comment_section)