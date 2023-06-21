import pygame
import random

pygame.init()

# Рисуем сетку игрового поля
def draw_grid(scr):
    pygame.draw.line(scr, (0, 0, 0), (100, 0), (100, 300), 3)
    pygame.draw.line(scr, (0, 0, 0), (200, 0), (200, 300), 3)
    pygame.draw.line(scr, (0, 0, 0), (0, 100), (300, 100), 3)
    pygame.draw.line(scr, (0, 0, 0), (0, 200), (300, 200), 3)

# Рисуем все 0 и Х на игровом поле
def draw_tic_tac_toe(scr, items):
    for i in range(3):
        for j in range(3):
            if items[i][j] == "0":
                pygame.draw.circle(scr, (255, 0, 0), (j * 100 + 50, i * 100 + 50), 45)
            elif items[i][j] == "x":
                pygame.draw.line(scr, (0, 0, 255), (j * 100 + 5, i * 100 + 5), (j * 100 + 95, i * 100 + 95), 3)
                pygame.draw.line(scr, (0, 0, 255), (j * 100 + 95, i * 100 + 5), (j * 100 + 5, i * 100 + 95), 3)

#Проверяем все победные исходы игры
def get_win_check(fodmaster, symbol):
    flag_win = False
    for line in fodmaster:
        if line.count(symbol) == 3:
            flag_win = True
    for i in range(3):
        if fodmaster[0][i] == fodmaster[1][i] == fodmaster[2][i] == symbol:
            flag_win = True
    if fodmaster[0][0] == fodmaster[1][1] == fodmaster[2][2] == symbol:
        flag_win = True
    if fodmaster[0][2] == fodmaster[1][1] == fodmaster[2][0] == symbol:
        flag_win = True
    return  flag_win

#Размер экрана
SCREEN_SIZE = (300, 300)

window = pygame.display.set_mode(SCREEN_SIZE)
screen = pygame.Surface(SCREEN_SIZE)

# Название игры
pygame.display.set_caption("Крестики-нолики")
screen.fill((255, 255, 255))

# Игровое поле
field = [['', '', ''],
         ['', '', ''],
         ['', '', '']]
mainloop = True
game_over = False

# Основной цикл, где будут обрабатываться все результаты и выводиться на экран
while mainloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False

# Проверка всех событий (игрем крестиками)
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            pos = pygame.mouse.get_pos()
            if field[pos[1] // 100][pos[0] // 100] == "":
                field[pos[1] // 100][pos[0] // 100] = "x"
                x, y = random.randint(0, 2), random.randint(0, 2)
                while field[x][y] != "":
                    x, y = random.randint(0, 2), random.randint(0, 2)
                field[x][y] = "0"

            player_win = get_win_check(field, "x")
            ai_comp = get_win_check(field, "0")
            if player_win or ai_comp:
                game_over = True
                if player_win:
                    pygame.display.set_caption("Победа!")
                else:
                    pygame.display.set_caption("Проиграл")
            elif field[0].count("x") + field[0].count(0) + field[1].count("x") + \
            field[1].count("0") + field[2].count("x") + field[2].count("0"):
                pygame.display.set_caption("Ничья?")

    draw_tic_tac_toe(screen, field)
    draw_grid(screen)
    window.blit(screen, (0, 0))
    pygame.display.update()