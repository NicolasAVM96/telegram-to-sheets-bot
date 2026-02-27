import gspread

# Nombre del archivo excel
SHEET_NAME = "Gym"

def guardar_entrenamiento(datos_dict):
    """
    Recibe un diccionario con: {fecha, tipo, ejercicio, series, reps, carga}
    Y lo escribe en la hoja 'Raw_Data'.
    """
    try:
        # gspread busca las credenciales 
        gc = gspread.service_account(filename='credentials.json')

        # Abrir la hoja de cálculo
        sh = gc.open(SHEET_NAME)

        # Seleccionamos la pestaña en la cual se va a trabajar
        worksheet = sh.worksheet("Raw_Data")

        fila = [
            datos_dict["fecha"],
            datos_dict["tipo_entreno"],
            datos_dict["ejercicio"],
            datos_dict["series"],
            datos_dict["reps"],
            datos_dict["carga"]
        ]

        # Escribir en la hoja
        worksheet.append_row(fila)
        return True

    except Exception as e:
        print(f"Error contactando a Google Sheets: {e}")
        return False

# --- Testing ---
# if __name__ == "__main__":
#     mock_data = {
#         "fecha": "26/02/2026",
#         "ejercicio": "Test de Conexión Python",
#         "series": 1,
#         "reps": 1,
#         "carga": "Funcionó"
#     }
    
#     print("Enviando datos a la nube...")
#     if guardar_entrenamiento(mock_data):
#         print("¡Éxito! Revisa tu Excel ahora mismo.")