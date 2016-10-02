from django.contrib import admin
from app.models import Topic, Location, Event


class TopicAdmin(admin.ModelAdmin):
    search_fields = ['name']
    sortable_field_name = "name"


admin.site.register(Topic,TopicAdmin)
admin.site.register(Location)
admin.site.register(Event)
