from django.http import HttpResponse
from django.shortcuts import render
import wikipedia,webbrowser

def getPage(request):
    wikipage = wikipedia.random(1)        
    wikiload = wikipedia.page(wikipage)

    return render(request, "index.html", {"wikipage" : wikipage})

def yes(request):       
    wikipage = wikipedia.random(1)  
    wikiload = wikipedia.page(wikipage)

    return render(request, "index.html", {"wikiload" : wikiload})
    