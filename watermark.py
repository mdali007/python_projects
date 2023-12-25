import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont


class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Watermark App")

        self.image_path = tk.StringVar()

        # Create UI elements
        self.label = tk.Label(root, text="Select an image:")
        self.label.pack(pady=10)

        self.browse_button = tk.Button(root, text="Browse", command=self.browse_image)
        self.browse_button.pack(pady=10)

        self.image_label = tk.Label(root)
        self.image_label.pack(pady=10)

        self.watermark_button = tk.Button(root, text="Add Watermark", command=self.add_watermark)
        self.watermark_button.pack(pady=10)

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", (".png", ".jpg", ".jpeg"))])
        if file_path:
            self.image_path.set(file_path)
            self.display_image(file_path)

    def display_image(self, file_path):
        image = Image.open(file_path)
        image.thumbnail((300, 300))
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo

    def add_watermark(self):
        # Get the selected image path
        image_path = self.image_path.get()

        # Check if an image is selected
        if not image_path:
            tk.messagebox.showerror("Error", "Please select an image first.")
            return

        # Ask the user to select a watermark image
        watermark_path = filedialog.askopenfilename(filetypes=[("Image files", (".png", ".jpg", ".jpeg"))])

        # Check if a watermark image is selected
        if not watermark_path:
            tk.messagebox.showerror("Error", "Please select a watermark image.")
            return

        # Ask the user for the output path
        output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])

        # Check if an output path is selected
        if not output_path:
            tk.messagebox.showerror("Error", "Please select an output path.")
            return

        # Load the image and watermark
        original_image = Image.open(image_path)
        watermark = Image.open(watermark_path)

        # Resize watermark to fit the original image
        watermark.thumbnail(original_image.size)

        # Paste the watermark onto the original image
        original_image.paste(watermark, (0, 0), watermark)

        # Save the result
        original_image.save(output_path)

        tk.messagebox.showinfo("Success", "Watermark added successfully.")


if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()
