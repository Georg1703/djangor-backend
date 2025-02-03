import uuid

from django.db import models


class Invitation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    guest_1_name = models.CharField(max_length=100)
    guest_2_name = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f"{self.guest_1_name} and {self.guest_2_name}"
            if self.guest_2_name
            else self.guest_1_name
        )
