"""
Configuracion de vistas del CMS
Vistas para usuarios de datos.gob.mx
"""
from django.http import Http404, HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Post, Category


# Create your views here.
def catalog_home(request, page=1):
    """
    URL: /soluciones-abiertas/p/<int:page>/
    Vista que lista los posts de herramientas
    pagina en grupos de 10 posts

    Los posts se ordenan del mas reciente al mas antiguo

    Parametros:
        - page <int>: Indice de paginacion
    """

    # Obteniendo posts publicados
    posts = Post.objects.prefetch_related('category').filter(public=True).order_by('-id')
    pagination = Paginator(posts, 10)

    # Obteniendo variables de control publicas
    categories = Category.objects.filter(public=True).order_by('id')

    # Paginacion
    page_obj = pagination.page(page)
    p_range = list(pagination.page_range)

    # Paginacion
    init = 0 if page <= 5 else page - 5
    end = page_obj.end_index() if page > page_obj.end_index() - 5 else page + 5
    p_range = p_range[init:end]

    context = {
        'settings': settings,
        'posts': page_obj,
        'categories': categories,
        'p_range': p_range,
        'init': init,
        'end': end
    }

    return render(request, 'catalog.html', context)


def catalog_filter(request, page=1):
    """
    URL: /soluciones-abiertas/search/p/<int:page>/
    Vista que lista los posts de herramientas
    pagina en grupos de 10 posts

    Los posts se ordenan del mas reciente al mas antiguo

    Parametros:
        - page <int>: Indice de paginacion
    """
    import operator
    from functools import reduce
    from django.db.models import Q

    title = request.GET.get('title', '').strip()
    tag = request.GET.get('tipo', '')
    level = request.GET.get('dificultad', '')

    if not title:
        return redirect('/soluciones-abiertas/')

    q_list = [Q(public=True), Q(title__unaccent__icontains=title)]

    if tag:
        q_list.append(Q(tag=tag))

    if level:
        q_list.append(Q(level=level))

    # Obteniendo posts publicados
    posts = Post.objects\
        .prefetch_related('category')\
        .filter(reduce(operator.and_, q_list))\
        .order_by('-id')
    pagination = Paginator(posts, 10)

    # Obteniendo variables de control publicas
    categories = Category.objects.filter(public=True).order_by('id')

    # Paginacion
    page_obj = pagination.page(page)
    p_range = list(pagination.page_range)

    # Paginacion
    init = 0 if page <= 5 else page - 5
    end = page_obj.end_index() if page > page_obj.end_index() - 5 else page + 5
    p_range = p_range[init:end]

    context = {
        'settings': settings,
        'posts': page_obj,
        'categories': categories,
        'p_range': p_range,
        'init': init,
        'end': end
    }

    return render(request, 'catalog.html', context)

def catalog_tool(request, slug=None):
    """
    URL: /soluciones-abiertas/herramientas/<str:slug>/
    Vista que muestra el post de la herramienta

    Parametros:
        - slug <str>: Slug del post publicado
    """

    # Prevencion de ataques
    if not slug:
        raise Http404

    # Se consulta por la nota publicada
    try:
        post = Post.objects.only(
            'title',
            'description',
            'slug',
            'text',
            'created',
            'link_external_tool'
        ).prefetch_related('category').get(slug=slug, public=True)
    except Exception:
        raise Http404

    return render(request, 'post.html', {'post': post, 'settings': settings})
