from django.shortcuts import redirect, render

from fruits.models import Fruit

from .forms import CreateProfileForm, DeleteProfileForm, EditProfileForm
from .models import Profile


def create_profile(request):
    profile = Profile.objects.first()
    form = CreateProfileForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return render(request, "dashboard.html")
    context = {"form": form, "profile": profile}
    return render(request, "create-profile.html", context)


def profile_details(request):
    profile = Profile.objects.first()
    post_count = Fruit.objects.filter(owner=profile).count()
    context = {"profile": profile, "post_count": post_count}
    return render(request, "details-profile.html", context)


def edit_profile(request):
    profile = Profile.objects.first()
    form = EditProfileForm(request.POST or None, instance=profile)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("profile-details")
    context = {"form": form, "profile": profile}
    return render(request, "edit-profile.html", context)


def delete_profile(request):
    profile = Profile.objects.first()
    form = DeleteProfileForm(request.POST or None, instance=profile)
    if request.method == "POST":
        profile.delete()
        return redirect("index")
    context = {"form": form, "profile": profile}
    return render(request, "delete-profile.html", context)
