from django.shortcuts import redirect, render

from cars.forms import CreateCarForm, DeleteCarForm, EditCarForm
from cars.models import Car
from profiles.models import Profile


def catalogue(request):
    cars = Car.objects.all()
    profile = Profile.objects.first()
    context = {
        "cars": cars,
        "profile": profile,
    }
    return render(request, "cars/catalogue.html", context)


def create_car(request):
    profile = Profile.objects.first()
    form = CreateCarForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.instance.owner = profile
        form.save()
        return redirect("catalogue")
    context = {"form": form, "profile": profile}
    return render(request, "cars/car-create.html", context)


def car_details(request, pk):
    profile = Profile.objects.first()
    car = Car.objects.get(pk=pk)

    context = {
        "car": car,
        "profile": profile,
    }
    return render(request, "cars/car-details.html", context)


def edit_car(request, pk):
    profile = Profile.objects.first()
    car = Car.objects.get(pk=pk)
    form = EditCarForm(request.POST or None, instance=car)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("catalogue")

    context = {
        "car": car,
        "profile": profile,
        "form": form,
    }
    return render(request, "cars/car-edit.html", context)


def delete_car(request, pk):
    profile = Profile.objects.first()
    car = Car.objects.get(pk=pk)
    form = DeleteCarForm(request.POST or None, instance=car)
    if request.method == "POST" and form.is_valid():
        car.delete()
        return redirect("catalogue")
    context = {
        "car": car,
        "profile": profile,
        "form": form,
    }
    return render(request, "cars/car-delete.html", context)
