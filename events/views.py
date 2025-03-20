from django.shortcuts import render, redirect
from events.models import Event, Participant, Category
from events.forms import EventForm, ParticipantForm, CategoryForm
from django.utils import timezone
from datetime import datetime

# Create your views here.
def event_list(request):
    events = Event.objects.select_related('category').all()
    return render(request, 'event_list.html', {'events': events})

def event_detail(request, event_id):
    event = Event.objects.select_related('category').prefetch_related('participants').get(pk=event_id)
    return render(request, 'event_detail.html', {'event': event})

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})

def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_detail', event_id=event.id)
    else:
        form = EventForm(instance=event)
    return render(request, 'update_event.html', {'form': form})

def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'delete_event.html', {'event': event})

def participant_list(request):
    participants = Participant.objects.prefetch_related('events').all()
    return render(request, 'participant_list.html', {'participants': participants})

def participant_detail(request, participant_id):
    participant = Participant.objects.prefetch_related('events').get(pk=participant_id)
    return render(request, 'participant_detail.html', {'participant': participant})

def create_participant(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('participant_list')
    else:
        form = ParticipantForm()
    return render(request, 'create_participant.html', {'form': form})

def update_participant(request, participant_id):
    participant = Participant.objects.get(pk=participant_id)
    if request.method == 'POST':
        form = ParticipantForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            return redirect('participant_detail', participant_id=participant.id)
    else:
        form = ParticipantForm(instance=participant)
    return render(request, 'update_participant.html', {'form': form})

def delete_participant(request, participant_id):
    participant = Participant.objects.get(pk=participant_id)
    if request.method == 'POST':
        participant.delete()
        return redirect('participant_list')
    return render(request, 'delete_participant.html', {'participant': participant})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def category_detail(request, category_id):
    category = Category.objects.prefetch_related('event_set').get(pk=category_id)
    return render(request, 'category_detail.html', {'category': category})

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'create_category.html', {'form': form})

def update_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_detail', category_id=category.id)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'update_category.html', {'form': form})

def delete_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'delete_category.html', {'category': category})

def organizer_dashboard(request):
    total_participants = Participant.objects.count()
    total_events = Event.objects.count()
    upcoming_events = Event.objects.filter(date__gte=timezone.now()).count()
    past_events = Event.objects.filter(date__lt=timezone.now()).count()
    todays_events = Event.objects.filter(date=datetime.today().date())

    context = {
        'total_participants': total_participants,
        'total_events': total_events,
        'upcoming_events': upcoming_events,
        'past_events': past_events,
        'todays_events': todays_events,
    }

    return render(request, 'organizer_dashboard.html', context)