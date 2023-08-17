from django.shortcuts import render, redirect
from eventer_app.web.forms import CreateProfileForm, CreateEventForm, EditEventForm, DeleteEventForm, EditProfileForm, \
    DeleteProfileForm
from eventer_app.web.models import ProfileModel, EventModel


def get_profile():
    try:
        return ProfileModel.objects.all()

    except ProfileModel.DoesNotExist:
        return None


def index(request):
    context = {'profile': get_profile()}
    return render(request, 'shared/home-page.html', context)


def profile_create(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {"form": form, 'profile': get_profile()}

    return render(request, 'profiles/profile-create.html', context)


def dashboard(request):
    events = EventModel.objects.all()
    context = {'events': events, 'profile': get_profile()}
    return render(request, 'events/dashboard.html', context)


def profile_details(request):
    profile = get_profile().first()
    events_count = EventModel.objects.count()

    context = {
        'profile': profile,
        'events_count': events_count,
    }

    return render(request, 'profiles/profile-details.html', context)


def profile_edit(request):
    profile = get_profile().get()

    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profiles/profile-edit.html', context)


def profile_delete(request):
    profile = get_profile().get()

    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profiles/profile-delete.html', context)


def event_create(request):
    if request.method == 'GET':
        form = CreateEventForm()
    else:
        form = CreateEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {"form": form, 'profile': get_profile()}

    return render(request, 'events/event-create.html', context)


def event_details(request, pk):
    event = EventModel.objects.get(pk=pk)
    context = {'event': event, 'profile': get_profile()}

    return render(request, 'events/events-details.html', context)


def event_edit(request, pk):
    event = EventModel.objects.get(pk=pk)

    if request.method == 'GET':
        form = EditEventForm(instance=event)
    else:
        form = EditEventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'event': event,
        'profile': get_profile(),
    }

    return render(request, 'events/event-edit.html', context)


def event_delete(request, pk):
    event = EventModel.objects.get(pk=pk)

    if request.method == 'GET':
        form = DeleteEventForm(instance=event)
    else:
        form = DeleteEventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'event': event,
        'profile': get_profile(),
    }

    return render(request, 'events/events-delete.html', context)
