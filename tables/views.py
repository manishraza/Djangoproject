from django.shortcuts import render
from .models import  student, Item, student, StudentProfile

# Create your views here.
def student_list(request):
    students = student.objects.all()
    return render(request, template_name="tables/student.html", context={"students": students})
def item(request):
    return render(request, template_name="tables/item.html", context={"items": Item.objects.all()})
def profile(request):
    return render(request, template_name="tables/profile.html",
                   context={"profiles": StudentProfile.objects.all()})

def Detail(request):
    return render(request, template_name="tables/Detail.html",
                   context={"Details": Detail.objects.all()})

