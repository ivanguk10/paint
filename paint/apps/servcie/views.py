from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import CommentForm


def main(request):
    return render(request, 'sto/main.html')


def main1(request):
    comm = Comment.objects.all()[:4]
    return render(request, 'sto/main1.html', {'comm': comm})

    #return render(request, 'sto/main1.html')


def remont(request):
    service = Service.objects.filter(service='Кузовной ремонт').first()
    return render(request, 'sto/remont/remont.html', {'service': service.services.all()})


def paint(request):
    return render(request, 'sto/paint/paint.html')


def tunning(request):
    tuning = Service.objects.filter(service='Кузовной тюнинг').first()
    return render(request, 'sto/tunning/tunning.html', {'tuning': tuning.services.all()})


def price(request):
    service = Service.objects.filter(service='Кузовной ремонт').first()
    paints = Service.objects.filter(service='Покраска').first()
    tuning = Service.objects.filter(service='Кузовной тюнинг').first()

    context = {'service': service.services.all(), 'paints': paints.services.all(), 'tuning': tuning.services.all()}

    return render(request, 'sto/price.html', context)


def comment(request):
    if request.method == "POST":
        new_comment = Comment()
        new_comment.comment_name = request.POST["comment_name"]
        new_comment.comment_email = request.POST["comment_email"]
        new_comment.comment_theme = request.POST["comment_theme"]
        new_comment.comment_body = request.POST["comment_body"]
        new_comment.save()
        comm = Comment.objects.all()
        return render(request, 'sto/comment.html', {'form': CommentForm(), 'comm': comm})

    elif request.method == "GET":
        comm = Comment.objects.all()
        return render(request, 'sto/comment.html', {'form': CommentForm(), 'comm': comm})


def navbar(request):
    return render(request, 'sto/navbar1.html')


def company(request):
    return render(request, 'sto/company.html')


def slide(request):
    return render(request, 'sto/slide.html')