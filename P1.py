import tkinter as tk
from tkinter import ttk
import funciones as fn
from PIL import Image, ImageTk

# Creamos ventana principal
ventana = tk.Tk()
ventana.geometry("1500x700")
ventana.title("To Do List")
ventana.iconbitmap("icono-todolist.ico")  # Añadir icono .ico
ventana.config(bg="lightgray")
ventana.resizable(False, False)
# Creamos el sidebar, hacemos que ocupeto todo el alto y lo alineamos a la izquierda
sidebar = tk.Frame(ventana)
sidebar.pack(fill=tk.Y, side=tk.LEFT)
# Creamos un titulo
h1 = tk.Label(sidebar, text="TO DO LIST", font=("Helvetica", 30))
h1.pack(pady=50)
# Creamos label del nombre
nombre_tarea_label = tk.Label(
    sidebar, text="Nombre de la tarea", font=("Helvetica", 12)
)
nombre_tarea_label.pack()
# Creamos el cuadro de texto del nombre
cuadro_texto_1 = tk.Text(sidebar, width=30, background="lightgray", height=2)
cuadro_texto_1.pack(pady=10, padx=30)
# Creamos label de la descripcion
descripcion_tarea_label = tk.Label(
    sidebar, text="Descripcion de la tarea", font=("Helvetica", 12)
)
descripcion_tarea_label.pack()
# Creamos el cuadro de texto de la descripcion
cuadro_texto_2 = tk.Text(sidebar, width=30, background="lightgray", height=2)
cuadro_texto_2.pack(pady=10, padx=30)
#
prioridad = tk.StringVar(value="Prioridad")
menu_desplegable = ttk.OptionMenu(
    sidebar, prioridad, prioridad.get(), "Baja ", "Media", "Alta"
)
menu_desplegable.pack(pady=10)


# Creamos un boton para añadir tareas
boton = tk.Button(
    sidebar,
    text="AÑADIR",
    command=lambda: fn.obtenerTarea(
        cuadro_texto_1.get("1.0", tk.END),
        cuadro_texto_2.get("1.0", tk.END),
        prioridad.get(),
    ),
    activebackground="#237544",
    activeforeground="#cecece",
    background="#36b167",
    border=0,
    foreground="#fefefe",
    padx=50,
    pady=5,
    font=("Helvetica", 15),
)
boton.pack(pady=25)

imagen_original = Image.open("actualizar.png")
imagen = imagen_original.resize((50,50))
imagen_tk = ImageTk.PhotoImage(imagen)
boton_actualizar = ttk.Button(ventana, command=fn.leer_tareas,image=imagen_tk, width=20)
boton_actualizar.pack(side='left', anchor='nw', pady=10,padx=10)

tarea_card = fn.leer_tareas(ventana)


# Mantenemos la ventana en un bucle infinito hasta que el usuario cierra la ventana
ventana.mainloop()
