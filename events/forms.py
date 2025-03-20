from django import forms
from events.models import Event, Participant, Category

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'time', 'location', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'border border-gray-300 rounded p-2 w-full'}),
            'description': forms.Textarea(attrs={'class': 'border border-gray-300 rounded p-2 w-full'}),
            'date': forms.SelectDateWidget(attrs={'class': 'border border-gray-300 rounded p-2 w-full'}),
            'time': forms.TimeInput(attrs={'class': 'border border-gray-300 rounded p-2 w-full'}),
            'location': forms.TextInput(attrs={'class': 'border border-gray-300 rounded p-2 w-full'}),
            'category': forms.Select(attrs={'class': 'border border-gray-300 rounded p-2 w-full'}),
        }

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'email', 'events']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'border border-gray-300 rounded p-2 w-full'}),
            'email': forms.EmailInput(attrs={'class': 'border border-gray-300 rounded p-2 w-full'}),
            'events': forms.CheckboxSelectMultiple(attrs={'class': 'border border-gray-300 rounded p-2 w-full'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'border border-gray-300 rounded p-2 w-full'}),
            'description': forms.Textarea(attrs={'class': 'border border-gray-300 rounded p-2 w-full'}),
        }