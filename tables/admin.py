from django.contrib import admin

from .models import  student, Item, StudentProfile, Detail, Classroom
admin.site.register(student)
admin.site.register(Item)
admin.site.register(StudentProfile)
admin.site.register(Detail)
admin.site.register(Classroom)
