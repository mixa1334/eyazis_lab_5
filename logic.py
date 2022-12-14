import pyttsx3
from datetime import datetime
import speech_recognition as sr

def text_to_speech(text, voice_str, rate_str, volume_str):
    engine = pyttsx3.init()

    voice_dict = {'Male': 2, 'Female': 1}
    voices = engine.getProperty('voices')
    voice = voices[voice_dict[voice_str]].id
    engine.setProperty('voice', voice)

    rate = 150
    volume = 0.5

    rate_volume_dic = {'Fast': 2, 'Default': 1 , 'Slow': 0.5}

    rate = rate * rate_volume_dic[rate_str]
    engine.setProperty('rate', rate)

    volume = volume * rate_volume_dic[volume_str]
    engine.setProperty('volume', volume)

    engine.say(text)
    engine.runAndWait()
    engine.stop()

def recognize_speech(text):
    result = ""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listeting...')
        audio = recognizer.listen(source)
        
    try:
        out_text = recognizer.recognize_google(audio, language='en-US')
        out_text = out_text.lower()
        if (("время" in out_text) or ("time" in out_text)):
            result = "команда time, результат: " + datetime.today().strftime("%H:%M %p")
        elif (("дата" in out_text) or ("date" in out_text)):
            result = "команда date, результат: " + datetime.today().strftime("%B %d, %Y")
        elif (("озвучь" in out_text) or ("voice" in out_text)):
            text_to_speech(text, 'Male','Default', 'Default')
            resul = "успешно озвучено сообщение: "+ text
        else:
            result = "команда не распознана: " + out_text
    except:
        result = "ошибка!"
    return result