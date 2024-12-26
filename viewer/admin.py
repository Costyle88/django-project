from django.contrib import admin
from viewer.models import Genre, Movie, Actor, MovieActor

# Register your models here.
admin.site.register(Genre)
# admin.site.register(Movie)

class ActorAdmin(admin.ModelAdmin):
    list_display = ('name','birth_date', 'eye_color')
    search_fields = ('name', 'eye_color')
    list_filter = ('name',)

class MovieActorInline(admin.TabularInline):
    model = MovieActor
    extra = 1

class MovieAdmin(admin.ModelAdmin):
    inlines = [MovieActorInline]

admin.site.register(Actor, ActorAdmin)
admin.site.register(MovieActor) #Creeaza in url-ul /admin modelul MovieActor

