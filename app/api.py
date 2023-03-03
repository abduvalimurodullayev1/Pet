from rest_framework import viewsets, permissions

from . import serializers
from . import models


class PetViewSet(viewsets.ModelViewSet):
    """ViewSet for the Pet class"""

    queryset = models.Pet.objects.all()
    serializer_class = serializers.PetSerializer
    permission_classes = [permissions.IsAuthenticated]


class ServiceViewSet(viewsets.ModelViewSet):
    """ViewSet for the Service class"""

    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]


class Our_teamViewSet(viewsets.ModelViewSet):
    """ViewSet for the Our_team class"""

    queryset = models.Our_team.objects.all()
    serializer_class = serializers.Our_teamSerializer
    permission_classes = [permissions.IsAuthenticated]
