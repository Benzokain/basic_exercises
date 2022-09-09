from collections import Counter
from for_challenges import get_gender

def dict_to_most_list(dict):
    some_list = []
    for element in dict:
        some_list.append(element['first_name'])
    most_names = Counter(some_list)
    return most_names

def get_gender(name, is_male):
    return ('девочка','мальчик')[is_male[name]]

def get_count_of_gender(dict:list, is_male:dict)->dict: # подаем school['students']
    list_of_gender = []
    list_of_names = []
    for element in dict:
        for name in element.get('students'):
            list_of_names.append(name.get('first_name'))
        # some_list.append(element['students'])
            for _name in list_of_names:
                list_of_gender.append(get_gender(_name, is_male))
    most_gender = Counter(list_of_gender)
    # most_names = Counter(some_list)
    return most_gender


        # for _class in school:
        # print('Класс ',_class.get('class'),':','девочки ', sep='')
        # for name in _class.get('students'):
        #     print(name.get('first_name'))

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


    # Задание 4
    # Для каждого класса нужно вывести количество девочек и мальчиков в нём.
    # Пример вывода:
    # Класс 2a: девочки 2, мальчики 0 
    # Класс 2б: девочки 0, мальчики 2

# def get_gender(name, is_male):
#     return ('женский','мужской')[is_male[name]]
    test = [
                {'class': '2a', 
                                'students': [
                                                {'first_name': 'Маша'}
                                            ]
                }
            ]
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
        print('Класс ',_class.get('class'),':','девочки ', sep='')
        for name in _class.get('students'):
            print(name.get('first_name'))

    print(get_count_of_gender(school, is_male))

    # for index, _class in enumerate(school, start=0):
    #     print('Класс ',_class.get('class'),':','девочки', _class.get('students')[index].get('first_name'))
        

#get_count_of_gender(_class.get('students'),is_male)

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
    # ???

if __name__ == "__main__":
    main()