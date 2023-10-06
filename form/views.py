from django.shortcuts import render, redirect
from tables.models import student , Item
from crud.models import ClassRoom
from .forms import ClassRoomForm, ClassRoomModelForm


def student_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        address = request.POST.get('address')
        bio = request.POST.get('bio')
        student.objects.create(name=name, age=age, email=email, address=address,bio=bio)
        return  redirect('student')

    return render(request, template_name='form/student_view.html')

def item_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        company = request.POST.get('company')
        colour = request.POST.get('colour')
        description = request.POST.get('description')
        Item.objects.create(name=name, price=price, company=company,colour=colour, description=description)
        return  redirect('item')

    return render(request, template_name='form/item_view.html')

def classroom(request):
    if request.method == "POST":
        form = ClassRoomForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            ClassRoom.objects.create(name=name)
            return redirect("forms_classroom")
    form = ClassRoomForm()
    classrooms = ClassRoom.objects.all()
    return render(request, template_name="forms/classroom.html",
                  context={"classrooms": classrooms, "form": form})


def model_classroom(request):
    if request.method == "POST":
        form = ClassRoomModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("forms_classroom")
    form = ClassRoomModelForm()
    classrooms = ClassRoom.objects.all()
    return render(request, template_name="forms/classroom.html",
                  context={"form": form, "classrooms": classrooms})

