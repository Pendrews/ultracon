from django.db import models
from django.contrib.auth.models import User, AbstractUser
import random


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(null=True, blank=True)
    other_names = models.CharField(max_length=250, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=25, null=True,blank=True)
    country = models.CharField(max_length=250, null=True, blank=True)
    country_of_birth = models.CharField(max_length=250, null=True, blank=True)
    place_of_birth = models.CharField(max_length=250, null=True, blank=True)
    phone = models.CharField(max_length=25, null=True, blank=True)
    alt_phone = models.CharField(max_length=25, null=True, blank=True)
    dig_address = models.CharField(max_length=250, null=True, blank=True)
    postal_address = models.CharField(max_length=250, null=True, blank=True)
    res_address = models.CharField(max_length=250, null=True, blank=True)
    ssnit = models.CharField(max_length=25, null=True, blank=True)
    national_id = models.CharField(max_length=50, null=True, blank=True)
    nok = models.CharField(max_length=200, null=True, blank=True)
    nok_address = models.CharField(max_length=255, null=True, blank=True)
    nok_rel = models.CharField(max_length=25, null=True, blank=True)
    nok_phone = models.CharField(max_length=25, null=True, blank=True)
    father_name = models.CharField(max_length=100,null=True, blank=True)
    father_address = models.CharField(max_length=250,null=True, blank=True)
    mother_name = models.CharField(max_length=100,null=True, blank=True)
    mother_address = models.CharField(max_length=250,null=True, blank=True)
    profil_pic = models.ImageField(default='ava.jpeg', upload_to='profile-pics')
    cover_pic = models.ImageField(default='cover.jpeg', upload_to='cover-pics')
    target = models.FloatField(default=25.00, null=True, blank=True)

    def __str__(self):
        return f'{self.user} {self.gender}'


class Test(models.Model):
    name = models.CharField(max_length=200)
    age = models.FloatField()

    def __str__(self):
        return f'{self.name}'


class ClientAUM(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    period = models.DateField()
    scheme = models.CharField(max_length=10, null=True, blank=True)
    aum = models.FloatField()
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'scheme:{self.scheme} period:{self.period} aum:{self.aum}'


class ClientPortfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    scheme = models.CharField(max_length=10, null=True, blank=True)
    total_cont = models.FloatField(null=True, blank=True)
    total_int = models.FloatField(null=True, blank=True)
    total_with = models.FloatField(null=True, blank=True)
    curr_balance = models.FloatField(null=True, blank=True)
    total_months = models.FloatField(null=True, blank=True)
    last_paid_date = models.DateField()
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.user} {self.curr_balance}'

    @property
    def rate(self):
        rate = (self.total_int / self.total_cont) * 100
        return rate


class Beneficiary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250,null=False, blank=False)
    last_name = models.CharField(max_length=250,null=True, blank=True)
    relationship = models.CharField(max_length=250,null=True, blank=True)
    allocation = models.FloatField(null=True, blank=True)
    address = models.CharField(max_length=450,null=True, blank=True)
    contact = models.CharField(max_length=250,null=True, blank=True)

    def __str__(self):
        return f'{self.user} {self.first_name} {self.allocation}'

