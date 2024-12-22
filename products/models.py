from django.db import models

class Product(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name
