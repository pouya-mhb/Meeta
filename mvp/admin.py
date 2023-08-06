from django.contrib import admin
from mvp.models import Meeting
from django.core.paginator import Paginator

# Register your models here.


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = [
        'host', 'subject', 'status', 'date_time'
    ]

    list_filter = [
        'host', 'subject', 'status', 'date_time'
    ]

    search_fields = [
        'host', 'subject', 'status', 'date_time'
    ]

    raw_id_fields = ('host',)

    date_hierarchy = 'date_time'

    ordering = (
        'host', 'subject', 'date_time'
    )
