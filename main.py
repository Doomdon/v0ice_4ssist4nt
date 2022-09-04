import speech_recognition


sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

def greeting():

    return 'Привет, Господин!'

def task():
    print('Что записать, хозяин?')

    with speech_recognition.Microphone() as mic:
        sr.adjust_for_ambient_noise(source=mic, duration=0.10)
        audio = sr.listen(source=mic)
        query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()

    with open('task.txt', 'a') as file:
        file.write(f'{query}\n')

    return f'Задача {query} добавлена'



with speech_recognition.Microphone() as mic:
    sr.adjust_for_ambient_noise(source=mic, duration=0.5)
    audio = sr.listen(source=mic)
    query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()

if query == 'в махачкалу ебанём':
    print(greeting())
elif query == 'добавь задачу':
    print(task())
elif query == 'серёга петух':
    print('согласен, еще и пидорас))')
else:
    print('Пошел на хуй')

# print(query)


