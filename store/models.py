from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe



class Store(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    logo = models.ImageField(blank=True, upload_to='stores/logos/')
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
   
