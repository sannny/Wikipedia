from django.shortcuts import render
import markdown2
from django.http import HttpResponseRedirect
from . import util
from markdown2 import Markdown
from django.urls import reverse
from django.shortcuts import redirect
from django import forms
from django.shortcuts import render
from django.db.models import Q

def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')
        if query is not None:
            #lookups= Q(title__icontains=query)
                url = ('').join(['wiki/',query])
                return HttpResponseRedirect(url)
        else:
            return HttpResponseRedirect("/")


markdowner = Markdown()
Curr_entry = ""

class NewForm(forms.Form):
    page_name = forms.CharField(label="page_name")
    text = forms.CharField(widget= forms.Textarea)

class TitleForm(forms.Form):
    Title = forms.HiddenInput()
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def view_Title(request,entry):
    if request.method == "POST":
        return edit_page(request,entry)
        #return HttpResponseRedirect("/wiki/edit_entry/",entry)
    html = util.get_entry(entry)
    if html == None:
        return HttpResponseRedirect("/")
    else:
        return render(request,"encyclopedia/title.html",{
            "entries": util.list_entries(),
            "name":entry,
            "html_text": markdowner.convert(html)
        })

def edit_page(request,entry):
    if request.method == "POST":
        form = NewForm(request.POST)
        util.save_entry(form.data["page_name"],form.data["text"])
        return HttpResponseRedirect("/")
        #else:
        #    return render(request,"encyclopedia/new_entry.html",{
         #       "form":form
         #   })
    elif request.method == "GET":
        data = {"page_name" : entry,
        "text" : util.get_entry(entry)
        }
        info = NewForm(initial=data)
        return render(request,"encyclopedia/new_entry.html",{
            "entries": util.list_entries(),
            "entry":entry,
            "form":info,
            "page_req": False
        })  
def New_Page(request):
    if request.method == "POST":
        form = NewForm(request.POST)
        util.save_entry(form.data["page_name"],form.data["text"])
        return HttpResponseRedirect("/")
        #else:
        #    return render(request,"encyclopedia/new_entry.html",{
         #       "form":form
         #   })
    return render(request,"encyclopedia/new_entry.html",{
        "entries": util.list_entries(),
        "form":NewForm(),
        "page_req": True
    })

