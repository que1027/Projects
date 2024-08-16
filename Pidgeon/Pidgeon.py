import tkinter as tk
from tkinter import filedialog
# Create the main window
root = tk.Tk()
root.title("Pidgeon")
root.geometry("500x400")  # Width x Height

# Header
header = tk.Label(root, text="Welcome to Pidgeon", font=("Arial", 24))
header.pack()  # Pack the header
def medias(media):
    if(media == 1):
        choice.delete("1.0", "end")
        choice.insert("1.0", "Facebook")
    elif(media == 2):
        choice.delete("1.0", "end")
        choice.insert("1.0", "Instagram")
    elif(media == 3):
        choice.delete("1.0", "end")     
        choice.insert("1.0", "snapchat")
    elif(media == 4):
        choice.delete("1.0", "end")
        choice.insert("1.0", "X")
    elif(media == 5):
        choice.delete("1.0", "end")
        choice.insert("1.0", "GMail")
    elif(media == 6):
        choice.delete("1.0", "end")
        choice.insert("1.0", "Outlook")
#Choose what service
fbButton = tk.Button(root, text="Facebook", command=lambda: medias(1) )
fbButton.pack()
igButton = tk.Button(root, text="Instagram", command=lambda: medias(2) )
igButton.pack()
scButton = tk.Button(root, text="snapchat", command=lambda: medias(3) )
scButton.pack()
xButton = tk.Button(root, text="X", command=lambda: medias(4) )
xButton.pack()
gmButton = tk.Button(root, text="GMail", command=lambda: medias(5) )
gmButton.pack()
olButton = tk.Button(root, text="Outlook", command=lambda: medias(6) )
olButton.pack()
choice = tk.Text(root, height=1,width=50);
choice.pack()  # Pack the choice
# Upload image 
uploadButton = tk.Button(root, text="Upload Image" , command=lambda:
                          tk.filedialog.askopenfiles(mode="r"));
uploadButton.pack() #pack the upload button

# Caption field
caption = tk.Text(root, height=5, width=50);
caption.pack()  # Pack the captions
#submit work
def submit():
    site = choice.get("1.0", "end")
    capText = caption.get("1.0", "end")

# Submit button
button = tk.Button(root, text="Submit", command=lambda:submit())
button.pack()  # Pack the button

# Run the application
root.mainloop()