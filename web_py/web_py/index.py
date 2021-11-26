#bash

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index_page(request):
    context ={}
    context['index']='this is index page!'
    template= loader.get_template('index.html')
    return HttpResponse(template.render(context, request))