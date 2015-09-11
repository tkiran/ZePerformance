from django.shortcuts import render
from django.template import RequestContext, loader
# Create your views here.
from django.http import HttpResponse
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse

def index(request):

    template = loader.get_template('ReviewProcess/index.html')
    context = RequestContext(request, {
       'name': 'Aman',
    })
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['uid']
        password = request.POST['upass']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    return HttpResponse(template.render(context))

@login_required(login_url='/index/')
def home(request):
    template = loader.get_template('ReviewProcess/home.html')
    context = RequestContext(request, {
       'name': 'Aman',
    })

    return HttpResponse(template.render(context))