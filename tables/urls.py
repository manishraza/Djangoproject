from django.urls import path
from .views import student_list, item, profile, Detail
urlpatterns = [
    path("student/", student_list, name="student"),
    path("item/", item, name="item"),
    path("profile/", profile, name="profile"),
    path("Detail/", Detail, name="Detail")
]