from django.shortcuts import render
from .models import PunePhotoLoc
from django.core.serializers import serialize

# Create your views here.

def Dashboard(request):
    obj = PunePhotoLoc.objects.all()
    # raw = PunePhotoLoc.objects.raw('SELECT * FROM pune_photo_loc')
    ser_test = serialize('geojson', obj,)
    context = {'image_loc':ser_test}  # send data to front end
    return render(request,"dashboard/dashboard.html",context)