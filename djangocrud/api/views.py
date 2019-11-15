from rest_framework import viewsets
from djangocrud.api.serializers import MovieSerializer,MovieMiniSerializer
from .models import Movie
from rest_framework.response import Response

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def list(selfself, request, *args, **kwargs):
        movies = Movie.objects.all()
        serializer = MovieMiniSerializer(movies, many=True)
        return Response(serializer.data)
