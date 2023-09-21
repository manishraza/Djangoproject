from django.db import models
class student(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()
    address = models.CharField(max_length=20)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    company = models.CharField(max_length=20)
    colour = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name

class StudentProfile(models.Model):
    student = models.OneToOneField(student, on_delete=models.CASCADE)
    contact = models.CharField(max_length=14)
    roll_no = models.IntegerField()
