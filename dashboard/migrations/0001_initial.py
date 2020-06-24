# Generated by Django 3.0.5 on 2020-06-24 09:46

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mmrda1',
            fields=[
                ('fid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=254)),
                ('descriptio', models.CharField(max_length=254)),
                ('fid_destri', models.CharField(max_length=254)),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
        ),
    ]
