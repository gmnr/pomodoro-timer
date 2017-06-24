#!/usr/bin/python3


import tkinter as tk
from tkinter import messagebox


# ~Functions~
# basic countdown function
def count(timer):
    global FINISH
    global job

    if timer <= -1:
        FINISH = True
        return

    m, s = divmod(timer, 60)
    time_label.configure(text='{:02d}:{:02d}'.format(m, s))
    cnt_label.configure(text='Streak: {}'.format(SESS_COUNTER))
    job = root.after(1000, count, timer - 1)


# activates the prompt messagebox based on Break or not (still improve TODO)
def alert():
    if SESS_COUNTER % 4 == 0:
        messagebox.askquestion("Break Done!!", "Ready for a new session")
    else:
        messagebox.askquestion("Time is Up!", "Start Break?")


# stops the countdown and resets the counter
def stop_count():
    global SESS_COUNTER

    root.after_cancel(job)
    time_label.configure(text='{:02d}:{:02d}'.format(0, 0))
    SESS_COUNTER = 0
    cnt_label.configure(text='Streak: {}'.format(0))
    start_btn.configure(text="Start", command=lambda: start())


# pauses the counter
def pause_count():
    root.after_cancel(job)
    start_btn.configure(text="Cont.", command=tk.DISABLED)


# starts counting loop
# def start():
    # global SESSION
    # global SHORT_BREAK
    # global SESS_COUNTER
    # global LONG_BREAK
    # global TEST
    # global FINISH

    # SESS_COUNTER += 1
    # start_btn.configure(command=tk.DISABLED)
    # count(TEST)
    # if SESS_COUNTER % 4 == 0 and FINISH:
        # res = alert()
        # if res == "yes":
            # count(LONG_BREAK)
        # else:
            # stop_count()
    # elif SESS_COUNTER % 4 != 0 and FINISH:
        # res = alert()
        # if res == "yes":
            # count(SHORT_BREAK)
        # else:
            # stop_count()

def start():
    global TEST
    global SESS_COUNTER
    SESS_COUNTER += 1
    start_btn.configure(command=tk.DISABLED)


# ~VARIABLE DECLARATION~
# define sessions
SHORT_BREAK = 5 * 60
LONG_BREAK = 20 * 60
SESSION = 25 * 60
TEST = 2

# status change
FINISH = False

# session counter
SESS_COUNTER = 0


# ~TKINTER SETTINGS~
# root & title
root = tk.Tk()
root.title('Pomodoro')
root.geometry('200x60')

# ~Labels~
# main label area
main_label = tk.Frame(root)
main_label.grid(row=2, column=3, sticky='nesw')

# column padding in window
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)


# row padding in window
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)

# time label
time_label = tk.Label(main_label, text='00:00')
time_label.grid(row=1, column=1, columnspan=1)
# placehodler label
placeholder_label = tk.Label(main_label, text=' ~ ')
placeholder_label.grid(row=1, column=2)
# counter label
cnt_label = tk.Label(main_label, text='Streak: 0')
cnt_label.grid(row=1, column=3, columnspan=1)

# ~Buttons~
start_btn = tk.Button(main_label, text="Start", command=lambda: start())
start_btn.grid(row=2, column=1)
pause_btn = tk.Button(main_label, text="Pause", command=lambda: pause_count())
pause_btn.grid(row=2, column=2)
stop_btn = tk.Button(main_label, text="Stop", command=lambda: stop_count())
stop_btn.grid(row=2, column=3)

# ~MainLoop~
root.mainloop()
