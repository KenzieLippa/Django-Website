from django.shortcuts import render

# Create your views here.
def BaseView(req):
    # model = Profile
    template_name = 'fightingTest/test.html'
    return render(req, template_name)

    