import datetime

def create_note(**kwargs):
    while kwargs ['username'] == '':
        kwargs ['username']=input('Вы не указали имя пользователя. Пожалуйста, укажите имя пользователя еще раз: ')
        continue
    while kwargs['title'] == '':
        kwargs['title']=input('Вы не указали заголовок. Пожалуйста, укажите заголовок еще раз: ')
        continue
    while kwargs['content'] == '':
        kwargs['content']=input('Вы не указали описание заметки. Пожалуйста, укажите описание еще раз: ')
        continue

    for i in kwargs:
        while i == 'status':
            if kwargs [i] == '1' or kwargs[i] == 'Новая':
                kwargs[i] = 'Новая'
                break

            if kwargs[i] == '2'or kwargs[i]=='В процессе':
                kwargs[i] = 'В процессе'
                break

            if kwargs[i]=='Выполнена' or kwargs[i] == '3':
                kwargs[i]='Выполнена'
                break

            else:
                kwargs[i]=input(f'Указан не существующий статус. \n'
                                'Укажите статус заметки\n'
                                '(Выберите соответствующую цифру\n'
                                ' или введите статус в текстовом формате):\n'
                                '1.Новая\n'
                                '2.В процессе\n'
                                '3.Выполнено \n'
                                'Ваш выбор: ').capitalize()
                continue

    while True:
        try:
            kwargs['issue_date'] = (datetime.date.strftime
                                    ((datetime.datetime.strptime(kwargs['issue_date'], '%d-%m-%Y')),
                                     '%d-%m-%Y'))
            break
        except ValueError:
            kwargs['issue_date']=input('Введен некорректный формат даты.'
                                       'Введите дату окончания дедлайна (в формате д-м-г): ')
            continue

    print(kwargs)

    return kwargs



create_note(username=input('Укажите имя пользователя: '), title= input('Укажите заголовок заметки: '),status=input(f'Укажите статус заметки\n'
                                '(Выберите соответствующую цифру\n'
                                ' или введите статус в текстовом формате):\n'
                                '1.Новая\n'
                                '2.В процессе\n'
                                '3.Выполнено \n'
                                'Ваш выбор: ').capitalize(),content=input('Укажите описание заметки:  '),
              create_date=datetime.date.strftime(datetime.datetime.today().date(),'%d-%m-%Y'),
              issue_date=input('Введите дату дедлайна (в формате: дд-мм-гг.): '))

