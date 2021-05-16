from django.db import models

class CommentSection(models.Model):
     name = models.CharField(max_length=126)
     email = models.EmailField(max_length=256)
     comment = models.CharField(max_length=1000)
     date_added = models.DateTimeField(auto_now_add=True, null=True)