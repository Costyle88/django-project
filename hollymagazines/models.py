from django.db import models

# Create your models here.

from django.db.models import CharField, Model, ForeignKey, DO_NOTHING, IntegerField, DateField, TextField, DateTimeField, SlugField
from django.utils.text import slugify


# Create your models here.
class Publicatie(Model):
    class Meta:
        verbose_name_plural="Publicatii"
    name = CharField(max_length=128)
    description = TextField(editable=False, default="")

    slug = SlugField(unique=True, editable=False, default="")

# Functie apelata implicit din Django cand afiseaza un obiect returneaza numele cu care va fi afisat
# obiectul in interfata de admin
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)




class Revista(Model):
    class Meta:
        verbose_name_plural="Reviste"
    title = CharField(max_length=128)
    publicatie = ForeignKey(Publicatie, on_delete=DO_NOTHING)
    released = DateField()
    description = TextField()
    created = DateTimeField(auto_now_add=True)
    slug = SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title