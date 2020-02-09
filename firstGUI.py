import tkinter as tk # import gui module

# import everything from tkinter
from tkinter import *

# construct main window
root = tk.Tk(screenName = None, baseName = None, className = 'Tk', useTk = 1)
frame = Frame(root)
frame.pack()
bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )
root.title('My First GUI')

# hello world
def hello():
    helloscreen = tk.Tk(screenName = None, baseName = None, className = 'Tk', useTk = 1)
    hi = 'Hello tkinter!'
    hi = Message(helloscreen, text = hi)
    hi.config(bg = 'hotpink')
    hi.pack()
    helloscreen.mainloop()

#create input field
def input():
    newscreen = tk.Tk(screenName = None, baseName = None, className = 'Tk', useTk = 1)
    Label(newscreen, text = 'Enter your username:').grid(row = 0)
    Label(newscreen, text = 'Enter your password:').grid(row = 1)
    e1 = Entry(newscreen)
    e2 = Entry(newscreen)
    e1.grid(row = 0, column = 1)
    e2.grid(row = 1, column = 1)
    click = tk.Button(
        newscreen,
        text = 'submit',
        command = click.destroy
    )
    click.grid(row = 3)
    newscreen.mainloop()

#create buttons
bluebutton = Button(
    frame, text = 'DO NOT CLICK',
    fg = 'blue',
    width = 12,
    command = quit
    )
bluebutton.grid(row = 0, column = 1)
greenbutton = Button(
    frame,
    text = 'hello',
    fg = 'green',
    width = 12,
    command = hello
    )
greenbutton.grid(row = 0, column = 2)
blackbutton = Button(
    bottomframe,
    text = 'password',
    fg = 'black',
    width = 12,
    command = input
    )
blackbutton.grid(row = 1, column = 1)
redbutton = Button(
    bottomframe,
    text = 'done',
    fg = 'red',
    width = 12,
    command = root.destroy
    )
redbutton.grid(row = 1, column = 2)

root.mainloop() # mainloop() is an infinite loop which runs the application, waits for event, and processes until window is not closed

print(s1, s2)
'''
#define values for checkboxes
boxA = IntVar()
boxB = IntVar()

#create checkboxes
Checkbutton(window, text = 'cheeseburger', variable = boxA).grid(row = 3, sticky = W)
Checkbutton(window, text = 'french fries', variable = boxB).grid(row = 4, sticky = W)

click = tk.Button( # make button
    window, 
    text = 'Click Me',
    width = 25,
    height = 25,
    command = window.destroy
) 
click.pack()
'''

'''
# use Canvas
master = Tk()
w = Canvas(master, width = 40, height = 60)
w.pack()
canvas_height = 20
canvas_width = 200
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y)
mainloop()
'''

'''
There are 3 geometric configurations for GUIs

pack() method:It organizes the widgets in blocks before placing in the parent widget.
grid() method:It organizes the widgets in grid (table-like structure) before placing in the parent widget.
place() method:It organizes the widgets by placing them on specific positions directed by the programmer

Some Button(master, option = value) values:

activebackground: to set the background color when button is under the cursor.
activeforeground: to set the foreground color when button is under the cursor.
bg: to set he normal background color.
command: to call a function.
font: to set the font on the button label.
image: to set the image on the button.
width: to set the width of the button.
height: to set the height of the button.

Some Canvas(master, option = value) values:

bd: to set the border width in pixels.
bg: to set the normal background color.
cursor: to set the cursor used in the canvas.
highlightcolor: to set the color shown in the focus highlight.
width: to set the width of the widget.
height: to set the height of the widget.

Some CheckButton(master, option = value) values:

Title: To set the title of the widget.
activebackground: to set the background color when widget is under the cursor.
activeforeground: to set the foreground color when widget is under the cursor.
bg: to set he normal backgrouSteganography
Break

Secret Code:

Attach a File:nd color.

command: to call a function.
font: to set the font on the button label.
image: to set the image on the widget.

some Entry(master, option = value) values:

bd: to set the border width in pixels.
bg: to set the normal background color.
cursor: to set the cursor used.
command: to call a function.
highlightcolor: to set the color shown in the focus highlight.
width: to set the width of the button.
height: to set the height of the button.

some Frame(master, option = value) values:

highlightcolor: To set the color of the focus highlight when widget has to be focused.
bd: to set the border width in pixels.
bg: to set the normal background color.
cursor: to set the cursor used.
width: to set the width of the widget.
height: to set the height of the widget.

'''
