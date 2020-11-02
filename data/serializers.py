from rest_framework.serializers import ModelSerializer

from title.models import Title, Genre, Category


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'slug',)


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug',)


class TitleSerializer(ModelSerializer):
    genre = GenreSerializer()
    category = CategorySerializer()

    class Meta:
        model = Title
        fields = (
            'id',
            'name',
            'year',
            'description',
            'genre',
            'category',
        )
