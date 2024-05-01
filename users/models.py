from django.db import models

# Create your models here.
class user_info1(models.Model):
    name = models.CharField(max_length=255)
    surname  = models.CharField(max_length=255)
    email  = models.CharField(max_length=255)
    address  = models.CharField(max_length=255)
    age  = models.IntegerField()


    def __str__(self):
        return f'{self.name} {self.surname}'


class user_subscription_info(models.Model):
    subscription_number = models.IntegerField()
    expire_date = models.IntegerField()
    number_rented_books = models.IntegerField()


    def __str__(self):
        return f'{self.subscription_number} {self.number_rented_books}'
