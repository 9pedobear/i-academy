from statistics import mode
from .forms import CommentForm, ApplicationForm
from unicodedata import category
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required


def lenta(request):
    context = {}
    context['makala'] = Category_makala.objects.all()[:8]
    return render(request, 'lenta.html', context)


def privacy(request):
    return render(request, 'privacy-policy.html')


def iacadem(request):
    template_name = 'iacadem.html'
    context = {
        'all_seminar': Seminar.objects.all()[:6],
        'all_trainings': Category_trainings.objects.all()[:6]
    }
    return render(request, template_name, context)


def iacademru(request):
    template_name = 'iacademru.html'
    context = {
        'all_seminar': Seminar.objects.all()[:6],
        'all_trainings': Category_trainings.objects.all()[:6]
    }
    return render(request, template_name, context)


def support(request):
    if request.POST:
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/support')
    context = {'form': ApplicationForm}
    return render(request, 'support_staff.html', context)


def post1(request):
    context = {}
    context['makala'] = Category_makala.objects.all()[:3]
    return render(request, 'post1.html')


def all_courses(request):
    context = {}
    context['all_courses'] = Category_trainings.objects.all()
    return render(request, 'all_courses.html', context)


def buissines0(request):
    if request.POST:
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/buissines0')
    context = {'form': ApplicationForm}
    return render(request, 'buissines0.html', context)


def buissines0ru(request):
    if request.POST:
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/buissines0ru')
    context = {'form': ApplicationForm}
    return render(request, 'buissines0ru.html', context)


def rus(request):
    context = {}
    context['makala'] = Category_makala.objects.all()[:8]
    return render(request, 'rus.html', context)


def terms_of_service(request):
    return render(request, 'terms_of_service.html')


def library(request):
    context = {}
    context['makala'] = Category_makala.objects.all()
    return render(request, 'library.html', context)


def all_seminar(request):
    context = {}
    context['all_seminar'] = Seminar.objects.all()
    return render(request, 'all_seminar.html', context)


def packages(request):
    if request.POST:
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/packages')
    context = {'form': ApplicationForm}
    return render(request, 'packages.html', context)


def packages1(request):
    if request.POST:
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/packages1')
    context = {'form': ApplicationForm}
    return render(request, 'packages1.html', context)


def payments_month(request):
    return render(request, 'pays/payments_month.html')


def payments_years(request):
    return render(request, 'pays/payments_years.html')


def payments_years_pluse(request):
    return render(request, 'pays/payments_years_pluse.html')


def payments_iclub(request):
    return render(request, 'pays/payments_standart_expensive.html')


def payments_iclub2(request):
    return render(request, 'pays/payments_iclub2.html')


def payments_iclub3(request):
    return render(request, 'pays/payments_iclub3.html')


def detail_trainings(request, id):
    trainings = get_object_or_404(Category_trainings, id=id)
    category_all = Category_trainings.objects.all()
    category = Detail_trainings.objects.all().filter(category=id)
    return render(request, 'Detail_trainings.html',
                  context={'category': trainings, 'trainings': category, 'category_all': category_all})


def buissines_trainings(request):
    template_name = 'buissines0_trainings.html'
    context = {
        'buissines': Buissines.objects.all(),
        'mentor': Mentor.objects.all()
    }
    return render(request, template_name, context)


def category_detail_trainings(request, id):
    product = get_object_or_404(Seminar, id=id)
    category_all = Seminar.objects.all()
    category = Category_detail_seminar.objects.all().filter(category=id)
    return render(request, 'category_detail_seminar.html',
                  context={'category': product, 'product': category, 'category_all': category_all})


def makala_detail(request, id):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    makala = get_object_or_404(Category_makala, id=id)
    category_all = Category_makala.objects.all()
    category = Makala_detail.objects.all().filter(category=id)
    return render(request, 'post1.html',
                  context={'category': makala, 'makala': category, 'category_all': category_all, 'form': CommentForm}, )


def reset_password(request):
    return render(request, 'reset-password.html')
