from django.db import models


# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    year = models.IntegerField()
    mpg = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.make} {self.model}'
