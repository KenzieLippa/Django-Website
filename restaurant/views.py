from django.shortcuts import render
import random
import time
from datetime import datetime, timedelta
# Create your views here.

Menu_Items = [
    {'name': 'Mr Squids Nachos', 'price': 13.99, 'image': 'mrSquidsNachos.png'},
    {'name':'Remies Salad', 'price': 5.01, 'image':'RatApprovedSalad.png'},
    {'name': 'Fly Away Fries', 'price': 3.51, 'image':'FlieFries.png'},
    {'name': 'Choco Flame', 'price': 4.51, 'image': 'lavaCake.png'},
    {'name': 'Pyschic Cookie', 'price': 9.99, 'image': 'eyeCookie.png'},
    {'name': 'Rat Bat Squid Burger Supreme', 'price': 29.99, 'image': 'theSpecial.png'}
    # can add more as well
]

def main(req):
    '''show the main page'''
    template_name = "restaurant/main.html"
    return render(req, template_name)

def order(req):
    '''base func to render order pageg'''
    # pick random item from menu to be the special
    daily_special = random.choice(Menu_Items)

    context = {
        'menu_items':Menu_Items,
        'daily_special':daily_special,
        
    }
    template_name = "restaurant/order.html"
    return render(req, template_name, context)

def confirmation(req):
    '''process the order and continue'''
    template_name = "restaurant/confirmation.html"
    # ready_time = time.localtime()
    
    if req.POST:
        # get selected items from the form
        order_items = req.POST.getlist('items')
        customer_name = req.POST.get('name')
        customer_phone = req.POST. get('phone')
        customer_email = req.POST.get('email')
        special_instructions = req.POST.get('instructions')

        total_price = 0
        ordered_items = []

        # add items to list and then calculate the price

        for item_name in order_items:
            for item  in Menu_Items:
                if item['name'] == item_name:
                    ordered_items.append(item)
                    total_price += item['price']


        # calculate the ready time
        ready_time = datetime.now() + timedelta(minutes=random.randint(30, 60))
        formatted_ready = ready_time.strftime("%H:%M")

        context = {
            'customer_name': customer_name,
            'customer_phone': customer_phone,
            'customer_email': customer_email,
            'ordered_items':ordered_items,
            'total_price': round(total_price,2),
            'special_instructions': special_instructions,
            'ready_time': formatted_ready
        }

        return render(req, template_name, context)
    # send it back to the main order page if no post request
    return render(req, 'restaurant/order.html')