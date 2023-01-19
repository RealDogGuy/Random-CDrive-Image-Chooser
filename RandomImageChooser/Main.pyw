import tkinter as tk
from PIL import Image, ImageTk
import random
import os

def choose_random_picture():
    picture_files = []
    for folder in ["C:\\Users\\" + os.getlogin() + "\\Desktop", "C:\\Users\\" + os.getlogin() + "\\Documents", "C:\\Users\\" + os.getlogin() + "\\Pictures", "C:\\Users\\" + os.getlogin() + "\\Downloads"]:
        for root, dirs, files in os.walk(folder):
            if "appdata" in dirs:
                dirs.remove("appdata")  # don't visit appdata directory
            if "minecraft" in dirs:
                dirs.remove("minecraft")
            for file in files:
                if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".gif"):
                    picture_files.append(os.path.join(root, file))
    if picture_files:
        random_picture = random.choice(picture_files)
        path_var.set(random_picture)
        # Open the picture file using PIL's Image module
        image = Image.open(random_picture)
        # Create a PhotoImage object to display in the GUI
        photo = ImageTk.PhotoImage(image)
        # Display the picture in the label
        label.config(image=photo)
        label.image = photo
    else:
        label.config(text = "No Images found")

# Create the GUI window
root = tk.Tk()
root.title("Time Machine")
script_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(script_dir, "icon.ico")
root.wm_iconbitmap(icon_path)

# Create the label to display the picture
label = tk.Label(root)
label.pack()

# Create the button
button = tk.Button(root, text="test your luck", command=choose_random_picture)
button.pack()

# Create the label to display the path
path_var = tk.StringVar()
path_label = tk.Label(root, textvariable=path_var)
path_label.pack()

# Run the GUI
root.mainloop()
