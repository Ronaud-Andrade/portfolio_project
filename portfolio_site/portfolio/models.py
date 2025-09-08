from django.db import models

# Create your models here.
class Projetos_novos(models.Model):
    dono = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
