from django.contrib import admin
from . models import Message
# Register your models here.
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('message', 'formatted_time')

    def formatted_time(self, obj):
        if obj.time is not None:
            return obj.time.strftime('%m.%d %H:%M')
        return None
    formatted_time.short_description = 'Added Time'