from django.shortcuts import redirect, render
from user_profile.models import Profile

from .forms import CreateFruitForm, DeleteFruitForm, EditFruitForm
from .models import Fruit


def index(request):
    profile = Profile.objects.first()
    context = {"profile": profile}
    return render(request, "index.html", context)


def dashboard(request):
    profile = Profile.objects.first()
    fruits = Fruit.objects.all()
    context = {"fruits": fruits, "profile": profile}
    return render(request, "dashboard.html", context)


def create_fruit(request):
    profile = Profile.objects.first()
    form = CreateFruitForm(request.POST or None)
    if request.method == "POST" and form.is_valid:
        form.instance.owner = profile
        form.save()
        return redirect("dashboard")
    context = {"form": form, "profile": profile}

    return render(request, "create-fruit.html", context)


def fruit_details(request, pk):
    fruit = Fruit.objects.get(pk=pk)
    profile = Profile.objects.first()
    context = {"fruit": fruit, "profile": profile}
    return render(request, "details-fruit.html", context)


def edit_fruit(request, pk):
    fruit = Fruit.objects.get(pk=pk)
    profile = Profile.objects.first()
    form = EditFruitForm(instance=fruit)
    if request.method == "POST":
        form = EditFruitForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    context = {"fruit": fruit, "profile": profile, "form": form}
    return render(request, "edit-fruit.html", context)


def delete_fruit(request, pk):
    fruit = Fruit.objects.get(pk=pk)
    profile = Profile.objects.first()
    form = DeleteFruitForm(instance=fruit)
    if request.method == "POST":
        fruit.delete()
        return redirect("dashboard")
    context = {"fruit": fruit, "profile": profile, "form": form}
    return render(request, "delete-fruit.html", context)
