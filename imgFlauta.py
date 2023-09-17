import tkinter as tk

def img_flauta():
    ventana.quit()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Visor de Imagen")

# Cargar la imagen 
imagen = tk.PhotoImage(file="flauta.png")  

# Crear un widget Label para mostrar la imagen
label_imagen = tk.Label(ventana, image=imagen)
label_imagen.pack()

# Crear un botón para salir
boton_salir = tk.Button(ventana, text="Salir", command=img_flauta)
boton_salir.pack()

ventana.mainloop()

