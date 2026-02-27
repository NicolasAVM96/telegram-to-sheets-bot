import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Importacion de módulos
from parser import procesar_mensaje_completo
from sheets_client import guardar_entrenamiento

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

async def recibir_rutina(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Esta función se ejecuta cada vez que le envías un mensaje al bot"""
    mensaje_texto = update.message.text
    chat_id = update.message.chat_id
    
    # Le avisamos al usuario que estamos procesando
    await context.bot.send_message(chat_id=chat_id, text="⏳ Procesando rutina...")
    
    lista_ejercicios = procesar_mensaje_completo(mensaje_texto)
    
    if not lista_ejercicios:
        await context.bot.send_message(chat_id=chat_id, text="❌ No pude entender el formato. Recuerda usar:\nTipo Entreno\nEjercicio RepsxSeries Carga")
        return

    # Iteramos la lista y la enviamos a Google Sheets
    exitos = 0
    errores = 0
    
    for ejercicio_dict in lista_ejercicios:
        if guardar_entrenamiento(ejercicio_dict):
            exitos += 1
        else:
            errores += 1
            
    # Respondemos con el resultado final
    respuesta = f"✅ ¡Listo, Nico! Se guardaron {exitos} ejercicios en tu Excel."
    if errores > 0:
        respuesta += f"\n⚠️ Hubo problema guardando {errores} ejercicios."
        
    await context.bot.send_message(chat_id=chat_id, text=respuesta)

if __name__ == '__main__':
    print("🤖 Iniciando el Bot de Entrenamiento...")
    
    # Construimos la aplicación del bot
    app = Application.builder().token(TOKEN).build()
    
    # Se le indica que solo escuche mensajes de texto y no un comando
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, recibir_rutina))
    
    print("✅ Bot encendido y escuchando. ¡Envíale un mensaje desde tu celular!")
    # Mantenemos el script corriendo
    app.run_polling()