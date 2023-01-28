from django.contrib import admin
from .models import Profile, Test, Beneficiary

# Register your models here.
admin.site.register(Test)
admin.site.register(Profile)
admin.site.register(Beneficiary)


