from django.shortcuts import redirect, render
from plants.models import Plant

from .forms import CreateProfileForm, EditProfileForm
from .models import Profile


def create_profile(request):
    if request.method == "POST":
        form = CreateProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("catalogue")
    else:
        form = CreateProfileForm()

    context = {"form": form}

    return render(request, template_name="create-profile.html", context=context)


def edit_profile(request):
    profile = Profile.objects.first()

    if request.method == "GET":
        context = {"form": EditProfileForm(initial=profile.__dict__)}
        return render(request, "edit-profile.html", context)
    else:
        form = EditProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()

            return redirect("profile-details")
        else:
            context = {"form": form}

            return render(request, "edit-profile.html", context)


def delete_profile(request):
    profile = Profile.objects.first()
    plants = Plant.objects.all()

    if request.method == "POST":
        profile.delete()
        plants.delete()

        return redirect("home")

    return render(request, "delete-profile.html")


def profile_details(request):
    profile = Profile.objects.first()
    all_plants = len(Plant.objects.all())

    context = {"profile": profile, "all_plants": all_plants}

    return render(request, template_name="profile-details.html", context=context)
