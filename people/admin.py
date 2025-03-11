from django.contrib import admin
from people.models import OrdinaryPerson, UnordinaryPerson

# Register your models here.
admin.site.register(OrdinaryPerson)
admin.site.register(UnordinaryPerson)
