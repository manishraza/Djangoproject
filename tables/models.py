from django.db import models
class Classroom(models.Model):
    name= models.CharField(max_length=20)


class student(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()
    address = models.CharField(max_length=20)
    bio = models.TextField()
    c = models.ForeignKey(Classroom, on_delete=models.CASCADE,
                                  related_name="classroom_students", null=True, blank=True)

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
    def __str__(self):
        return self.student.name
class Detail(models.Model):
    model_id_no = models.OneToOneField(Item, on_delete=models.CASCADE)
    brand = models.CharField(max_length=14)
    EMI_no = models.IntegerField()
    def __str__(self):
        return self.model_id_no.name

class Publication(models.Model):
    title = models.CharField(max_length=20)
    def __str__(self):
        return self.title
class Article(models.Model):
    headline = models.CharField(max_length=20)
    publications = models.ManyToManyField(Publication)


def __str__(self):
    return self.headline