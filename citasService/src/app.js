import express from 'express';
import citasRoutes from './citas.routes.js';
import { loginRequired } from './login.middleware.js';

const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(loginRequired);

app.use(citasRoutes);

export default app;