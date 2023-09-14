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
import webbrowser 	#Abrir navegador y abrir sitios Web.
#---------------------------------
import os 		   	  #Sistema operativo (Linux)
#---------------------------------
import smtplib 	  	  #Envío de correos electrónicos.
#---------------------------------

#Link del video: https://www.youtube.com/watch?v=Lp9Ftuq2sVI&ab_channel=CodeWithHarry
#MINUTO 31:42 DEL VÍDEO

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
    '''   
    Esto toma el microfono, para los comandos del usuario     
    '''  
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        r.pause_threshold  = 1
        audio = r.listen(source) 
    
    try:
        print ("Reconociendo askldjaslkd")
        query = r.recognize_google(audio, language='es')
        print(f"El usuario dijo:  {query}\n")

    except Exception as e:
        #print (e)
        print("¿podrías repetir?")
        return "None"
    return query
    
    
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        #logica para ejecutar basada en query
        #------------------Busqueda en Wikipedia-------------------------------
        if "wikipedia" in query:
            speak("Buscando wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3 )
            speak("Accediendo a Wikipedia ")
            
            speak(results)
        #-----------------------------------------------------
        elif "abre youtube" in query:
            webbrowser.open("youtube.com")
        #-----------------------------------------------------
        elif "abre google" in query:
            webbrowser.open("google.com")
        #------------------------------------------------------

            

    
    