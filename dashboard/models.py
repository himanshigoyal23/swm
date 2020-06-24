# from django.db import models
from django.contrib.gis.db import models  # for adding geospatial fields

from django.contrib.auth.models import User

# Create your models here.
class mmrda1(models.Model):
	fid = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=254)
	descriptio = models.CharField(max_length=254)
	fid_destri = models.CharField(max_length=254)
	geom = models.PolygonField(srid=4326)

class PunePhotoLoc(models.Model):
    id = models.CharField(primary_key=True, max_length=254)
    geom = models.MultiPointField(blank=True, null=True)  # This field type is a guess.
    fid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    camera_mod = models.CharField(db_column='camera-mod', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    azimuth = models.CharField(max_length=254, blank=True, null=True)
    lon = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    date = models.CharField(max_length=8, blank=True, null=True)
    time = models.CharField(max_length=254, blank=True, null=True)
    north = models.CharField(max_length=254, blank=True, null=True)
    path = models.CharField(max_length=254, blank=True, null=True)
    lat = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    camera_mak = models.CharField(db_column='camera-mak', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    altitude = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pune_photo_loc'