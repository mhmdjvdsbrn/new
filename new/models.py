from django.db import models



class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    text = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
# Create your models here.
