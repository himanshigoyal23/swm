from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class mmrda1(models.Model):
	fid = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=254)
	descriptio = models.CharField(max_length=254)
	fid_destri = models.CharField(max_length=254)
	geom = models.PolygonField(srid=4326)
