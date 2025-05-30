import pandas as pd
from datetime import datetime, timedelta

def obtener_citas(dia='hoy'):
    try:
        df = pd.read_excel('AGENDAVET.xlsx')
        df['Fecha'] = pd.to_datetime(df['Fecha'], errors='coerce')  

        if dia == 'hoy':
            fecha_objetivo = datetime.now().date()
        elif dia == 'mañana':
            fecha_objetivo = (datetime.now() + timedelta(days=1)).date()
        else:
            return "Opción inválida."

        citas_dia = df[df['Fecha'].dt.date == fecha_objetivo]

        if citas_dia.empty:
            return f"No hay citas para {dia}."

        resultado = f"Citas para {dia}:\n"
        for _, fila in citas_dia.iterrows():
            resultado += (
                f"- {fila['Nombre']} trae a {fila['Nombre_mascota']} "
                f"({fila['Raza']}) para {fila['Servicio']}. Tel: {fila['Telefono']}\n"
            )

        return resultado.strip()
    
    except Exception as e:
        return f"Error al leer el archivo Excel: {e}"
