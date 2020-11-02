from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from title.serializers import TitleSerializer
from title.models import Category, Genre, Title


def index(request):
    categories = Category.objects.all()
    genre = Genre.objects.all()
    title = Title.objects.all()
    return render(
        request,
        "index.html",
        {
            "categories": categories,
            "genre": genre,
            "title": title
        }
        )


class TitlesViewSet(ModelViewSet):
    queryset = Title.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = TitleSerializer
