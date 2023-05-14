from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE ,default=1)
    description = models.TextField(max_length=200, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/products/', null=True, blank=True)

    def __str__(self):
        return self.name
    

    @staticmethod
    def get_products_by_id(id_lst):
        return Product.objects.filter(id__in =id_lst)

    

    @staticmethod
    def get_all_products():
        return Product.objects.all()
    


    @staticmethod
    def get_product_by_id(category_id):
        if category_id:
            return Product.objects.filter(category_id=category_id)
            
        else:
            return Product.objects.all()