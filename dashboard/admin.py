from django.contrib import admin
from .models import AUM, acc_ballance, all_scheme
from user.models import ClientAUM, ClientPortfolio

admin.site.register(AUM)
admin.site.register(ClientAUM)
admin.site.register(ClientPortfolio)
admin.site.register(acc_ballance)
admin.site.register(all_scheme)

# Register your models here.


