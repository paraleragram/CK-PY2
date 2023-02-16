import random

if __name__ == "__main__":
    class Games:
        def __init__(self, name: str, developer: str, genre: str):

            """
            Создание и подготовка к работе объекта "Игры"
            :param name: Название игры
            :param developer: Разработчик игры
            :param genre: Жанр игры

            Примеры:
            >>> game1 = Games('The witcher 3: Wild Hunt', 'CD Project RED', 'RPG')
            """
            self._name = name
            self._developer = developer
            self._genre = genre

        @property
        def name(self) -> str:
            return self._name
        @name.setter
        def name(self, name) -> None:
            if  not isinstance(name, str):
                raise TypeError('The name of game must be str!')

        @property
        def developer(self) -> str:
            return self._developer

        @developer.setter
        def developer(self, developer) -> None:
            if not isinstance(developer, str):
                raise TypeError('The developer`s name of game must be str!')

        @property
        def genre(self) -> str:
            return self._genre

        @genre.setter
        def genre(self, genre) -> None:
            if not isinstance(genre, str):
                raise TypeError('The genre of game must be str!')

        @staticmethod
        def start_the_game():

            """
            Функция выводит предупреждение о том, что игра началась
            :return: None

            Примеры:

            >>> game1 = Games('The witcher 3: Wild Hunt', 'CD Project RED', 'RPG')
            >>> game1.start_the_game()
            """
            print('The game is afoot!')

        @staticmethod
        def character_selection(character_list: list) -> str:

            """
            Функция определяет, какого персонажа выбрал пользователь. Есть возможность выбрать пользователя случайным
            образом
            :param character_list: список доступных персонажей
            :return: выбранного персонажа

            Примеры:

            >>> game2 = Games('Grand Theft Auto V', 'Rockstar North', 'Action-Adventure' )
            >>> character_list = ['Michael De Santa', 'Franklin Clinton', 'Trevor Philips']
            >>> game2.character_selection(character_list)
            """
            flag = input('random character?[y/n]')
            if flag is 'y':
                selected_character = random.choice(character_list)
            else:
                selected_character = character_list[int(input('number of your character'))-1]

            return selected_character

        def __str__(self) -> str:
            return f'Игра {self.name}, от разработчика {self.developer} в жанре {self.genre}'

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(name={self.name!r}, developer={self.developer!r}, genre={self.genre!r})"

    class TableGame(Games):

        def __init__(self, name: str, developer: str, genre: str, min_number_of_players: int, max_number_of_players: int):
            """
            Создание и подготовка к работе объекта "Настольная игра"
            :param name: название игры
            :param developer: разработчик игры
            :param genre: жанр игры
            :param min_number_of_players: минмальное количество игроков
            :param max_number_of_players: максимальное количество игроков

            Примеры:
            >>> game3 = TableGame('Catan', 'Klaus Teuber', 'стратегия', 3, 4)
            """
            super().__init__(name, developer, genre)
            self._min_number_of_players = min_number_of_players
            self._max_number_of_players = max_number_of_players

        @property
        def min_number_of_players(self) -> int :
            return self._min_number_of_players

        @min_number_of_players.setter
        def min_number_of_players(self, new_players) -> None:
            if new_players is int:
                if new_players > self._max_number_of_players:
                    raise ValueError('Too many players!')
            else: raise TypeError('The number of players must be int!')

        @property
        def max_number_of_players(self) -> int:
            return self._max_number_of_players

        @max_number_of_players.setter
        def max_number_of_players(self, new_players) -> None:
            if new_players is int:
                if new_players < self._min_number_of_players:
                    raise ValueError('Not enough players!')
            else:
                raise TypeError('The number of players must be int!')

        def character_selection(self, character_list: list) -> str:
            """
            Функция определяет, какого персонажа выбрал пользователь. После того как пользователь выбрал персонажа,
            имя персонажа удаляется из списка. Если в игре нет конкретных персонажей, то с помощью функции определяется
            очерёдность ходов игроков
            :param character_list: список персонажей
            :return: выбранного персонажа одним конкретным пользователем

            Примеры:
            >>>character_list = [Player1, Player2, Player3, Player4]
            >>>game3 = TableGame('Catan', 'Klaus Teuber', 'стратегия', 3, 4)
            >>>game3.character_selection(character_list)
            """
            selected_character = character_list[int(input('number of your character')) - 1]
            character_list.remove(selected_character)

            return selected_character

        def __str__(self) -> str:
            return f'Игра {self.name}, от разработчика {self.developer} в жанре {self.genre}, количество игроков ' \
                   f'{self.min_number_of_players}-{self.max_number_of_players}'

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(name={self.name!r}, developer={self.developer!r}, genre={self.genre!r},"\
                   f"min_number_of_players={self.min_number_of_players}, max_number_of_players=" \
                   f"{self.max_number_of_players})"

    class ComputerGame(Games):
        def __init__(self, name: str, developer: str, genre: str, memory_usage: float):
            """
            Создание и подготовка к работе объекта "Компьютерная игра"
            :param name: название игры
            :param developer: разработчик игры
            :param genre: жанр игры
            :param memory_usage: объём занимаемой памяти

            Примеры:

            >>> game4 = ComputerGame('Counter-Strike Global Offensive', 'Valve Corporation', 'FPS', 15.0)
            """
            super().__init__(name, developer, genre)
            self._memory_usage = memory_usage

        @property
        def memory_usage(self) -> float:
            return self._memory_usage

        @memory_usage.setter
        def memory_usage(self, new_memory_usage: float) -> None:
            if new_memory_usage is not float:
                raise TypeError('The memory usage must be float!')

        def __str__(self) -> str:
            return f'Игра {self.name}, от разработчика {self.developer} в жанре {self.genre}, необходимая память ' \
                   f'{self.memory_usage} Гб'

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(name={self.name!r}, developer={self.developer!r}, genre={self.genre!r}, " \
                   f"memory_usage={self.memory_usage})"

    pass
