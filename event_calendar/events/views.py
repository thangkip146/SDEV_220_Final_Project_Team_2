from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event, MagicCornerUser, GameRoom


#Default to current Month and Year
def index(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    #Render page using the year and month passed from the url or default if not passed
    name = "Nathan"
    #ensure the month from url has capital so it is recognized by calendar
    month = month.title()
    #Convert month from name to number
    month_number = int(list(calendar.month_name).index(month))

    #create the calendar from information provided
    cal = HTMLCalendar().formatmonth(
        year, 
        month_number)
    #get current year and month
    now = datetime.now()
    current_year = now.year
    current_month = now.month

    #month_number = int(month_number)
    return render(request, 'events/index.html', {
        "year":year,
        "month":month,
        "name": name,
        "month_number":month_number,
        "cal":cal,
        "current_year":current_year,
        "current_month":current_month,
    })

def all_games(request):
    game_list = Event.objects.all()
    return render(request, 'events/game_list.html',
                  {'game_list': game_list})