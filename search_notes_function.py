notes = [{'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая',
          'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
         {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'в процессе',
          'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
         {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект', 'status': 'выполнено',
          'created_date': '20-11-2024', 'issue_date': '26-11-2024'}]

def search_notes(notes, keyword = None, status = None):
    if len(notes) == 0:
        print('Список заметок пуст!!!!')
        pass
    if keyword == status == '':
        print('Вы не указали ни одного критерия для поиска!')
        pass
    while keyword and status:
        list_count1 = []
        for i in notes:
            if keyword in i.values() and status in i.values():
                print(f'Заметка № {notes.index(i) + 1}')
                for j,k in i.items():
                    print(j,k)
            else:
                list_count1.append('')
                if len(list_count1) == len(notes):
                    print('По Вашему запросу заметок не найдено!')
        return notes

    while keyword:
        list_count2 = []
        for i in notes:
            if keyword in i.values():
                print(f'Заметка № {notes.index(i) + 1}')
                for j, k in i.items():
                    print(j, k)
            else:
                list_count2.append('')
                if len(list_count2) == len(notes):
                    print('По Вашему запросу заметок не найдено!')
        return notes

    while status:
        list_count3 = []
        for i in notes:
            if status in i.values():
                print(f'Заметка № {notes.index(i) + 1}')
                for j, k in i.items():
                    print(j, k)
            else:
                list_count3.append('')
                if len(list_count3) == len(notes):
                    print('По Вашему запросу заметок не найдено!')
        return notes

search_notes(notes, status = input("Введите статус: ").lower(), keyword = (input('Введите ключевое слово: ')).capitalize())




