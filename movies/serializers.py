from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'


    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError("A data de lançamento não pode ser anterior a 1990.")
        return value

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError("O resumo não pode exceder 200 caracteres.")
        elif len(value) < 10:
            raise serializers.ValidationError("O resumo deve conter pelo menos 10 caracteres.")
        return value


class MovieDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True, read_only=True)
    genre = GenreSerializer(read_only=True)
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'relese_date', 'rate', 'resume']


    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)

        return None
