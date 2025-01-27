import datetime
from colorama import init, Fore
from colorama import Back
from colorama import Style
init(autoreset=True)


# ФУНКЦИЯ ДЛЯ СОЗДАНИЯ ЗАМЕТКИ
def create_note(**kwargs):
    while kwargs ['username'] == '':
        kwargs ['username'] = input('Вы не указали имя пользователя. Пожалуйста, укажите имя пользователя еще раз: ').capitalize()
        continue
    while kwargs['title'] == '':
        kwargs['title'] = input('Вы не указали заголовок. Пожалуйста, укажите заголовок еще раз: ').capitalize()
        continue
    while kwargs['content'] == '':
        kwargs['content'] = input('Вы не указали описание заметки. Пожалуйста, укажите описание еще раз: ').capitalize()
        continue
    for i in kwargs:
        while i == 'status':
            if kwargs [i] == '1' or kwargs[i] == 'Новая':
                kwargs[i] = 'Новая'
                break
            if kwargs[i] == '2'or kwargs[i]=='В процессе':
                kwargs[i] = 'В процессе'
                break
            if kwargs[i] == 'Выполнена' or kwargs[i] == '3':
                kwargs[i] = 'Выполнена'
                break
            else:
                kwargs[i] = input(f'Указан не существующий статус. \n'
                                'Укажите статус заметки\n'
                                '(Выберите соответствующую цифру\n'
                                ' или введите статус в текстовом формате):\n'
                                '1.Новая\n'
                                '2.В процессе\n'
                                '3.Выполнена \n'
                                'Ваш выбор: ').capitalize()
                continue
    while True:
        try:
            kwargs['issue_date'] = (datetime.date.strftime
                                    ((datetime.datetime.strptime(kwargs['issue_date'], '%d-%m-%Y')),
                                     '%d-%m-%Y'))
            break
        except ValueError:
            kwargs['issue_date'] = input('Введен некорректный формат даты.'
                                       'Введите дату окончания дедлайна (в формате д-м-г): ')
            continue
    print(Fore.LIGHTMAGENTA_EX + "Заметка успешно создана!!!")
    return kwargs




# ФУНКЦИЯ ВВОДА ДЕДЛАЙНА

def issue_date():
    while True:
        day = input(f"Укажите дату дедлайна (цифрами):\n"
                " день - ").replace('.','')
        month = input(" месяц - ").replace('.','')
        year = input(" год - 20").replace('.','')
        issue_date_input = (day + '.' + month + '.' + '20'+year)
        try:
            issue_date_input = datetime.datetime.strptime(issue_date_input,'%d.%m.%Y')
            print(datetime.date.strftime(issue_date_input,'%d.%m.%Y'))
            issue_date = datetime.date.strftime(issue_date_input,'%d-%m-%Y')
            return issue_date
        except ValueError:
            print ('Введен некорректный формат даты')
            continue

# ФУНКЦИЯ ДЛЯ ПОКАЗА ЗАМЕТОК

def display_notes(notes):
    if len(notes[::]) == 0:
        print(f'У вас нет сохранённых заметок.')
    else:
        while input('Если Вы хотите вывести на экран заметки целиком, то введите цифру - 1, '
                    'а если только заголовки - отличную от 1: ') == '1':
            print(Fore.YELLOW + 'Список заметок.')
            for i in notes:
                print(Fore.YELLOW + '------------------------------------------------------')
                print(Style.BRIGHT+Fore.LIGHTMAGENTA_EX+f'Заметка № {notes.index(i) + 1}:')
                for j,k in i.items():
                    print(Fore.LIGHTCYAN_EX+f'{j}: {k}')
            return notes

        else:
            print(Fore.YELLOW + 'Список заголовков.')
            for dict_ in notes:
                print(Fore.YELLOW + '------------------------------------------------------')
                print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + f'Заголовок № {notes.index(dict_) + 1}:')
                print(Fore.LIGHTCYAN_EX +f'{dict_['title']}')
    return notes



# ФУНКЦИЯ ДЛЯ ОБНОВЛЕНИЯ ЗАМЕТОК

def update_note(note):
    print(f'Текущие данные заметки:\n'
          f'{note}')
    answ_key = input('Какие данные вы хотите обновить? (username, title, content, status, issue_date): ').lower()
    while answ_key not in list(note.keys()) and answ_key != '':
        answ_key = input('Указано неверное имя поля. Укажите имя поля еще раз: ').lower()
        continue
    else:
                if answ_key == '' :
                    print('Новое имя поля не указано.')
                    return update_note(note)
                elif answ_key == 'issue_date':
                    note['issue_date'] = issue_date()
                    while input('Хотите изменить другое поле заметки(Да/Нет)?: ').capitalize() == 'Да':
                        return update_note(note)
                    else:
                        return note
                while True:
                    for key in note:
                        while answ_key == key and answ_key != 'issue_date':
                            note_key = input(f'Введите новое значение для {answ_key}: ').capitalize()
                            if input(f'Вы уверены, что хотите изменить поле - {answ_key} (Да/Нет)?: ').capitalize() != 'Да':
                                return update_note(note)
                            note[key] = note_key
                            while input('Хотите изменить другое поле заметки(Да/Нет)?: ').capitalize() == 'Да':
                                print('Заметка НЕ обновлена')
                                return update_note(note)
                            else:
                                print(f'Заметка обновлена!')
                                return note


# ФУНКЦИЯ ДЛЯ ПОИСКА ЗАМЕТОК

def search_notes(notes, keyword, status):
    if keyword == status == '':
        print('Вы не указали ни одного критерия для поиска!')
        return notes
    way_search = input('Выберите способ поиска:\n'
          '1 - поиск по ключевому слову и статусу, 2 - поиск по ключевому слову, 3 - поиск по статусу: ')
    if way_search not in ['1', '2', '3']:
        print('Вы указали не существующий способ поиска')
        return search_notes(notes, keyword, status)
    while way_search == '1':
        counter_1 = 0
        for i in notes:
            if keyword in i.values() and status in i.values():
                print(f'Заметка № {notes.index(i) + 1}')
                for j,k in i.items():
                    print(j,k)
            else:
                counter_1 += 1
            if counter_1 == len(notes):
                    print('По Вашему запросу заметок не найдено!')
                    return search_notes(notes,keyword,status)
        return notes

    while way_search == '2':
        counter_2 = 0
        for i in notes:
            if keyword in i.values():
                print(f'Заметка № {notes.index(i) + 1}')
                for j, k in i.items():
                    print(j, k)
            else:
                counter_2 += 1
            if counter_2 == len(notes):
                print('По Вашему запросу заметок не найдено!')
                return search_notes(notes,keyword,status)
        return notes
    while way_search == '3':
        counter_3 = 0
        for i in notes:
            if status in i.values():
                print(f'Заметка № {notes.index(i) + 1}')
                for j, k in i.items():
                    print(j, k)
            else:
                counter_3 += 1
            if counter_3 == len(notes):
                print('По Вашему запросу заметок не найдено!')
                return search_notes(notes,keyword,status)
        return notes
    return notes


# ФУНКЦИЯ ДЛЯ УДАЛЕНИЯ ЗАМЕТОК

def delete_note(delete_list):
    input_ = input('Укажите имя пользователя или заголовок заметки, которую хотите удалить: ').capitalize()
    while input_ == '':
        input_ = input('Вы ничего не указали, пожалуйста, укажите имя пользователя или заголовок еще раз: ').capitalize()
        continue
    else:
        while True:
            count_del = len(delete_list)
            for i in delete_list:
                if input_ == i.get('username') or input_ == i.get('title'):
                    answ_sure_del = input('Вы уверены, что хотите удалить заметку!? (Да/Нет): ').capitalize()
                    if answ_sure_del == 'Да':
                        delete_list.remove(i)
                    else:
                        return delete_list
                continue
            if len(delete_list) != count_del:
                print('Заметка успешно удалена!')
            elif len(delete_list) == count_del:
                print('Заметка не найдена!')
            return delete_list



# ФУНКЦИЯ МЕНЮ

def menu():
    list_note = []
    while True:
        choice = input(Back.BLACK + Fore.RED + Style.DIM + '\tМеню действий:\n' + Back.RESET
                       + Fore.RESET  + Style.RESET_ALL + Fore.LIGHTBLUE_EX + '1 - Создать новую заметку\n'
                       + Fore.RESET + Fore.LIGHTBLUE_EX + '2 - Показать все заметки\n'
                       + Fore.RESET + Fore.LIGHTBLUE_EX + '3 - Обновить заметку\n'
                       + Fore.RESET + Fore.LIGHTBLUE_EX + '4 - Удалить заметку\n'
                       + Fore.RESET + Fore.LIGHTBLUE_EX + '5 - Найти заметки\n'
                       + Fore.RESET + Fore.LIGHTBLUE_EX + '6 - Выйти из программы.\n'
                       + Fore.RESET + Fore.LIGHTBLUE_EX + 'Ваш выбор: ')
        if choice == '1':
           list_note.append(create_note(username=input('Укажите имя пользователя: ').capitalize(), title= input('Укажите заголовок заметки: ').capitalize(),status=input(f'Укажите статус заметки\n'
                                '(Выберите соответствующую цифру\n'
                                ' или введите статус в текстовом формате):\n'
                                '1.Новая\n'
                                '2.В процессе\n'
                                '3.Выполнено \n'
                                'Ваш выбор: ').capitalize(),content=input('Укажите описание заметки:  ').capitalize(),
              create_date=datetime.date.strftime(datetime.datetime.today().date(),'%d-%m-%Y'),
              issue_date=input('Введите дату дедлайна (в формате: дд-мм-гг.): ')))
           continue
        elif choice == '2':
            display_notes(list_note)
            continue
        elif choice not in ['1','2','3','4','5','6']:
            print(Fore.RED + Back.LIGHTYELLOW_EX + 'Неверный выбор. Пожалуйста, выберите действие из списка.')
            continue
        elif choice == '3':
                while choice:
                    try:
                        num_note = int(input(('Заметку под каким номером Вы хотите обновить?: '))) - 1
                        list_note[num_note] = update_note(list_note[num_note])
                        break
                    except ValueError:
                        print(Fore.RED + Back.LIGHTYELLOW_EX + 'Указано неверное значение. Номер заметки необходимо указывать цифрами.')
                        continue
                    except IndexError:
                        print(Fore.RED + Back.LIGHTYELLOW_EX + 'Заметки под таким номером не существует!!!')
                        break
        elif choice == '4':
            delete_note(list_note)
            continue
        elif choice == '5':
            while len(list_note) != 0:
                search_notes(list_note, input('Введите ключевое слово для поиска Вашей заметки: ').capitalize(), input('Введите статус для поиска Вашей заметки: ').capitalize())
                break
            else:
                print(Fore.RED + Back.LIGHTYELLOW_EX + 'Заметки еще не созданы!!!!')
                continue
        elif choice == '6':
            return list_note

menu()




