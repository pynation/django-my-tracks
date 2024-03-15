from django.contrib import admin

from core.models import Artist, Track


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    pass


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    pass
