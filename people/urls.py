from django.urls import path
from . import views

app_name = "people"

urlpatterns = [
    path("getOrdinaryPeople", views.getOrdinaryPeople, name="getOrdinaryPeople"),
    path("getOrdinaryPeople/<int:id>", views.getOrdinaryPeopleById, name="getOrdinaryPeopleById"),
    path("createOrdinaryPeople", views.createOrdinaryPeople, name="createOrdinaryPeople"),
    path("deleteOrdinaryPeople/<int:id>", views.deleteOrdinaryPeople, name="deleteOrdinaryPeople"),
    path("updateOrdinaryPeople/<int:id>", views.updateOrdinaryPeople, name="updateOrdinaryPeople"),
    
    path("getUnordinaryPeople", views.getUnordinaryPeople, name="getUnordinaryPeople"),
    path("getUnordinaryPeople/<int:id>", views.getUnordinaryPeopleById, name="getUnordinaryPeopleById"),
    path("createUnordinaryPeople", views.createUnordinaryPeople, name="createUnordinaryPeople"),
    path("deleteUnordinaryPeople/<int:id>", views.deleteUnordinaryPeople, name="deleteUnordinaryPeople"),
]
