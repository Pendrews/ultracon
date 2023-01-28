from django.urls import path
from .views import dashboard, contribution, t2dashboard, t3dashboard


urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('t2-dashboard/', t2dashboard, name='t2dashboard'),
    path('t3-dashboard/', t3dashboard, name='t3dashboard'),
    path('payments-records/', contribution, name='cont'),
]
