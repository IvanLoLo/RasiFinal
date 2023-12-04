import { Router } from 'express';
import { getCitas, createCita, getCitaById, getCitaByFecha, getCitaByMes, getCitaByEspecialidad } from './citas.controller.js';

const router = Router();

router.get('/citas', getCitas);
router.post('/citas', createCita);

router.get('/citas/:citaId', getCitaById);
router.get('/citas/fecha/:fecha', getCitaByFecha);
router.get('/citas/mes/:mes', getCitaByMes);
router.get('/citas/especialidad/:especialidad', getCitaByEspecialidad);

export default router;