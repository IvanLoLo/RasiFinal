import json
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from .logic import basics_logic as vl
from .auth0backend import getRole


@csrf_exempt
def basics_view(request):
    role = getRole(request)
    if role not in ['Admin']: return HttpResponse("Unauthorized User", status=401)
    if request.method == 'GET':
        return HttpResponse("Hello, from Basics Microservice!")

@csrf_exempt
def contract_view(request):
    role = getRole(request)
    if role not in ['Admin']: return HttpResponse("Unauthorized User", status=401)
    if request.method == 'POST':
        try:
            # print(request.body)
            contract_dto = vl.create_contract(request.FILES['file'])
            contract = serializers.serialize('json', [contract_dto,])
            return HttpResponse('Nice', 'application/json')
        except Exception as e:
            return HttpResponse(e, 'application/json')