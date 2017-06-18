#!/usr/bin/python3


import tkinter as tk
from tkinter import messagebox


# functions
def count(timer):
    m, s = divmod(timer, 60)
    global m
    global s
    time_label.configure(text='{:02d}:{:02d}'.format(m, s))
    cnt_label.configure(text='Session: {}'.format(counter))
    job = root.after(1000, count, timer - 1)
    global job


def alert():
    messagebox.askquestion("Time is Up!", "Start Break?")


def stop_count():
    root.after_cancel(job)
    time_label.configure(text='{:02d}:{:02d}'.format(0, 0))
    counter = 0
    global counter
    cnt_label.configure(text='Session: {}'.format(0))


def pause_count():
    # TODO
    return 0


def start():
    global session
    global short_break
    global counter
    global long_break
    global test

    counter += 1
    count(test)
    if counter % 4 == 0:
        if m == 0 and s == 0:
            res = alert()
            if res == "yes":
                count(long_break)
            else:
                stop_count()
    else:
        if m == 0 and s == 0:
            res = alert()
            if res == "yes":
                count(short_break)
            else:
                stop_count()

# root & title
root = tk.Tk()
root.title('Pomodoro')

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
start_button = tk.Button(main_label, text="Start", command=lambda: start())
start_button.grid(row=2, column=1)
pause_button = tk.Button(main_label, text="Pause", command=lambda: pause_count())
pause_button.grid(row=2, column=2)
stop_button = tk.Button(main_label, text="Stop", command=lambda: stop_count())
stop_button.grid(row=2, column=3)

# mainloop
root.mainloop()
