from django.urls import path
from .views import student_list ,item
urlpatterns = [
    path("student/", student_list, name="student"),
    path("item/", item, name="item")
]