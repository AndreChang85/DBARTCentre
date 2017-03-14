from django.shortcuts import render
from django.http import HttpResponse
from . import models

def index (request):
    return render(request, 'artcenter/index.html')

def program (request):
    program_list = models.Program.objects.all()
    context = {'program_list': program_list}
    return render(request, 'artcenter/program.html', context)


def employee (request):
    employee_list = models.Employee.objects.all()
    context = {'employee_list': employee_list}
    return render(request, 'artcenter/employee.html', context)

def job (request):
    job_list = models.Job.objects.all()
    context = {'job_list': job_list}
    return render(request, 'artcenter/job.html', context)

def equipment (request):
    equip_list = models.Equipment.objects.all()
    context = {'equip_list': equip_list}
    return render(request, 'artcenter/equipment.html', context)

def program_detail (request,program_id):
    program_entry_detail = models.Program.objects.get(id=program_id)
    program_time_detail = models.Time_of_program.objects.filter(program_id=program_id)
    program_ticket_detail = models.Ticket.objects.filter(program_id=program_id)
    program_work_on_detail = models.Works_on.objects.filter(program_id=program_id)
    program_use_detail = models.Use.objects.filter(program_id=program_id)
    program_perform_detail = models.Perform.objects.filter(program_id=program_id)
    context = {
    'program_entry_detail': program_entry_detail,
    'program_time_detail':program_time_detail,
    'program_ticket_detail':program_ticket_detail,
    'program_work_on_detail':program_work_on_detail,
    'program_use_detail':program_use_detail,
    'program_perform_detail':program_perform_detail,
    }
    return render(request, 'artcenter/program_detail.html', context)

def program_questionnaire_detail (request,program_id):
    program_entry = models.Program.objects.get(id=program_id)
    program_title = program_entry.title
    back_id = program_entry.id
    program_questionnaire_detail = models.Questionnaire.objects.filter(program_id=program_id)
    context = {
    'program_entry':program_entry,
    'program_questionnaire_detail': program_questionnaire_detail,
    'program_title':program_title,
    'back_id' :back_id,
    }
    return render(request, 'artcenter/program_questionnaire_detail.html', context)

def employee_detail (request,employee_id):
    employee_entry_detail = models.Employee.objects.get(id=employee_id)
    employee_do_detail = models.Do.objects.filter(employee_id=employee_id)
    employee_work_on_detail_temp = models.Works_on.objects.filter(employee_id=employee_id)
    employee_work_on_detail = employee_work_on_detail_temp[:5]
    context = {
    'employee_entry_detail': employee_entry_detail,
    'employee_do_detail': employee_do_detail,
    'employee_work_on_detail': employee_work_on_detail,
    }
    return render(request, 'artcenter/employee_detail.html', context)

def job_detail (request,job_string):
    job_entry_detail = models.Job.objects.get(job_type=job_string)
    job_member_detail = models.Do.objects.filter(job=job_string)
    context = {
    'job_entry_detail': job_entry_detail,
    'job_member_detail':job_member_detail,
    }
    return render(request, 'artcenter/job_detail.html', context)

def equipment_detail (request,equipment_id):
    equipment_entry_detail = models.Equipment.objects.get(id=equipment_id)
    equipment_used_detail = models.Use.objects.filter(equipment_id=equipment_id)
    context = {
    'equipment_entry_detail': equipment_entry_detail,
    'equipment_used_detail':equipment_used_detail,
    }
    return render(request, 'artcenter/equipment_detail.html', context)
