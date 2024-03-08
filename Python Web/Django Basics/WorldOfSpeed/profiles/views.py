from django.shortcuts import redirect, render

from cars.models import Car
from profiles.forms import CreateProfileForm, DeleteProfileForm, EditProfileForm
from profiles.models import Profile


def create_profile(request):
    profile = Profile.objects.first()
    form = CreateProfileForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("catalogue")
    context = {"form": form, "profile": profile}
    return render(request, "profiles/profile-create.html", context)


def profile_details(request):
    profile = Profile.objects.first()
    total_cars = Car.objects.filter(owner=profile)
    total_price = sum(car.price for car in total_cars)
    context = {"profile": profile, "total_price": total_price}

    return render(request, "profiles/profile-details.html", context)


def edit_profile(request):
    profile = Profile.objects.first()
    form = EditProfileForm(request.POST or None, instance=profile)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("profile-details")
    context = {"form": form, "profile": profile}
    return render(request, "profiles/profile-edit.html", context)


def delete_profile(request):
    profile = Profile.objects.first()
    form = DeleteProfileForm(request.POST or None, instance=profile)
    if request.method == "POST" and form.is_valid():
        profile.delete()
        return redirect("index")
    context = {"form": form, "profile": profile}
    return render(request, "profiles/profile-delete.html", context)
