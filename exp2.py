# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from tkinter import *
from tkinter import messagebox 
import random
from tkinter import scrolledtext

games = Tk()
games.title('Сandies')
game_run = True
candies_count = 2021
limits = 28
complexity = IntVar()
names = ['Player1: ', 'Player2: ', 'Computer: ']
move = 0
games.geometry('400x350')
text_progres = Label(games, text = 'Осталось конфет: 2021', font=('Verdana', 10))
pole = scrolledtext.ScrolledText(games, width=47, height=13, font=('Verdana', 10), state='disabled') 

def new_game():   
    global game_run
    game_run = True
    global candies_count
    candies_count = 2021
    global move
    move = 0
    text_progres.configure(text=f'Осталось конфет: 2021')
    pole.configure(state='normal')
    pole.delete(1.0, END)
    pole.configure(state='disabled')

def click(): 
    global candies_count 
    global complexity
    global move
    if (game_run) & (int(txt.get()) <= limits) & (int(txt.get()) <= candies_count): 
        write_complexity(int(txt.get()), names[move])     
        check_win(names[move], candies_count)
        if (game_run) & (candies_count != 0):
            if int(complexity.get()) == 0:
                if move == 0:
                    move = 1
                else:
                    move = 0 
            else:
                computer_move()

def write_complexity(count, name):
    global candies_count
    candies_count -= count
    res = "Осталось конфет: {}".format(candies_count)
    text_progres.configure(text=res) 
    pole.configure(state='normal')
    pole.insert(INSERT, f'{name}{count}\n')  
    pole.configure(state='disabled')             

def check_win(name, count):
    if count == 0:
        global game_run
        game_run = False
        messagebox.showinfo('Info', f'{name} Win!')

def computer_move():
    global complexity
    global candies_count
    count = 0
    write = 0
    if 1471 < candies_count < 1500:
        messagebox.showinfo('Computer', 'Тебе меня не победить!')
    if 300 < candies_count < 329:
        messagebox.showinfo('Computer', 'Сдавайся!')
    if (random.randint(1, 10) <= int(complexity.get())):
        while candies_count > count:
            count += 29           
        if candies_count == count:
            write = random.randint(1,28)
        elif candies_count > 29:
            write = candies_count - (count - 29)
        elif candies_count < 29:
            write = candies_count
    elif candies_count > 28:
        write = random.randint(1,28)
    elif candies_count < 29:
        write = candies_count   
    write_complexity(write, names[2])
    check_win(names[2], candies_count)

menu = Menu(games)  
new_games = Menu(menu)  
new_games.add_radiobutton(label= 'User', value=0, variable=complexity, command=new_game)
new_games.add_radiobutton(label= 'Easy', value=3, variable=complexity, command=new_game)
new_games.add_radiobutton(label= 'Medium', value=5, variable=complexity, command=new_game)
new_games.add_radiobutton(label= 'Hard', value=9, variable=complexity, command=new_game) 
menu.add_cascade(label = 'Games', menu = new_games)  
games.config(menu=menu) 
lbl = Label(games, text = 'Введите колличество конфет:', font=('Verdana', 10,))
txt = Entry(games, width=2, font=('Verdana', 15, 'bold'))
btn = Button(games, text='OK', width=3, 
             font=('Verdana', 15, 'bold'),
             background='lavender', command=click, )
new_button = Button(games, text='new game', command=new_game)
text_progres.grid(column=0, row=0)
pole.grid(column=0, row=1)
lbl.grid(column=0, row=2)
txt.grid(column=0, row=3)
btn.grid(column=0, row=4)
new_button.grid(row=5, column=0, columnspan=3, sticky='nsew')
games.mainloop()