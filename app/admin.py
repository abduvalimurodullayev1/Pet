from django.contrib import admin
from django import forms

from . import models


class PetAdminForm(forms.ModelForm):

    class Meta:
        model = models.Pet
        fields = "__all__"


class PetAdmin(admin.ModelAdmin):
    form = PetAdminForm
    list_display = [
        "title",
        "description",
        "image",
        "price",
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "title",
        "description",
        "image",
        "price",
        "last_updated",
        "created",
    ]


class ServiceAdminForm(forms.ModelForm):

    class Meta:
        model = models.Service
        fields = "__all__"


class ServiceAdmin(admin.ModelAdmin):
    form = ServiceAdminForm
    list_display = [
        "description",
        "last_updated",
        "imege",
        "service_title",
        "created",
    ]
    readonly_fields = [
        "description",
        "last_updated",
        "imege",
        "service_title",
        "created",
    ]


class Our_teamAdminForm(forms.ModelForm):

    class Meta:
        model = models.Our_team
        fields = "__all__"


class Our_teamAdmin(admin.ModelAdmin):
    form = Our_teamAdminForm
    list_display = [
        "full_name",
        "image",
        "age",
        "information",
    ]
    readonly_fields = [
        "full_name",
        "image",
        "age",
        "information",
    ]


admin.site.register(models.Pet, PetAdmin)
admin.site.register(models.Service, ServiceAdmin)
admin.site.register(models.Our_team, Our_teamAdmin)
