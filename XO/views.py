from django.shortcuts import render
from django.http import HttpResponse

#Testing waiting winning approch
gaming_list1 = []
gaming_list2 = []
gaming_list3 = []

for element in range(3):
    gaming_list1.append('-')
    gaming_list2.append('-')
    gaming_list3.append('-')

states = ' '
def index(request, num):
    #lma agy anady 3la el index mn el code adeha ay rakm fo2 el 9
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
