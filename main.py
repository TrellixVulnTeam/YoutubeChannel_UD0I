import sqlite3
import random
import string
from tkinter import *

root = Tk()

class Password:

    password = []
    letters = string.ascii_lowercase
    new_pwd = ''

    def __init__(self, number_char, context):
        self._number_char = int(number_char)
        self._context = context

    def add_password(self):
        # Falta gerar condicional para caso o number_char seja par ou ímpar.
        for i in range(self._number_char):
            if i % 2 == 0:
                self.password.append(random.choice(self.letters))
            elif i % 2 == 1:
                self.password.append(random.randint(0, 9))  
        #self.password = str(self.password)  
        print(f'Password with {self._number_char} characters for {self._context}: ', end='')    
        for text in self.password:
            print(f'{text}', end='')
        
class GUI(Password):
    def __init__(self):
        self.root = root
        self.screen()

    def screen(self):
        self.root.title('Password Manager 1.0')
        self.root.configure(bg='black')
        self.root.geometry('700x500+300+120')
        self.root.mainloop()


class BackEnd:
    pass
    


if __name__ == '__main__':

    GUI()


