from django.db import models
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    file = models.FileField(upload_to='profiles/')

    def __str__(self):
        return self.user.username
    
class category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class courses(models.Model):
    title=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=8,decimal_places=3)
    def __str__(self):
        return self.title

class student(models.Model):

    name=models.CharField(
        max_length=100,
        null=False,
        blank=False,
        unique=False,
        default="unknown"
    )

    

    email=models.EmailField(unique=True)

    age=models.IntegerField(
        null=True,
        blank=True
    )

    is_active=models.BooleanField(default=True)

class Course(models.Model):

    title=models.CharField(max_length=100)

    description=models.TextField()

    price=models.DecimalField(
        max_digits=8,decimal_places=3
    )

    duration=models.IntegerField()

    is_published=models.BooleanField(default=True)

    created_at=models.DateTimeField(
        auto_now_add=True
    )
    updated_at=models.DateTimeField(
        auto_now=True
    )


 
