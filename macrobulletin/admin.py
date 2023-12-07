from django.contrib import admin
from .models import Topic, EconomicIndex, Table


class TopicAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']


class EconomicIndexAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'macro_topic']
    search_fields = ['name', 'macro_topic__name'] 


admin.site.register(Topic, TopicAdmin)
admin.site.register(EconomicIndex, EconomicIndexAdmin)
admin.site.register(Table)
