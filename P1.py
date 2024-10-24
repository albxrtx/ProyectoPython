import tkinter as tk
from tkinter import ttk

def obtenerText():
     print(cuadro_texto_1.get())

ventana = tk.Tk()
ventana.config(width="900",height="500")

ventana.title("ToDo List")

ventana.iconbitmap("")
ventana.config(bg="lightgray")

cuadro_texto_1 = ttk.Entry(width=30)
cuadro_texto_1.place(x=100,y=100)
cuadro_texto_1.pack()
boton = ttk.Button(text="Añadir",command= obtenerText)
boton.pack()
# frame_1 = Frame()

# frame_1.pack(fill="both")
# frame_1.config(width="1500", height="800")

# Siempre al final
ventana.mainloop()