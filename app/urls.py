from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Pet", api.PetViewSet)
router.register("Service", api.ServiceViewSet)
router.register("Our_team", api.Our_teamViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("app/Pet/", views.PetListView.as_view(), name="app_Pet_list"),
    path("app/Pet/create/", views.PetCreateView.as_view(), name="app_Pet_create"),
    path("app/Pet/detail/<int:pk>/", views.PetDetailView.as_view(), name="app_Pet_detail"),
    path("app/Pet/update/<int:pk>/", views.PetUpdateView.as_view(), name="app_Pet_update"),
    path("app/Pet/delete/<int:pk>/", views.PetDeleteView.as_view(), name="app_Pet_delete"),
    path("app/Service/", views.ServiceListView.as_view(), name="app_Service_list"),
    path("app/Service/create/", views.ServiceCreateView.as_view(), name="app_Service_create"),
    path("app/Service/detail/<int:pk>/", views.ServiceDetailView.as_view(), name="app_Service_detail"),
    path("app/Service/update/<int:pk>/", views.ServiceUpdateView.as_view(), name="app_Service_update"),
    path("app/Service/delete/<int:pk>/", views.ServiceDeleteView.as_view(), name="app_Service_delete"),
    path("app/Our_team/", views.Our_teamListView.as_view(), name="app_Our_team_list"),
    path("app/Our_team/create/", views.Our_teamCreateView.as_view(), name="app_Our_team_create"),
    path("app/Our_team/detail/<int:pk>/", views.Our_teamDetailView.as_view(), name="app_Our_team_detail"),
    path("app/Our_team/update/<int:pk>/", views.Our_teamUpdateView.as_view(), name="app_Our_team_update"),
    path("app/Our_team/delete/<int:pk>/", views.Our_teamDeleteView.as_view(), name="app_Our_team_delete"),

)
