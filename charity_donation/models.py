from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    email = models.EmailField()
    password = models.CharField(max_length=128)


class Category(models.Model):
    name = models.CharField(max_length=256)


class Institution(models.Model):
    FUNDACJA = 'Fundacja'
    NGO = 'NGO'
    ZBIORKA_LOKALNA = 'Zbiórka lokalna'
    CHOICES = [
        (FUNDACJA, 'Fundacja'),
        (NGO, 'NGO'),
        (ZBIORKA_LOKALNA, 'Zbiórka lokalna'),

    ]

    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1028)
    type = models.CharField(max_length=256, choices=CHOICES, default=FUNDACJA)
    categories = models.ManyToManyField(Category)


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=512)
    city = models.CharField(max_length=128)
    zip_cope = models.CharField(max_length=128)
    pick_up_date = models.DateField(max_length=128)
    pick_up_time = models.CharField(max_length=128)
    pick_up_comment = models.CharField
    user = models.ForeignKey(User, on_delete=models.CASCADE)
