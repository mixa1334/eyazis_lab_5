import pyttsx3

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