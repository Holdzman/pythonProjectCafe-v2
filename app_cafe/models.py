from django.db import models


# Create your models here.

class Spicy(models.Model):
    level = models.CharField(max_length=10, blank=True, null=True)
    cover = models.ImageField(upload_to='Spicecovers')

    def __str__(self):
        return self.level


class Drink(models.Model):
    title = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='covers')
    price = models.IntegerField()

    def __str__(self):
        return self.title


class Hotdog(models.Model):
    name = models.CharField(max_length=30)
    cover = models.ImageField(upload_to='hotdogs')
    data_create = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    data_update = models.DateTimeField(auto_now=True, blank=True, null=True)
    price = models.IntegerField()
    composition = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class Hotdog_Spicy(models.Model):
    hotdog = models.ForeignKey(Hotdog, on_delete=models.CASCADE)
    spicy = models.ForeignKey(Spicy, on_delete=models.CASCADE)



