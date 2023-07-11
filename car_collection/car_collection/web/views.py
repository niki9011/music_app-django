from django.shortcuts import render, redirect

from car_collection.web.forms import CreateProfileForm, CreateCarForm, EditCarForm, DeleteCarForm
from car_collection.web.models import Profile, Car


def get_profile():
    try:
        return Profile.objects.all()

    except Profile.DoesNotExist:
        return None


def index(request):
    context = {'profile': get_profile()}
    return render(request, 'home/index.html', context)


def catalog(request):
    cars = Car.objects.all()
    context = {'cars': cars, 'profile': get_profile()}
    return render(request, 'cars/catalogue.html', context)


def profile_create(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog')

    context = {"form": form,'profile': get_profile()}

    return render(request, 'profiles/profile-create.html', context)


def profile_details(request):
    return render(request, 'profiles/profile-details.html')


def profile_edit(request):
    return render(request, 'profiles/profile-edit.html')


def profile_delete(request):
    return render(request, 'profiles/profile-delete.html')


def car_create(request):
    if request.method == 'GET':
        form = CreateCarForm()
    else:
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog')

    context = {"form": form, 'profile': get_profile()}

    return render(request, 'cars/car-create.html', context)


def car_details(request, pk):
    car = Car.objects.get(pk=pk)
    context = {'car': car, 'profile': get_profile()}

    return render(request, 'cars/car-details.html', context)


def car_edit(request, pk):
    car = Car.objects.get(pk=pk)

    if request.method == 'GET':
        form = EditCarForm(instance=car)
    else:
        form = EditCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalog')

    context = {
        'form': form,
        'car': car,
        'profile': get_profile(),
    }

    return render(request, 'cars/car-edit.html', context)


def car_delete(request, pk):
    car = Car.objects.get(pk=pk)

    if request.method == 'GET':
        form = DeleteCarForm(instance=car)
    else:
        form = DeleteCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalog')

    context = {
        'form': form,
        'car': car,
        'profile': get_profile(),
    }

    return render(request, 'cars/car-delete.html', context)
