from django.shortcuts import render, redirect
from .forms import ProfileCreateForm, FruitCreateForm, FruitEditForm, FruitDeleteForm, ProfileEditForm
from .models import Profile, Fruit


def get_profile():
    profile = Profile.objects.first()
    return profile


def index(request):
    return render(request, 'index.html')


def profile_create(request):
    form = ProfileCreateForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'create-profile.html', context)


def profile_details(request):
    profile = get_profile()
    fruit_numbers = Fruit.objects.count()

    context = {
        'profile': profile,
        'posts': fruit_numbers,
    }

    return render(request, 'details-profile.html', context)


def profile_edit(request):
    profile = Profile.objects.first()
    form = ProfileEditForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile-details')

    context = {
        'form': form,
        'profile': profile
    }

    return render(request, 'edit-profile.html', context)


def profile_delete(request):
    profile = Profile.objects.first()
    fruits = Fruit.objects.all()
    if request.method == 'POST':
        profile.delete()
        fruits.delete()
        return redirect('index')

    return render(request, 'delete-profile.html')


def dashboard(request):
    fruits = Fruit.objects.all()

    context = {
        'fruits': fruits
    }

    return render(request, 'dashboard.html', context)


def fruit_create(request):
    if request.method == "GET":
        form = FruitCreateForm()
    else:
        form = FruitCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'create-fruit.html', context)


def fruit_details(request, pk):
    fruit = Fruit.objects.filter(pk=pk).get()

    context ={
        'fruit': fruit
    }
    return render(request, 'details-fruit.html', context)


def fruit_edit(request, pk):
    fruit = Fruit.objects.filter(pk=pk).get()
    form = FruitEditForm(request.POST or None, instance=fruit)

    if form.is_valid():
        form.save()

        return redirect('dashboard')
    context = {
        'form': form,
        'fruit': fruit,
    }

    return render(request, 'edit-fruit.html', context)


def fruit_delete(request, pk):
    fruit = Fruit.objects.filter(pk=pk).get()
    form = FruitDeleteForm(request.POST or None, instance=fruit)

    if form.is_valid():
        form.save()

        return redirect('dashboard')

    context = {
        'form': form,
        'fruit': fruit,
    }

    return render(request, 'delete-fruit.html', context)
