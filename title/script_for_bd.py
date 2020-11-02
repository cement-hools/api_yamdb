import csv
from itertools import islice

from django.shortcuts import redirect

from title.models import Category, Genre


def fill_tables(request):
    # заполняем категории
    with open('data/category.csv', encoding='utf8') as f:
        reader = csv.reader(f)
        for row in islice(reader, 1, None):
            _, created = Category.objects.get_or_create(
                id=row[0],
                name=row[1],
                slug=row[2],
            )
    # заполняем жанры
    with open('data/genre.csv', encoding='utf8') as f:
        reader = csv.reader(f)
        for row in islice(reader, 1, None):
            _, created = Genre.objects.get_or_create(
                id=row[0],
                name=row[1],
                slug=row[2],
            )

    # with open('data/titles.csv', encoding='utf8') as f:
    #     reader = csv.reader(f)
    #     for row in islice(reader, 1, None):
    #         _, created = Genre.objects.get_or_create(
    #             id=row[0],
    #             name=row[1],
    #             slug=row[2],
    #         )
    return redirect("index")