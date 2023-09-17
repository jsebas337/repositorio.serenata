import tkinter as tk

def img_guitarra():
    ventana.quit()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Visor de Imagen")

# Cargar la imagen 
imagen = tk.PhotoImage(file="guitarra.png")  

# Crear un widget Label para mostrar la imagen
label_imagen = tk.Label(ventana, image=imagen)
label_imagen.pack()

# Crear un botón para salir
boton_salir = tk.Button(ventana, text="Salir", command=img_guitarra)
boton_salir.pack()

ventana.mainloop()

