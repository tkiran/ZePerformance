from django.conf.urls import url, include
from ReviewProcess import views

urlpatterns = [
               url(r'^$', views.index, name='index'),
              # url(r'^add$', views.index, name='index'),
               url(r'^home$', views.home, name='home'),
               url(r'^logout/$', views.user_logout, name='logout'),
               url(r'^profiles/$', views.user_profile, name='profiles'),		
               url(r'^createtask/$', views.createtask, name='createtask'),		
               url(r'^getreviewquestion/$', views.getreviewquestion, name='getreviewquestion'),
               url(r'^editpage/$', views.update_profile, name='editpage'),
               url(r'^assignusertask/$', views.save_user_question, name='assignusertask'),
               url(r'^showassignedtask/$', views.show_user_task, name='showassignedtask'),
               url(r'^showassignedform/$', views.show_user_form, name='showassignedform'),
               url(r'^sendformtoreviewer/$', views.send_review_form_to_reviewer, name='sendformtoreviewer'),
               url(r'^getformfromreportee/$', views.get_review_form_reportee, name='getformfromreportee'),
]