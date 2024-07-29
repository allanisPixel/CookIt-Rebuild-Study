from django.db import models
from PIL import Image
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    foto_usuario = models.ImageField(upload_to='usuario', blank=True, null=True)
    banido = models.BooleanField(default = False)
    visivel = models.BooleanField(default = True)

    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'password']
    #REQUIRED_FIELDS = ['username', 'phone', 'first_name', 'last_name']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email