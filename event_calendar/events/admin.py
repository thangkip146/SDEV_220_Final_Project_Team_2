from django.contrib import admin
from .models import Event
from .models import MagicCornerUser
from .models import GameRoom


admin.site.register(MagicCornerUser)
admin.site.register(GameRoom)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display=('game_name', 'game_date', 'table_host')
    ordering = ('game_date',)
    search_fields = ('game_name', 'game_date', 'table_host')