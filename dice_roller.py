import tkinter as tk
import random
from PIL import Image, ImageTk


class DiceRoller(tk.Tk):
    """
        Attributes:
            dice_images (list): List of image filenames for dice faces.

        Methods:
            __init__(self)
                Initializes the DiceRoller GUI application with title, size, frames, labels, and buttons.

            roll_dices(self)
                Simulates rolling two dice, updates displayed dice images, and calculates the total value of the dice rolls.
        """
    dice_images = ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png"]

    def __init__(self):
        """
        Initialize the DiceRoller GUI application.
        Sets up the application window, creates frames, labels, and buttons.
        """
        super().__init__()
        self.title("Dice Roller")
        self.geometry("400x220")
        self.resizable(False, False)
        self.iconbitmap("images/icon.ico")
        self.sm_font_style = ("Helvetica", "10", "bold")
        self.lg_font_style = ("Helvetica", "13", "bold")

        self.top_frame = tk.Frame(self)
        self.top_frame.pack(pady=10)
        self.dice_image1 = tk.Label(self.top_frame)
        self.dice_image1.pack(side=tk.LEFT)
        self.dice_image2 = tk.Label(self.top_frame)
        self.dice_image2.pack(side=tk.LEFT)

        self.middle_frame = tk.Frame(self)
        self.middle_frame.pack()
        self.total_value = tk.Label(self.middle_frame, fg="cornflowerblue", font=self.lg_font_style)
        self.total_value.pack()

        self.bottom_frame = tk.Frame(self)
        self.bottom_frame.pack(pady=10)
        self.roll_button = tk.Button(self.bottom_frame, text="Roll dices", fg="white", bg="cornflowerblue", relief="groove", command=self.roll_dices,
                                     font=self.sm_font_style, width=10, cursor="hand2")
        self.roll_button.pack(side=tk.LEFT, padx=10)
        self.exit_button = tk.Button(self.bottom_frame, text="Exit", fg="white", bg="cornsilk4", relief="groove", command=self.quit, font=self.sm_font_style,
                                     width=10, cursor="hand2")
        self.exit_button.pack(side=tk.LEFT)

    def roll_dices(self):
        """
        Simulates rolling two dice, updates displayed dice images, and calculates the total value of the dice rolls.
        Generates two random numbers between 1 and 6 to simulate rolling two dice.
        Updates the displayed images of the dice faces.
        Calculates and displays the total value of the dice rolls.
        """
        total_value = 0
        for dice_image_widget in [self.dice_image1, self.dice_image2]:
            dice_value = random.randint(1, 6)
            path_to_image = f"images/{dice_value}.png"
            dice_image = ImageTk.PhotoImage(Image.open(path_to_image))
            dice_image_widget.configure(image=dice_image)
            dice_image_widget.image = dice_image
            total_value += dice_value
        self.total_value.config(text=f"Total value: {total_value}")


if __name__ == "__main__":
    app = DiceRoller()
    app.roll_dices()
    app.mainloop()
