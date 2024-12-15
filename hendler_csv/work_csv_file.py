import csv
import datetime
from pprint import pprint
from typing import Any


def get_info_work_day() -> list[dict[str | Any, str | Any]]:
    """
    Функция, которая получает имя пользователя и потом проходиься по
    csv файлу и помещает в js файл
    :param user: как записан в exel файле
    :return:
    """
    name_file = 'data_base'
    js = []
    with open(f'{name_file}.csv', newline='', encoding='utf-8') as File:
        reader = csv.reader(File)
        for row in reader:
            js.append({
                'date': row[0].replace('\n', ' '),
                'order': row[1].replace('\n', ' '),
                'equipment': row[2].replace('\n', ' '),
                'comment': row[3],
                'Time': row[4].replace(' ', '').replace('.', ':'),
                'Watch': row[5].replace('\n', ' '),
                'comment|foto': row[6].replace('\n', ' '),
                'Teacher': row[7].replace('\n', ' '),
            })
    return js


def show_index(data, day: int, count: int = 0):
    """
    Функция предназначена для отображения index
     начало дня который указан в параметрах функции day

    Аргументы:
    - data : list - список заказов
    - day : int - число
    - count: int - счетчик
    """
    for order in data:
        order_day = order['date'][:2]
        count += 1
        try:
            if int(order_day) == int(day):
                return count
        except:
            pass


def filter_orders(data: list, start_index: int, finish_index: int):
    data_cut = data[start_index:finish_index]
    list_current_orders = []
    for data_element in data_cut:
        if data_element['order']:
            list_current_orders.append(data_element)
        else:
            pass
    return list_current_orders


def show_orders(day_start: int = 0, day_finish: int = 1):
    result = (get_info_work_day())
    day_today = datetime.date.today().day + day_start
    dey_tomorrow = datetime.date.today().day + day_finish
    stat_index = show_index(result, day_today)
    finish_index = show_index(result, dey_tomorrow)
    list_orders = filter_orders(result, stat_index, finish_index)
    return list_orders



