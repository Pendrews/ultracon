from django.shortcuts import render, redirect, HttpResponse
from .forms import UserRegisterForm, U_UpdateForm, P_UpdateForm, CreateBene
from .models import Beneficiary,Profile
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from user.render_pdf import clientpdfform
from django.contrib.auth.models import User


from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa


def generate_pdf(request):
    us = User.objects.filter(id = request.user.id)
    pro = Profile.objects.filter(user_id=request.user)
    bene = Beneficiary.objects.filter(user_id=request.user)
    data = {'name': 'John Smith',
            'age': 35,
            'us': us,
            'pro': pro,
            'bene': bene}

    pdf = render_to_pdf('user/userformpdf.html', data)
    return HttpResponse(pdf, content_type='application/pdf')


def render_to_pdf(template_src, context_dict={}, filename='my_pdf_file.pdf'):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename={}'.format(filename)
        return response
    else:
        return None


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()

    site = 'register'
    template = 'user/register.html'
    context = {
        'site': site,
        'form': form,
    }
    return render(request, template, context)


@login_required()
def profile(request):
    benelist = Beneficiary.objects.all()

    if request.method == 'POST':
        p_form = P_UpdateForm(request.POST, request.FILES, instance=request.user.profile)
        u_form = U_UpdateForm(request.POST, instance=request.user)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('beneficiary')
    else:
        u_form = U_UpdateForm(instance=request.user)
        p_form = P_UpdateForm(instance=request.user.profile)

    profile = 'profile'

    context = {
        'profile': profile,
        'u_form': u_form,
        'p_form': p_form,
        'benelist': benelist,
    }
    template = 'user/profile.html'
    return render(request, template, context)


@login_required()
def beneficiary(request):
    if request.method=='POST':
        form = CreateBene(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('beneficiary')
    else:
        form = CreateBene()

    allosum = Beneficiary.objects.filter(user_id=request.user)
    total_allocation = allosum.aggregate(Sum('allocation'))['allocation__sum'] or 0.00
    balance = 100 - total_allocation
    postive_blance = total_allocation - 100

    benelist = Beneficiary.objects.all()
    status = 0

    context = {
        'benelist':  benelist,
        'form': form,
        'total_allocation': total_allocation,
        'balance': balance,
        'postive_blance': postive_blance,
        'status': status,
    }
    template = 'user/bene.html'
    return render(request, template, context)


@login_required()
def create(request):
    if request.method=='POST':
        form = CreateBene(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('beneficiary')
    else:
        form = CreateBene()

    allosum = Beneficiary.objects.filter(user_id=request.user)
    total_allocation = allosum.aggregate(Sum('allocation'))['allocation__sum'] or 0.00
    total = total_allocation/2

    context = {
        'form': form,
        'total_allocation': total_allocation,
        'total': total


    }
    template = 'user/create.html'

    return render(request, template, context)


@login_required()
def update(request, pk):
    item = Beneficiary.objects.get(id=pk)
    if request.method=='POST':
        form = CreateBene(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('beneficiary')
    else:
        form = CreateBene(instance=item)
    context ={
        'form':form,
    }
    template = 'user/update.html'
    return render(request, template, context)


@login_required()
def delete(request, pk):
    template = 'user/delete.html'
    beneficiary = Beneficiary.objects.get(id=pk)
    if request.method == 'POST':
        beneficiary.delete()
        return redirect('beneficiary')

    context = {
        'beneficiary': beneficiary,
    }
    return render(request, template, context)


def pdf(request):
    us = User.objects.all()
    pdf = clientpdfform("user/userformpdf.html")
    return HttpResponse(pdf, content_type='application/pdf')


