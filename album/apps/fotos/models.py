from django.db import models

# Create your models here.
class MiFoto(models.Model):
    nombre = models.CharField(max_length=90)
    descripcion = models.CharField(max_length=2000)
    imageurl = models.CharField(max_length=120)
    publish = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
