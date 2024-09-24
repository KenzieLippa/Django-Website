from django.shortcuts import render
from django.http import HttpResponse
import random

# this material is from the challenge thingy
# def home_page_view(request):
#     return HttpResponse("Hello WOrld!")
# global views
quotes = [
    '''"Society is now separated between lions and scavengers.
The lions are people who wish to provide, who wish to produce. They are people 
who actually wish to build things. They're the innovators, the entrepreneurs the family
builders, the people who go to church and try to form a community, those are the lions in society
the scavengers are people who live off of their scraps. Those are the people who don't produce anything who are career leeches who spend all of their time talking about redistributing all of the good stuff that's produced by the lions
and every so often the lions get weak and stupid and the scavengers try to overtake and kill them but then they end up starving because it turns out that when you kill the lions there isn't anyone to hunt or reproduce"''',
'''"[Moral Relativism] means that the more evil you are the more there must be a justification to your evil because otherwise you wouldn't be evil... you believe the more evil you behave the more you have been victimized.
 The victim victimizer matrix is undefeated in terms of its stupidity and immorality." ''' ,
 '''"Never in our country’s history has a generation been so empowered, so wealthy, so privileged—and yet so empty."'''

]

images = [
    "ben.png",
    "boyscouts.png",
    "instagramMeme.png"
]


def quote_view(req):
    '''This function selects a random quote and then returns a render 
    then places this into the context which is then returned in the render call so that the page that is called
    can use it as a variable'''
    selected_quote = random.choice(quotes)
    selected_image = random.choice(images)
    print(selected_image)
    context = {
        'quote' : selected_quote,
        'image' : selected_image
    }
    return render( req, "quotes/quote.html", context)

# Create your views here.

def show_all_view(req):
    '''here we zip the combined data because it will allow us to loop through both 
    on our webpage instead of just one at a time. This results in one for loop instead of two
    we then returned the combined data as an argument like before'''
    combined_data = zip(quotes, images)
    context = {
        'combined_data':combined_data
    }
    return render(req, "quotes/show_all.html", context)

def about_view(req):
    '''here we have a new image that will allow us to see ben in all his glory
    like before we pass the image in through the context and then will use it as a variable on the front end'''
    context = {
        'image': "ben-face.png"
    }
    return render(req, "quotes/about.html", context)