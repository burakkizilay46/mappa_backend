# Generated by Django 4.2.14 on 2025-03-11 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('source', '0002_rename_secondarysources_secondarysource_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('ascii_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Geometry',
            fields=[
                ('citybase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='place.citybase')),
            ],
            bases=('place.citybase',),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('citybase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='place.citybase')),
                ('geonames_id', models.CharField(max_length=200)),
                ('alternate_names', models.CharField(max_length=200)),
                ('country_code', models.CharField(max_length=200)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('sources', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='source.writtensource')),
            ],
            bases=('place.citybase',),
        ),
    ]
