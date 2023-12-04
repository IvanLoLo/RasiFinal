import { DataTypes } from "sequelize";
import { sequelize } from "./database.config.js";

export const Cita = sequelize.define("cita", {
  id: {
    type: DataTypes.UUID,
    defaultValue: DataTypes.UUIDV4,
    primaryKey: true,
  },
  paciente: {
    type: DataTypes.INTEGER,
    allowNull: false,
  },
  doctor: {
    type: DataTypes.INTEGER,
    allowNull: false,
  },
  especialidad: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  fecha: {
    type: DataTypes.DATE,
    allowNull: false,
  },
  motivo: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  estadoCita: {
    type: DataTypes.ENUM("Programada", "Confirmada", "Atendida", "Cancelada"),
    allowNull: false,
  },
});
