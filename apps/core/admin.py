from django.contrib import admin

from apps.core.models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name')
    search_fields = ['name', 'last_name']
    list_max_show_all = 5000
