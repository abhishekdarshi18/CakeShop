from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    @staticmethod
    def get_all_category_name():
        return Category.objects.all()