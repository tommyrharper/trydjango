from django.http import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): # *args, **kwargs
  print('request: ', request)
  print('args: ', args, 'kwargs: ', kwargs)
  print(request.user)
  # return HttpResponse("<h1>Hello World</h1>") # string of HTML code
  return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
  # return HttpResponse("<h1>Contact</h1>")
  return render(request, "contact.html", {})

def social_view(request, *args, **kwargs):
  # return HttpResponse("<h1>Social</h1>")
  return render(request, "social.html", {})

def about_view(request, *args, **kwargs):
  # return HttpResponse("<h1>About</h1>")
  return render(request, "about.html", {})