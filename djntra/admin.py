from django.contrib import admin
from djntra.models import Thing


class ThingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Thing, ThingAdmin)