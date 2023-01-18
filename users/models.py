from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, phone_number, first_name, last_name,password=None):
        user=self.model(
            phone_number=phone_number, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self, phone_number, first_name, last_name):
        user=self.create_user(phone_number=phone_number,first_name=first_name,last_name=last_name)
        user.staff=True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    phone_number = models.CharField(max_length=12,unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    active = models.BooleanField(default=False)
    staff=models.BooleanField(default=False)
    is_teacher=models.BooleanField(default=False)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'phone_number'
    objects = UserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def is_active(self):
        return self.active
