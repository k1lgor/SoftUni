from album.models import Album
from django.shortcuts import redirect, render
from user.models import Profile


def profile_details(request):
    profile = Profile.objects.first()
    all_albums = len(Album.objects.all())
    context = {"profile": profile, "all_albums": all_albums}
    return render(request, "profile-details.html", context)


def delete_profile(request):
    if request.method == "POST":
        profile = Profile.objects.first()
        profile.delete()
        Album.objects.all().delete()
        return redirect("home-page")
    return render(request, "profile-delete.html")
