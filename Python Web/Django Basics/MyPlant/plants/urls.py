from django.urls import path

from plants import views


urlpatterns = [
    path("", views.home, name="home"),
    path("catalogue/", views.catalogue, name="catalogue"),
    path("create/", views.create_plant, name="create-plant"),
    path("edit/<int:pk>/", views.edit_plant, name="edit-plant"),
    path("delete/<int:pk>/", views.delete_plant, name="delete-plant"),
    path("details/<int:pk>/", views.plant_details, name="plant-details"),
]
