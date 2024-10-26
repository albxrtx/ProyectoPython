import tkinter as tk
import pandas as pd


def obtenerTarea(nombre_tarea, descripcion_tarea, prioridad_tarea):
    nombre_tarea = nombre_tarea.strip()
    descripcion_tarea = descripcion_tarea.strip()
    error = ""

    if nombre_tarea == "" or descripcion_tarea == "":
        error = "No puedo haber un cuadro vacio"
        crear_ventana_error(error)
    elif prioridad_tarea == "Prioridad":
        error = "Selecciona un prioridad"
        crear_ventana_error(error)
    else:
        introducir_nueva_tarea(nombre_tarea, descripcion_tarea, prioridad_tarea)


def crear_ventana_error(error):
    ventana_error = tk.Tk()
    ventana_error.geometry("300x100")
    ventana_error.title("error")
    ventana_error.iconbitmap("icono-todolist.ico")
    ventana_error.resizable(0, 0)

    mensaje_error = tk.Label(
        ventana_error,
        text=error,
        foreground="red",
        font=("Helvetica", 13),
    )
    mensaje_error.pack(pady=30)


def introducir_nueva_tarea(nombre, descripcion, prioridad):
    archivo_tareas = pd.read_csv("tareas.csv")
    nueva_fila = {"nombre": nombre, "descripcion": descripcion, "prioridad": prioridad}
    new_df = pd.DataFrame([nueva_fila])
    archivo_tareas = pd.concat([archivo_tareas, new_df])
    archivo_tareas.to_csv("tareas.csv", index=False)
    print("Tarea añadida correctamente")
