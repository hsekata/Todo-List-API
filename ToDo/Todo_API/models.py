from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserToDoManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        if self.model.objects.filter(is_superuser=True).exists():
            raise ValidationError("Only one superuser is allowed")

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)
class UserToDo(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserToDoManager() 
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]

    def __str__(self):
        return self.email

class ToDos(models.Model):
    title = models.TextField()
    description = models.TextField()
    usertodo = models.ForeignKey(UserToDo, on_delete=models.CASCADE, null=True)
    done = models.BooleanField(default=False)
    def __str__(self):
        return self.usertodo.name + "'s todo" 
