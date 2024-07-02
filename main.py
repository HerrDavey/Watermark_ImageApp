from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk

# Assets
COLOR_SET = ['#5A639C', '#7776B3', '#9B86BD', '#E2BBE9']
FONT_H1 = ("Comic Sans MS", 20, "bold")

# Set window
root = Tk()
root.geometry('900x600')
root.maxsize(900, 600)
root.title("Watermark your Image")
root.resizable(False, False)
root.config(bg=COLOR_SET[2])


def OpenFile():
    try:
        #file = filedialog.askopenfilename(initialdir="C:", filetypes=[("Image file", (".png", ".jpg"))])
        #if file:
        img = ImageTk.PhotoImage(Image.open(file).resize((750,450)))
        photo = Label(central_frame, image=img)
        photo.pack()

    except FileNotFoundError:
        messagebox.showerror("Unfound file", "The selected file was not found.")


# Frames
top_frame = Frame(root, width=750, height=100, bg=COLOR_SET[1])
top_frame.place(anchor="n", relx=.5, rely=.02)
central_frame = Frame(root, width=750, height=450, bg=COLOR_SET[0])
central_frame.place(anchor="c", relx=.5, rely=.6)

# Components 
Label(top_frame, text="Welcome to Watermark App!", bg=COLOR_SET[1], font=FONT_H1).place(anchor="c", relx=.5, rely=.5)
Button(central_frame, text="Select File", command=OpenFile).place(anchor="c", relx=.5, rely=.5)

# Turn on the loop
root.mainloop()


 