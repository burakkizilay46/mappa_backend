from django.urls import path
from . import views

app_name = "people"

urlpatterns = [
    path("ordinary-people/", views.get_ordinary_people, name="ordinary_people_list"),
    path("ordinary-people", views.create_ordinary_person, name="ordinary_person_create"),
    path("ordinary-people/<int:id>/", views.ordinary_person_detail, name="ordinary_person_detail"),

    path("unordinary-people/", views.get_unordinary_people, name="unordinary_people_list"),
    path("unordinary-people", views.create_unordinary_person, name="unordinary_person_create"),
    path("unordinary-people/<int:id>/", views.unordinary_person_detail, name="unordinary_person_detail"),
    
]
