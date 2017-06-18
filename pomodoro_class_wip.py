#!/usr/bin/python3

# Pomodoro Timer
# Created by Guido Minieri
# Date - June 2017
# Desc: My personal take for the most popular productivity tool out there.

import tkinter as t


# Class Definition
class Pomodoro(t.Tk):
    def __init__(self):
        t.Tk.__init__(self)
        self.title('Pomodoro Timer')
        self.tm_label = t.Label(self, text='', width=25)
        self.tm_label.pack()
        self.remaining = 0
        self.countdown(25 * 60)

    def countdown(self, remaining=None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.tm_label.configure(text='Time is up!')
        else:
            self.m, self.s = divmod(self.remaining, 60)
            self.tm_label.configure(text="{:02d}:{:02d}  ||  Counter:".format(self.m, self.s))
            self.remaining -= 1
            self.after(1000, self.countdown)

    def update_counter(self):
        return 1

# Main function
if __name__ == '__main__':
    app = Pomodoro()
    app.mainloop()
