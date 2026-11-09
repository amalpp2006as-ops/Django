from django.db import models
class courses(models.Model):
    title=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=8,decimal_places=3)
    def __str__(self):
        return self.title













