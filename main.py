from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk


class WatermarkApp:

    def __init__(self, root):
        self.root = root
        self.COLOR_SET = ['#5A639C', '#7776B3', '#9B86BD', '#E2BBE9']
        self.FONT_H1 = ("Comic Sans MS", 20, "bold")
        self.setup_ui()

    def setup_ui(self):
        self.root.geometry('900x600')
        self.root.maxsize(900, 600)
        self.root.title("Watermark your Image")
        self.root.resizable(False, False)
        self.root.config(bg=self.COLOR_SET[2])

        self.top_frame = Frame(self.root, width=750, height=100, bg=self.COLOR_SET[1])
        self.top_frame.place(anchor="n", relx=.5, rely=.02)
        self.central_frame = Frame(self.root, width=750, height=450, bg=self.COLOR_SET[0])
        self.central_frame.place(anchor="c", relx=.5, rely=.6)

        Label(self.top_frame, text="Welcome to Watermark App!", bg=self.COLOR_SET[1], font=self.FONT_H1).place(anchor="c", relx=.5, rely=.5)
        Button(self.central_frame, text="Select File", command=self.OpenFile).place(anchor="c", relx=.5, rely=.5)


    def OpenFile(self):
        try:
            file = filedialog.askopenfilename(initialdir="C:", filetypes=[("Image file", (".png", ".jpg"))])
            if file:
                
                for widget in self.central_frame.winfo_children():
                    widget.destroy()
                
                img = ImageTk.PhotoImage(Image.open(file).resize((750,450)))
                photo = Label(self.central_frame, image=img)
                photo.image=img
                photo.pack() 

        except FileNotFoundError:
            messagebox.showerror("Unfound file", "The selected file was not found.")

        except Exception as e:
            messagebox.showerror("Something goes wrong", str(e))


if __name__ == "__main__":
    root=Tk()
    app=WatermarkApp(root=root)
    root.mainloop()


 