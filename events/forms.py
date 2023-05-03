from django import forms
from django.forms import ModelForm
from .models import GameRoom, Event

#Game room form for creating game room without using Admin page
class GameRoomForm(ModelForm):
    class Meta:
        model = GameRoom
        fields = ('room_name', 'max_players')

#Super user event form
class EventFormAdmin(ModelForm):
    class Meta:
        model = Event
        fields = ('game_name', 'game_date', 'game_room', 'table_host', 'game_description')
        labels = {
           'game_name':'Game Name' ,
           'game_date':'Game Date YYYY-MM-DD HH:MM:SS' ,
           'game_room':'Game Room' ,
           'table_host':'Table Host' ,
           'game_description':'Game Description' ,
           
        }
        widgets={
            'game_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Game Name'}),
            'game_date': forms.TextInput(attrs={'class': 'form-control','placeholder':'YYYY-MM-DD HH:MM:SS'}),
            'game_room': forms.Select(attrs={'class': 'form-select','placeholder':'Game Room'}),
            'game_host': forms.Select(attrs={'class': 'form-select','placeholder':'Game Host'}),
            'game_description': forms.Textarea(attrs={'class': 'form-control','placeholder':'Game Description'}),
        }

#Standard User Event form
class EventFormUser(ModelForm):
    class Meta:
        model = Event
        fields = ('game_name', 'game_date', 'game_room', 'game_description')
        labels = {
           'game_name':'Game Name' ,
           'game_date':'Game Date' ,
           'game_room':'Game Room' ,
           'game_description':'Game Description' ,
           
        }
        widgets={
            'game_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Game Name'}),
            'game_date': forms.TextInput(attrs={'class': 'form-control','placeholder':'YYYY-MM-DD HH:MM:SS'}),
            'game_room': forms.Select(attrs={'class': 'form-select','placeholder':'Game Room'}),
            'game_description': forms.Textarea(attrs={'class': 'form-control','placeholder':'Game Description'}),
        }