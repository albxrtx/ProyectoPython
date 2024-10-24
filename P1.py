import tkinter as tk
from tkinter import ttk

def imprimirDatos():
    print(f"Titulo: {cuadro_texto_1.get('1.0', tk.END).strip()}\nDescripcion: {cuadro_texto_2.get('1.0', tk.END).strip()}")

ventana = tk.Tk()

ventana.title("ToDo List")

ventana.iconbitmap("")
ventana.config(bg="lightgray")
frame1 = ttk.Frame(width= 500,height=200)
frame1.config()
frame1.pack()

cuadro_texto_1 = tk.Text(frame1,width=30, height=2)
cuadro_texto_1.pack(pady=10)

cuadro_texto_2 = tk.Text(frame1,width=30, height=2)
cuadro_texto_2.pack(pady=10)


boton = tk.Button(frame1,text="Añadir",background="#36b167",foreground="#fefefe",padx = 30,pady = 10,font= 20,command= imprimirDatos)
boton.pack()


# Siempre al final
ventana.mainloop()