from django.db import models
from django.conf import settings
from django.utils import timezone 

# Create your models here.
class Post(models.Model):
    # Referencia a otra tabla: autor
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # usamos métodos de clase para crear título, contenido, time stamps...
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    # Fx que publica nuestro post
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
