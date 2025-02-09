from django.contrib import admin
from django.utils.html import format_html
from src.settings import HOST

from .models import Invitation


@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'guest_1_name',
        'guest_2_name',
        'invitation_link'
    )

    def invitation_link(self, obj):
        url = f"{HOST}{obj.id}/"
        return format_html('<a href="{0}" target="_blank">View Invitation</a>', url)
