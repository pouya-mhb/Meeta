from django.contrib import admin
from mvp.models import Meeting
from django.core.paginator import Paginator

# Register your models here.


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = [
        'host', 'subject', 'status', 'date', 'time_start', 'time_end'
    ]

    list_filter = [
        'host', 'subject', 'status', 'date', 'time_start', 'time_end'
    ]

    search_fields = [
        'host', 'subject', 'status', 'date', 'time_start', 'time_end'
    ]

    raw_id_fields = ('host',)

    date_hierarchy = 'date'

    ordering = (
        'host', 'subject', 'date', 'time_start', 'time_end'
    )
