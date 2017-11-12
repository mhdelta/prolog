
import tkinter as tk
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
# import time
# import subprocess



# #//////////////////////////             GUI             //////////////////////////

def callback():
    print("  ...")

def read_str(word):
    print(word)

def regresar(frame):
    frame.destroy()
    root.deiconify()

def acerca_de_nosotros():
    root.withdraw()
    ventana = tk.Tk()
    w = 400 # width for the Tk root
    h = 200 # height for the Tk root

    # get screen width and height
    ws = ventana.winfo_screenwidth() # width of the screen
    hs = ventana.winfo_screenheight() # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    # set the dimensions of the screen 
    # and where it is placed

    mensaje = tk.Message(ventana, text="Integrantes del grupo:\nMiguel Henao\nJuliana Pineda\nCristian Andres Arce", font = "Courier10Pitch")
    mensaje.pack()
    b1 = tk.Button(ventana, text="REGRESAR", command =lambda:regresar(ventana) ,font = "Courier10Pitch")
    b1.pack()
    ventana.geometry('%dx%d+%d+%d' % (w, h, x, y))

def diagnostico():
    root.withdraw()
    diagnostico = tk.Tk()
    w = 400 # width for the Tk root
    h = 200 # height for the Tk root

    # get screen width and height
    ws = diagnostico.winfo_screenwidth() # width of the screen
    hs = diagnostico.winfo_screenheight() # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    # set the dimensions of the screen 
    # and where it is placed


#MENSAJE    
    var = tk.StringVar(diagnostico)                   #string var must have a master
    mensaje = tk.Label(diagnostico, textvariable=var, font = "Courier10Pitch")
    mensaje.pack()

    var.set("hola")


#ENTRADA DE TEXTO
    e = tk.Entry(diagnostico)
    e.pack()
#ACCIONAR CON ENTER    
    diagnostico.bind('<Return>', lambda x:read_str(e.get()))
#BOTON
    b1 = tk.Button(diagnostico, text="REGRESAR", command =lambda:regresar(diagnostico) ,font = "Courier10Pitch")
    b1.pack()
    
    diagnostico.geometry('%dx%d+%d+%d' % (w, h, x, y))

root = tk.Tk()

photo = Image.open("ojo.jpg")
photo = photo.resize((350, 100), Image.ANTIALIAS)
photon = ImageTk.PhotoImage(photo)
    
label = tk.Label(image=photon)
label.image = photon # keep a reference!
label.pack()

b1 = tk.Button( text="Iniciar diagnostico", command = diagnostico,font = "Courier10Pitch")       #this font probably wont work, change it 
b2 = tk.Button( text="Acerca de nosotros", command=acerca_de_nosotros, font = "Courier10Pitch")

b1.pack()
b2.pack()

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
#============================================================================================================================================
# root = tk.Tk()

# photo = Image.open("ojo.jpg")
# photo = photo.resize((350, 100), Image.ANTIALIAS)
# photon = ImageTk.PhotoImage(photo)
    
# label = tk.Label(image=photon)
# label.image = photon # keep a reference!
# label.pack()

# b1 = tk.Button( text="Iniciar diagnostico", command = diagnostico,font = "Courier10Pitch")       #this font probably wont work, change it 
# b2 = tk.Button( text="Acerca de nosotros", command=acerca_de_nosotros, font = "Courier10Pitch")

# b1.pack()
# b2.pack()

# w = 400 # width for the Tk root
# h = 200 # height for the Tk root

# # get screen width and height
# ws = root.winfo_screenwidth() # width of the screen
# hs = root.winfo_screenheight() # height of the screen

# # calculate x and y coordinates for the Tk root window
# x = (ws/2) - (w/2)
# y = (hs/2) - (h/2)

# # set the dimensions of the screen 
# # and where it is placed
# root.geometry('%dx%d+%d+%d' % (w, h, x, y))
#///////////////////////////////////////////////////////////////////////////////////
# root = tk.Tk() 

# e = tk.Entry(root)
# e.grid()

# b = tk.Button(root,text='QUIT',command=root.quit)
# b.grid()

# def entryreturn(event):
#     proc.stdin.write(bytes((e.get()+'\n'), 'utf-8')) # the '\n' is important to flush stdin
#     e.delete(0,tk.END)


# when you press Return in Entry, use this as stdin 
# and remove it
# e.bind("<Return>", entryreturn)
# e.focus()
# proc = subprocess.Popen('./test.py', stdin=subprocess.PIPE)



# root.mainloop()
#///////////////////////////////////////////////////////////////////////////////////

#!/usr/bin/env python
"""
- read subprocess output without threads using Tkinter
- show the output in the GUI
- stop subprocess on a button press
"""
# import logging
# import os
# import sys
# from subprocess import Popen, PIPE, STDOUT

# try:
#     import Tkinter as tk
# except ImportError: # Python 3
#     import tkinter as tk

# info = logging.getLogger(__name__).info

# # define dummy subprocess to generate some output
# cmd = [sys.executable or "python3", "-u", "-c", """
# import proyecto_progra
# print("hello")
# """]

# class ShowProcessOutputDemo:
#     def __init__(self, root):
#         """Start subprocess, make GUI widgets."""
#         self.root = root

#         # start subprocess
#         self.proc = Popen(cmd, stdout=PIPE, stderr=STDOUT)

#         # show subprocess' stdout in GUI
#         self.root.createfilehandler(
#             self.proc.stdout, tk.READABLE, self.read_output)
#         self._var = tk.StringVar() # put subprocess output here
#         tk.Label(root, textvariable=self._var).pack()

#         # stop subprocess using a button
#         tk.Button(root, text="Stop subprocess", command=self.stop).pack()

#     def read_output(self, pipe, mask):
#         """Read subprocess' output, pass it to the GUI."""
#         data = os.read(pipe.fileno(), 1 << 20)
#         if not data:  # clean up
#             info("eof")
#             self.root.deletefilehandler(self.proc.stdout)
#             self.root.after(5000, self.stop) # stop in 5 seconds
#             return
#         info("got: %r", data)
#         self._var.set(data.strip(b'\n').decode())

#     def stop(self, stopping=[]):
#         """Stop subprocess and quit GUI."""
#         if stopping:
#             return # avoid killing subprocess more than once
#         stopping.append(True)

#         info('stopping')
#         self.proc.terminate() # tell the subprocess to exit

#         # kill subprocess if it hasn't exited after a countdown
#         def kill_after(countdown):
#             if self.proc.poll() is None: # subprocess hasn't exited yet
#                 countdown -= 1
#                 if countdown < 0: # do kill
#                     info('killing')
#                     self.proc.kill() # more likely to kill on *nix
#                 else:
#                     self.root.after(1000, kill_after, countdown)
#                     return # continue countdown in a second

#             self.proc.stdout.close()  # close fd
#             self.proc.wait()          # wait for the subprocess' exit
#             self.root.destroy()       # exit GUI
#         kill_after(countdown=5)

# logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
# root = tk.Tk()
# app = ShowProcessOutputDemo(root)
# root.protocol("WM_DELETE_WINDOW", app.stop) # exit subprocess if GUI is closed
# root.mainloop()
# info('exited')
