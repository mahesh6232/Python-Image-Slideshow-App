import tkinter as tk
import time
from PIL import Image, ImageTk

# Main window
root = tk.Tk()
root.title("Photo Slideshow Album")
root.geometry("800x600")

# List of Image Paths
image_paths = [
    r"C:\Users\Asus\desktop\images\img1.jpg",
    r"C:\Users\Asus\desktop\images\img2.jpg",
    r"C:\Users\Asus\desktop\images\img3.jpg",
    r"C:\Users\Asus\desktop\images\img4.jpg",
    r"C:\Users\Asus\desktop\images\img5.jpg",
    r"C:\Users\Asus\desktop\images\img6.jpg",
    r"C:\Users\Asus\desktop\images\img7.jpg",
    r"C:\Users\Asus\desktop\images\img8.jpg",
]
images = []

for path in image_paths:
    img = Image.open(path)
    img = img.resize((700, 700))
    images.append(img)  # Adding each image in the List

# Convert PIL Images into Tkinter Compatible Image
final_images = []
for img in images:
    photo = ImageTk.PhotoImage(img)
    final_images.append(photo)

# Label widget to keep Photo
image_label = tk.Label(root)
image_label.pack(pady=30)


# Slideshow Function
def start_slideshow():
    for photo in final_images:
        image_label.config(image=photo)
        root.update()
        time.sleep(3)


# Button
play_button = tk.Button(
    root,
    text="Play the Slideshow",
    font=("math italic", 18),
    bg="green",
    borderwidth=2,
    command=start_slideshow,
)

play_button.pack(pady=40)

root.mainloop()
