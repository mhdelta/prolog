import tkinter as tk
from PIL import Image, ImageTk

class Root(tk.Tk):
    def __init__(self):
        super().__init__()

        photo = Image.open("ojo.jpg")
        photo = photo.resize((350, 100), Image.ANTIALIAS)
        photon = ImageTk.PhotoImage(photo)
        
        label = tk.Label(image=photon)
        label.image = photon # keep a reference!
        label.pack()
    

        b1 = tk.Button(self, text="Comenzar diagnostico", command=callback(), font = "Courier10Pitch")      #this font probably wont work, change it 
        b2 = tk.Button(self, text="Ver lista de enfermedades", command=callback(), font = "Courier10Pitch")
        b3 = tk.Button(self, text="Acerca de nosotros", command=callback(), font = "Courier10Pitch")
        b1.pack()
        b2.pack()
        b3.pack()

def callback():
    print("  ...")
if __name__ == "__main__":
    root = Root()
    w = 400 # width for the Tk root
    h = 200 # height for the Tk root

    # get screen width and height
    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    # set the dimensions of the screen 
    # and where it is placed
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.mainloop()