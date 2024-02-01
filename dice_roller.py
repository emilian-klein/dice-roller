import random
import os
import tkinter as tk
from PIL import Image, ImageTk


class DiceRoller(tk.Tk):
    """
    Application main class.
    """
    dice_images = ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png"]
    images_path = "images"

    def __init__(self):
        """
        Initializes the DiceRoller GUI application.
        Sets up the application window size, font styles and places widgets like labels and buttons.
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
        self.dice_image1.pack(side="left")

        self.dice_image2 = tk.Label(self.top_frame)
        self.dice_image2.pack(side="left")

        self.middle_frame = tk.Frame(self)
        self.middle_frame.pack()

        self.total_value_label = tk.Label(self.middle_frame, fg="#2883A6", font=self.lg_font_style)
        self.total_value_label.pack()

        self.bottom_frame = tk.Frame(self)
        self.bottom_frame.pack(pady=10)

        self.roll_button = tk.Button(self.bottom_frame, text="Roll dices", fg="#FFFFFF", bg="#2883A6", relief="groove", command=self.roll_dices,
                                     font=self.sm_font_style, width=10, cursor="hand2")
        self.roll_button.pack(side="left", padx=10)

        self.exit_button = tk.Button(self.bottom_frame, text="Exit", fg="#FFFFFF", bg="#7A7A7A", relief="groove", command=self.quit, font=self.sm_font_style,
                                     width=10, cursor="hand2")
        self.exit_button.pack(side="left")

    def roll_dices(self):
        """
        Simulates rolling two dice. Updates displayed dice images and calculates the total value of the dice rolls.
        """
        total_value = 0
        for dice_image_widget in [self.dice_image1, self.dice_image2]:
            dice_value = random.randint(1, 6)
            path_to_image = os.path.join(self.images_path, f"{dice_value}.png")
            dice_image = ImageTk.PhotoImage(Image.open(path_to_image))
            dice_image_widget.configure(image=dice_image)
            dice_image_widget.image = dice_image
            total_value += dice_value
        self.total_value_label.config(text=f"Total value: {total_value}")


if __name__ == "__main__":
    app = DiceRoller()
    app.roll_dices()
    app.mainloop()
