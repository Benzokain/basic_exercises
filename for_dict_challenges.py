from collections import Counter
from for_challenges import get_gender

def dict_to_most_list(dict):
    some_list = []
    for element in dict:
        some_list.append(element['first_name'])
    most_names = Counter(some_list)
    return most_names

def main():
    # Задание 1
    # Дан список учеников, нужно посчитать количество повторений каждого имени ученика
    # Пример вывода:
    # Вася: 1
    # Маша: 2
    # Петя: 2

    students = [
        {'first_name': 'Вася'},
        {'first_name': 'Петя'},
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Петя'},
    ]

    for name, count in dict_to_most_list(students).items():
        print(f'{name}: {count}')


    # Задание 2
    # Дан список учеников, нужно вывести самое часто повторящееся имя
    # Пример вывода:
    # Самое частое имя среди учеников: Маша
    students = [
        {'first_name': 'Вася'},
        {'first_name': 'Петя'},
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ]
    print(f'Самое частое имя среди учеников: {max(dict_to_most_list(students), key=dict_to_most_list(students).get)}')
    print('*'*20)

    # Задание 3
    # Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
    # Пример вывода:
    # Самое частое имя в классе 1: Вася
    # Самое частое имя в классе 2: Маша

    school_students = [
        [  # это – первый класс
            {'first_name': 'Вася'},
            {'first_name': 'Вася'},
        ],
        [  # это – второй класс
            {'first_name': 'Маша'},
            {'first_name': 'Маша'},
            {'first_name': 'Оля'},
        ],[  # это – третий класс
            {'first_name': 'Женя'},
            {'first_name': 'Петя'},
            {'first_name': 'Женя'},
            {'first_name': 'Саша'},
        ],
    ]
    for num_class, name in enumerate(school_students, start=1):
        print(f'Самое частое имя в классе {num_class}: {max(dict_to_most_list(name), key=dict_to_most_list(name).get)}')
    # print('*'*20)

    # Задание 4
    # Для каждого класса нужно вывести количество девочек и мальчиков в нём.
    # Пример вывода:
    # Класс 2a: девочки 2, мальчики 0 
    # Класс 2б: девочки 0, мальчики 2

    school = [
        {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
        {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
        {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
    ]
    is_male = {
        'Олег': True,
        'Маша': False,
        'Оля': False,
        'Миша': True,
        'Даша': False,
    }

    print('*'*20)    
    for _class in school:
        gender_list = []
        print(f'Класс {_class.get("class")}: ', end='')
        for name in _class.get('students'):
            gender_list.append(get_gender(name.get('first_name'),is_male, plural=True))
        else:
            print(f'девочки {gender_list.count("девочки")}, мальчики {gender_list.count("мальчики")}')
    print('*'*20)
        

    # Задание 5
    # По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
    # Пример вывода:
    # Больше всего мальчиков в классе 3c
    # Больше всего девочек в классе 2a

    school = [
        {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
        {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    ]
    is_male = {
        'Маша': False,
        'Оля': False,
        'Олег': True,
        'Миша': True,
    }
    gender_list = []
    result_dict = {}
  
    for _class in school:
        for name in _class.get('students'):
            gender_list.append(get_gender(name.get('first_name'), is_male, plural='yes'))
        else:
            result_dict.setdefault(_class.get("class"), dict(девочки = gender_list.count("девочки"), мальчики=gender_list.count("мальчики")))
            gender_list.clear()
    print(result_dict)
    # print(result_dict.get('2a')) # <class 'NoneType'> ?
    if result_dict.get('2a').get('мальчики') > result_dict.get('3c').get('мальчики'):
        print(f'Больше всего мальчиков в классе 2a')
    else:
        print(f'Больше всего мальчиков в классе 3c')

    if result_dict.get('2a').get('девочки') > result_dict.get('3c').get('девочки'):
        print(f'Больше всего девочек в классе 2a')
    else:
        print(f'Больше всего девочек в классе 3c')




    # for key, value in result_dict.items():
    #     if value['маль']

if __name__ == "__main__":
    main()