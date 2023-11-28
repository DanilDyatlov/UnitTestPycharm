"""Модуль тестов"""
from comparison import ListComparison


comp = ListComparison()


def test_calculation_average_value():
    """ Проверка на правильность расчетов """
    lst = [1, 1, 1, 1, 1]
    assert comp.calculation_average_value(lst) == 1.0


def test_average_value_first_more_second():
    """ Сравнение первого и второго """
    lst_1 = [3, 3, 3, 3, 3]
    lst_2 = [1, 1, 1, 1, 1]
    assert comp.comparison(lst_1, lst_2) == "Первый список имеет большее среднее значение"


def test_average_value_second_more_first():
    """ Сравнение первого и второго """
    lst_3 = [1, 1, 1, 1, 1]
    lst_4 = [3, 3, 3, 3, 3]
    assert comp.comparison(lst_3, lst_4) == "Второй список имеет большее среднее значение"


def test_average_value_first_equal_second():
    """ Сравнение первого и второго """
    lst_5 = [1, 1, 1, 1, 1]
    lst_6 = [1, 1, 1, 1, 1]
    assert comp.comparison(lst_5, lst_6) == "Средние значения равны"
