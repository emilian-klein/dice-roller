import random
import tkinter as tk


class DiceRoller(tk.Tk):
    dice_images = ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png"]

    def __init__(self):
        super().__init__()
        self.title("Dice Roller")
        self.geometry("400x200")
        self.resizable(False, False)
        self.iconbitmap("images/icon.ico")
        self.font_style = ("Helvetica", "10", "bold")

        self.top_frame = tk.Frame(self)
        self.top_frame.pack()

        self.bottom_frame = tk.Frame(self)
        self.bottom_frame.pack()

        self.roll_button = tk.Button(self.bottom_frame, text="Roll dices", fg="white", bg="cornflowerblue", relief="groove",
                                     command=self.roll_dices, font=self.font_style)
        self.roll_button.pack()

        self.exit_button = tk.Button(self.bottom_frame, text="Exit", fg="white", bg="cornflowerblue", relief="groove", command=self.quit,
                                     font=self.font_style)
        self.exit_button.pack()

    def roll_dices(self):
        dice_value = random.randint(1, 6)
        dice_image = tk.PhotoImage(file=f"images/{dice_value}.png")

        dice_image = dice_image.subsample(3)
        dice_label = tk.Label(self.top_frame, image=dice_image)
        dice_label.pack()


if __name__ == "__main__":
    app = DiceRoller()
    app.mainloop()

# #Author: emilian-klein
#
# from tkinter import *
# from PIL import Image, ImageTk
# import random
#
# #function which is called when button is pressed
# def rollDice():
#     dice_value1 = random.choice(dice)
#     dice_value2 = random.choice(dice)
#     value = int(dice_value1.split('.')[0]) + int(dice_value2.split('.')[0])
#     values_label.configure(text='Total value: ' + str(value))
#     dice_image1 = ImageTk.PhotoImage(Image.open(dice_value1))
#     dice_image2 = ImageTk.PhotoImage(Image.open(dice_value2))
#     dice_label1.configure(image=dice_image1)
#     dice_label1.image = dice_image1
#     dice_label2.configure(image=dice_image2)
#     dice_label2.image = dice_image2
#
# #main application window
# root = Tk()
# root.geometry('400x200')
# root.title('Dice Roller')
# root.resizable(False, False)
# root.iconbitmap('icon.ico')
#
# #frames to separate widgets within the window
# topframe = Frame(root)
# topframe.pack(expand=TRUE)
#
# bottomframe = Frame(root)
# bottomframe.pack()
#
# #list of dice pictures
# dice = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png']
# dice_value1 = random.choice(dice)
# dice_value2 = random.choice(dice)
# dice_image1 = ImageTk.PhotoImage(Image.open(dice_value1))
# dice_image2 = ImageTk.PhotoImage(Image.open(dice_value2))
#
# dice_label1 = Label(topframe, image=dice_image1)
# dice_label1.image = dice_image1
# dice_label1.pack(side=LEFT)
#
# dice_label2 = Label(topframe, image=dice_image2)
# dice_label2.image = dice_image2
# dice_label2.pack(side=LEFT)
#
# #getting sum of dice_value1 and dice_value2
# value = int(dice_value1.split('.')[0]) + int(dice_value2.split('.')[0])
# values_label = Label(bottomframe, text='Total value: ' + str(value))
# values_label.pack(side=TOP)
#
# roll_button = Button(bottomframe, text='Roll the dice', fg='blue', relief='groove', command=rollDice)
# roll_button.configure(font=('Helvetica', '10', 'bold'))
# roll_button.pack()
#
# root.mainloop()
