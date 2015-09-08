from django.shortcuts import render
from django.template import RequestContext, loader
# Create your views here.
from django.http import HttpResponse

def index(request):
   template = loader.get_template('ReviewProcess/index.html')
   context = RequestContext(request, {
       'name': 'Aman',
   })
   return HttpResponse(template.render(context))
