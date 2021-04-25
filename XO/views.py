from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
import time

# Create your views here.
#gi
gaming_list1 = []
gaming_list2 = []
gaming_list3 = []

for element in range(3):
    gaming_list1.append('-')
    gaming_list2.append('-')
    gaming_list3.append('-')

states = ' '
def index(request, num):
    #THere is delay in win
    if(win()):
        return render(request, "win.html",{
            "game_list1":gaming_list1,
            "game_list2":gaming_list2,
            "game_list3":gaming_list3,
            "winner":win
        })
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
