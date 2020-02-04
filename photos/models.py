from django.db import models
import datetime as dt
# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length=20)
    def __str__(self):
        return self.location

class  Category(models.Model):
    category = models.CharField(max_length=20)
    def __str__(self):
        return self.category
    
class Photo(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    date = models.DateTimeField(auto_now=True)

    def save_images(self):
        self.save()

    # @classmethod
    # def search_by_category(cls, search_term):
    #     '''
    #     Method to filter images by category
    #     '''
    #     result = cls.objects.filter(category__category__icontains=search_term)
    #     return result
    # def __str__(self):
    #     return self.name

  


