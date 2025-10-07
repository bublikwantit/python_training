import random


class BoardOutException(Exception):
    """ Исключение для выхода за границы доски """
    pass


class BoardUsedException(Exception):
    """ Исключение для выстрела в уже использованную клетку """
    pass


class BoardWrongShipException(Exception):
    """ Исключение для неправильной расстановки кораблей """
    pass


class Dot:
    """ Класс точки на поле """

    def __init__(self, x, y):
        self.x = x  # номер строки
        self.y = y  # номер столбца

    def __eq__(self, other):
        """ Проверка точек на равенство """
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Dot({self.x}, {self.y})"


class Ship:
    """ Класс корабля """

    def __init__(self, bow, length, direction):
        self.bow = bow  # точка носа корабля
        self.length = length  # длина корабля
        self.direction = direction  # 0 - горизонтальное, 1 - вертикальное
        self.lives = length  # количество жизней

    @property
    def dots(self):
        """ Возвращает список всех точек корабля """
        ship_dots = []
        for i in range(self.length):
            if self.direction == 0:  # горизонтальный
                new_x = self.bow.x
                new_y = self.bow.y + i
            else:  # вертикальный
                new_x = self.bow.x + i
                new_y = self.bow.y
            ship_dots.append(Dot(new_x, new_y))
        return ship_dots

    def shooten(self, shot):
        """ Проверка, попадает ли выстрел в корабль """
        return shot in self.dots


class Board:
    """ Основной класс игровой доски """

    def __init__(self, hid=False):
        self.field = [["О"] * 6 for _ in range(6)]  # игровое поле
        self.ships = []  # список кораблей
        self.hid = hid  # скрывать корабли или нет
        self.live_ships = 0  # количество живых кораблей
        self.busy = []  # занятые точки (корабли + контуры)
        self.shots = []  # точки, в которые уже стреляли

    def __str__(self):
        """ Отображение доски в консоли """
        res = "    | 1 | 2 | 3 | 4 | 5 | 6 |"
        res += "\n   -----------------------------"
        for i, row in enumerate(self.field):
            res += f"\n {i + 1} | " + " | ".join(row) + " |"
        if self.hid:
            res = res.replace("■", "О")
        return res

    def out(self, dot):
        """ Проверка, выходит ли точка за границы доски """
        return not ((0 <= dot.x < 6) and (0 <= dot.y < 6))

    def contour(self, ship, verb=False):
        """ Обводит корабль по контуру, если он был убит - вокруг корабля стрелять нельзя, автоматически помечаются Т """
        around = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        for dot in ship.dots:
            for dx, dy in around:
                cur = Dot(dot.x + dx, dot.y + dy)
                if not self.out(cur) and cur not in self.busy:
                    if verb:
                        # Помечаем только пустые клетки как промахи
                        if self.field[cur.x][cur.y] == "О":
                            self.field[cur.x][cur.y] = "T"
                    self.busy.append(cur)

    def add_ship(self, ship):
        """ Добавление корабля на доску """
        for dot in ship.dots:
            if self.out(dot) or dot in self.busy:
                raise BoardWrongShipException()

        for dot in ship.dots:
            self.field[dot.x][dot.y] = "■"
            self.busy.append(dot)

        self.ships.append(ship)
        self.live_ships += 1
        self.contour(ship)

    def shot(self, dot):
        """ Выстрел по доске """
        if self.out(dot):
            raise BoardOutException("Выстрел за границы поля!")

        if dot in self.shots:
            raise BoardUsedException("Уже стреляли в эту клетку!")

        self.shots.append(dot)

        for ship in self.ships:
            if dot in ship.dots:
                ship.lives -= 1
                self.field[dot.x][dot.y] = "X"
                if ship.lives == 0:
                    self.live_ships -= 1
                    self.contour(ship, verb=True)
                    print("Корабль уничтожен!")
                    return True
                else:
                    print("Корабль ранен!")
                    return True

        self.field[dot.x][dot.y] = "T"
        print("Мимо!")
        return False


class Player:
    """Базовый класс игрока"""

    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def ask(self):
        """ Спросить игрока, куда стрелять """
        raise NotImplementedError()

    def move(self):
        """ Сделать ход """
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except (BoardOutException, BoardUsedException) as e:
                print(e)


class AI(Player):
    """ Класс игрока-компьютера AI """

    def ask(self):
        """С лучайный выстрел AI """
        dot = Dot(random.randint(0, 5), random.randint(0, 5))
        print(f"Ход AI: {dot.x + 1} {dot.y + 1}")
        return dot


class User(Player):
    """Класс игрока-пользователя"""

    def ask(self):
        """ Запрос координат выстрела у пользователя """
        while True:
            try:
                coords = input("Ваш ход (строка столбец): ").split()
                if len(coords) != 2:
                    print("Введите 2 координаты!")
                    continue

                x, y = coords  # x - строка, y - столбец
                if not (x.isdigit()) or not (y.isdigit()):
                    print("Введите числа!")
                    continue

                x, y = int(x), int(y)
                return Dot(x - 1, y - 1)  # x - строка, y - столбец

            except ValueError:
                print("Ошибка ввода! Попробуйте снова.")


class Game:
    """ Класс игры """

    def __init__(self):
        self.user_board = self.random_board()
        self.ai_board = self.random_board()
        self.ai_board.hid = True  # скрываем корабли компьютера

        self.user = User(self.user_board, self.ai_board)
        self.ai = AI(self.ai_board, self.user_board)

    def random_board(self):
        """ Генерация случайной доски """
        board = None
        while board is None:
            board = self.random_place()
        return board

    def random_place(self):
        """ Попытка расставить корабли на доске """
        board = Board()
        attempts = 0

        # Расставляем корабли: 1x3, 2x2, 4x1
        ships = [3, 2, 2, 1, 1, 1, 1]

        for length in ships:
            attempts = 0
            while True:
                attempts += 1
                if attempts > 2000:
                    return None  # Не удалось расставить корабли

                # Случайные координаты и направление
                direction = random.randint(0, 1)
                if direction == 0:  # горизонтальный
                    x = random.randint(0, 5)  # строка фиксирована
                    y = random.randint(0, 6 - length)  # столбец меняется
                else:  # вертикальный
                    x = random.randint(0, 6 - length)  # строка меняется
                    y = random.randint(0, 5)  # столбец фиксирован

                ship = Ship(Dot(x, y), length, direction)

                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass

        # Очищаем список занятых точек для начала игры
        board.busy = []
        return board

    def greet(self):
        """ Приветствие """
        print("-------------------")
        print("      Привет!      ")
        print("                   ")
        print(" Игра Морской бой  ")
        print("-------------------")
        print(" формат ввода: x y ")
        print(" x - номер строки  ")
        print(" y - номер столбца ")
        print("Пример: 3 4 - строка 3, столбец 4")

    def loop(self):
        """ Основной игровой цикл """
        num = 0
        while True:
            print("-" * 20)
            print("Доска пользователя:")
            print(self.user_board)
            print("-" * 20)
            print("Доска компьютера:")
            print(self.ai_board)

            if num % 2 == 0:
                print("-" * 20)
                print("Ходит пользователь!")
                repeat = self.user.move()
            else:
                print("-" * 20)
                print("Ходит компьютер!")
                repeat = self.ai.move()

            if self.ai_board.live_ships == 0:
                print("-" * 20)
                print("Пользователь выиграл!")
                break

            if self.user_board.live_ships == 0:
                print("-" * 20)
                print("Компьютер выиграл!")
                break

            if repeat:
                num -= 1

            num += 1

    def start(self):
        """Запуск игры"""
        self.greet()
        self.loop()


def main():
    """ Запускаем главную функцию """
    try:
        game = Game()
        game.start()
    except KeyboardInterrupt:
        print("\n\nИгра прервана!")
    except Exception as e:
        print(f"\nПроизошла ошибка: {e}")


if __name__ == "__main__":
    main()
