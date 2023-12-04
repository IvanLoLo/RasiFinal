from django.contrib import admin
from .models import Paciente, Doctor

admin.site.register(Paciente)
admin.site.register(Doctor)