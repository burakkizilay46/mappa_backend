from django.urls import path
from . import views
app_name = 'people'

urlpatterns = [
    path('getOrdinaryPeople',views.getOrdinaryPeople, name='getOrdinaryPeople'),
    path('getUnordinaryPeople',views.getUnordinaryPeople, name='getUnordinaryPeople')
]
