from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Invitation
from .serializers import InvitationSerializer


class InvitationViewSet(viewsets.ModelViewSet):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer

    @action(detail=True, methods=['get'], url_path='<uuid:guid>/')
    def get_by_uuid(self, request, uuid=None):
        invitation = get_object_or_404(Invitation, uuid=uuid)
        serializer = self.get_serializer(invitation)
        return Response(serializer.data)
