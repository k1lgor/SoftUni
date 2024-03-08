from django.shortcuts import redirect, render
from user_profile.models import Profile

from .forms import CreatePlantForm, DeletePlantForm
from .models import Plant


def home(request):
    profile = Profile.objects.first()
    context = {"profile": profile}
    return render(request, "home-page.html", context)


def catalogue(request):
    plants = Plant.objects.all()
    context = {"plants": plants}
    return render(request, "catalogue.html", context)


def create_plant(request):
    form = CreatePlantForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("catalogue")
    context = {
        "form": form,
    }
    return render(request, "create-plant.html", context)


def edit_plant(request, plant_id):
    plant = Plant.objects.get(id=plant_id)

    if request.method == "GET":
        context = {"form": CreatePlantForm(initial=plant.__dict__)}
        return render(request, "edit-plant.html", context)
    else:
        form = CreatePlantForm(request.POST, instance=plant)

        if form.is_valid():
            form.save()
            return redirect("catalogue")
        else:
            context = {"form": form}
            return render(request, "edit-plant.html", context)


def delete_plant(request, plant_id):
    plant = Plant.objects.get(id=plant_id)

    if request.method == "POST":
        plant.delete()
        return redirect("catalogue")

    form = DeletePlantForm(instance=plant)
    context = {"form": form}

    return render(request, "delete-plant.html", context)


def plant_details(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    context = {"plant": plant}
    return render(request, "plant-details.html", context)
