from django import forms
from django.forms import ModelForm
from .models import GameRoom

#Game room form for creating game room without using Admin page
class GameRoomForm(ModelForm):
    class Meta:
        model = GameRoom
        fields = ('room_name', 'max_players')
