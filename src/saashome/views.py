# from django.http import HttpResponse
from django.shortcuts import render,redirect
# There are two ways to render Document in Django , one is throught the Django way and other way is through python way.
# import pathlib # this is to deal with the Directory and File System
# this_dir = pathlib.Path(__file__).resolve().parent # this will give the Directory of the Parent

# This is the Pythonic Way to do things.
# def index(request,*args, **kwargs):# Here I have made this error free that it can take anytype of arguements.
#     html_ = ""
#     html_file_path = this_dir/"home.html"
#     html_ = html_file_path.read_text()
#     return HttpResponse(html_)

def index(request):
    context = {
        "title": "Home Page",
    }
    html_template = "saashome/home.html"
    return render(request,html_template,context)