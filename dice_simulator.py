#Author: emilian-klein

from tkinter import *
from PIL import Image, ImageTk
import random

#function which is called when button is pressed
def rollDice():
    dice_value1 = random.choice(dice)
    dice_value2 = random.choice(dice)
    value = int(dice_value1.split('.')[0]) + int(dice_value2.split('.')[0])
    values_label.configure(text='Total value: ' + str(value))
    dice_image1 = ImageTk.PhotoImage(Image.open(dice_value1))
    dice_image2 = ImageTk.PhotoImage(Image.open(dice_value2)) 
    dice_label1.configure(image=dice_image1)
    dice_label1.image = dice_image1
    dice_label2.configure(image=dice_image2)
    dice_label2.image = dice_image2

#main application window
root = Tk()
root.geometry('400x200')
root.title('Dice Roller')
root.resizable(False, False)
root.iconbitmap('dice_simulator_icon.ico')

#frames to separate widgets within the window
topframe = Frame(root)
topframe.pack(expand=TRUE)

bottomframe = Frame(root)
bottomframe.pack()

#list of dice pictures
dice = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png']
dice_value1 = random.choice(dice)
dice_value2 = random.choice(dice)
dice_image1 = ImageTk.PhotoImage(Image.open(dice_value1))
dice_image2 = ImageTk.PhotoImage(Image.open(dice_value2))

dice_label1 = Label(topframe, image=dice_image1)
dice_label1.image = dice_image1
dice_label1.pack(side=LEFT)

dice_label2 = Label(topframe, image=dice_image2)
dice_label2.image = dice_image2
dice_label2.pack(side=LEFT)

#getting sum of dice_value1 and dice_value2
value = int(dice_value1.split('.')[0]) + int(dice_value2.split('.')[0])
values_label = Label(bottomframe, text='Total value: ' + str(value))
values_label.pack(side=TOP)

roll_button = Button(bottomframe, text='Roll the dice', fg='blue', relief='groove', command=rollDice)
roll_button.configure(font=('Helvetica', '10', 'bold'))
roll_button.pack()

root.mainloop()