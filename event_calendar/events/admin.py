from django.contrib import admin
from .models import Event
from .models import MagicCornerUser
from .models import GameRoom

admin.site.register(Event)
admin.site.register(MagicCornerUser)
admin.site.register(GameRoom)

