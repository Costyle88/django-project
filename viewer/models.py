from django.db.models import CharField, Model, ForeignKey, DO_NOTHING, IntegerField, DateField, TextField, DateTimeField, SlugField
from django.utils.text import slugify


# Create your models here.
class Genre(Model):
    name = CharField(max_length=128)

    slug = SlugField(unique=True, editable=False, default="")

# Functie apelata implicit din Django cand afiseaza un obiect returneaza numele cu care va fi afisat
# obiectul in interfata de admin
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)




class Movie(Model):
    title = CharField(max_length=128)

    # ForeignKey face referire la un obiect din tabelul Genre
    genre = ForeignKey(Genre, on_delete=DO_NOTHING)
    rating = IntegerField()


    # Camp care contine o data (zi/luna/an)
    released = DateField()
    description = TextField()

    # Camp care contine o data si ora (zi/luna/an ora/minut/secunda)
    # auto_now_add adauga ora si data la care s-a creat obiectul automat
    created = DateTimeField(auto_now_add=True)

    # Slug se refenra la numele obiectului in format corect pentru URL
    # ex.: The Good Place -> Slug: the-good-place
    # unique: True -> nu putem avea 2 obicete cu acelasi slug
    # editable=False -> nu putem edita acest camp
    slug = SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title + " - " + self.description
