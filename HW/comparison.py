"""Модуль приложения"""


class ListComparison:
    """Класс для сравнения списков"""
    @staticmethod
    def calculation_average_value(lst):
        """Метод для расчета среднего значения списка.
        Использование статического метода обосновано те,
        что он не знает ничего о классе и экземпляре.
        Он просто получает аргументы и его можно вызвать без создания экземпляра класса.
        Сделали проверку, если лист пустой"""
        # if not lst:
        #     return 0
        return sum(lst) / len(lst)

    def comparison(self, lst_1, lst_2):
        """ Методы для сравнения средних размеров списка с выводом ответа.
        Для расчета использую статический метод """
        average_1 = self.calculation_average_value(lst_1)
        average_2 = self.calculation_average_value(lst_2)
        if average_1 > average_2:
            return "Первый список имеет большее среднее значение"
        if average_1 < average_2:
            return "Второй список имеет большее среднее значение"
        return "Средние значения равны"
