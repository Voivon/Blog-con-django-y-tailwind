from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)  # Campo para el título
    content = models.TextField()  # Campo para el contenido


    def __str__(self):
        return self.title  # Esto mostrará el título en el admin
