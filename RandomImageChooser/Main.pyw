import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import random
import os

# New Image on button Press

def choose_random_picture():
    picture_files = []
    # Get the home directory of the current user
    home = os.path.expanduser("~")
    # Add the directories to search for images
    if os.name == 'nt':
        username = os.getlogin() or os.getenv('USER')
        folders = ["C:\\Users\\" + username + "\\Desktop", "C:\\Users\\" + username + "\\Documents", "C:\\Users\\" + username + "\\Pictures", "C:\\Users\\" + username + "\\Downloads"]
    elif os.name == 'posix':
        folders = [os.path.join(home, "Desktop"), os.path.join(home, "Documents"), os.path.join(home, "Pictures"), os.path.join(home, "Downloads")]

    for folder in folders:
        if os.path.exists(folder):
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

# New Image on Space Pressed

def call_choose_random_picture(event=None):
    choose_random_picture()

# On P Open Path

def open_picture_path(event=None):
    path = path_var.get()
    folder_path = os.path.dirname(path)
    if os.name == 'nt':
        subprocess.Popen(f'explorer.exe /select,"{path}"')
    elif os.name == 'posix':
        subprocess.call(["open", "-R", folder_path,path])





# Create the GUI window
root = tk.Tk()
root.title("Time Machine (You can also press space to choose a new picture) (Press P to open the path of the image)")
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
root.bind("<space>", call_choose_random_picture)
root.bind("<p>", open_picture_path)
root.mainloop()
