from django.contrib import admin
from .models import WrittenSource, SecondarySource

# Register your models here.
admin.site.register(WrittenSource)
admin.site.register(SecondarySource)