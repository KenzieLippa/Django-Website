from django.shortcuts import render, redirect


# can in future pass in context stuff lol
# Create your views here.

def show_form(request):
    template_name = "formdata/form.html"
    # build a response using our template
    return render(request, template_name)

def submit(req):
    '''stupid annoying doc string explination of 
    basic obvious and rudementary python code 
    that anyone looking at should be able to understand'''
    template_name = "formdata/submit.html"

    if req.POST:
        print(req.POST['name'])
        name = req.POST['name']
        favorite_color = req.POST['favorite_color']

        context = {
            'name': name,
            'favorite_color': favorite_color,
        }
        return render(req, template_name, context)
    
    return redirect("show_form")