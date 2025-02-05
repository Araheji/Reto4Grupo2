import speech_recognition as sr
import gTTS
import os
from jetbot import Robot

robot = Robot()

# Función para reconocer lo que dices desde un archivo de audio
def reconocer_voz_desde_archivo(archivo_audio):
    recognizer = sr.Recognizer()
    with sr.AudioFile(archivo_audio) as source:  # Cargar el archivo de audio
        print(f"Procesando archivo: {archivo_audio}")
        audio = recognizer.record(source)  # Leer el archivo de audio
    try:
        print("Reconociendo...")
        texto = recognizer.recognize_google(audio, language='es-ES')
        print(f"Comando reconocido: {texto}")
        return texto.lower()  # Convertimos el texto a minúsculas para compararlo mejor
    except Exception as e:
        print(f"Error: {e}")
        return None

# Función para convertir texto en voz (respuesta del robot)
def hablar(texto):
    tts = gTTS.gTTS(texto, lang='es')
    tts.save("respuesta.mp3")
    os.system("mpg321 respuesta.mp3")  # Reproducir el audio generado

# Función de control del robot
def controlar_robot(comando):
    if "avanzar" in comando:
        print("El robot avanza")
        robot.forward()  # Avanza
        hablar("Voy hacia adelante")
    elif "detener" in comando:
        print("El robot se detiene")
        robot.stop()  # Detiene el robot
        hablar("Me detengo")
    elif "retroceder" in comando:
        print("El robot retrocede")
        robot.backward()  # Retrocede
        hablar("Voy hacia atrás")
    elif "izquierda" in comando:
        print("El robot gira a la izquierda")
        robot.left()  # Gira a la izquierda
        hablar("Voy a la izquierda")
    elif "derecha" in comando:
        print("El robot gira a la derecha")
        robot.right()  # Gira a la derecha
        hablar("Voy a la derecha")
    else:
        print("Comando no reconocido")
        hablar("No entiendo el comando")

# Lista de archivos de audio a probar
archivos_audio = ["Detener.wav", "Avanzar.wav"]  # Asegúrate de tener estos archivos en la misma carpeta

# Flujo principal modificado
def main():
    for archivo_audio in archivos_audio:
        comando = reconocer_voz_desde_archivo(archivo_audio)  # Procesar el archivo de audio
        if comando:
            controlar_robot(comando)

if __name__ == "__main__":
    main()
