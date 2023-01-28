from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


# Create your models here.


class AUM(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    period = models.DateField()
    period_code = models.CharField(max_length=250, null=True, blank=True)
    value = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'{self.user} GHs:{self.value}'


class acc_ballance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    scheme = models.CharField(max_length=10, null=True, blank=True)
    contribution = models.FloatField(default=0.00)
    last_cont_date = models.DateField(null=True, blank=True)
    interest = models.FloatField(default=0.00)
    withdrawal = models.FloatField(default=0.00)
    balance = models.FloatField(default=0.00)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} {self.balance}'

    @property
    def rate(self):
        rate = (self.interest / self.contribution)*100
        return rate

    # @property
    # def all_acc(self):
    #     total_cont = Sum(self.contribution)
    #     return total_cont


class all_scheme(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contribution = models.FloatField(default=0.00)
    last_cont_date = models.DateField(null=True, blank=True)
    interest = models.FloatField(default=0.00)
    withdrawal = models.FloatField(default=0.00)
    balance = models.FloatField(default=0.00)
    updated = models.DateTimeField(auto_now=True)


    @property
    def rate(self):
        rate = (self.interest / self.contribution)*100
        return rate