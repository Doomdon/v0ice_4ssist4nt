import speech_recognition


sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.9

def greeting():

    return 'Привет, Господин!'

with speech_recognition.Microphone() as mic:
    sr.adjust_for_ambient_noise(source=mic, duration=0.5)
    audio = sr.listen(source=mic)
    query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()

if query == 'в махачкалу ебанём':
    print(greeting())
elif query == 'алло':
    print('Че надо, хозяин?')
elif query == 'серёга петух':
    print('согласен, еще и пидорас))')
else:
    print('Пошел на хуй')

# print(query)


