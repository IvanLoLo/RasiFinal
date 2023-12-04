from ..models import Doctor, Paciente
from datetime import datetime

def create_paciente(paciente):
    """
    Create a new paciente
    :param paciente: paciente data
    :return: paciente object
    """
    date_obj = datetime.strptime(paciente['fecha_nacimiento'], "%Y-%m-%d")
    paciente['fecha_nacimiento'] = date_obj.date()
    paciente = Paciente.objects.create(**paciente)
    return paciente

def create_doctor(doctor):
    """
    Create a new doctor
    :param doctor: doctor data
    :return: doctor object
    """
    doctor = Doctor.objects.create(**doctor)
    return doctor

def get_doctors():
    """
    Get all doctores
    :return: doctor object list
    """
    doctores = Doctor.objects.all()
    return doctores

def get_doctor(id):
    """
    Get doctor by id
    :param id: doctor id
    :return: doctor object
    """
    doctor = Doctor.objects.get(pk=id)
    return doctor

def get_pacientes():
    """
    Get all pacientes
    :return: paciente object list
    """
    pacientes = Paciente.objects.all()
    return pacientes

def get_paciente(id):
    """
    Get paciente by id
    :param id: paciente id
    :return: paciente object
    """
    paciente = Paciente.objects.get(pk=id)
    return paciente
