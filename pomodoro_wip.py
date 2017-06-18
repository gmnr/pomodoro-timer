#!/usr/bin/python3


import tkinter as tk
from tkinter import messagebox


# functions
def count(timer):
    m, s = divmod(timer, 60)
    time_label.configure(text='{:02d}:{:02d}'.format(m, s))
    cnt_label.configure(text='Session: {}'.format(counter))
    if timer == 0:
        time_label.configure(text='TIME IS UP!!')
        alert()
        return 0
    root.after(1000, count, timer - 1)


def alert():
    messagebox.askquestion("Work Session Terminated", "Click here to rest")


def stop_count():
    # TODO
    return 0


def pause_count():
    # TODO
    return 0


# root & title
root = tk.Tk()
root.geometry('{}x{}'.format(200, 50))
root.title('Pomodoro Timer')

# main label area
main_label = tk.Frame(root)
main_label.grid(row=2, column=3, columnspan=1)

# time label
time_label = tk.Label(main_label, text='00:00')
time_label.grid(row=1, column=1, columnspan=1)

# placehodler label
placeholder_label = tk.Label(main_label, text=' ~ ')
placeholder_label.grid(row=1, column=2)
# counter label
cnt_label = tk.Label(main_label, text='Session: 0')
cnt_label.grid(row=1, column=3, columnspan=1)

# define periods
short_break = 5 * 60
long_break = 20 * 60
session = 25 * 60
test = 2

# counter
counter = 0

# buttons
start_button = tk.Button(main_label, text="Start", command=lambda: count(test))
start_button.grid(row=2, column=1)
stop_button = tk.Button(main_label, text="Stop", command=lambda: stop_count)
stop_button.grid(row=2, column=2)
pause_button = tk.Button(main_label, text="Pause", command=lambda: pause_count)
pause_button.grid(row=2, column=3)

# mainloop
root.mainloop()
