from django.contrib import admin
from people.models import OrdinaryPerson, UnordinaryPerson, Ethnicity, Religion,Profession

# Register your models here.
admin.site.register(OrdinaryPerson)
admin.site.register(Ethnicity)
admin.site.register(Religion)
admin.site.register(Profession)
admin.site.register(UnordinaryPerson)
