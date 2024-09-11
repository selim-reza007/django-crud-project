from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=20)
    content = models.TextField()
    banner = models.ImageField(default='default.jpg', blank=True)


    def __str__(self):
        return self.title
    