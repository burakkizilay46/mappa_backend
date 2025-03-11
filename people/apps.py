from django.apps import AppConfig
from django.db.models.signals import post_migrate

def create_default_genders(sender, **kwargs):
    Gender = sender.get_model('Gender')
    Gender.objects.get_or_create(name='Male')
    Gender.objects.get_or_create(name='Female')

class PeopleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'people'
    def ready(self):
        post_migrate.connect(create_default_genders, sender=self)
