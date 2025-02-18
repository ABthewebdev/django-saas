from django.http import HttpResponse
from django.shortcuts import render
import pathlib
from visits.models import PageVisit

def home_page_view(request, *args, **kwargs):
    my_title = 'My Page'
    my_context = {
        "page_title": my_title
    }
    html_template = 'home.html'
    PageVisit.objects.create()
    return render(request, html_template, my_context)