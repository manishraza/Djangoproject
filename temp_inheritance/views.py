from django.shortcuts import render
def main(request):
    people = [
        {"name": "ram", "age": 30, "address": "ktm"},
        {"name": "sita", "age": 20, "address": "pkr"},
        {"name": "shyam", "age": 10, "address": "bir"}
    ]
    context = {"people": people}
    return render(request, template_name='temp_inheritance/home.html', context=context)
def features(request):
    item = [
        {"name": "Laptop", "features": "A portable computer"},
        {"name": "iphone", "features": "this is the best phone"},
        {"name": "macbook", "features": "its is fastest computer"}
    ]
    return render(request, template_name='temp_inheritance/features.html', context={"items": item})
def pricing(request):
    item = [
        {"name": "Laptop", "price": "1200000"},
        {"name": "iphone", "price": "2700000"},
        {"name": "macbook", "price": "3800000"}
    ]
    return render(request, template_name='temp_inheritance/pricing.html', context={"goods": item})