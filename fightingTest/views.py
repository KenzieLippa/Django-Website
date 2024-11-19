from django.shortcuts import render

# Create your views here.
def BaseView(req):
    # model = Profile
    template_name = 'FightingTest/test.html'
    return render(req, template_name)

    