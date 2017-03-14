
from django.conf.urls import url

from . import views

urlpatterns = [
    #homepage
    url(r'^$', views.index,name='index'),
    #program
    url(r'^program/$', views.program,name='program'),
    #employee
    url(r'^employee/$', views.employee,name='employee'),
    #job
    url(r'^job/$', views.job,name='job'),
    #equipment
    url(r'^equipment/$', views.equipment,name='equipment'),

    #detail of program
    url(r'^program/(?P<program_id>[0-9]+)/$', views.program_detail, name='program_detail'),

    #detail of employee
    url(r'^employee/(?P<employee_id>[0-9]+)/$', views.employee_detail, name='employee_detail'),

    #detail of job
    url(r'^job/(?P<job_string>[\w\-]+)/$', views.job_detail, name='job_detail'),

    #detail of equipment
    url(r'^equipment/(?P<equipment_id>[0-9]+)/$', views.equipment_detail, name='equipment_detail'),

    #detail of program_questionnaire
    url(r'^program/(?P<program_id>[0-9]+)/questionnaire/$', views.program_questionnaire_detail, name='program_queationaire_detail'),
]
