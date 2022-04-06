from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(verbose_name='nom', max_length = 125)
    image = models.ImageField("couvertur", upload_to="media/")
    created = models.DateTimeField(verbose_name="date", auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    

class Product(models.Model):
    CHOICES = [("USD","dollars"), ("CDF","franc")]
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    name = models.CharField(verbose_name='nom', max_length = 125)
    price = models.FloatField("prix")
    devise = models.CharField(verbose_name='devise', choices= CHOICES, max_length = 10)
    image = models.ImageField("couvertur", upload_to="media/")
    created = models.DateTimeField(verbose_name="date", auto_now_add=True)
    
    def __str__(self):
        return self.name