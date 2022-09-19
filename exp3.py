# Создайте программу для игры в ""Крестики-нолики"".

from tkinter import *
import random
from tkinter import messagebox 

games = Tk()
games.title('Criss-cross')
game_run = True
pole = []
cross_count = 0

def new_game():
    for row in range(3):
        for col in range(3):
            pole[row][col]['text'] = ' '
            pole[row][col]['background'] = 'lavender'
    global game_run
    game_run = True
    global cross_count
    cross_count = 0

def click(row, col):
    if (game_run) & (pole[row][col]['text'] == ' '):
        pole[row][col]['text'] = 'X'
        global cross_count
        cross_count += 1
        check_win('X')
        if (game_run) & (cross_count < 5):
            computer_move()
            check_win('O')
        elif cross_count == 5:
            messagebox.showinfo('Info', 'Ничья!')

def check_win(smb):
    for n in range(3):
        check_line(pole[n][0], pole[n][1], pole[n][2], smb)
        check_line(pole[0][n], pole[1][n], pole[2][n], smb)
    check_line(pole[0][0], pole[1][1], pole[2][2], smb)
    check_line(pole[2][0], pole[1][1], pole[0][2], smb)

def check_line(a1,a2,a3,smb):
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:       
        global game_run
        game_run = False
        if a1['text'] == 'O':
            a1['background'] = a2['background'] = a3['background'] = 'red'
            messagebox.showinfo('Info', 'Lose!')
        else:
            a1['background'] = a2['background'] = a3['background'] = 'green'
            messagebox.showinfo('Info', 'Win!')

def can_win(a1,a2,a3,smb):
    res = False
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ':
        a3['text'] = 'O'
        res = True
    if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb:
        a2['text'] = 'O'
        res = True
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb:
        a1['text'] = 'O'
        res = True
    return res

def computer_move():
    for n in range(3):
        if can_win(pole[n][0], pole[n][1], pole[n][2], 'O'):
            return
        if can_win(pole[0][n], pole[1][n], pole[2][n], 'O'):
            return
    if can_win(pole[0][0], pole[1][1], pole[2][2], 'O'):
        return
    if can_win(pole[2][0], pole[1][1], pole[0][2], 'O'):
        return
    for n in range(3):
        if can_win(pole[n][0], pole[n][1], pole[n][2], 'X'):
            return
        if can_win(pole[0][n], pole[1][n], pole[2][n], 'X'):
            return
    if can_win(pole[0][0], pole[1][1], pole[2][2], 'X'):
        return
    if can_win(pole[2][0], pole[1][1], pole[0][2], 'X'):
        return
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if pole[row][col]['text'] == ' ':
            pole[row][col]['text'] = 'O'
            break

for row in range(3):
    line = []
    for col in range(3):
        button = Button(games, text=' ', width=4, height=2, 
                        font=('Verdana', 25, 'bold'),
                        background='lavender',
                        command=lambda row=row, col=col: click(row,col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    pole.append(line)
new_button = Button(games, text='new game', command=new_game)
new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')
games.mainloop()