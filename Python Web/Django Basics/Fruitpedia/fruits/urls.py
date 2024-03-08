from django.urls import include, path
from fruits import views

urlpatterns = [
    path("create/", views.create_fruit, name="create-fruit"),
    path(
        "<int:pk>/",
        include(
            [
                path("details/", views.fruit_details, name="details-fruit"),
                path("edit/", views.edit_fruit, name="edit-fruit"),
                path("delete/", views.delete_fruit, name="delete-fruit"),
            ]
        ),
    ),
]
