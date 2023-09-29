from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("tables/", include('tables.urls')),
    path("form/", include('form.urls')),
    path("inherit/", include('temp_inheritance.urls')),
    path("tables/", include('tables.urls')),
    path("", include("crud.urls")),
    path("", include("myapp.urls")),

]
