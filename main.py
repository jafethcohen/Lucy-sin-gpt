import datetime
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak (audio):
    engine.say(audio)
    engine.runAndWait()

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
        print(f"El usuario dijo:  {query}")
        
    except Exception as e:
        #print (e)
        print("¿podrías repetir?")
        return "None"
    return query
    
    
if __name__ == "__main__":
    wishMe()
    takeCommand()
    
    