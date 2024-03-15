from django.contrib import admin

from core.models import Artist


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    pass
