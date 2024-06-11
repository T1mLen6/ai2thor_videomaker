import tkinter as tk
from tkinter import filedialog, simpledialog
from PIL import Image, ImageTk, ImageDraw, ImageFont
import os
import re

class ImageEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Editor")
        self.root.geometry("800x800")

        self.image_label = tk.Label(root)
        self.image_label.pack()

        self.load_folder_button = tk.Button(root, text="Load Folder", command=self.load_folder)
        self.load_folder_button.pack()

        self.text_entry = tk.Entry(root, width=50)
        self.text_entry.pack()

        self.add_text_button = tk.Button(root, text="Add Text", command=self.add_text)
        self.add_text_button.pack()

        self.save_button = tk.Button(root, text="Save Image", command=self.save_image)
        self.save_button.pack()

        self.next_image_button = tk.Button(root, text="Next Image", command=self.next_image)
        self.next_image_button.pack()


        self.folder_path = None
        self.image_files = []
        self.current_image_index = 0
        self.image = None
        self.tk_image = None

    def load_folder(self):
        self.folder_path = filedialog.askdirectory()
        if not self.folder_path:
            return
        # Get all image files and sort them
        self.image_files = sorted(
            [f for f in os.listdir(self.folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif'))],
            key=lambda x: int(re.search(r'\d+', x).group())
        )
        self.current_image_index = 0
        self.load_image()

    def load_image(self):
        if not self.image_files:
            return
        self.image_path = os.path.join(self.folder_path, self.image_files[self.current_image_index])
        self.image = Image.open(self.image_path)
        self.resize_image()
        self.display_image()

    def resize_image(self):
        max_size = (800, 600)
        self.image.thumbnail(max_size, Image.LANCZOS)

    def display_image(self):
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.image_label.config(image=self.tk_image)

    def add_text(self):
        text = self.text_entry.get()
        if self.image and text:
            draw = ImageDraw.Draw(self.image)
            font_size = 25
            font_color = (0, 255, 0)
            text_position = (10, 10)  # Top left corner

            font = ImageFont.truetype("DejaVuSans-Bold.ttf", font_size)


            draw.text(text_position, text, font=font, fill=font_color)
            self.display_image()

    def save_image(self):
        if self.image:
            save_path = os.path.join(self.folder_path, f"modified_{self.image_files[self.current_image_index]}")
            self.image.save(save_path)

    def next_image(self):
        if self.image_files:
            self.current_image_index = (self.current_image_index + 1) % len(self.image_files)
            self.load_image()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditorApp(root)
    root.mainloop()

