from django.urls import path
from . import views

app_name = "people"

urlpatterns = [
    path("ordinary-people/", views.get_ordinary_people, name="ordinary_people_list"),
    path("ordinary-people/<int:id>/", views.get_ordinary_byid, name="ordinary_person_detail"),
    path("ordinary-people", views.create_ordinary_person, name="ordinary_person_create"),
    path("ordinary-people/<int:id>/", views.delete_ordinary_person, name="ordinary_person_delete"),
    path("ordinary-people/<int:id>/", views.update_ordinary_person, name="ordinary_person_update"),
]
