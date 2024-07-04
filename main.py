from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog
from PIL import Image, ImageTk


class WatermarkApp:

    def __init__(self, root):
        self.root = root
        self.COLOR_SET = ['#151515', '#A91D3A', '#C73659', '#EEEEEE']
        self.FONT_H1 = ("MS Reference Sans Serif", 20, "bold")
        self.main_image = None
        self.watermark = None
        self.setup_ui()

    def setup_ui(self):
        self.configure_root()
        self.create_frames()
        self.create_top_frame_content()
        self.create_central_frame_content()

    def configure_root(self):
        self.root.geometry('950x600')
        self.root.maxsize(950, 600)
        self.root.title("Watermark your Image")
        self.root.resizable(False, False)
        self.root.config(bg=self.COLOR_SET[2])

    def create_frames(self):
        self.top_frame = Frame(self.root, width=950, height=60, bg=self.COLOR_SET[1])
        self.top_frame.place(anchor="n", relx=.5, rely=.02)
        self.central_frame = Canvas(self.root, width=750, height=450, bg=self.COLOR_SET[0])
        self.central_frame.place(anchor="c", relx=.5, rely=.55)

    def create_top_frame_content(self):
        Label(self.top_frame, text="Welcome to Watermark App!", bg=self.COLOR_SET[1], font=self.FONT_H1).place(anchor="c", relx=.5, rely=.5)

    def create_central_frame_content(self):
        Button(self.central_frame, text="Select File", command=self.start_app).place(anchor="c", relx=.5, rely=.5)

    def start_app(self):
        self.openfile()
        self.change_topbar()

    def openfile(self):
        file = filedialog.askopenfilename(initialdir="C:", filetypes=[("Image file", (".png", ".jpg"))])
        if file:
            self.main_image = Image.open(file)
            self.display_image(self.main_image)
        else:
            self.handle_no_file_selected()

    def handle_no_file_selected(self):
        question = messagebox.askquestion("You did not choose file", "Do you want to try again?")
        if question == "yes":
            self.start_app()
        else:
            self.root.quit()

    def display_image(self, image):
        self.clear_frame(self.central_frame)
        img = self.resize_image(image, 750, 450)
        self.show_image(img, self.central_frame)

    def resize_image(self, image, max_width, max_height):        
        if image.width > max_width or image.height > max_height:
            return ImageTk.PhotoImage(image.resize((550, 450)))
        else:
            return ImageTk.PhotoImage(image.resize((int(image.width * 0.5), int(image.height * 0.5))))


    def show_image(self, img, frame):
        photo = Label(frame, image=img)
        photo.image = img
        photo.pack()

    def openwatermark(self):
        file = filedialog.askopenfilename(initialdir="C:", filetypes=[("Image file", (".png"))])
        if file:
            self.watermark = Image.open(file)
            self.apply_watermark()

    def apply_watermark(self):
        if self.main_image and self.watermark:
            watermark = self.watermark.resize((int(self.main_image.width * 0.25), int(self.main_image.height * 0.25)))
            self.main_image.paste(watermark, (0, 0), watermark)
            self.display_image(self.main_image)
            self.clear_frame(self.top_frame)
            self.create_export_button()


    def change_topbar(self):
        self.clear_frame(self.top_frame)
        self.create_watermark_button()

    def create_watermark_button(self):
        Button(self.top_frame, text="Choose watermark", command=self.openwatermark).place(anchor="c", relx=.5, rely=.5)
    
    def create_export_button(self):
        Button(self.top_frame, text="Export your image", command=self.export_image).place(anchor="c", relx=.5, rely=.5)

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def export_image(self):
        file_name = simpledialog.askstring("Name your file", "Enter your file name: ")
        self.main_image.save(file_name+".jpg")
        messagebox.showinfo("Saving Complete", "Your image was saved correctly")
        self.root.quit()

if __name__ == "__main__":
    root = Tk()
    app = WatermarkApp(root=root)
    root.mainloop()

