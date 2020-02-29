from django.db import models
import datetime as dt

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='gallery/'),
    image_name =models.CharField(max_length =30),
    image_description = models.CharField(max_length = 150),
    image_location = models.ForeignKey("Location", on_delete=models.CASCADE)
    image_category = models.ForeignKey("Category", on_delete=models.CASCADE)
    image_post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save_image(self):
        self.save

    class Meta:
        ordering = ['title']

    @classmethod
    def get_images(cls):
        Images = cls.objects.all()
        return  Images

class Location(mmodels.Model):
    location = models.CharField(max_length = 60)

    @classmethod
    def get_location(cls):
        location = cls.objects.all()
        return location

    @classmethod
    def del_location(cls, id):
        cls.objects.filter(id = id).delete()

class Category(models.Model):
    category = models.CharField(max_length = 30),



