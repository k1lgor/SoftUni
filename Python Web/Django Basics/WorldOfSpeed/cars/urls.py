from django.urls import include, path

from cars import views

urlpatterns = [
    path("catalogue/", views.catalogue, name="catalogue"),
    path("create/", views.create_car, name="create-car"),
    path("<int:pk>/", include([
        path("details/", views.car_details, name="car-details"),
        path("edit/", views.edit_car, name="edit-car"),
        path("delete/", views.delete_car, name="delete-car"),
    ]))
]
