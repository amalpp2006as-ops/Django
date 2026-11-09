from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class StudentProfile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    age = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.student.name