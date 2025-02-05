import speech_recognition as sr
import gTTS
import os
from jetbot import Robot

robot = Robot()

def reconocer_voz():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando... Di algo")
        recognizer.adjust_for_ambient_noise(source)  
        audio = recognizer.listen(source)
    try:
        print("Reconociendo...")
        texto = recognizer.recognize_google(audio, language='es-ES')
        print(f"Comando reconocido: {texto}")
        return texto.lower() 
    except Exception as e:
        print(f"Error: {e}")
        return None

def hablar(texto):
    tts = gTTS.gTTS(texto, lang='es')
    tts.save("respuesta.mp3")
    os.system("mpg321 respuesta.mp3")

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

# Flujo principal
def main():
    while True:
        comando = reconocer_voz()
        if comando:
            controlar_robot(comando)

if __name__ == "__main__":
    main()
