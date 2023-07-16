from django.shortcuts import render, redirect

from .forms import CreateProfileForm, CreateGameForm, EditGameForm, DeleteGameForm, EditProfileForm, DeleteProfileForm
from .models import ProfileModel, GameModel


def get_profile():
    try:
        return ProfileModel.objects.all()

    except ProfileModel.DoesNotExist:
        return None


def home(request):
    context = {'profile': get_profile()}
    return render(request, 'home/home-page.html', context)


def dashboard(request):
    games = GameModel.objects.all()
    context = {'games': games, 'profile': get_profile()}
    return render(request, 'game/dashboard.html', context)


def profile_details(request):
    profile = get_profile().get()
    games = GameModel.objects.all().count()

    if games:
        average_rating = sum(g.rating for g in GameModel.objects.all()) / games
    else:
        average_rating = 0

    context = {
        'profile': profile,
        'games_qty': games,
        'rating_average': average_rating
    }

    return render(request, 'profiles/details-profile.html', context)


def profile_create(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {"form": form, 'profile': get_profile()}

    return render(request, 'profiles/create-profile.html', context)


def profile_edit(request):
    profile = get_profile().get()

    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profiles details')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profiles/edit-profile.html', context)


def profile_delete(request):
    profile = get_profile().get()

    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profiles/delete-profile.html', context)


def game_create(request):
    if request.method == 'GET':
        form = CreateGameForm()
    else:
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {"form": form, 'profile': get_profile()}

    return render(request, 'game/create-game.html', context)


def game_details(request, pk):
    game = GameModel.objects.get(pk=pk)
    context = {'game': game, 'profile': get_profile()}

    return render(request, 'game/details-game.html', context)


def game_edit(request, pk):
    game = GameModel.objects.get(pk=pk)

    if request.method == 'GET':
        form = EditGameForm(instance=game)
    else:
        form = EditGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'game': game,
        'profile': get_profile(),
    }

    return render(request, 'game/edit-game.html', context)


def game_delete(request, pk):
    game = GameModel.objects.get(pk=pk)

    if request.method == 'GET':
        form = DeleteGameForm(instance=game)
    else:
        form = DeleteGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'game': game,
        'profile': get_profile(),
    }

    return render(request, 'game/delete-game.html', context)
