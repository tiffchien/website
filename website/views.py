from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth import login
from django.template import Context, Template
from django.forms import *
from django.core.serializers.json import DjangoJSONEncoder
import json, re

def index(request):
    template = loader.get_template('website/index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def tos(request):
    template = loader.get_template('website/tos.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def faq(request):
    template = loader.get_template('website/faq.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))
