from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.contrib.auth.models import User
from .models import Event, MagicCornerUser, GameRoom
from .forms import GameRoomForm, EventFormAdmin, EventFormUser
from django.http import HttpResponseRedirect
from django.contrib import messages

#Default to current Month and Year
def index(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    #Render page using the year and month passed from the url or default if not passed
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

    #get games by date
    games_list = Event.objects.filter(
        game_date__year = year,
        game_date__month = month_number
    )
    #get user's name if they are logged in
    name=request.user
    return render(request, 'events/index.html', {
        "year":year,
        "month":month,
        "month_number":month_number,
        "cal":cal,
        "current_year":current_year,
        "current_month":current_month,
        "games_list":games_list,
        "name":name,
    })

#Page to list all the registered games in one list
def all_games(request):
    game_list = Event.objects.all().order_by('game_date', 'game_name')
    return render(request, 'events/game_list.html',
                  {'game_list': game_list})

#Page to list individual game
def show_game(request, game_id):
    game = Event.objects.get(pk=game_id)
    return render(request, 'events/game.html',
                  {'game': game})

#page to display search games results
def search_games(request):
    if request.method == "POST":
        searched = request.POST['searched']
        games = Event.objects.filter(game_name__contains = searched)
        return render(request, 'events/search_games.html', {'searched':searched,
                                                            'games':games})
    else:
        return render(request, 'events/search_games.html', {})

#page to add new games to the calendar
def add_game(request):
    submitted = False
    #Validate if form is being submitted to post to database
    if request.method == "POST":
        #Test for admin vs standard user and load appropriate form
        if request.user.is_superuser:
            form = EventFormAdmin(request.POST)
            if form.is_valid:
                form.save()
                return HttpResponseRedirect('/add_game?submitted=True/')
        else:
            form = EventFormUser(request.POST)
            if form.is_valid():
                new_game = form.save(commit=False)
                new_game.table_host = request.user
                new_game.save()
                return HttpResponseRedirect('/add_game?submitted=True/')
    else:
        if request.user.is_superuser:
            form = EventFormAdmin(request.POST)
        else:
            form = EventFormUser(request.POST)
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, 'events/add_game.html',
                  {'form':form, 'submitted': submitted})

#page to edit/update games
def update_game(request, game_id):
    game = Event.objects.get(pk=game_id)
    if request.user.is_superuser:
        form = EventFormAdmin(request.POST or None, instance=game)
    else:
        form = EventFormUser(request.POST or None, instance=game)
    if form.is_valid():
        form.save()
        return redirect('list-games')
    return render(request, 'events/update_game.html',
                  {'game': game,
                   'form':form})

#page to delete game
def delete_game(request, game_id):
    game = Event.objects.get(pk=game_id)
    if request.user == game.table_host:
        game.delete()
        messages.success(request, "Game Canceled")
        return redirect('list-games')
    else:
        messages.success(request, "Not Authorized to cancel this game")
        return redirect('list-games')

#Page to add new game rooms (locked behind page admin access only)
def add_room(request):
    submitted = False
    #Validate if form is being submitted to post to database
    if request.method == "POST":
        form = GameRoomForm(request.POST)
        if form.is_valid():
            new_room = form.save(commit=False)
            new_room.table_host = request.user
            new_room.save()
            return HttpResponseRedirect('/add_room?submitted=True/')

    else:
        form = GameRoomForm
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, 'events/add_room.html',
                  {'form':form, 'submitted': submitted})

#page to show all game rooms
def all_rooms(request):
    room_list = GameRoom.objects.all()
    return render(request, 'events/rooms_list.html',
                  {'room_list': room_list})

#page to show individual game rooms
def show_room(request, room_id):
    room = GameRoom.objects.get(pk=room_id)
    return render(request, 'events/room.html',
                  {'room': room})

#page to update the room tables
def update_room(request, room_id):
    room = GameRoom.objects.get(pk=room_id)
    form = GameRoomForm(request.POST or None, instance=room)
    if form.is_valid():
        form.save()
        return redirect('list-rooms')
    return render(request, 'events/update_room.html',
                  {'room': room,
                   'form':form})

#page to delete a room
def delete_room(request, room_id):
    room = GameRoom.objects.get(pk=room_id)
    room.delete()
    return redirect('list-rooms')