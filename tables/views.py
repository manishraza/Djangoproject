from django.shortcuts import render
from .models import  student, Item

# Create your views here.
def student_list(request):
    students = student.objects.all()
    return render(request, template_name="tables/student.html", context={"students": students})
def item(request):
    students = Item.objects.all()
    return render(request, template_name="tables/item.html", context={"items": students})

