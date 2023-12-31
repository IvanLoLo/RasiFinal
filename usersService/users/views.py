import json
from django.shortcuts import render
from django.http import HttpResponse
from .logic import variables_logic as vl
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from usersService.auth0backend import getRole
        
@csrf_exempt
def paciente_view(request, pk=None):
    if request.method == 'GET': return paciente_get_view(request, pk)
    if request.method == 'POST':
        paciente_dto = vl.create_paciente(json.loads(request.body))
        paciente = serializers.serialize('json', [paciente_dto,])
        return HttpResponse(paciente, 'application/json')
    
#@login_required
def paciente_get_view(request, pk=None):
    role = getRole(request)
    if role not in ['Admin', 'Medico']: return HttpResponse("Unauthorized User", status=401)
    if pk:
        paciente = vl.get_paciente(pk)
        paciente_dto = serializers.serialize('json', [paciente,])
        return HttpResponse(paciente_dto, 'application/json')
    else:
        pacientes = vl.get_pacientes()
        pacientes_dto = serializers.serialize('json', pacientes)
        return HttpResponse(pacientes_dto, 'application/json')
        
@csrf_exempt
#@login_required
def medico_view(request, pk=None):
    role = getRole(request)
    if request.method == 'GET':
        if role not in ['Admin', 'Medico']: return HttpResponse("Unauthorized User", status=401)
        if pk:
            medico = vl.get_doctor(pk)
            medico_dto = serializers.serialize('json', [medico,])
            return HttpResponse(medico_dto, 'application/json')
        else:
            medicos = vl.get_doctors()
            medicos_dto = serializers.serialize('json', medicos)
            return HttpResponse(medicos_dto, 'application/json')
        
    if request.method == 'POST':
        if role != 'Admin': return HttpResponse("Unauthorized User", status=401)
        medico_dto = vl.create_doctor(json.loads(request.body))
        medico = serializers.serialize('json', [medico_dto,])
        return HttpResponse(medico, 'application/json')