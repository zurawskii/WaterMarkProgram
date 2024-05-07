# avoid wildcard import
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image

# initialize global variables
file = file2 = None


def watermark():
    # check if two files are selected
    if file and file2:
        # make sure the loaded images support transparency
        logo_image = Image.open(file2).convert("RGBA")
        background_image = Image.open(file).convert("RGBA")

        logo_width, logo_height = logo_image.size
        background_width, background_height = background_image.size

        if logo_width > background_width or logo_height > background_height:
            # I am using thumbnail()to keep the image aspect ratio
            logo_image.thumbnail((background_width, background_height))

        logo_x = 0
        logo_y = 0

        background_image.paste(logo_image, (logo_x, logo_y), mask=logo_image)
        background_image.show()


def open_file():
    global file
    file = filedialog.askopenfilename(initialdir='Users/picture')


def open_filelogo():
    global file2
    file2 = filedialog.askopenfilename(initialdir='Users/picture')


window = tk.Tk()
window.title("Water Mark APP")
window.geometry('500x400')

label = ttk.Label(window, text="Select the image", font=("Arial", 25))
label.pack()

button1 = ttk.Button(window, text="Select Image", command=open_file)
button1.pack()

button2 = ttk.Button(window, text="Select Image Logo", command=open_filelogo)
button2.pack()

# I create the third button to display the watermark image
button3 = ttk.Button(window, text="Show Watermark Image", command=watermark)
button3.pack()

window.mainloop()
