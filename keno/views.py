import random
from django.shortcuts import redirect, render
from django.http import JsonResponse

# Create your views here.
def kenoBase(req):
    '''show the main page'''
    template_name = "keno/home.html"
   
    return render(req, template_name)

def kenoCard(req):
    template_name = "keno/card.html"
    # if req.method == "POST":
    #     return redirect('keno_game')
    # if req.method == "POST":
    #     max_selection = int(req.POST.get('max_selection_hidden', 1))
    #     selected_buttons = req.POST.get('selected_buttons', '')
    #     selected_buttons = [int(x) for x in selected_buttons.split(',')] if selected_buttons else []
    #     if len(selected_buttons) > max_selection:
    #         #handle the error
    #         return render(req, template_name, {
    #             'range_80':range(1,81),
    #             'selected_buttons': [],
    #             'error_message': f'You can only select up to {max_selection} spots.'
    #         })
    #     # return redirect('createKeno', )
    
    # else:
    #     max_selection = 1
    #     selected_buttons = []


    context = {
        'range_80':range(1,81),
        'selected_buttons':[],
        'max_selection' : 1,
        'money_per_game':1,

    }
   
    return render(req, template_name, context)

def chose_20():
    numbers = []
    i = 0
    while i < 20:
        number = random.randint(1,80)
        if number not in numbers:
            numbers.append(number)
            i+=1
    numbers.sort()
    return numbers

def find_matches(numbers, chosen):
    counter = 0
    for i in numbers:
        for x in chosen:
            if i == x:
                counter +=1

    return counter

def createKeno(req):
    # TODO add the game id back in 
    '''the place where the post request from the save js comes'''
    print("pre post")
    template_name = "keno/game.html"
    if req.method == "POST":
        print("post")
        max_selection = int(req.POST.get('max_selection_hidden', 1))
        selected_buttons = req.POST.get('selected_buttons', '')
        print("seleceted buttons: ", selected_buttons)
        selected_buttons = [int(x) for x in selected_buttons.split(',')] if selected_buttons else []
        money_per_game = int(req.POST.get('moneyPerGame',1))
    
        if len(selected_buttons) > max_selection:
            #handle the error
            return render(req, template_name, {
                'range_80':range(1,81),
                'selected_buttons': [],
                'error_message': f'You can only select up to {max_selection} spots.'
            })
    
    else:
        max_selection = 1
        selected_buttons = []
        money_per_game = 1

    choices = chose_20()
    counter = find_matches(choices, selected_buttons)




    context = {
        'range_80':range(1,81),
        'selected_buttons':selected_buttons,
        'max_selection' : max_selection,
        'money_per_game': money_per_game,
        '20_chosen': choices,
        'counter' : counter
    }
   
    return render(req, template_name, context)