from django.db import models
import datetime as dt

# Create your models here.
class Image(models.Model):
    post_image = models.ImageField(upload_to = 'images/', default = 'image')
    image_title = models.CharField(max_length = 100, default = 'title')
    image_description = models.TextField(max_length=200, default = 'description')
    image_location = models.ForeignKey("Location", on_delete=models.CASCADE)
    image_category = models.ForeignKey("Category", on_delete=models.CASCADE)
    image_post_date =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_title

    def save_image(self):
        self.save

    @classmethod
    def get_images(cls):
        Images = cls.objects.all()
        return  Images

class Location(models.Model):
    location = models.CharField(max_length = 60)

    @classmethod
    def get_location(cls):
        location = cls.objects.all()
        return location

    @classmethod
    def del_location(cls, id):
        cls.objects.filter(id = id).delete()

class Category(models.Model):
    category = models.CharField(max_length = 60, default = 'category')



