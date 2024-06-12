import random
import tkinter as tk
from PIL import Image, ImageTk
import os
from numpy import matrix
from cod import escribir_matriz_en_archivo, limpiar_archivos, generar_salida


equipos_famosos = ["Real Madrid", "Barcelona", "Manchester United", "Junior", 
                  "Juventus", "Paris Saint-Germain", "Liverpool", "Roma", 
                  "Nice", "Ajax", "Bayern Munich", "Arsenal"]

def ventanaSeleccionEquipos(cantidad):
    
    seleccionados = []

    def abrirVentanaMatriz(seleccionados):
        VentanaMatriz = tk.Toplevel()
        VentanaMatriz.title("Matriz de Equipos")
        VentanaMatriz.geometry("800x400")
        VentanaMatriz.configure(bg='#1E1E1E')
        matriz_frame = tk.Frame(VentanaMatriz, bg='#1E1E1E')
        matriz_frame.pack(pady=20)
        
        def cambiar_estado(boton):
            if boton.cget("text") == "0":
                boton.config(text="1", bg='#2C2C2C', fg='#6fff00')
            else:
                boton.config(text="0", bg='#2C2C2C', fg='red')
                
        iconos_path = "Iconos"
        
        for i, equipo in enumerate(seleccionados):
            icon_path = os.path.join(iconos_path, f"ico{equipos_famosos.index(equipo) + 1}.png")
            try:
                icon_image = Image.open(icon_path)
                icon_image = icon_image.resize((30, 30), Image.Resampling.LANCZOS)
                icon = ImageTk.PhotoImage(icon_image)
            except FileNotFoundError:
                print(f"Icono no encontrado: {icon_path}")
                icon = None
        # Crear encabezados en la columna izquierda, solo traer el icono
        for i, equipo in enumerate(seleccionados):
            icon_path = os.path.join(iconos_path, f"ico{equipos_famosos.index(equipo) + 1}.png")
            try:
                icon_image = Image.open(icon_path)
                icon_image = icon_image.resize((30, 30), Image.Resampling.LANCZOS)
                icon = ImageTk.PhotoImage(icon_image)
            except FileNotFoundError:
                print(f"Icono no encontrado: {icon_path}")
                icon = None

            label = tk.Label(matriz_frame, image=icon, bg='#1E1E1E')
            label.image = icon  # Necesario para mantener una referencia del objeto de imagen
            label.grid(row=i+1, column=0, padx=10, pady=5)
        

            boton = tk.Button(matriz_frame, text="", font=("Segoe UI", 12, "bold"), 
                             bg='#2C2C2C', fg='white', 
                             compound=tk.LEFT, image=icon, padx=10)
            boton.image = icon
            boton.grid(row=0, column=i+1, padx=10, pady=5)
        
            
        # Crear matriz de botones
        for i, equipo1 in enumerate(seleccionados):
            for j, equipo2 in enumerate(seleccionados):
                boton = tk.Button(matriz_frame, text="0", font=("Segoe UI", 14, "bold"),
                                bg='#2C2C2C', fg='red', padx=10, pady=5)
                boton.grid(row=i+1, column=j+1, padx=10, pady=5)  # Comenzar desde la segunda fila y columna
                boton.config(command=lambda b=boton: cambiar_estado(b))
     
       #Guardar Matriz para ingresarlo a txt entrada
        def guardar_matriz():
            matriz = []
            for i in range(len(seleccionados)):
                fila = []
                for j in range(len(seleccionados)):
                    boton = matriz_frame.grid_slaves(row=i+1, column=j+1)[0]
                    fila.append(int(boton.cget("text")))
                matriz.append(fila)
            print(matriz)
            
            escribir_matriz_en_archivo("entrada.txt", matriz)
            VentanaMatriz.destroy()
       
 
            
        BotonPlay = tk.Button(VentanaMatriz, text="Guardar", font=("Segoe UI", 12, "bold"),
                      bg='#FF9900', fg='white', padx=10, pady=5, command=guardar_matriz)
        BotonPlay.place(x=100, y=150)

 



        VentanaMatriz.update_idletasks()
        width = VentanaMatriz.winfo_width()
        height = VentanaMatriz.winfo_height()
        x = (VentanaMatriz.winfo_screenwidth() // 2) - (width // 2)
        y = (VentanaMatriz.winfo_screenheight() // 2) - (height // 2)
        VentanaMatriz.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    VentanaEquipos = tk.Toplevel()
    VentanaEquipos.title("Seleccionar Equipos")
    VentanaEquipos.geometry("800x400")
    VentanaEquipos.configure(bg='#1E1E1E')

    content_frame = tk.Frame(VentanaEquipos, bg='#1E1E1E')
    content_frame.pack(pady=20)

    titulo = tk.Label(content_frame, text="Selecciona tus equipos", font=("Segoe UI", 18, "bold"), bg='#1E1E1E', fg='white')
    titulo.pack(pady=10)

    selecciones_restantes = tk.Label(content_frame, text=f"Selecciones restantes: {cantidad}", font=("Segoe UI", 14), bg='#1E1E1E', fg='#FF9900')
    selecciones_restantes.pack()

    def seleccionar_equipo(equipo):
        nonlocal cantidad
        if cantidad > 0:
            seleccionados.append(equipo)
            print(f"Equipo seleccionado: {equipo}")
            cantidad -= 1
            selecciones_restantes.config(text=f"Selecciones restantes: {cantidad}")
            if cantidad == 0:
                VentanaEquipos.destroy()
                abrirVentanaMatriz(seleccionados)

    equipos_frame = tk.Frame(content_frame, bg='#1E1E1E')
    equipos_frame.pack(pady=20)

    iconos_path = "Iconos"

    for i, equipo in enumerate(equipos_famosos):
        icon_path = os.path.join(iconos_path, f"ico{i+1}.png")
        try:
            icon_image = Image.open(icon_path)
            icon_image = icon_image.resize((30, 30), Image.Resampling.LANCZOS)
            icon = ImageTk.PhotoImage(icon_image)
        except FileNotFoundError:
            print(f"Icono no encontrado: {icon_path}")
            icon = None

        boton = tk.Button(equipos_frame, text=equipo, font=("Segoe UI", 12, "bold"), 
                         bg='#2C2C2C', fg='white', 
                         command=lambda e=equipo: seleccionar_equipo(e),
                         compound=tk.LEFT, image=icon, padx=10)
        boton.image = icon
        boton.grid(row=i//3, column=i%3, padx=10, pady=10)

    for i in range(3):
        equipos_frame.grid_columnconfigure(i, weight=1)

    for widget in equipos_frame.winfo_children():
        widget.grid_configure(sticky='n')

    VentanaEquipos.update_idletasks()
    width = VentanaEquipos.winfo_width()
    height = VentanaEquipos.winfo_height()
    x = (VentanaEquipos.winfo_screenwidth() // 2) - (width // 2)
    y = (VentanaEquipos.winfo_screenheight() // 2) - (height // 2)
    VentanaEquipos.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def mover_balones(canvas, balones, canvas_width, canvas_height):
    for balon in balones:
        canvas.move(balon['id'], balon['dx'], balon['dy'])
        x, y = canvas.coords(balon['id'])
        if x <= 0 or x >= canvas_width:
            balon['dx'] *= -1
        if y <= 0 or y >= canvas_height:
            balon['dy'] *= -1
    canvas.after(30, mover_balones, canvas, balones, canvas_width, canvas_height)

    
def ventanaIngreso():
    VentanaSelecciones = tk.Toplevel()
    VentanaSelecciones.title("Ingreso Selecciones")
    VentanaSelecciones.geometry("400x300")
    VentanaSelecciones.configure(bg='#1E1E1E')



    # Crear un canvas para los balones animados
    canvas = tk.Canvas(VentanaSelecciones, width=400, height=300, bg='#1E1E1E')
    canvas.pack(fill="both", expand=True)
    
    
    titulo = tk.Label(canvas, text="Cantidad de Selecciones", font=("Segoe UI", 18, "bold"), bg='#1E1E1E', fg='white')
    titulo.pack(pady=10)
    
    entrada = tk.Entry(canvas, font=("Segoe UI", 12), justify='center', bg='#2C2C2C', fg='white')
    entrada.insert(0, "Ingresa la cantidad")
    entrada.pack()

    def clear_text(event):
        entrada.delete(0, tk.END)

    entrada.bind("<Button-1>", clear_text)

    def get_text_and_open_equipos():
        cantidad = int(entrada.get())
        VentanaSelecciones.destroy()
        ventanaSeleccionEquipos(cantidad)

    botonGuardar = tk.Button(canvas, text="Guardar", font=("Segoe UI", 12, "bold"), 
                            bg='#FF9900', fg='white', padx=20, pady=10, 
                            command=get_text_and_open_equipos)
    botonGuardar.pack(pady=20)
    VentanaSelecciones.update_idletasks()

    width = VentanaSelecciones.winfo_width()
    height = VentanaSelecciones.winfo_height()
    x = (VentanaSelecciones.winfo_screenwidth() // 2) - (width // 2)
    y = (VentanaSelecciones.winfo_screenheight() // 2) - (height // 2)
    VentanaSelecciones.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    
    
def mostrar_salida():
    
    ventana_salida = tk.Toplevel()
    ventana_salida.title("Villas Creadas")
    ventana_salida.geometry("600x400")
    ventana_salida.configure(bg='#1E1E1E')

    scrollbar = tk.Scrollbar(ventana_salida)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    text_area = tk.Text(ventana_salida, wrap=tk.WORD, yscrollcommand=scrollbar.set)
    text_area.pack(fill=tk.BOTH, expand=1)
    text_area.config(bg='#2C2C2C', fg='white', font=("Segoe UI", 12, "bold")) 
    
    generar_salida()
    
    with open("salida.txt", "r") as f:
        contenido = f.read()
        text_area.insert(tk.END, contenido)

    scrollbar.config(command=text_area.yview)
    
    ventana_salida.update_idletasks()
    width = ventana_salida.winfo_width()
    height = ventana_salida.winfo_height()
    x = (ventana_salida.winfo_screenwidth() // 2) - (width // 2)
    y = (ventana_salida.winfo_screenheight() // 2) - (height // 2)
    ventana_salida.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    


def VentanaPrincipal():
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    taskbar_height = 50
    window_width = screen_width
    window_height = screen_height - taskbar_height
    root.geometry(f'{window_width}x{window_height}+0+0')
    root.resizable(False, False)
    root.title("App ADA")
    icon_path = "Imagenes/icon.ico"
    root.iconbitmap(icon_path)
    
    # Cargar la imagen de la cancha
    image_path = "Imagenes/cancha.png"
    image = Image.open(image_path)
    image = image.resize((window_width, window_height), Image.Resampling.LANCZOS)
    bg_image = ImageTk.PhotoImage(image)

    # Crear un canvas para los balones animados
    canvas = tk.Canvas(root, width=window_width, height=window_height, bg='white', highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    # Colocar la imagen de la cancha como fondo del canvas
    canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)

    # Cargar la imagen del balón
    imagen_balon = Image.open("Imagenes/football.png")
    imagen_balon = imagen_balon.resize((80, 80), Image.ANTIALIAS)
    balon_tk = ImageTk.PhotoImage(imagen_balon)

    # Crear balones animados
    balones = []
    for _ in range(7):  # Crear 5 balones
        x = random.randint(0, window_width)
        y = random.randint(0, window_height)
        balon_id = canvas.create_image(x, y, image=balon_tk)
        balones.append({
            'id': balon_id,
            'dx': random.uniform(1, 3) * random.choice([-1, 1]),
            'dy': random.uniform(1, 3) * random.choice([-1, 1])
        })
    mover_balones(canvas, balones, window_width, window_height)

    # Crear componentes adicionales en la ventana principal
    menu_frame = tk.Frame(canvas, bg='#225444', height=50)
    menu_frame.pack(side=tk.TOP, fill=tk.X)

    def change_size(event, button, small_font, big_font):
        if event.type == '7':  # <Enter>
            button.config(font=big_font)
        elif event.type == '8':  # <Leave>
            button.config(font=small_font)

    botones = [
        ("Ingresar", ventanaIngreso),
        ("Play", mostrar_salida),
        ("Limpiar", limpiar_archivos),
        ("Ayuda", lambda: print("Ayuda"))
    ]

    for i, (texto, comando) in enumerate(botones):
        boton = tk.Button(menu_frame, text=texto, font=("Segoe UI", 12, "bold"),
                         command=comando, bg='#225444', fg='white', bd=0,
                         activebackground='#225444', activeforeground='white')
        boton.pack(side=tk.LEFT, padx=20)

        small_font = ("Segoe UI", 12, "bold")
        big_font = ("Segoe UI", 14, "bold")
        boton.bind("<Enter>", lambda e, b=boton: change_size(e, b, small_font, big_font))
        boton.bind("<Leave>", lambda e, b=boton: change_size(e, b, small_font, big_font))

    Titulo = tk.Label(root, text="90:00", fg="white", bg='#225444', font=("Segoe UI", 24, "bold"))
    Titulo.place(x=640, y=0)

    root.mainloop()

VentanaPrincipal()