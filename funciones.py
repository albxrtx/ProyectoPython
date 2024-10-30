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


def leer_tareas(contenedor):
    # Limpiar el contenedor de tareas antes de cargar nuevas tareas
    for widget in contenedor.winfo_children():
        widget.destroy()
    # Leer el CSV, asegurando que los encabezados están en la primera línea
    archivo = pd.read_csv("tareas.csv", header=0)
    contador = 0
    # Iteramos cada fila con el metodo iterrows de pandas y la imprimimos
    for index, fila in archivo.iterrows():
        contador += 1
        nombre = base64.b64decode(eval(fila["nombre"])).decode("utf-8")
        descripcion = base64.b64decode(eval(fila["descripcion"])).decode("utf-8")
        prioridad = base64.b64decode(eval(fila["prioridad"])).decode("utf-8")
        # Crear tarjeta de tarea con los datos descodificados
        crear_tarea_card(contenedor, nombre, descripcion, prioridad)
    return contador  

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

def formulario_delete():
    ventana_delete = tk.Tk()
    ventana_delete.geometry("300x200")
    ventana_delete.title("error")
    ventana_delete.iconbitmap("icono-todolist.ico")
    ventana_delete.resizable(0, 0)
    h1 = tk.Label(ventana_delete, text="Introduce el nombre de una tarea",font=("Helvetica", 12))
    h1.pack(pady=5)
    cuadro_texto = tk.Text(ventana_delete,width=30,background="lightgray",height=2)
    cuadro_texto.pack(pady=5)

    boton = tk.Button(
    ventana_delete,
    text="Eliminar",
    command=lambda : eliminar_tarea(cuadro_texto.get("1.0", tk.END)),
    activebackground="#ba1b1d",
    activeforeground="#cecece",
    background="#dd2527",
    border=0,
    padx=50,
    pady=5,
    foreground="#fefefe",
    font=("Helvetica", 15),
    )
    boton.pack(pady=10)

def eliminar_tarea(tarea):
    archivo = pd.read_csv("tareas.csv", header = 0)
    tarea = tarea.strip()
    for index, fila in archivo.iterrows():
        nombre_tarea = base64.b64decode(eval(fila["nombre"])).decode("utf-8")
        
    if tarea == "":
        error = "Introduce una tarea"
        crear_ventana_error(error)
    elif tarea != nombre_tarea:
        error = f"'{tarea}' no existe"
        crear_ventana_error(error)
    else:
        print(f"'{tarea}' ha sido eliminado")




def crear_tarea_card(contenedor, nombre, descripcion, prioridad):
    tarea_card = tk.Frame(contenedor, bg="lightgray", bd=1, relief="solid")
    tarea_card.pack(fill=tk.X, padx=10, pady=5)

    nombre_label = tk.Label(
        tarea_card, text=f"Tarea: {nombre}", font=("Helvetica", 12), bg="lightgray"
    )
    nombre_label.pack(anchor="w", padx=10, pady=5)

    descripcion_label = tk.Label(
        tarea_card,
        text=f"Descripción: {descripcion}",
        font=("Helvetica", 12),
        bg="lightgray",
    )
    descripcion_label.pack(anchor="w", padx=10, pady=5)

    prioridad_label = tk.Label(
        tarea_card,
        text=f"Prioridad: {prioridad}",
        font=("Helvetica", 12),
        bg="lightgray",
    )
    prioridad_label.pack(anchor="w", padx=10, pady=5)
