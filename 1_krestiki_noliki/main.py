# Консольная игра "Крестики-нолики" (3x3)
# Используются: простые типы данных, функции, условные операторы, циклы, переменные
# Дополнительно показаны декоратор, замыкание и генератор

# --- Декоратор для красивого вывода действий ---
def announce(func):
    def wrapper(*args, **kwargs):
        print("-" * 25)
        result = func(*args, **kwargs)
        print("-" * 25)
        return result
    return wrapper

# --- Инициализация поля ---


def new_board():
    return [["-" for _ in range(3)] for _ in range(3)]

# --- Печать поля ---


@announce
def print_board(board):
    print("  0 1 2")
    for i, row in enumerate(board):
        print(i, " ".join(row))

# --- Замыкание: функция проверки победителя ---


def make_winner_checker(board):
    def check():
        lines = []
        # строки
        lines.extend(board)
        # столбцы
        for c in range(3):
            lines.append([board[r][c] for r in range(3)])
        # диагонали
        lines.append([board[i][i] for i in range(3)])
        lines.append([board[i][2 - i] for i in range(3)])

        for line in lines:
            if line[0] != "-" and line.count(line[0]) == 3:
                return line[0]
        return None
    return check

# --- Генератор свободных клеток ---


def free_cells(board):
    for r in range(3):
        for c in range(3):
            if board[r][c] == "-":
                yield r, c

# --- Основная игра ---


def game():
    board = new_board()
    check_winner = make_winner_checker(board)
    players = ["x", "o"]
    turn = 0

    print("Крестики-нолики 3x3. Пустые клетки — '-'.")
    print_board(board)

    while True:
        player = players[turn % 2]
        # ввод координат
        try:
            move = input(f"Ход игрока '{player}' (строка столбец): ").split()
            r, c = int(move[0]), int(move[1])
        except (ValueError, IndexError):
            print("Ошибка ввода! Нужно два числа через пробел (0..2).")
            continue

        if (r, c) not in list(free_cells(board)):
            print("Клетка занята или вне диапазона. Попробуйте снова.")
            continue

        board[r][c] = player
        print_board(board)

        # проверка победителя
        w = check_winner()
        if w:
            print(f"Победил игрок '{w}'!")
            break

        # ничья
        if not any(True for _ in free_cells(board)):
            print("Ничья!")
            break

        turn += 1


if __name__ == "__main__":
    game()
