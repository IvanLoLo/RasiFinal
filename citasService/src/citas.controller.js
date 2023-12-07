import { Cita } from './citas.model.js';
import { Op } from 'sequelize';
import uuidValidate from 'uuid-validate';
import getRole from './auth0backend.js';
import axios from 'axios';

const reviewRole = async (req, roles) => {
    const role = await getRole(req);
    if(roles.includes(role)) return true;
    return false;
}

const validDoctor = async (req, doctor) => {
    try {
        const response = await axios.get(`http://${process.env.USERS_PATH}/users/medicos/${doctor}`,
            {headers: {
                'Authorization': req.headers.authorization
            }});
        if(response.status === 200) return true;
        return false;
    } catch (error) {
        return false;
    }
}

const validPatient = async (req, patient) => {
    try {
        const response = await axios.get(`http://${process.env.USERS_PATH}/users/pacientes/${patient}`,
        {headers: {
            'Authorization': req.headers.authorization
        }});
        if(response.status === 200) return true;
        return false;
    } catch (error) {
        return false;
    }
}


export const getCitas = async (req, res) => {
    try {
        if(!await reviewRole(req, ['Admin', 'Doctor'])) return res.status(401).json({message: 'Unauthorized User'});
        const citas = await Cita.findAll();
        res.json(citas);
    } catch (error) {
        res.status(500).json({
            message: 'Something goes wrong',
            data: {}
        });
    }
}

export const getCitaById = async (req, res) => {
    const id = req.params.citaId;
    if(!id) return res.status(400).json({message: 'Id not provided'});
    if(!uuidValidate(id)) return res.status(400).json({message: 'Invalid id'});
    try {
        if(!await reviewRole(req, ['Admin', 'Doctor'])) return res.status(401).json({message: 'Unauthorized User'});
        const cita = await Cita.findOne({
            where: {
                id
            }
        });
        if(!cita) return res.status(404).json({message: 'Cita not found'});
        res.json({
            data: cita
        });
    } catch (error) {
        //console.log(error);
        res.status(500).json({
            message: 'Something goes wrong',
            data: {}
        });
    }
}

export const getCitaByFecha = async (req, res) => { //yyyy-mm-dd format
    const currentDate = new Date(req.params.fecha);
    if(currentDate.getFullYear() < 2010 || isNaN(currentDate.getTime())) return res.status(400).json({message: 'Invalid date'});
    const nextWeek = new Date(req.params.fecha);
    nextWeek.setDate(currentDate.getDate() + 7);
    try {
        if(!await reviewRole(req, ['Admin'])) return res.status(401).json({message: 'Unauthorized User'});
        const count = await Cita.count({
            where: {
                fecha: {
                    [Op.between]: [currentDate, nextWeek]
                }
            }
        });

        res.json({
            total_citas: count
        });
    } catch (error) {
        //console.log(error);
        res.status(500).json({
            message: 'Something goes wrong',
            data: {}
        });
    }
}

export const getCitaByMes = async (req, res) => { //yyyy-mm format
    const date = req.params.mes;
    const currentDate = new Date(date);
    if(currentDate.getFullYear() < 2010 || isNaN(currentDate.getTime())) return res.status(400).json({message: 'Invalid date'});

    try {
        if(!await reviewRole(req, ['Admin'])) return res.status(401).json({message: 'Unauthorized User'});

        const year = currentDate.getFullYear();
        const month = currentDate.getMonth();

        const count = await Cita.count({
            where: {
                fecha: {
                    [Op.and]: [
                        { [Op.gte]: new Date(year, month, 1) }, // Start of the month
                        { [Op.lt]: new Date(year, month + 1, 1) }, // Start of the next month
                    ],
                },
              },
        });

        res.json({
            total_citas: count/4
        });

    } catch (error) {
        //console.log(error);
        res.status(500).json({
            message: 'Something goes wrong',
            data: {}
        });
    }
}

export const getCitaByEspecialidad = async (req, res) => {
    const especialidad = req.params.especialidad;
    try {
        if(!await reviewRole(req, ['Admin'])) return res.status(401).json({message: 'Unauthorized User'});

        const count = await Cita.count({
            where: {
                especialidad: especialidad
            }
        });

        res.json({
            count: count
        });
    } catch (error) {
        //console.log(error);
        res.status(500).json({
            message: 'Something goes wrong',
            data: {}
        });
    }
}

export const createCita = async (req, res) => {
    const { paciente, doctor, especialidad, fecha, motivo, estadoCita } = req.body;
    if (!paciente || !doctor || !especialidad || !fecha || !motivo || !estadoCita) 
        return res.status(400).json({message: 'Invalid data'});
    try {
        if(!await reviewRole(req, ['Admin', 'Doctor', 'Patient User'])) return res.status(401).json({message: 'Unauthorized User'});
        if(!await validDoctor(req, doctor)) return res.status(400).json({message: 'Invalid doctor'});
        if(!await validPatient(req, paciente)) return res.status(400).json({message: 'Invalid patient'});

        const newCita = await Cita.create({
            paciente,
            doctor,
            especialidad,
            fecha,
            motivo,
            estadoCita
        }, {
            fields: ['paciente', 'doctor', 'especialidad', 'fecha', 'motivo', 'estadoCita']
        });
        if (newCita) {
            return res.json({
                message: 'Cita created successfully',
                data: newCita
            });
        }
    } catch (error) {
        //console.log(error);
        res.status(500).json({
            message: 'Something goes wrong',
            data: {}
        });
    }
}