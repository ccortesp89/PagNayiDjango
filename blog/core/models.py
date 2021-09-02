from django.db import models

# Create your models here.
class entrevista(models.Model):
    artista = models.CharField(max_length=100)
    fotoSmall = models.CharField(max_length=100, blank=True,null=True)

    def __str__(self):
        return self.artista