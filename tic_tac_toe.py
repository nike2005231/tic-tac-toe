print("Игра крестики-нолики, правила всем знакомы.")

# Переменная для отслеживания конца игры
end = False

# Игровое поле
table = [["*", "*", "*"],
         ["*", "*", "*"],
         ["*", "*", "*"]]

def display_table():
    for row in table:
        print(" ".join(row))

def check_draw():
    if all(cell != "*" for row in table for cell in row):
        print("Ничья")
        display_table()
        return True
    return False

def check_winner(player):
    symbol = "X" if player == 1 else "O"
    
    # Проверка строк и столбцов
    for i in range(3):
        if all(table[i][j] == symbol for j in range(3)) or all(table[j][i] == symbol for j in range(3)):
            print(f"Игрок {player} выиграл!")
            return True
    
    # Проверка диагоналей
    if all(table[i][i] == symbol for i in range(3)) or all(table[i][2 - i] == symbol for i in range(3)):
        print(f"Игрок {player} выиграл!")
        return True

    return False

def make_move(player):
    symbol = "X" if player == 1 else "O"
    while True:
        try:
            print(f"Ход игрока {player} ({symbol}):")
            row = int(input("Введите номер строки (1-3): ")) - 1
            col = int(input("Введите номер столбца (1-3): ")) - 1

            if 0 <= row < 3 and 0 <= col < 3 and table[row][col] == "*":
                table[row][col] = symbol
                break
            else:
                print("Некорректный ввод или ячейка уже занята. Попробуйте снова.")
        except ValueError:
            print("Пожалуйста, вводите только числа от 1 до 3.")

# Основной цикл игры
def main():
    global end
    display_table()

    while not end:
        for player in [1, 2]:
            make_move(player)
            display_table()

            if check_winner(player):
                end = True
                break
            
            if check_draw():
                end = True
                break

if __name__ == "__main__":
    main()