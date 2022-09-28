from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Members
from django.urls import reverse

# Create your views here.


def index(request):
    template = loader.get_template("index.html")

    return HttpResponse(template.render())

def members(request):
    allMembers = Members.objects.all().values()
    output = ""
    for member in allMembers:
        output += member["firstname"]    
    return HttpResponse(allMembers)

def tables(request):
    allMembers = Members.objects.all().values()
    template = loader.get_template("temp.html")
    context = {
        "listofMembers" : allMembers
        }
    return HttpResponse(template.render(context, request))    

def add(request):
    template = loader.get_template("add.html")
    return HttpResponse(template.render({}, request))

def addrecord(request):
    x = request.POST["first"]
    y = request.POST["last"]
    member = Members(firstname= x, lastname=y)
    member.save()
    return HttpResponseRedirect(reverse("list"))

def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse("list"))    

def update(request, id):
    member = Members.objects.get(id=id)
    template = loader.get_template("update.html")
    context = {
        "member" : member
        }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    fname = request.POST["fname"]
    lname = request.POST["lname"]
    member = Members.objects.get(id=id)
    member.firstname = fname
    member.lastname = lname
    member.save()
    return HttpResponseRedirect(reverse("list"))
