import tkinter as tk
import requests

# URL de la API de mockapi
url_api = "https://66ed811f380821644cdd146e.mockapi.io/IotCar"

# Función para enviar el estado a la API
def enviar_a_api(direccion):
    datos = {"direccion": direccion}
    try:
        response = requests.post(url_api, json=datos)
        if response.status_code == 201:
            mensaje = f"Dirección '{direccion}' enviada correctamente."
            print(mensaje)
            actualizar_salida(mensaje)
        else:
            mensaje = f"Error al enviar la dirección '{direccion}'. Estado: {response.status_code}"
            print(mensaje)
            actualizar_salida(mensaje)
    except requests.RequestException as e:
        mensaje = f"Error al conectar con la API: {e}"
        print(mensaje)
        actualizar_salida(mensaje)

# Función para actualizar la salida de mensajes
def actualizar_salida(mensaje):
    salida_texto.config(state=tk.NORMAL)  # Habilitar la modificación del widget de texto
    salida_texto.delete(1.0, tk.END)  # Limpiar el texto anterior
    salida_texto.insert(tk.END, mensaje)  # Insertar el nuevo mensaje
    salida_texto.config(state=tk.DISABLED)  # Deshabilitar la edición

# Función para manejar el envío desde la interfaz gráfica
def manejar_envio():
    direccion = entrada_direccion.get()
    enviar_a_api(direccion)

# Configurar la ventana principal
ventana = tk.Tk()
ventana.title("Enviar Estado a MockAPI")

# Entrada para la dirección
tk.Label(ventana, text="Dirección:").grid(row=0, column=0, padx=10, pady=10)
entrada_direccion = tk.Entry(ventana)
entrada_direccion.grid(row=0, column=1, padx=10, pady=10)

# Botón para enviar la dirección
boton_enviar = tk.Button(ventana, text="Enviar", command=manejar_envio)
boton_enviar.grid(row=1, column=0, columnspan=2, pady=10)

# Área de texto para mostrar el mensaje de salida
salida_texto = tk.Text(ventana, height=5, width=50, state=tk.DISABLED)
salida_texto.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Ejecutar la ventana
ventana.mainloop()
