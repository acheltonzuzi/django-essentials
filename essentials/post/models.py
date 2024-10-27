from django.db import models
from django.contrib.auth.models import User  # Importa o modelo User do Django

class Post(models.Model):
    title = models.CharField(max_length=75, null=False)
    body = models.TextField(null=False)
    slug = models.SlugField(max_length=75, null=False)
    date = models.DateField(auto_now_add=True)
    banner = models.ImageField(default='fallback.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,default=None)  # Relacionamento com User

    def __str__(self):
        return self.title
