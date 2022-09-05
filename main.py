import speech_recognition
import playsound
import os
import webbrowser
import winsound



sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

command = {
    'commands': {
        'greeting': ['ахунно сделай', 'ахуено сделай', 'ахуенно', 'сделай'],
        'task': ['добавь задачу', 'добавь'],
        'che': ['привет', 'прив', 'ниндзя', 'нинзя'],
        'song': ['включи музыку','музыку','уёбак','кизара','кизару']
    }
}


def listen_command():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()

        return query
    except speech_recognition.UnknownValueError:
        return playsound.playsound('nikto.mp3', True)

        # return os.startfile('nikto.mp3')


def song():
    # webbrowser.open('https://www.youtube.com/watch?v=zwrXt0wCep0&list=RDzwrXt0wCep0&start_radio=1&ab_channel=YungLean', new=2)
    # os.startfile('kizaru.mp3')
    playsound.playsound('kizaru.mp3', True)

def che():
    playsound.playsound('che.mp3', True)
    # playsound.playsound('che.mp3', False)
#     # playsound('che.mp3')


def greeting():
    return playsound.playsound('axyenno.mp3', True)


def task():
    print('Что записать, хозяин?')
    query = listen_command()
    with open('task.txt', 'a') as file:
        file.write(f'{query}\n')

    return f'Задача {query} добавлена'


def main():
    query = listen_command()

    for k, v in command['commands'].items():
        if query in v:
            print(globals()[k]())
    # if query == 'ахуенно сделай':
    #     print(greeting())
    # elif query == 'добавь задачу':
    #     print(task())
    # elif query == 'привет':
    #     playsound("che.mp3")
    # else:
    #     print('Пошел на хуй')


if __name__ == '__main__':
    main()
