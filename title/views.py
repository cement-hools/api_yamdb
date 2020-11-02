import csv
from itertools import islice

from django.http import HttpResponse
from django.shortcuts import render, redirect

from title.models import Category, Genre


def index(request):
    categories = Category.objects.all()
    genre = Genre.objects.all()
    return render(
        request,
        "index.html",
        {
            "categories": categories,
            "genre": genre,
        }
        )
