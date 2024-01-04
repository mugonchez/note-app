from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.
class UserManager(BaseUserManager):
    '''
    create normal user
    '''
    def create_user(self,first_name, last_name, email, password, **other_fields):
         email = self.normalize_email(email)
         user = self.model(email=email, 
                          first_name=first_name,
                          last_name=last_name,
                           **other_fields)
         user.set_password(password)
         user.save()
         return user
    
    '''
    create superuser
    '''
    def create_superuser(self,first_name, last_name, email, password, **other_fields):
         email = self.normalize_email(email)
         other_fields.setdefault('is_staff', True)
         other_fields.setdefault('is_superuser', True)
         other_fields.setdefault('is_active', True)
         if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned staff privileges.')
         if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned superuser priviledges')

         return self.create_user(first_name, last_name, email, password, **other_fields)


# user model
class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'last_name']


    def __str__(self):
        return self.first_name
