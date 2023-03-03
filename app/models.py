from django.db import models
from django.urls import reverse


class Pet(models.Model):

    # Fields
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    image = models.ImageField(upload_to="upload/images/")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("app_Pet_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("app_Pet_update", args=(self.pk,))



class Service(models.Model):

    # Fields
    description = models.TextField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    imege = models.ImageField(upload_to="upload/images/")
    service_title = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("app_Service_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("app_Service_update", args=(self.pk,))



class Our_team(models.Model):

    # Fields
    full_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to="upload/images/")
    age = models.IntegerField()
    information = models.TextField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("app_Our_team_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("app_Our_team_update", args=(self.pk,))

