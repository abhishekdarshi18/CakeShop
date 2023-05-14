from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order

# Register your models here.
@admin.register(Product)
class productAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price','category','description', 'image')

@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Customer)
class customerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone','password')


@admin.register(Order)
class orderAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'customer', 'quantity', 'price', 'address', 'phone', 'date', 'status')