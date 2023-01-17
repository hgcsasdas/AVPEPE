import speech_recognition as sr
import pyttsx3
from datetime import datetime
from functions.comandos_locales import open_calculator, open_cmd, open_notepad, open_discord, open_League
from functions.comandos_online import buscar_en_google, buscar_en_wikipedia, poner_en_yt, mandar_was, buscar_en_internet, chiste_random, tiempo_grafico, tiempo
#from random import choice
#from utils import opening_text

recognizer = sr.Recognizer()
r = sr.Recognizer()
mic = sr.Microphone(device_index=3)
engine = pyttsx3.init('sapi5')

#########################################################
#Configuración de la voz
# Set Rate
engine.setProperty('rate', 210)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Conversión Texto a Voz
def speak(text):
    """Usado para decir cualquier texto que le sea entregado"""
    
    engine.say(text)
    engine.runAndWait()

####################################################################

################################################
#Saludo inicial del user

Username = "hgc88"
Botname = "pepe"

def greet_user():
    """Saluda al usuario de acuerdo al horario"""
    
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Buenos días {Username}")
    elif (hour >= 12) and (hour < 19):
        speak(f"Buenas tardes {Username}")
    elif (hour >= 19) and (hour < 24):
        speak(f"Buenas noches {Username}")
    speak(f"Yo soy {Botname}. ¿Cómo puedo asistirle?")

######################################################################


################################################################
#que la aplicación furule 
def hablar():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Te escucho....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Dígamee...')
        query = r.recognize_google(audio, language='es-es')
        if not 'dormir' in query or 'parar' in query:
            #speak(choice(opening_text))
            print('f')
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Buenas noches señor, hasta mañana!")
            else:
                speak('Tenga un buen día señor!')
            exit()
    except Exception:
        speak('Lo siento no te he entendido, ¿podrías repertirlo de nuevo porfavor?')
        query = 'None'
    return query
###BIENVENIDA####
greet_user()
#################
#Bucle de esperar
def esperar():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Esperando....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='es-es')
    except Exception:
        query = 'None'
    return query
wait = False
##################################
while True:
    query = hablar().lower()
    
    #comandos de interacción
  
    if 'hola' in query:
        speak('hola señor')
    elif 'tu puta madre' in query:
      speak('la tuya que se me abre hijueputa')
    elif 'gracias' in query:
        speak('no hay de qué señor')
    elif 'hora' in query:
        speak(f'son las: {datetime.now().hour} horas, {datetime.now().minute} minutos' )
    elif 'espera' in query:
        speak('Sí señor')
        wait = True
        while wait:
            query = esperar().lower()
            if f'{Botname}' in query:
                speak("Dígame, señor")
                wait = False
    elif 'buenos días' in query:
        speak('Buenos días señor')
    elif 'buenos noches' in query:
        speak('Buenas noches señor')
    elif 'cómo te llamas' in query:
        speak(f'Me llamo {Botname} señor')
    elif 'cómo me llamo' in query:
        speak(f'Se llama {Username} señor')

    #comandos de abrir programas

    elif 'abre la cmd' in query or 'open cmd' in query:
      open_cmd()
    elif 'abre la calculadora' in query:
      open_calculator()
    elif 'abre discord' in query:
       open_discord()
    elif 'abre el bloc de notas' in query:
      open_notepad()
    elif 'abre el lol' in query:
      open_League()
    

    #Comandos online

    elif 'buscar en google' in query:
        speak('¿Qué quieres buscar?')
        query = hablar().lower()
        buscar_en_google(query)
    elif 'buscar en wikipedia' in query:
        speak('¿Qué quieres buscar en la wikipedia?')
        search_query = hablar().lower()
        results = buscar_en_wikipedia(search_query)
        speak(f"De acuerdo a la wikipedia, {results}")
        speak("Voy a imprimir todo ahora")
        print(results)
    elif 'buscar en youtube' in query:
        speak('¿Qué quieres buscar en youtube?')
        video = hablar().lower()
        poner_en_yt(video)
    elif 'mandar whatsap' in query:
        speak('Señor dígame el número')
        number = input("número: ")
        speak("¿Qué le quiere decir?")
        message = hablar().lower()
        mandar_was(number, message)
        speak("ya lo he mandado señor")
    elif 'explícame algo' in query:
        speak('¿Qué quieres saber?')
        info = hablar().lower()
        speak('¿Cuántas líneas quieres de información?')
        nlineas = int(input("Número: "))
        results = buscar_en_internet(info, nlineas)
    elif 'chiste' in query:
        engine.setProperty('rate', 140)
        chiste = chiste_random()
        speak(chiste)
        engine.setProperty('rate', 210)
        print(chiste)
    elif 'gráfico del tiempo' in query:
        speak('¿De qué ciudad te gustaría el gráfico?')
        ciu = hablar().lower()
        tiempo_grafico(ciu)
    elif 'tiempo' in query:
        speak('¿de qué ciudad quiere saber el tiempo señor?')
        ciu = hablar().lower()
        tiempoC = tiempo(ciu)
        speak(f'Hace una temperatura de {tiempoC[0]} grados celsius en {ciu}')
        speak(tiempoC[1])