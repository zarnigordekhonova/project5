from django.db import models

# Create your models here.

class Books_info(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    cover_type = models.CharField(max_length=255)


    def __str__(self):
        return f'{self.title} {self.author}'

class Books_rent_info(models.Model):
    start_date = models.IntegerField()
    end_date = models.IntegerField()
    rent_days = models.IntegerField()


    def __str__(self):
        return f'{self.start_date} {self.end_date}'






