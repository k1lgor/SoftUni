from album.forms import CreateAlbumForm, DeleteAlbumForm
from album.models import Album
from django.shortcuts import redirect, render
from user.forms import CreateProfileForm
from user.models import Profile


# Create your views here.
def home_page(request):
    profile = Profile.objects.first()
    albums = Album.objects.all()
    if profile:
        template = "home-with-profile.html"
        context = {"profile": profile, "albums": albums}
    else:
        template = "home-no-profile.html"
        if request.method == "POST":
            form = CreateProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("home-page")
        else:
            form = CreateProfileForm()
        context = {"form": form}
    return render(request, template, context)


def add_album(request):
    profile = Profile.objects.first()
    if request.method == "POST":
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home-page")
        context = {"form": form, "profile": profile}
        return render(request, "add-album.html", context)
    form = CreateAlbumForm()
    context = {"form": form, "profile": profile}
    return render(request, "add-album.html", context)


def album_details(request, pk):
    album = Album.objects.get(id=pk)
    context = {"album": album}
    return render(request, "album-details.html", context)


def edit_album(request, pk):
    album = Album.objects.get(id=pk)
    if request.method == "GET":
        context = {"form": CreateAlbumForm(initial=album.__dict__)}
        return render(request, "edit-album.html", context)
    else:
        form = CreateAlbumForm(request.POST, instance=album)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect("home-page")
        else:
            context = {"form": form}
            return render(request, "edit-album.html", context)


def delete_album(request, pk):
    album = Album.objects.get(id=pk)
    if request.method == "POST":
        album.delete()
        return redirect("home-page")

    form = DeleteAlbumForm(instance=album)
    context = {"form": form, "profile": Profile.objects.first()}
    return render(request, "delete-album.html", context)
