import random


def date_to_text(date):
    day = {'01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвертое', '05': 'пятое', '06': 'шестое', '07': 'седьмое',
           '08': 'восьмое', '09': 'девятое', '10': 'десятое', '11': 'одиннадцатое', '12': 'двенадцатое', '13': 'тринадцатое',
           '14': 'четырнадцатое', '15': 'пятнадцатое', '16': 'шестнадцатое', '17': 'семнадцатое', '12': 'восемнадцатое',
           '19': 'девятнадцатое', '20': 'двадцатое', '30': 'тридцатое', '31': 'тридцать первое'}
    for i in range(1,10):  # в двадцатых числах есть хоть какое-то единообразие, их автоматизируем
        day['2'+str(i)] = 'двадцать ' + day['0'+str(i)]

    month = {'01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая', '06': 'июня', '07': 'июля',
             '08': 'августа', '09': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря'}

    date_list = date.split('.')
    return day[date_list[0]]+' '+month[date_list[1]]+' '+date_list[2]+' года'

famous_people = {'Александр Сергеевич Пушкин': '26.05.1799', 'Вольфганг Амадей Моцарт': '27.01.1756', 'Исаак Ньютон': '04.01.1643',
                 'Альберт Эйнштейн': '14.03.1879', 'Чарльз Дарвин': '12.02.1809', 'Николай Коперник': '19.02.1473',
                 'Джордж Вашингтон': '22.02.1732', 'Карл Маркс': '05.05.1818', 'Людвиг ван Бетховен': '16.12.1770',
                 'Зигмунд Фрейд': '06.05.1856'}

answer = 'y'

while answer == 'y':
    sample = random.sample(sorted(famous_people), 5)

    correct = 0
    for person in sample:
        d = input('Когда родился '+person+'? ')
        if d.strip() != famous_people[person]:
            print('Это неверный ответ. Дата рождения '+person+': ' + date_to_text(famous_people[person]))
        else:
            print('Это верный ответ!')
            correct += 1
    answer = input('Раунд окончен, количество верных ответов: '+str(correct)+'. Хотите повторить? (y/n) ')
