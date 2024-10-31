import tkinter as tk
import pandas as pd
import base64


def añadir_tarea(contenedor, nombre_tarea, descripcion_tarea, prioridad_tarea):
    nombre_tarea = nombre_tarea.strip()
    descripcion_tarea = descripcion_tarea.strip()
    contador_tareas = leer_tareas(contenedor)
    if contador_tareas == 5:
        error_texto = "Máximo de tareas 5, elimina alguna tarea"
        crear_ventana_error(error_texto)
        return

    # Comprobamos que los cuadros de texto no están vacíos
    if nombre_tarea == "" or descripcion_tarea == "":
        # Declaramos el error y llamamos a la función de crear una ventana de error con ese mensaje
        error_texto = "Ambos campos deben estar completos"
        crear_ventana_error(error_texto)
    elif prioridad_tarea == "Prioridad":
        error_texto = "Selecciona un prioridad"
        crear_ventana_error(error_texto)
    else:
        # Si todo está correcto introducimos la nueva tarea y actualizamos el contenedor de tareas
        introducir_nueva_tarea(nombre_tarea, descripcion_tarea, prioridad_tarea)
        leer_tareas(contenedor)


def leer_tareas(contenedor):
    # Limpiar el contenedor de tareas para evitar duplicar las tareas
    for widget in contenedor.winfo_children():
        widget.destroy()
    # Leemos el csv ignorando la primera línea
    archivo = pd.read_csv("tareas.csv", header=0)
    contador_tareas = 0
    # Recorremos cada fila del csv
    for index, fila in archivo.iterrows():
        # Decodificamos cada dato
        contador_tareas += 1
        nombre = base64.b64decode(eval(fila["nombre"])).decode("utf-8")
        descripcion = base64.b64decode(eval(fila["descripcion"])).decode("utf-8")
        prioridad = base64.b64decode(eval(fila["prioridad"])).decode("utf-8")
        # LLamamos al método y le pasamos los datos descodificados
        crear_tarea_card(contenedor, nombre, descripcion, prioridad)
    return contador_tareas


def introducir_nueva_tarea(nombre, descripcion, prioridad):
    # Codificamos los datos en base64/utf-8
    nombre_codificado = encriptar_datos(nombre)
    descripcion_codificado = encriptar_datos(descripcion)
    prioridad_codificado = encriptar_datos(prioridad)

    # Leemos el csv
    archivo_tareas = pd.read_csv("tareas.csv")
    # Creamos una nueva fila con los datos (ya codificados) que el usuario haya introducido
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


# Creamos un nuevo cuadro con la tarea
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


# Creamos una venta para advertir del error que haya cometido el usuario
def crear_ventana_error(error_texto):
    ventana_error = tk.Tk()
    ventana_error.geometry("300x100")
    ventana_error.title("error")
    ventana_error.iconbitmap("icono-todolist.ico")
    ventana_error.resizable(0, 0)

    mensaje_error = tk.Label(
        ventana_error,
        text=error_texto,
        foreground="red",
        font=("Helvetica", 13),
    )
    mensaje_error.pack(pady=30)


# Codificamos el dato en base644/utf-8
def encriptar_datos(dato):
    return base64.b64encode(bytes(dato, "utf-8"))


# Creamos una ventana en la que el usuario podrá introducir la tarea a eliminar
def formulario_delete():
    ventana_delete = tk.Tk()
    ventana_delete.geometry("300x200")
    ventana_delete.title("error")
    ventana_delete.iconbitmap("icono-todolist.ico")
    ventana_delete.resizable(0, 0)
    h1 = tk.Label(
        ventana_delete, text="Introduce el nombre de una tarea", font=("Helvetica", 12)
    )
    h1.pack(pady=5)
    cuadro_texto = tk.Text(ventana_delete, width=30, background="lightgray", height=2)
    cuadro_texto.pack(pady=5)

    boton = tk.Button(
        ventana_delete,
        text="Eliminar",
        command=lambda: eliminar_tarea(ventana_delete, cuadro_texto.get("1.0", tk.END)),
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


# Eliminamos la tarea que el usuario haya introducido
def eliminar_tarea(contenedor, tarea_input):
    # Indicamos que csv tiene que leer
    archivo = pd.read_csv("tareas.csv", header=0)
    tarea_input = tarea_input.strip()
    # Creamos una variable para comprobar que la tarea exista en el csv
    tarea_encontrada = False

    if tarea_input == "":
        error_texto = "El cuadro no pueda estar vacío"
        crear_ventana_error(error_texto)
        return
    # Recorremos todas las filass del csv
    for index, fila in archivo.iterrows():
        nombre_tarea = base64.b64decode(eval(fila["nombre"])).decode("utf-8")
        # Si el nombre introducido por el usuario es igual a algún valor del csv se elimina
        if nombre_tarea == tarea_input:
            archivo = archivo.drop(index)
            archivo.to_csv("tareas.csv", index=False)
            # Hemos encontrado la tarea
            tarea_encontrada = True
            # Cerramos el formulario de borrar tareas
            contenedor.destroy()
            break
    # Si la tarea introducida por el usuario no se encuentra en el csv
    # mandamos una ventana de error
    if not tarea_encontrada:
        error_texto = f"''{tarea_input}'' no existe"
        crear_ventana_error(error_texto)
