from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

    def register(self):
        self.save()

    
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
        

