from django.conf.urls import url, include
from ReviewProcess import views

urlpatterns = [
               url(r'^$', views.index, name='index'),
              # url(r'^add$', views.index, name='index'),
               url(r'^home$', views.home, name='home'),
               url(r'^logout/$', views.user_logout, name='logout'),
               url(r'^profiles/(?P<edit_option>\w+)/$', views.user_profile, name='profiles'),		
]