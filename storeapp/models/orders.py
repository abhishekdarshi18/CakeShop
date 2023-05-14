from django.db import models
from .customer import Customer
from .product import Product
import datetime

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    address = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=20, default='')
    date = models.DateField(default=datetime.datetime.now)
    status = models.BooleanField(default=False)


    def placeOrder(self):
        self.save()


    @staticmethod
    def get_order_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date').reverse()


