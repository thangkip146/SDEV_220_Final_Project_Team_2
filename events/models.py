from django.db import models
from django.contrib.auth.models import User

class MagicCornerUser(models.Model):
    first_name = models.CharField('First Name', max_length=30)
    last_name = models.CharField('Last Name', max_length=30)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
class GameRoom(models.Model):
    room_name = models.CharField('Room Name', max_length=30, blank=True)
    max_players = models.IntegerField('Max Players')
    owner = models.IntegerField(blank=False, default=1)

    def __str__(self):
        return str(self.room_name)

class Event(models.Model):
    game_name = models.CharField('Game Name', max_length=120)
    game_date = models.DateTimeField('Game Date')
    game_room = models.ForeignKey(GameRoom, blank=True, null=True, on_delete=models.CASCADE)
    table_host = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    game_description = models.TextField(blank=True)
    players = models.ManyToManyField(MagicCornerUser, blank=True)

    def __str__(self):
        return self.game_name
    
