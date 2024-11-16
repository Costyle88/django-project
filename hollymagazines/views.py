from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from . models import Publicatie, Revista

from django.http import HttpResponse


from datetime import date


# Url parameters cu regular expressions
# def hello(request, s, other_s):
#     return HttpResponse(f'Hello, {s} and {other_s} World!')

# URL Encoding
# def hello(request):
    # print(request.GET)
    # s = request.GET.get('s', '')
    # other_s = request.GET.get('other_s', '')
    # return HttpResponse(f'Hello {s} and {other_s} World!')

# def hello(request):
    # sql WHERE -> .filter()
    # movie1 = Movie.objects.filter(rating=8)

    # Filmele unde genre-ul are numele SciFi
    # genre = Genre.objects.get(name='SciFi')
    # movie2 = Movie.objects.filter(genre=genre)

    # Filmele cu rating mai mare de 8
    # movie3 = Genre.objects.filter(rating__gt=8)

    # .filter() inlantuite
    # movie4 = Movie.objects.filter(title_icontains='godfather').filter(rating=10)

    # cate obiecte sunt in query
    # movie_count = Movie.obejcts.all().count()

    # Varianta 1 de creat un obiect
    # Genre.objects.create(name='Horror')

    # sau varianta 2
    # g = Genre.objects.create(name='Horror')
    # g.save()

    # return HttpResponse('<h1>Filmele mele</h1>')

def list_reviste(request):
    publicatii = Publicatie.objects.all()
    reviste = Revista.objects.all()

    return render(
        request, template_name='lista_reviste.html',
        context={'publicatii': publicatii, 'reviste': reviste})

def list_reviste_pub(request, pub_name):
    publicatii = Publicatie.objects.all()

    publicatie = Publicatie.objects.get(name=pub_name)
    reviste = Revista.objects.filter(publicatie=publicatie)

    return render(
        request, template_name='lista_reviste.html',
        context={'publicatii': publicatii, 'reviste': reviste})

def revista_detail(request, slug):
    revista = Revista.objects.get(slug=slug)

    return render(
        request, template_name='revista_detalii.html',
        context={'revista': revista}
    )