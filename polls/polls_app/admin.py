from django.contrib import admin

from polls_app.models import Poll


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    fields = ['name', 'start_date', 'end_date', 'description']
