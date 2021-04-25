from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
import time


gaming_list1 = []
gaming_list2 = []
gaming_list3 = []

for element in range(3):
    gaming_list1.append('-')
    gaming_list2.append('-')
    gaming_list3.append('-')


def index(request):
    return render(request, "Welcome.html")

states = ' '
def game(request, num):
    #THere is delay in win

    if request.method == "POST":
        Player_one = request.POST['Player_one']
        Player_two = request.POST['Player_two']
    global states
    if num < 3:
        if  gaming_list1[num] == '-':
            if states == ' ' or states == 'O':
                gaming_list1[num]= 'X'
                states = 'X'
            else:
                gaming_list1[num]= 'O'
                states = 'O'
    elif num < 6:
        if gaming_list2[num-3] == '-':
            if states == ' ' or states == 'O':
                gaming_list2[num-3]= 'X'
                states = 'X'
            else:
                gaming_list2[num-3]= 'O'
                states = 'O'
    elif num < 9:
        if gaming_list3[num-6] == '-':
            if states == ' ' or states == 'O':
                gaming_list3[num-6]= 'X'
                states = 'X'
            else:
                gaming_list3[num-6]= 'O'
                states = 'O'
    wins = win()
    if(wins):
        if wins == 'X':
            playe_win = "player one "
        else:
            playe_win = "player two "
        return render(request, "win.html",{
            "game_list1":gaming_list1,
            "game_list2":gaming_list2,
            "game_list3":gaming_list3,
            "winner":win,
            "playe_win":playe_win.capitalize(),
        })


    return render(request, "tic.html",{
        "game_list1":gaming_list1,
        "game_list2":gaming_list2,
        "game_list3":gaming_list3
    })

def win():
    game_list = gaming_list1+gaming_list2+gaming_list3
    win = False
    for i in range(0,9,3):
        if game_list[i] == game_list[i+1] == game_list[i+2] != '-':
            win = game_list[i]
    for i in range(0,3):
        if game_list[i] == game_list[i+3] == game_list[i+6] != '-':
            win = game_list[i]

    if game_list[0] == game_list[4] == game_list[8] != '-':
        win = game_list[0]

    if game_list[2] == game_list[4] == game_list[6] != '-':
        win = game_list[2]

    return win
