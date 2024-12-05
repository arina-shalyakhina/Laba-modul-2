import doctest
class Pot:
  def __init__(self, real_pelmeni_number: int, max_pelmeni_number: int):
        """
        Создание и подготовка к работе объекта "Кастрюля"

        :param real_pelmeni_number: число пельменей в кастрюле в действительности
        :param max_pelmeni_number: максимальное число пельменей, помещаемых в кастрюлю
        Примеры:
        >>> pot = Pot(12, 20) # инициализация экземпляра класса
        """
        if not isinstance(real_pelmeni_number, int):
            raise TypeError("число пельменей должно быть типа int")
        if real_pelmeni_number <= 0:
            raise ValueError("Число пельменей должен быть положительным числом")
        self.real_pelmeni_number = real_pelmeni_number

        if not isinstance(max_pelmeni_number, int):
            raise TypeError(" Максимальное число пельменей должно быть int")
        if max_pelmeni_number < 0:
            raise ValueError("максимальное число пельменей не может быть отрицательным числом")
        self.max_pelmeni_number = max_pelmeni_number
  def is_empty_pot(self) -> bool:
        """
        Функция которая проверяет есть ли пельмешки в кастрюле

        :return: Является ли кастрюля пустой

        Примеры:
        >>> pot = Pot(12, 20)
        >>> pot.is_empty_pot()
        """
        ...
  def remove_pelmeni_from_pot(self, extracted_pelmeni: int) -> None:
        """Извлечение пельменей из кастрюли

        :param extracted_pelmeni: Объем извлекаемых пельменей
        :raise ValueError: Если количество извлекаемых пельменей превышает число пельменей в кастрюле в действительности,
        то возвращается ошибка.

        :return: Объем реально удалённых пельменей

        Примеры:
        >>> pot = Pot(12, 20)
        >>> pot.remove_pelmeni_from_pot(3)
        """
        ...

if __name__ == "__main__":
    doctest.testmod()
class Phone:
  def __init__(self, brand: str, price: int):
        """
        Создание и подготовка к работе объекта "Телефон"

        :param brand: название фирмы, изготовившей телефон
        :param price: стоимость телефона
        Примеры:
        >>> phone = Phone("Samsung", 20000) # инициализация экземпляра класса
        """
        if not isinstance(brand, str):
            raise TypeError("Фирма должна быть типа str")
        self.brand = brand

        if not isinstance(price, int):
            raise TypeError(" Стоимость должна быть int")
        if price <= 0:
            raise ValueError("Стоимость не может быть неположительным числом")
        self.price = price
  def cost_per_month(self, months: int) -> None:
        """Сколько нужно платить в месяц за телефон, если купил в условиях рассрочки (проценты не начисляются)

        :param months: число месяцев в договоре рассрочки

        :return: Стоимость за телефон в месяц

        Примеры:
        >>> phone = Phone("Samsung", 20000)
        >>> phone.cost_per_month(3)
        """
        ...
  def cost_comparison(self, compared_price: int) -> bool:
        """Проверка на равенство цены телефона с неким целым числом

        :param compared_price: цена, для которой следует установить или опровергнуть равенство с фактической ценой телефона

        :return: равна ли фактическая цена телефона compared_price

        Примеры:
        >>> phone = Phone("Samsung", 20000)
        >>> phone.cost_comparison(20000)
        """
        ...

if __name__ == "__main__":
    doctest.testmod()
class Programmer:
  def __init__(self, language: str, projects_number: int):
        """
        Создание и подготовка к работе объекта "Программист"

        :param language: название наиболее часто используемого языка программирования
        :param projects_number: число выполненных проектов
        Примеры:
        >>> programmer = Programmer("Python", 20) # инициализация экземпляра класса
        """
        if not isinstance(language, str):
            raise TypeError("Язык программирования должна быть типа str")
        self.language = language
        if not isinstance(projects_number, int):
            raise TypeError(" Число проектов должно быть int")
        if projects_number < 0:
            raise ValueError("Стоимость не может быть отрицательным числом")
        self.projects_number = projects_number
  def wage_for_projects(self, per_project: int) -> None:
        """Сколько программист может получить всего денег, если выполнил определенное число проектов (за каждый проект одно и то же число денег)

        :param per_project: число денег за один проект
        :return: Сколько всего денег получил за проекты

        Примеры:
        >>> programmer = Programmer("Python", 20)
        >>> programmer.wage_for_projects(200)
        """
        ...
  def cost_comparison(self, verifiable_language) -> bool:
        """Является ли тот или иной язык программирования предпочтительным для программиста

        :param verifiable_language: язык программирования, с которым сравниваем используемый язык

        :return: соответствует ли используемый язык проверяемому языку

        Примеры:
        >>> programmer = Programmer("Python", 20)
        >>> programmer.cost_comparison("R")
        """
        ...
if __name__ == "__main__":
    doctest.testmod()