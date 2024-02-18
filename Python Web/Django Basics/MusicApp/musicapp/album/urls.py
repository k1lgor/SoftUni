from django.urls import path

from .views import add_album, album_details, delete_album, edit_album, home_page

urlpatterns = [
    path("", home_page, name="home-page"),
    path("album/add/", add_album, name="add-album"),
    path("album/details/<int:pk>/", album_details, name="album-details"),
    path("album/edit/<int:pk>/", edit_album, name="edit-album"),
    path("album/delete/<int:pk>/", delete_album, name="delete-album"),
]
