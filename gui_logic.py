from tkinter import *
import os

def main() -> None:
    global display
    global equation
    problem = []
    equation = ''
    root = Tk()			#Creates a widget that acts as a window.
    root.title('logic_calc')		#Gives the window a name.
    root.geometry('540x580')		#Sets the length and width of the window.
    root.resizable(False, False)			#Will make the window unchangeable.
    root.configure(bg = '#333333') #Sets the background color.

    Button(root, text='T', width=4, height=1, font=('arial', 30), bd=1, fg='#00FFFF', bg='#000000', command=lambda: [modify(' T '), problem.append(True)]).place(x=0,y=220)
    Button(root, text='F', width=4, height=1, font=('arial', 30), bd=1, fg='#00FFFF', bg='#000000', command=lambda: [modify(' F '), problem.append(False)]).place(x=180, y=220)
    Button(root, text='clear', width=4, height=1, font=('arial', 30), bd=1, fg='#00FFFF', bg='#000000', command=lambda: [modify(''), problem.clear(), display.config(text='')]).place(x=360, y=220)
    Button(root, text='or', width=4, height=1, font=('arial', 30), bd=1, fg='#00FFFF', bg='#000000', command=lambda: [modify(' or '), problem.append('or')]).place(x=0, y=310)
    Button(root, text='and', width=4, height=1, font=('arial', 30), bd=1, fg='#00FFFF', bg='#000000', command=lambda:[modify(' and '), problem.append('and')]).place(x=180, y=310)
    Button(root, text='enter', width=4, height=1, font=('arial', 30), bd=1, fg='#00FFFF', bg='#000000', command=lambda: [modify(''), enter(problem)]).place(x=360, y=310)
    Button(root, text='nor', width=4, height=1, font=('arial', 30), bd=1, fg='#00FFFF', bg='#000000', command=lambda: [modify(' nor '), problem.append('nor')]).place(x=0, y=400)
    Button(root, text='nand', width=4, height=1, font=('arial', 30), bd=1, fg='#00FFFF', bg='#000000', command=lambda: [modify(' nand '), problem.append('nand')]).place(x=180, y=400)
    Button(root, text='xor', width=4, height=1, font=('arial', 30), bd=1, fg='#00FFFF', bg='#000000', command=lambda: [modify(' xor '), problem.append('xor')]).place(x=360, y=400)
    Button(root, text='funny button', width=15, height=0, font=('arial', 30), bd=1, fg='#00FFFF', bg='#000000', command=lambda: funny_function()).place(x=0, y=490)


    display = Label(root, width=20, height=3, text=equation, font=('arial', 30))

    display.pack()
    root.mainloop()


def modify(value) -> None:
    global display
    global equation

    value = str(value)
    if value == 'TRUE' or value == 'FALSE':
        display.config(text='')
        display.config(text=value)

    elif value == '':
        equation = ''
        display.config(text=equation)

    else:
        equation += value
        display.config(text=equation)

def enter(equation_list) -> None:
    if equation_list[1] == 'or':
      ansr = OR(equation_list[0], [2])
      modify(ansr)
    if equation_list[1] == 'and':
        ansr = AND(equation_list[0], [2])
        modify(ansr)
    if equation_list[1] == 'nor':
        ansr = NOR(equation_list[0], [2])
        modify(ansr)
    if equation_list[1] == 'nand':
        ansr = NAND(equation_list[0], [2])
        modify(ansr)
    if equation_list[1] == 'xor':
        ansr = XOR(equation_list[0], [2])
        modify(ansr)


def funny_function() -> None:
    modify(' get rickrolled lol ')
    os.system('chromium https://shattereddisk.github.io/rickroll/rickroll.mp4')

def OR(a, b) -> bool:
    if a == True or b == True:
        return True
    else:
        return False
def AND(a, b) -> bool:
    if a == True and b == True:
        return True
    else:
        return False
def NOR(a, b) -> bool:
    if a == True or b == True:
        return False
    else:
        return True
def NAND(a, b) -> bool:
    if a == True and b == True:
        return False
    else:
        return True
def XOR(a, b) -> bool:
    if a == True and b == True:
        return False
    elif a == False and b == False:
        return False
    elif a == True or b == True:
        return True


main()