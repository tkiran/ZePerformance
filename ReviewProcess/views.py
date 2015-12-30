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
from ReviewProcess.models import ReportingManagerProfile
from django import forms
from ReviewProcess.models import ReviewQuestion, UserReviewQuestion, UserTask
from django.contrib.auth.models import User

def index(request):
    template = loader.get_template('ReviewProcess/index.html')
    context = RequestContext(request, {
       'incorrect_login': False,
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
        else:
            context = RequestContext(request, {
                    'incorrect_login': True,
            })
    return HttpResponse(template.render(context))

@login_required(login_url='/index/')
def home(request):
    template = loader.get_template('ReviewProcess/home.html')
    assignedtask = False
    if(request.user.usertask_set.all()):
        assignedtask = True
    context = RequestContext(request, {
       'name': 'Aman',
       'assignedtask' : assignedtask
    })
    return HttpResponse(template.render(context))
@login_required
def user_logout(request):
    context = RequestContext(request,
        {"logout":"True"})
    logout(request)
    # Redirect back to index page.
    template = loader.get_template('ReviewProcess/index.html')
    return HttpResponse(template.render(context))

@login_required
def user_profile(request):
    context = RequestContext(request,
        {"user_id":request.user.id})
    # Redirect back to index page.
    template = loader.get_template('ReviewProcess/profile.html')
    return HttpResponse(template.render(context))
@login_required
def Test(request):
    context = RequestContext(request)
    # Redirect back to index page.
    template = loader.get_template('ReviewProcess/DropDown.html')
    return HttpResponse(template.render(context))
@login_required
def createtask(request):
    # Redirect back to index page.
    context = {}
    if ReportingManagerProfile.objects.filter(id=request.user.id).count():
        reporter = ReportingManagerProfile.objects.get(id=request.user.id)
        reportees = reporter.reportees.all()
        allobj = ReviewQuestion.objects.all()
        context['reviewquestions'] = allobj
        questiondict = {}
        questionset = []
        context = {'reportees': reportees,'reviewquestions' : allobj}
    return render_to_response(
       'ReviewProcess/createtask.html',context,
       context_instance=RequestContext(request)
   )

@login_required
def getreviewquestion(request):
    # Redirect back to index page.
    context = {}
    allobj = ReviewQuestion.objects.all()
    context['reviewquestions'] = allobj
    questiondict = {}
    questionset = []
    return render_to_response(
       'ReviewProcess/myform.html',context,
       context_instance=RequestContext(request)
   )
@login_required
def update_profile(request):
    error = False
    if request.REQUEST.get('user', None):
        user = User.objects.get(username=request.REQUEST.get('user'))
        if request.method == 'POST':
            user.last_name = request.REQUEST.get('lname')
            user.save()
    context = {
        'error' : error
    }
    return render_to_response('ReviewProcess/profile.html',
                              context,
                              context_instance=RequestContext(request))

@login_required
def save_user_question(request):
    """
    """
    uname = ''
    if request.method == 'POST':
        sel_value = request.POST.get('selectcount').split(',')
        count = len(sel_value)
        uid = request.POST.get('userid')
        uname = request.POST.get('username')
        if(UserTask.objects.count() > 0):
            try:
                user_task = UserTask.objects.get(user_id=uid)
            except UserTask.DoesNotExist, e:
                user_task = UserTask.objects.create(user_id=uid,assigned_by=int(request.user.id))
        else:
            user_task_exits.objects.create(user_id=uid,assigned_by=int(request.user.id))
        if(UserReviewQuestion.objects.count()):
            dd = UserReviewQuestion.objects.get(user_id=uid)
            dd.delete()
            urq = UserReviewQuestion.objects.create(user_id=uid)
            urq.question.clear()
            for index in range(count):
                quesid = request.POST.get('sel_ques_'+sel_value[index])
                urq.question.add(ReviewQuestion.objects.get(id=int(quesid)))
                urq.save()
        else:
            urq = UserReviewQuestion.objects.create(user_id=uid)
            urq.question.clear()
            for index in range(count):
                quesid = request.POST.get('sel_ques_'+sel_value[index])
                urq.question.add(ReviewQuestion.objects.get(id=int(quesid)))
                urq.save()
    
    return render_to_response(
            'ReviewProcess/createtask.html', {'taskassigned': True,'username':uname,'assignedtask': True},
            context_instance=RequestContext(request))

@login_required
def show_user_task(request):
    """
    """
    uname = request.GET.get('uname')
    UserReviewQuestion.objects.get(username=uname)

@login_required
def show_user_form(request):
    """
    """
    questions = UserReviewQuestion.objects.get(user_id=int(request.user.id)).question.all()
    assigned_by_id = UserTask.objects.get(user_id=int(request.user.id)).assigned_by
    assigned_by_obj =  User.objects.get(id = int(assigned_by_id))

    return render_to_response(
            'ReviewProcess/show_user_form.html',{'assignedtask': True,'questions':questions,'assigned_by_obj':assigned_by_obj},
            context_instance=RequestContext(request))

@login_required
def send_review_form_to_reviewer(request):
    """
    """
    import pdb;pdb.set_trace()
    return render_to_response(
            'ReviewProcess/show_user_form.html',{'assignedtask': True,'questions':questions,'assigned_by_obj':assigned_by_obj})


