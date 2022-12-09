from typing import Union
import doctest

# TODO Написать 3 класса с документацией и аннотацией типов
class Dress:
    def __init__(self, cost: Union[int, float], color: str, size: Union[str, int]):
        """
        Создание и подготовка к работе объекта "Платье"
        :param cost: Цена платья
        :param color: Цвет платья
        :param size: Размер платья

        Примеры:
        >>> dress1 = Dress(4500, 'yellow', 'M')
        >>> dress2 = Dress(5000, 'black', 42)
        """
        if not isinstance(cost, (int, float)):
            raise TypeError("Цена платья должна быть типа int или float")
        if cost < 0:
            raise ValueError("Цена платья не может быть отрицательным числом")
        self.cost = cost
        if not isinstance(color, str):
            raise TypeError("Цвет платья должен быть типа str")
        self.color = color
        if not isinstance(size, (str, int)):
            raise TypeError("Размер платья должен быть типа str или int")
        if type(size) is int:
            if not size > 0:
                raise ValueError("Размер платья не может быть отрицательным числом")
        self.size = size

    def purch(self, wallet: Union[int, float]) -> Union[int, float]:
        """
        Функция определяет, сколько денег останется у покупателя после покупки платья
        :param wallet: количество денег в кошельке
        :param self: платье
        :return: остаток в кошельке 
        
        Примеры:
        >>> dress1 = Dress(4500, 'yellow', 'M')
        >>> dress1.purch(30000)
        """
        if not isinstance(wallet, (int, float)):
            raise TypeError("Количество денег в кошельке должно быть типа int или float")
        ...

    def sale(self, wallet: Union[int, float]) -> Union[int, float]:
        """
        Функция определяет, сколько денег будет у продавца после продажи платья
        :param wallet:
        :param self:
        :return: остаток в кошельке
        
        Примеры:
        >>> dress1 = Dress(4500, 'yellow', 'M')
        >>> dress1.sale(180000)
        """
        if not isinstance(wallet, (int, float)):
            raise TypeError("Количество денег в кошельке должно быть типа int или float")
        ...
if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()

class Profile:
    def __init__(self, nickname: str, subscribers: int, content: str):
        """
        Создание и подготовка объекта "Профиль" в социальной сети
        :param nickname: Имя профиля
        :param subscribers: количество подписчиков
        :param content: контент страницы

        Примеры:
        >>> profile_ivan = Profile('Ivan99', 654, 'Hello, world!')
        """
        if not isinstance(nickname, str):
            raise TypeError("Имя профиля должно быть типа str")
        self.nickname = nickname
        if not isinstance(subscribers, int):
            raise TypeError("Количество подписчиков должно быть типа int")
        if subscribers < 0:
            raise ValueError("Количество подписчиков не может быть отрицательным числом")
        self.subscribers = subscribers
        if not isinstance(content, str):
            raise TypeError("Контент должен быть типа str")
        self.content = content

    def subscribe(self) -> None:
        """
        Изменяет количество подписчиков в профиле
        
        Примеры:
        >>> profile_ivan = Profile('Ivan99', 654, 'Hello, world!')
        >>> profile_ivan.subscribe()
        """
        ...

    def add_content(self, addition: str) -> None:
        """
        Добавление контента в профиль
        :param addition: новая запись
        
        Пример:
        >>> profile_ivan = Profile('Ivan99', 654, 'Hello, world!')
        >>> profile_ivan.add_content('My name is Ivan Ivanov')
        """
        if not isinstance(addition, str):
            raise TypeError("Контент должен быть типа str")
        ...

if __name__ == "__main__":
    doctest.testmod()

class FoodBasket:
    def __init__(self, products: list, wheels: bool):
        """
        Создание и подготовка объекта "Продуктовая корзина"
        :param products: список продуктов в корзине
        :param wheels: коризна на колёсиках или нет

        Примеры:
        >>> basket = FoodBasket(['bar of chocolate', 'loaf', 'head of garlic', 'head of garlic', 'Kefir'], False)
        """
        if not isinstance(products, list):
            raise TypeError("Список продуктов должен быть типа list")
        self.products = products

        if not isinstance(wheels, bool):
            raise TypeError("Наличие колёс должно быть типа bool")
        self.wheels = wheels

    def empty(self) -> None:
        """
        Освободить корзину от покупок
        
        Примеры:
        >>> basket = FoodBasket(['bar of chocolate', 'loaf', 'head of garlic', 'head of garlic', 'Kefir'], False)
        >>> basket.empty()
        """
        ...

    def add_to_basket(self, product: str) -> None:
        """
        Добавить в корзину товар
        :param product: товар
        :return: None

        Примеры:
        >>> basket = FoodBasket(['bar of chocolate', 'loaf', 'head of garlic', 'head of garlic', 'Kefir'], False)
        >>> basket.add_to_basket('eggplant')
        """

        if not isinstance(product, str):
            raise TypeError("Товар должен быть типа str")
        ...

    def is_empty(self) -> bool:
        """
        Функция проверяет, пустая ли корзина
        :return: Пустая ли корзина

        Примеры:
        >>> basket = FoodBasket(['bar of chocolate', 'loaf', 'head of garlic', 'head of garlic', 'Kefir'], False)
        >>> basket.is_empty()
        """
        ...

if __name__ == "__main__":
    doctest.testmod()