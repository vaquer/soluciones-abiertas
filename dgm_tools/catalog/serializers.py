"""
Serializadores de modelos para mostrar
resultados en el API del CMS
"""
from rest_framework import serializers
from .models import Post


class PostSingleSerializer(serializers.ModelSerializer):
    """
    Clase que configura la serializacion
    de una entrada en la base de datos
    para ser expuesta en el API del CMS
    """
    category = serializers.StringRelatedField(many=False)
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'slug',
            'image',
            'description',
            'category',
            'level',
            'tags',
            'public',
            'created',
            'text'
        )


class PostListSerializer(serializers.ModelSerializer):
    """
    Clase que configura la serializacion
    de un conjunto de entradas en la base
    de datos para ser expuestas en el API del CMS
    """
    category = serializers.StringRelatedField(many=False)
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'slug',
            'image',
            'description',
            'category',
            'level',
            'tags',
            'public',
            'created',
        )
