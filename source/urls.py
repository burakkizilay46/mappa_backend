from django.urls import path
from . import views

app_name = "source"
urlpatterns = [
    path("getWrittenSources", views.getWrittenSources, name="getWrittenSources"),
    path("getSecondarySources", views.getSecondarySources, name="getSecondarySources"),
]
