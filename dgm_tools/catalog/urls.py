from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .viewsets import PostViewSet
from .views import catalog_home, catalog_tool


router = DefaultRouter()
router.register(r'posts', PostViewSet)


urlpatterns = [
    url(r'^api/', include(router.urls)),
    path('', catalog_home, name="home"),
    path('p/<int:page>/', catalog_home, name="home_pagination"),
    path('herramientas/<slug:slug>/', catalog_tool, name='catalog_post'),
]
