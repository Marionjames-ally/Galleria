from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='gallery/'),
    image_name =models.CharField(max_length =30),

class Location(mmodels.Model):
    location = models.CharField(max_length = 60)

    @classmethod
    def get_location(cls):
        location = cls.objects.all()
        return location

    @classmethod
    def del_location(cls, id):
        cls.objects.filter(id = id).delete()

