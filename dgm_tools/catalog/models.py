"""
Modelos usados en el CMS
de Soluciones de presidencia
"""
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from slugify import slugify


class Post(models.Model):
    """
    Modelo de las entradas
    del CMS
    """
    title = models.CharField(null=False, max_length=110, verbose_name='Título', db_index=True, unique=True)
    description = models.TextField(blank=True, verbose_name='Encabezado', max_length=300)
    image = models.ImageField(upload_to="media/dev-media" if settings.DEBUG else "media/prod-media", verbose_name="Imagen", null=True, blank=True)
    slug = models.SlugField(max_length=210, unique=True)
    text = models.TextField(blank=True, verbose_name='Texto')
    # Categorization
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name="Categoría")
    level = models.IntegerField(
        'Nivel',
        blank=True,
        null=True,
        db_index=True,
        choices=(
            (1, 'Principiante'),
            (2, 'Intermedio'),
            (3, 'Avanzado')
        )
    )
    tags = models.ManyToManyField('Tag')
    link_external_tool = models.URLField(verbose_name="Link de Solución", blank=True)
    # State
    public = models.BooleanField(default=False, verbose_name='Publicado', db_index=True)
    # Periodicity
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    modified = models.DateTimeField(auto_now=True, verbose_name='Modificado')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')

    def __str__(self):
        """
        Verbose de una instancia
        entrada en la base de datos
        """
        return '{}'.format(self.title)

    def get_absolute_url(self):
        """
        Url relativa de la entrada
        dentro del CMS
        """
        from django.urls import reverse
        return reverse('catalog_post', kwargs={'slug': self.slug})

    def get_image(self):
        if not self.image:
            return 'https://datos.gob.mx/public/img/uploads/5a3801925f14526e00dcdd64/f6GxgdxBGHm13LbR.png'

        return self.image.url

    def save(self):
        """
        Crea un nuevo registro entrada
        en la base de datos. Genera el slug
        automaticamente a patir del
        del titulo
        """
        if not self.id:
            slug = slugify(self.title)
            count = Post.objects.filter(slug__startswith=slug).count()
            if count > 0:
                slug = '{}-{}'.format(slug, count)

            self.slug = slug

        super(Post, self).save()

    class Meta:
        """
        Meta del modelo de entradas
        Se agregan indices conjuntos
        y verbose del modelo
        """
        index_together = ['slug', 'public']
        verbose_name = 'solución'
        verbose_name_plural = 'soluciones'


class Category(models.Model):
    """
    Modelo de categoria
    para el CMS
    """
    name = models.CharField(null=False, max_length=110, verbose_name='Nombre', unique=True)
    slug = models.SlugField(db_index=True, editable=False, max_length=300)
    description = models.TextField(blank=True, verbose_name='Descripcion')
    # Periodicity
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    public = models.BooleanField(default=False, verbose_name='Publicado', db_index=True)

    def __str__(self):
        """
        Verbose de una instancia
        categoria en la base de datos
        """
        return '{}'.format(self.name)

    def save(self):
        """
        Crea un nuevo registro categoria
        en la base de datos. Genera el slug
        automaticamente a patir del
        del nombre
        """
        if not self.id:
            self.slug = slugify(self.name)

        super(Category, self).save()

    class Meta:
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'


class Tag(models.Model):
    """
    Modelo de tag
    para el CMS
    """
    tag = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(db_index=True, editable=False, max_length=300)

    # Periodicity
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    public = models.BooleanField(default=False, verbose_name='Publicado', db_index=True)

    def __str__(self):
        """
        Verbose de una instancia
        tag en la base de datos
        """
        return '{}'.format(self.tag)

    def save(self):
        """
        Crea un nuevo registro categoria
        en la base de datos. Genera el slug
        automaticamente a patir del
        del tag
        """
        if not self.id:
            self.slug = slugify(self.tag)

        super(Tag, self).save()

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
