from django.urls import path
from . import views

app_name = "people"

urlpatterns = [
    path("getOrdinaryPeople", views.getOrdinaryPeople, name="getOrdinaryPeople"),
    path("getOrdinaryPeople/<int:id>", views.getOrdinaryPeopleById, name="getOrdinaryPeopleById"),
    path("getUnordinaryPeople", views.getUnordinaryPeople, name="getUnordinaryPeople"),
    path("getUnordinaryPeople/<int:id>", views.getUnordinaryPeopleById, name="getUnordinaryPeopleById"),
]
