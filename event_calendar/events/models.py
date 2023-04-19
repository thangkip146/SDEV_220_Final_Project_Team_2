from django.db import models
class MagicCornerUser(models.Model):
    first_name = models.CharField('First Name', max_length=30)
    last_name = models.CharField('Last Name', max_length=30)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
class GameRoom(models.Model):
    room_number = models.IntegerField('Room Number')
    max_players = models.IntegerField('Max Players')
    is_full = models.BooleanField(blank=False, null=False)

    def __str__(self):
        return self.name

class Event(models.Model):
    game_name = models.CharField('Game Name', max_length=120)
    game_date = models.DateTimeField('Game Date')
    game_room = models.ForeignKey(GameRoom, blank=True, null=True, on_delete=models.CASCADE)
    table_host = models.CharField('Game Host', max_length=60)
    game_description = models.TextField(blank=True)
    players = models.ManyToManyField(MagicCornerUser, blank=True)
    def __str__(self):
        return self.name
    
