import tkinter as tk
import pandas as pd
import base64


def obtenerTarea(nombre_tarea, descripcion_tarea, prioridad_tarea):
    nombre_tarea = nombre_tarea.strip()
    descripcion_tarea = descripcion_tarea.strip()

    if nombre_tarea == "" or descripcion_tarea == "":
        error = "Ambos campos deben estar completos"
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


def leer_tareas(ventana):
    #Declaramos el csv que vamos a leer
    archivo = pd.read_csv("tareas.csv")
    #Iteramos cada fila con el metodo iterrows de pandas y la imprimimos
    for index, fila in archivo.iterrows():
            crear_tarea_card(ventana)
            # print(fila)

def introducir_nueva_tarea(nombre, descripcion, prioridad):
    # Codificamos los datos en base64/utf-8
    nombre_codificado = encriptar_datos(nombre)
    descripcion_codificado = encriptar_datos(descripcion)
    prioridad_codificado = encriptar_datos(prioridad)
    # Decodificamos los datos
    # prioridad_decodificado = base64.b64decode(prioridad_codificado).decode('utf-8')

    # Leemos el csv
    archivo_tareas = pd.read_csv("tareas.csv")
    # Creamos una nueva fila con los datos introducidos por el usuario
    nueva_fila = {
        "nombre": nombre_codificado,
        "descripcion": descripcion_codificado,
        "prioridad": prioridad_codificado,
    }
    # Creamos un DataFrame con la nueva fila
    new_df = pd.DataFrame([nueva_fila])
    # Añadimos el DataFrame al csv
    archivo_tareas = pd.concat([archivo_tareas, new_df])
    archivo_tareas.to_csv("tareas.csv", index=False)
    # Mensaje de confirmación
    print("Tarea añadida correctamente")


def encriptar_datos(dato):
    return base64.b64encode(bytes(dato, "utf-8"))
    # return dato

def crear_tarea_card(ventana):
    tarea_card = tk.Frame(ventana)
    nombre_label = tk.Label(tarea_card, text="Tarea", font=("Helvetica", 12))
    nombre_label.pack(pady=10)
    descripcion_label = tk.Label(tarea_card, text="Descripcion", font=("Helvetica", 12))
    descripcion_label.pack(pady=10)
    prioridad_label = tk.Label(tarea_card, text="Prioridad", font=("Helvetica", 12))
    prioridad_label.pack(pady=10)
    return tarea_card
