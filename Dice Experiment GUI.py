#import modules
import tkinter as tk
import matplotlib.pyplot as plt
import math
import numpy as np
import random
import os

#import functions from modules
from tkinter import *
from tkinter.ttk import *
from random import seed
from random import randint
from matplotlib.ticker import MaxNLocator

# construct main window
root = tk.Tk(screenName = None, baseName = None, className = 'Tk', useTk = 1)
frame = Frame(root)
frame.pack()
bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )
root.title('Dice Experiment')

#styling
style = Style()
style.configure('TButton', bg = 'orange', font = ('calibri', 20, 'bold'), borderwidth = '4')
style.map('TButton', foreground = [('active', 'green')],
                     background = [('active', 'black')])

#close window
def close(diceExperiment):
    root.destroy()

#results window
def results():
    resultScreen = tk.Tk(screenName = 'Results', baseName = None, className = 'Tk', useTk = 1)
    with open('randomDiceToss.txt', 'r') as file:
        Label(resultScreen, text=file.read()).pack()
    resultScreen.title('Results')
    resultScreen.mainloop()
    
    
#dice experiment
def diceExperiment():
    #seed random number generator
    seed(1)

    #how many rolls
    times = [10, 100, 1000, 10000]

    #roll the die
    for t in times:
        y = int(t)
        #set face count values
        one = 0
        two = 0
        three = 0
        four = 0
        five = 0
        six = 0
        #roll 10 times
        for i in range(y):
            #roll die
            roll = randint(1, 6)
            #count faces
            if roll == 1:
                one += 1
            elif roll == 2:
                two += 1
            elif roll == 3:
                three += 1
            elif roll == 4:
                four += 1
            elif roll == 5:
                five += 1
            else:
                six += 1
        #create temporary file
        with open('randomDiceToss.txt', 'a') as file:
            if y == 10:
                file.write('FOR TEN TOSSES \n')
            elif y == 100:
                file.write('FOR ONE HUNDRED TOSSES \n')
            elif y == 1000:
                file.write('FOR ONE THOUSAND TOSSES \n')
            else:
                file.write('FOR TEN THOUSAND TOSSES \n')
            file.write('ones: ' + str(one) + '\n')
            file.write('twos: ' + str(two) + '\n')
            file.write('threes: ' + str(three) + '\n')
            file.write('fours: ' + str(four) + '\n')
            file.write('fives: ' + str(five) + '\n')
            file.write('sixes: ' + str(six) + '\n')
            file.write('\n')
        #create bar chart
        columns = ('one', 'two', 'three', 'four', 'five', 'six')
        count = (one, two, three, four, five, six)

        #count by whole numbers
        ax = plt.figure().gca()
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))

        #Set table labels
        plt.bar(columns, count, align='center', alpha=0.5)
        plt.gca().yaxis.grid(True)
        if y == 10:
            plt.title('10 Tosses')
            plt.xlabel('Number Rolled \n Close window to see 100 tosses')
        elif y == 100:
            plt.title('100 Tosses')
            plt.xlabel('Number Rolled \n Close window to see 1000 tosses')
        elif y == 1000:
            plt.title('1000 Tosses')
            plt.xlabel('Number Rolled \n Close window to see 10000 tosses')
        else:
            plt.title('10000 Tosses')
        plt.ylabel('Frequency')

        #display table
        plt.show()
    close(diceExperiment)
    #display results
    results()
    #remove file
    os.remove('randomDiceToss.txt')
        
#create buttons
button = Button(
    frame,
    text = 'Click Here to \n Roll the Die',
    command = diceExperiment
    )
button.grid(row = 1, column = 1, padx = 20, pady = 5)

