import django_otp.models
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import AUM, acc_ballance, all_scheme
from user.models import ClientAUM, ClientPortfolio
from user.api_com import all_scheme_aum


@login_required()
def dashboard(request):
    aum = AUM.objects.all().order_by('period')
    all_scheme_aum()
    balance = acc_ballance.objects.all()
    rate = all_scheme.objects.all()

    dashbaord = 'dashbaord'
    maindash = 'maindash'
    context = {
        'dashbaord': dashbaord,
        'aum': aum,
        'maindash': maindash,
        'balance': balance,
        'rate': rate,

    }
    template = 'dashboard/dashboard.html'
    return render(request, template, context)


@login_required()
def contribution(request):
    dash = 'dash'
    context = {
        'dash': dash,
    }
    template = 'dashboard/cont.html'
    return render(request, template, context)


@login_required()
def t2dashboard(request):
    t2aum = ClientAUM.objects.filter(scheme='162').order_by('period')
    bal = acc_ballance.objects.filter(scheme=162)
    rate = acc_ballance.objects.filter(scheme=162)
    dashbaord = 'dashbaord'
    tiertwodash = 'tiertwodash'
    dash = 'dash'
    context = {
        'dashbaord': dashbaord,
        't2aum': t2aum,
        'tiertwodash': tiertwodash,
        'bal': bal,
        'rate': rate,


    }
    template = 'dashboard/t2dashboard.html'
    return render(request, template, context)


def t3dashboard(request):
    t3aum = ClientAUM.objects.filter(scheme='181').order_by('period')
    bal = acc_ballance.objects.filter(scheme='181')
    rate = acc_ballance.objects.filter(scheme=181)
    dashbaord = 'dashbaord'
    tierthreewodash = 'tierthreewodash'

    context = {
        'dashbaord': dashbaord,
        't3aum': t3aum,
        'tierthreewodash': tierthreewodash,
        'bal': bal,
        'rate': rate,
    }
    template = 'dashboard/t3dashboard.html'
    return render(request, template, context)