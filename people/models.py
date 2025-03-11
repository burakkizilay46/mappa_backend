from django.db import models
from source.models import WrittenSource


# Create your models here.
class Ethnicity(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Religion(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Profession(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=200)
    alternate_name = models.CharField(max_length=200)
    birth_year = models.DateTimeField(null=True, blank=True)
    death_year = models.DateTimeField(null=True, blank=True)
    description = models.TextField(null=True)
    probable_birth_date = models.DateTimeField(null=True, blank=True)
    probable_death_date = models.DateTimeField(null=True, blank=True)
    ethnicity = models.ForeignKey(
        Ethnicity, on_delete=models.SET_NULL, null=True, blank=True
    )
    religion = models.ManyToManyField(Religion, blank=True)
    gender = models.ForeignKey(Gender, on_delete=models.DO_NOTHING, null=True)
    profession = models.ForeignKey(
        Profession, on_delete=models.SET_NULL, null=True, blank=True
    )
    sources = models.OneToOneField(
        WrittenSource, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.name


class UnordinaryPerson(Person):
    pass


class OrdinaryPerson(Person):
    religion_explanation = models.TextField(null=True, blank=True)
    profession_explanation = models.TextField(null=True, blank=True)
    interesting_feature = models.TextField(null=True, blank=True)
    interaction_with_ordinary_explanation = models.TextField(null=True, blank=True)
    interaction_with_unordinary_explanation = models.TextField(null=True, blank=True)
    biography = models.TextField(null=True, blank=True)
    description_in_the_source = models.TextField(null=True, blank=True)
    explanation_of_ethnicity = models.TextField(null=True, blank=True)
