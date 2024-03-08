from django.shortcuts import render

from profiles.models import Profile


def index(request):
    profile = Profile.objects.first()
    if profile is None:
        return render(request, "web/index.html")
    return render(request, "web/index.html", {"profile": profile})
