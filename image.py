import os
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox
from PIL import Image

def resize_image(file_path, width, height):
    try:
        with Image.open(file_path) as img:
            original_width, original_height = img.size
            aspect_ratio = original_width / original_height

            if aspect_ratio > 1:
                new_width = width
                new_height = int(width / aspect_ratio)
            else:
                new_height = height
                new_width = int(height * aspect_ratio)

            resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            save_path = file_path.replace(".", "_resized.")
            resized_img.save(save_path)
            messagebox.showinfo("Success", f"Image resized and saved as {save_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to resize image: {e}")

def select_file():
    file_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    return file_path

def start_resizing():
    file_path = select_file()
    if not file_path:
        messagebox.showwarning("Warning", "No file selected.")
        return

    try:
        width = int(entry_width.get())
        height = int(entry_height.get())
    except ValueError:
        messagebox.showerror("Error", "Width and Height must be integers.")
        return

    resize_image(file_path, width, height)

# Create the Tkinter window
root = Tk()
root.title("Image Resizer")

# Width Label and Entry
Label(root, text="Width:").grid(row=0, column=0, padx=10, pady=10)
entry_width = Entry(root)
entry_width.grid(row=0, column=1, padx=10, pady=10)

# Height Label and Entry
Label(root, text="Height:").grid(row=1, column=0, padx=10, pady=10)
entry_height = Entry(root)
entry_height.grid(row=1, column=1, padx=10, pady=10)

# Resize Button
Button(root, text="Resize Image", command=start_resizing).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()
