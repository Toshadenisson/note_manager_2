import datetime

note_dict = {'username':'Алексей', 'title':'Список покупок',
             'content':'Купить продукты на неделю','status':'Новая',
             'created_date': '27-11-2024', 'issue_date': '30-11-2024'}

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


def update_note(note = note_dict):
    print(f'Текущие данные заметки:\n'
          f'{note}')
    answ_key = input('Какие данные вы хотите обновить? (username, title, content, status, issue_date): ')
    while answ_key not in list(note.keys()) and answ_key != '':
        answ_key = input('Указано неверное имя поля. Укажите имя поля еще раз: ')
        continue
    else:
                if answ_key == '' :
                    print('Новое имя поля не указано.')
                    print(note)
                    return note
                elif answ_key == 'issue_date':
                    note['issue_date'] = issue_date()
                    while input('Хотите изменить другое поле заметки(Да/Нет)?: ').capitalize() == 'Да':
                        return update_note()
                    else:
                        print(note)
                        return note
                while True:
                    for key in note:
                        while answ_key == key and answ_key != 'issue_date':
                            note_key = input(f'Введите новое значение для {answ_key}: ')
                            if input(f'Вы уверены, что хотите изменить поле - {answ_key} (Да/Нет)?: ').capitalize() != 'Да':
                                return update_note()
                            note[key] = note_key
                            while input('Хотите изменить другое поле заметки(Да/Нет)?: ').capitalize() == 'Да':
                                print('Заметка НЕ обновлена')
                                return update_note()
                            else:
                                print(f'Заметка обновлена:'
                                      f'\n note')
                                return note

update_note()







