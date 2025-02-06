from django.contrib import admin

from .models import Invitation


@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    list_display = (
        'guest_1_name',
        'guest_2_name',
        'created_at',
    )
