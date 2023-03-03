from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class PetListView(generic.ListView):
    model = models.Pet
    form_class = forms.PetForm


class PetCreateView(generic.CreateView):
    model = models.Pet
    form_class = forms.PetForm


class PetDetailView(generic.DetailView):
    model = models.Pet
    form_class = forms.PetForm


class PetUpdateView(generic.UpdateView):
    model = models.Pet
    form_class = forms.PetForm
    pk_url_kwarg = "pk"


class PetDeleteView(generic.DeleteView):
    model = models.Pet
    success_url = reverse_lazy("app_Pet_list")


class ServiceListView(generic.ListView):
    model = models.Service
    form_class = forms.ServiceForm


class ServiceCreateView(generic.CreateView):
    model = models.Service
    form_class = forms.ServiceForm


class ServiceDetailView(generic.DetailView):
    model = models.Service
    form_class = forms.ServiceForm


class ServiceUpdateView(generic.UpdateView):
    model = models.Service
    form_class = forms.ServiceForm
    pk_url_kwarg = "pk"


class ServiceDeleteView(generic.DeleteView):
    model = models.Service
    success_url = reverse_lazy("app_Service_list")


class Our_teamListView(generic.ListView):
    model = models.Our_team
    form_class = forms.Our_teamForm


class Our_teamCreateView(generic.CreateView):
    model = models.Our_team
    form_class = forms.Our_teamForm


class Our_teamDetailView(generic.DetailView):
    model = models.Our_team
    form_class = forms.Our_teamForm


class Our_teamUpdateView(generic.UpdateView):
    model = models.Our_team
    form_class = forms.Our_teamForm
    pk_url_kwarg = "pk"


class Our_teamDeleteView(generic.DeleteView):
    model = models.Our_team
    success_url = reverse_lazy("app_Our_team_list")
