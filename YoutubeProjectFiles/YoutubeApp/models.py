from django.db import models

# Create your models here.

class Comment(models.Model):
    videoId = models.TextField(max_length=20)
    content = models.TextField(max_length=50)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    

    # replies field to be revisited, will hold multiple replies (max_length=???, PK and FK for replies?)

class Reply(models.Model):
    replies = models.TextField(max_length=100)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
   


