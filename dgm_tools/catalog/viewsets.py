"""
Clases de configuracion
para los endpoints del API CMS
"""
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Post
from .serializers import PostListSerializer, PostSingleSerializer


class PostFilter(filters.FilterSet):
    """
    Clase que configura la forma
    de filtrar entradas en el API
    del CMS
    """
    title = filters.CharFilter(name="title", method="unaccent_search")
    class Meta:
        model = Post
        fields = ["category", "tags", "title", "level"]

    def unaccent_search(self, queryset, name, value):
        return queryset.filter(title__unaccent__icontains=value)


class PostViewSet(ReadOnlyModelViewSet):
    """
    Clase que configura la salida
    del endpoint de entradas
    dentro del API del CMS
    """
    queryset = Post.objects.select_related('category').only(
        'id',
        'text',
        'title',
        'slug',
        'description',
        'category',
        'level',
        'tags',
        'public',
        'created'
    ).prefetch_related('tags', 'category').filter(public=True)

    serializer_class = PostListSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = PostFilter

    def get_serializer_class(self):
        """
        Funcion que selecciona el serializador
        dependiendo si se consulta un listado
        de entradas o una entrada en particular
        """

        if self.action == 'retrieve':
            return PostSingleSerializer

        return PostListSerializer
