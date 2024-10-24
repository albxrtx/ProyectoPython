import tkinter as tk
from tkinter import ttk

def imprimirDatos():
    print(f"Titulo: {cuadro_texto_1.get('1.0', tk.END).strip()}\nDescripcion: {cuadro_texto_2.get('1.0', tk.END).strip()}")

ventana = tk.Tk()
ventana.geometry("900x500")
ventana.title("ToDo List")
#Añadir icono .ico
ventana.iconbitmap("")
ventana.config(bg="lightgray")

frame1 = ttk.Frame(ventana)
frame1.pack(fill=tk.Y, side=tk.LEFT)

h1 = tk.Label(frame1,text="To Do List",font=("Helvetica", 30))
h1.pack(pady=50)

cuadro_texto_1 = tk.Text(frame1,width=30, height=2)
cuadro_texto_1.pack(pady=10, padx=30)

cuadro_texto_2 = tk.Text(frame1,width=30, height=2)
cuadro_texto_2.pack(pady=10, padx=30)


boton = tk.Button(frame1,text="Añadir",activebackground="#237544",activeforeground="#cecece", background="#36b167",border= 0,foreground="#fefefe",padx = 50,pady = 5,font=("Helvetica", 15),command= imprimirDatos)
boton.pack(pady=10)


# Siempre al final
ventana.mainloop()