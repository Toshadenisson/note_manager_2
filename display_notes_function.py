from colorama import init, Fore
from colorama import Back
from colorama import Style
init(autoreset=True)

def display_notes(notes):
    if len(notes[::]) == 0:
        print(f'У вас нет сохранённых заметок.')
    else:
        while input('Если Вы хотите вывести на экран заметки целиком, то введите цифру - 1, '
                    'а если только заголовки - отличную от 1: ') == '1':
            print(Back.LIGHTBLUE_EX+Fore.BLACK+'Список заметок.')
            for i in notes:
                print('------------------------------------------------------')
                print(Style.BRIGHT+Fore.LIGHTMAGENTA_EX+f'Заметка № {notes.index(i) + 1}:')
                for j,k in i.items():
                    print(Fore.LIGHTCYAN_EX+f'{j}: {k}')
            return notes

        else:
            print(Back.LIGHTBLUE_EX + Fore.BLACK + 'Список заголовков.')
            for dict_ in notes:
                print('------------------------------------------------------')
                print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + f'Заголовок № {notes.index(dict_) + 1}:')
                print(Fore.LIGHTCYAN_EX +f'{dict_['Заголовок']}')

    return notes


x_1 = [{'Имя пользователя': 'Мария','Заголовок': 'Учеба',
                'Описание': 'Подготовиться к экзамену',
                'Статус': 'в процессе','Дата создания': '25-11-2024', 'Дедлайн': '01-12-2024'}]
x_2 = [{'Имя пользователя': 'Мария', 'Заголовок': 'Учеба',
        'Описание': 'Подготовиться к экзамену','Статус': 'в процессе',
        'Дата создания': '25-11-2024','Дедлайн': '01-12-2024'},
       {'Имя пользователя': 'Алексей','Заголовок': 'Список покупок',
                'Описание': 'Подготовиться к экзамену',
                'Статус': 'новая','Дата создания': '27-11-2024', 'Дедлайн': '30-11-2024'}]
display_notes(x_2)
