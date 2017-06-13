from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    phone_number = models.CharField(max_length=12)
    work_place = models.CharField(max_length=254)
    company = models.CharField(max_length=254)
    e_mail = models.EmailField(max_length=254)

    def __str__(self):
        return '{} {}'.format(self.name, self.last_name)
