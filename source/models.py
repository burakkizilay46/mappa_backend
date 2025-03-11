from django.db import models


# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class WrittenSource(models.Model):
    alternate_names = models.CharField(max_length=200)  # want to array
    author = models.CharField(max_length=200)
    year_written = models.IntegerField()  # want to array
    known_copies = models.CharField(max_length=200)  # want to array
    survived_copies = models.CharField(max_length=200)  # want to array
    library_information = models.CharField(max_length=300)
    other_information = models.TextField(null=True, blank=True)
    probable_year_written = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.alternate_names


class SecondarySource(models.Model):
    alternate_names = models.CharField(max_length=200)  # want to array
    author = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    year_written = models.DateField()
    bibliography_information = models.TextField()
    other_information = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.id
