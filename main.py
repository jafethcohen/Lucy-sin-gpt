#Importacion de librerias
#---------------------------------
import datetime
#---------------------------------
import pyttsx3
#---------------------------------
import speech_recognition as sr         #reconocimiento de voz
#---------------------------------
#from googletrans import Translator, constants         #Para traducir
#---------------------------------
import wikipedia #Para buscar en Wikipedia
#---------------------------------
import webbrowser  	#Abrir navegador y abrir sitios Web.
#---------------------------------
import os 		   	  #Sistema operativo (Linux)
#---------------------------------
import smtplib 	  	  #Envío de correos electrónicos.
#---------------------------------
import csv
import pywhatkit
from pygame import mixer
import keyboard

#Link del video: https://www.youtube.com/watch?v=Lp9Ftuq2sVI&ab_channel=CodeWithHarry
#MINUTO 38:50 DEL VÍDEO

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak (audio):
    engine.say(audio)
    engine.runAndWait()

#Funcion toma la hora del pc y toma una de las bienvenidas

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak ("Buenos días vida mía")
    elif hour>=12 and hour<18:
        speak ("Buenas tardes cosita")
    else:
        speak("Buenas noches meu amor")
        
    speak("Soy lucy, tu asistente virtual personal, ¿en qué puedo ayudarte?")
            
            
def takeCommand():
    
#----Esto toma el microfono, para los comandos del usuario     

    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Escuchando...")
        print("Escuchando...")
        r.pause_threshold  = 1
        audio = r.listen(source) 
    
    try:
        print ("Reconociendo askldjaslkd")
        query = r.recognize_google(audio, language='es')
        print(f"El usuario dijo:  {query}\n")
        r.pause_threshold  = 2

    except Exception:
        print("¿podrías repetir?")
        return "None"
    return query



def sendEmail (to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('el correo de dónde se va a enviar', 'contraseña de ese correo')
    server.sendmail('el correo de dónde se va a enviar', to, content)
    server.close()
    

   
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        #logica para ejecutar tareas basada en query
        #------------------Busqueda en Wikipedia-------------------------------          
        if 'busca' in query:
            search = query.replace('busca', '')
            wikipedia.set_lang("es")
            info = wikipedia.summary(search, 2)
            speak(info)           
        elif 'quién fue' in query:
            search = query.replace('quién fue', '')
            wikipedia.set_lang("es")
            info = wikipedia.summary(search, 2)
            speak(info)                     
        #------------------Reproducción de contenido en youtube-----------------------------------
        elif "reproduce" in query:
            music = query.replace('replace', '')
            speak("Reproduciendo en youtube")
            pywhatkit.playonyt(music)           
        #-----------------------------------------------------
        elif "hora feliz" in query:
            webbrowser.open("pornhub.com")
        #---------------------------------------------------------     
        elif "hora" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Son las {strTime}") 
            
        elif "alarma" in query:
            num = query.replace('alarma', '')
            num = num.strip()
            speak("Alarma programada a las: " + num + " horas")
            while True: 
                if datetime.datetime.now().strftime('%H:%M') == num:
                    print("alarma activada")
                    mixer.init()
                    mixer.music.load("alarma.mp3")
                    mixer.music.play()
                    if keyboard.read_key() == "s":
                        mixer.music.stop()
                        break
                                   
        elif "correo" in query:
                
            try: 
                speak("¿Qué debo decir?")
                content = takeCommand()
                to = "El correo al que lo vas a enviar"
                sendEmail(to, content)
                speak("Se ha enviado correctamente el correo")
            except Exception as e:
                print (e)
                speak("Lo siento, no se pudo enviar el correo")            
        
                     

