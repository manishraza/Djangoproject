from django.shortcuts import render, redirect
from tables.models import student , Item


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

