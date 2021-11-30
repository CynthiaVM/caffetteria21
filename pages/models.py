from django.db import models
from ckeditor.fields import RichTextField


class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = RichTextField(verbose_name='Contenido')
    order = models.PositiveSmallIntegerField (verbose_name=  "orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

#order sirve para q rompa la base de datos

    class Meta:
        verbose_name = 'pagina'
        verbose_name_plural = 'paginas'

def __str__(self) -> str:
        return self.title

