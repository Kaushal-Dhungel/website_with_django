from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class mydatabase(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    
    location = models.CharField(max_length = 50)
    b_group = models.CharField(max_length = 30)
    
    
    def __str__(self):
        return self.user.username
    