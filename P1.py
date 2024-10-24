import tkinter as tk
from tkinter import ttk
import funciones as fn

#Creamos ventana principal
ventana = tk.Tk()
ventana.geometry("1500x700")
ventana.title("ToDo List")
ventana.iconbitmap("") #Añadir icono .ico
ventana.config(bg="lightgray")
ventana.resizable(False,False)
#Creamos el sidebar, hacemos que ocupeto todo el alto y lo alineamos a la izquierda
sidebar = ttk.Frame(ventana)
sidebar.pack(fill=tk.Y, side=tk.LEFT)
#Creamos un titulo 
h1 = tk.Label(sidebar,text="To Do List",font=("Helvetica", 30))
h1.pack(pady=50)
#Creamos label del nombre
nombre_tarea_label = tk.Label(sidebar,text="Nombre de la tarea",font=("Helvetica", 12))
nombre_tarea_label.pack()
#Creamos el cuadro de texto del nombre
cuadro_texto_1 = tk.Text(sidebar,width=30, height=2)
cuadro_texto_1.pack(pady=10, padx=30)
#Creamos label de la descripcion
descripcion_tarea_label = tk.Label(sidebar,text="Descripcion de la tarea",font=("Helvetica", 12))
descripcion_tarea_label.pack()
#Creamos el cuadro de texto de la descripcion
cuadro_texto_2 = tk.Text(sidebar,width=30, height=2)
cuadro_texto_2.pack(pady=10, padx=30)
#Creamos un boton para añadir tareas
msg1 = cuadro_texto_1.get('1.0', tk.END)
msg2 = cuadro_texto_2.get('1.0', tk.END)
boton = tk.Button(sidebar,text="Añadir",command=lambda: fn.obtenerTarea(msg1,msg2),activebackground="#237544",activeforeground="#cecece", background="#36b167",border= 0,foreground="#fefefe",padx = 50,pady = 5,font=("Helvetica", 15))
boton.pack(pady=25)

copy = tk.Label(sidebar,text= "©albxrtx Todos los derechos reservados")
copy.pack(pady=10,side=tk.BOTTOM)

# Mantenemos la ventana en un bucle infinito hasta que el usuario cierra la ventana
ventana.mainloop()