from django.db import models
from source.models import WrittenSource

# Create your models here.


class CityBase(models.Model):
    name = models.CharField(max_length=200)
    ascii_name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class City(CityBase):
    geonames_id = models.CharField(max_length=200)
    alternate_names = models.CharField(max_length=200)  # need to array
    country_code = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    sources = models.OneToOneField(
        WrittenSource, on_delete=models.CASCADE, null=True, blank=True
    )
    def __str__(self):
        return self.name


# add later
""" class CityDetail(CityBase):
    geonames_id = models.CharField(max_length=200, null=True)
    alternate_names = models.CharField(max_length=200, null=True) # need to array
    country_code = models.CharField(max_length=200, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True) """


class Geometry(CityBase):
    pass
