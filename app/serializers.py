from rest_framework import serializers

from . import models


class PetSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Pet
        fields = [
            "title",
            "description",
            "image",
            "price",
            "last_updated",
            "created",
        ]

class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Service
        fields = [
            "description",
            "last_updated",
            "imege",
            "service_title",
            "created",
        ]

class Our_teamSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Our_team
        fields = [
            "full_name",
            "image",
            "age",
            "information",
        ]
