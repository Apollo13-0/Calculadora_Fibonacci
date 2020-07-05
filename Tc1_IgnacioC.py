from tkinter import *
from threading import Thread
import time
import winsound
import turtle

#abre menu
def abrir():
    Vmenu.deiconify()
    Vprincipal.withdraw ()

# abre calculadora
def abrir_cal():
    Vmenu.withdraw()
    Vcal.transient(Vmenu)
    Vcal.deiconify()

# abre Datos del programador
def abrir_dat():
    Vmenu.withdraw ()
    Vdat.transient(Vmenu)
    Vdat.deiconify()

# Vuelve a pantalla principal
def abrir_Vprincipal():
    Vmenu.withdraw()
    Vprincipal.deiconify ()
    
# vuelve a menu
def volver ():
    Vmenu.deiconify()
    Vcal.withdraw()

# vuelve a menu
def volver_dat ():
    Vmenu.deiconify()
    Vdat.withdraw()

# poner musica
def play():
    winsound.PlaySound("cancion.wav", winsound.SND_FILENAME)
    
# Sucesion de Fibonacci pila
# E: un nomero entero
# S: sumade fibonacci
# R: numero entero mayor a 0

def FibPil():
    n = int(numero.get())
    if isinstance (n, int) and n >= 0:
        return resultadoPil.set(FibPil_aux(n,0))
    else:
        return resultadoPil.set("Favor ingresar un numero entero")

def FibPil_aux (n, cont):
    if n == 0 or n == 1: # caso base
        llamadas_Pil.set(cont)
        return n
    else:
        return FibPil_aux (n - 1, cont + 1) + FibPil_aux (n - 2, cont + 1)


# Sucesion de Fibonacci cola
# E: un nomero entero
# S: sumade fibonacci
# R: numero entero mayor a 0

def FibCol():
    n = int(numero.get())
    if isinstance (n, int) and n >= 0:
       return resultadoCol.set(FibCol_aux(n, 0, 1, 0))
    else:
        return resultadoCol.set("Favor ingresar un numero entero positivo")

def FibCol_aux(n, cont, n1, n2):
    if cont == n: # caso base
        llamadas_Col.set(cont)
        return n2
    else:
        return FibCol_aux(n, cont + 1, n2, n1 + n2)
    
# Funcion que ejecuta las funciones de fibonacci y miden su riempo

def Fib3 ():
    start = time.time() # toma el tiempo
    FibPil ()
    end = time.time() # toma el tiempo
    tiempo_pil.set(end - start) # Resta los 2 tiempos anteriores
    start2 = time.time() # toma el tiempo
    FibCol ()
    end2 = time.time() # toma el tiempo
    tiempo_col.set(end2 - start2) # Resta los 2 tiempos anteriores
    
# codigo de las animaciones con turtle

    # Animacion 1
    
def anumacion(lados, cont, poli, cont2):
    poligono1.hideturtle() #esconde la tortuga
    if poli != cont2:
        if lados == cont: # Cuando termina el poligono
            poligono1.left(135.0) # gira hacia la izquierda 
            return anumacion (lados, 0, poli, cont2 +1)
        elif lados != cont:
            poligono1.forward(40) # dibuja linea
            poligono1.right(360 / 8) # gira hacia la derecha
            return anumacion (lados, cont + 1, poli, cont2)
    elif poli == cont2:  # caso base
        return False
    else:
        poligono1.left(135.0) # gira hacia la izquierda 
        return anumacion (lados, cont, poli, cont2 +1)
    
    #Animacion2
    
def anumacion2(lados, cont, poli, cont2):
    poligono2.hideturtle() #esconde la tortuga
    if poli != cont2:
        if lados == cont: # Cuando termina el poligono
            poligono2.left(135.0) # gira hacia la izquierda 
            return anumacion2 (lados, 0, poli, cont2 +1)
        elif lados != cont:
            poligono2.forward(40) # dibuja linea
            poligono2.right(360 / 8) # gira hacia la derecha
            return anumacion2 (lados, cont + 1, poli, cont2)
    elif poli == cont2:  # caso base
        return False
    else:
        poligono2.left(135.0) # gira hacia la izquierda
        return anumacion2 (lados, cont, poli, cont2 +1)
    
    #Animacion3
    
def anumacion3(lados, cont, poli, cont2):
    poligono3.hideturtle() #esconde la tortuga
    if poli != cont2:
        if lados == cont: # Cuando termina el poligono
            poligono3.left(135.0) # gira hacia la izquierda
            return anumacion3 (lados, 0, poli, cont2 +1)
        elif lados != cont:
            poligono3.forward(40) # dibuja linea
            poligono3.right(360 / 8) # gira hacia la derecha
            return anumacion3 (lados, cont + 1, poli, cont2)
    elif poli == cont2: # caso base
        return False
    else:
        poligono3.left(135.0) # gira hacia la izquierda
        return anumacion3 (lados, cont, poli, cont2 +1)

# Hilos para la ejecucion simultanea

def hilo1():
    t1 = Thread(target = anumacion, args=(8,0,8,0))
    t1.start()
    
def hilo2():
    t2 = Thread(target = anumacion2,args =(8,0,8,0))
    t2.start()

def hilo3():
    t2 = Thread(target = anumacion3,args =(8,0,8,0))
    t2.start()
  
# Ventana principal, aqui se encuentra la animacion

Vprincipal = Tk() # se crea una ventana de inicio
Vprincipal.title ("Calculadora Fibonacci") # Cambiar el nombre a la ventana
Vprincipal.iconbitmap("luna.ico") # Se cambia el icono de la ventana
Vprincipal.geometry ("800x600+100+100")
Vprincipal.resizable (0,0)  # No hay cambio de tamaño de la ventana

#se crea un canvas para dibujar
canvas1 = Canvas(Vprincipal, width = 800, height = 600, bg = "cornsilk2" )
canvas1.pack()

# se crean las lineas para la decoracion 
canvas1.create_rectangle(0,0,800,50, fill = "MistyRose4", outline = "MistyRose4")
canvas1.create_rectangle(0,0,775,50, fill = "cyan4", outline = "cyan4")
canvas1.create_rectangle(0,0,750,50, fill = "#ffa500", outline = "#ffa500")
canvas1.create_rectangle(0,540,800,600, fill = "#e44f28", outline = "#e44f28")
canvas1.create_text(150,25, text = "Sucesión de Fibonacci", font = ("Times", 22))

# animacion 1

animacionCav = Canvas (Vprincipal, width = 200, height = 200, bg = "cornsilk2",highlightbackground = "cornsilk2" )
animacionCav.place(x = 300, y = 100)

poligono = turtle.TurtleScreen(animacionCav) #s se translada la tortuga a una canva
poligono.bgcolor("cornsilk2") # color del foondo
poligono1 = turtle.RawTurtle(poligono) # Se define una tortuga en la canva de tkinter
poligono1.color ("cyan4") # color de la linea
poligono1.speed(10) # velocidad de la tortuga 
poligono1.width(3) # ancho de la linea

# Animacion 2

animacion2Cav = Canvas (Vprincipal, width = 200, height = 200, bg = "cornsilk2", highlightbackground = "cornsilk2")
animacion2Cav.place(x = 50, y = 200)

poligono = turtle.TurtleScreen(animacion2Cav) #s se translada la tortuga a una canva
poligono.bgcolor("cornsilk2") # color del foondo
poligono2 = turtle.RawTurtle(poligono) # Se define una tortuga en la canva de tkinter
poligono2.color ("#ffa500") # color de la linea
poligono2.speed(10) # velocidad de la tortuga
poligono2.width(3) # ancho de la linea

# Animacin 3

animacion3Cav = Canvas (Vprincipal, width = 200, height = 200, bg = "cornsilk2", highlightbackground = "cornsilk2")
animacion3Cav.place(x = 550, y = 200)

poligono = turtle.TurtleScreen(animacion3Cav) #s se translada la tortuga a una canva
poligono.bgcolor("cornsilk2") # color del foondo
poligono3 = turtle.RawTurtle(poligono) # Se define una tortuga en la canva de tkinter
poligono3.color ("#e44f28")  # color de la linea
poligono3.speed(10) # velocidad de la tortuga
poligono3.width(3) # ancho de la linea

#Ejecucion de la animacion simultaneamente

hilo1()
hilo2()
hilo3()

#botones Ventana principal

boton_iniciar = Button (Vprincipal, text = "Pulsa para iniciar", font = ("Times", 18),
                        overrelief = "flat", activeforeground = "#ffa500", command = abrir)
boton_iniciar.configure (bg = "#ffa500")
boton_iniciar.place(x = 300, y = 375, width = 200, height = 50)

# Ventana Menu, aqui se encuentran los botones para la calculadora, datos y volver a la principal

Vmenu = Toplevel() # se crea ventana para el menu
Vmenu.title ("Menu") # cambia el nombre de la ventana
Vmenu.iconbitmap("luna.ico") # Se cambia el icono de la ventana
Vmenu.geometry ("800x600+100+100")
Vmenu.resizable (0,0)  # No hay cambio de tamaño de la ventana
Vmenu.iconify()

#se crea un canvas para dibujar
canvas2 = Canvas(Vmenu, width = 800, height = 600, bg = "cornsilk2" )
canvas2.pack()

# se crean las lineas para la decoracion 
canvas2.create_rectangle(0,0,800,50, fill = "#ffa500", outline = "#ffa500")
canvas2.create_rectangle(0,0,775,50, fill = "MistyRose4", outline = "MistyRose4")
canvas2.create_rectangle(0,0,750,50, fill = "cyan4", outline = "cyan4")
canvas2.create_rectangle(0,540,800,600, fill = "#e44f28", outline = "#e44f28")
canvas2.create_text(60,25, text = "Menu", font = ("Times", 22))

#botones Menu

boton_calcu = Button (Vmenu, text = "Calcular sucesión", font = ("Times", 16),
                      overrelief = "flat", activeforeground = "cyan4", command = abrir_cal)
boton_calcu.configure (bg = "#ffa500")
boton_calcu.place(x = 300, y = 200, width = 200, height = 50)

boton_datos = Button (Vmenu, text = "Datos del programador", font = ("Times", 16),
                      overrelief = "flat", activeforeground = "cyan4", command = abrir_dat)
boton_datos.configure (bg = "#ffa500")
boton_datos.place(x = 300, y = 275, width = 200, height = 50)

boton_principal = Button (Vmenu, text = "Volver al inicio", font = ("Times", 16),
                      overrelief = "flat", activeforeground = "cyan4", command = abrir_Vprincipal)
boton_principal.configure (bg = "#ffa500")
boton_principal.place(x = 300, y = 350, width = 200, height = 50)

# Ventana Calcu

Vcal = Toplevel() # se crea ventana para el menu
Vcal.title ("Calculadora") # cambia el nombre de la ventana
Vcal.iconbitmap("luna.ico") # Se cambia el icono de la ventana
Vcal.geometry ("800x600+100+100")
Vcal.resizable (0,0)  # No hay cambio de tamaño de la ventana
Vcal.iconify()

#se crea un canvas para dibujar
canvas3 = Canvas(Vcal, width = 800, height = 600, bg = "cornsilk2" )
canvas3.pack()

# se crean las lineas para la decoracion 
canvas3.create_rectangle(0,0,800,50, fill = "cyan4", outline = "cyan4")
canvas3.create_rectangle(0,0,775,50, fill = "#ffa500", outline = "#ffa500")
canvas3.create_rectangle(0,0,750,50, fill = "MistyRose4", outline = "MistyRose4")
canvas3.create_rectangle(0,540,800,600, fill = "#e44f28", outline = "#e44f28")
canvas3.create_text(150,25, text = "Calculadora Fibonacci", font = ("Times", 22), fill = "white")

# Se crea el texto en ventana calcu
etiqueta1 = Label (Vcal, bg = "cornsilk2", font = ("times", 20), text = "Definición: ")
etiqueta1.place (x = 10, y = 80)
etiqueta2 = Label (Vcal, bg = "cornsilk2", font = ("times", 18), text = "Es una sucesión definida por recurrencia, es decir, para calcular un término ")
etiqueta2.place (x = 10, y = 120)
etiqueta3 = Label (Vcal, bg = "cornsilk2", font = ("times", 18), text = "necesita de los términos anteriores.")
etiqueta3.place (x = 10, y = 150)
etiqueta4 = Label (Vcal, bg = "cornsilk2", font = ("times", 18), text = "Ingrese la cantidad de terminos:")
etiqueta4.place (x = 10, y = 200)
etiqueta5 = Label (Vcal, bg = "cornsilk2", font = ("Times", 18), text = "La suma obtenida es:")
etiqueta5.place (x = 10, y = 325)
resultadoPil = StringVar () # Se define la variable que da el resultado
etiqueta6 = Label (Vcal, bg = "cornsilk2", font = ("Times", 18), textvariable = resultadoPil)
etiqueta6.place (x = 10, y = 375)
resultadoCol = StringVar () # Se define la variable que da el resultado
etiqueta35 = Label (Vcal, bg = "cornsilk2", font = ("Times", 18), textvariable = resultadoCol)
etiqueta35.place (x = 400, y = 375)
# Para recursividad de pila
etiqueta7 = Label (Vcal, bg = "cornsilk2", font = ("Times", 18), text = "Recursividad de pila")
etiqueta7.place (x = 10, y = 420)
etiqueta9 = Label (Vcal, bg = "cornsilk2", font = ("Times", 14), text = "Tiempo:")
etiqueta9.place (x = 10, y =450)
tiempo_pil = StringVar() # Se define la variable que da el tiempo
etiqueta10 = Label(Vcal, bg = "cornsilk2", font = ("Times", 14), textvariable = tiempo_pil)
etiqueta10.place(x = 80, y = 450)
etiqueta11 = Label(Vcal, bg = "cornsilk2", font = ("Times", 14), text= "Total de llamadas:")
etiqueta11.place(x = 10, y = 480)
llamadas_Pil = StringVar() # Se crea una variable para insetar texto
etiqueta12 = Label(Vcal, bg = "cornsilk2", font = ("Times", 14), textvariable = llamadas_Pil)
etiqueta12.place(x = 200, y = 480)
# Para recursividad de cola
etiqueta8 = Label (Vcal, bg = "cornsilk2", font = ("Times", 18), text = "Recursividad de cola")
etiqueta8.place (x = 400, y = 420)
etiqueta13 = Label (Vcal, bg = "cornsilk2", font = ("Times", 14), text = "Tiempo:")
etiqueta13.place (x = 400, y =450)
tiempo_col = StringVar() # Se define la variable que da el tiempo
etiqueta14 = Label(Vcal, bg = "cornsilk2", font = ("Times", 14), textvariable = tiempo_col)
etiqueta14.place(x = 470, y = 450)
etiqueta15 = Label(Vcal, bg = "cornsilk2", font = ("Times", 14), text= "Total de llamadas:")
etiqueta15.place(x = 400, y = 480)
llamadas_Col = StringVar() # Se crea una variable para insetar texto
etiqueta16 = Label(Vcal, bg = "cornsilk2", font = ("Times", 14), textvariable = llamadas_Col)
etiqueta16.place(x = 600, y = 480)

# Se crean botones para obtener resultado y devolve a menu

boton_fib = Button (Vcal, text = "Calcular", font = ("Times", 18), command = Fib3, overrelief = "flat", activeforeground = "MistyRose4")
boton_fib.configure (bg = "#ffa500", font = ("Times", 18))
boton_fib.place (x = 300, y = 250, width = 200, height = 50)


imagen1 = PhotoImage(file = "atras.gif") # Se llama a la imagen .gif
imagen_volver1 = imagen1.subsample (11,11)
boton_volver1 = Button (Vcal, image = imagen_volver1, command = volver)
boton_volver1.configure (bg = "#e44f28", relief = "flat", activebackground = "#e44f28")
boton_volver1.place (x = 740, y = 545, width = 50, height = 50)

#Se crea el cuadro de texto para obtener entradas
numero = Entry (Vcal, font = "Times")
numero.place (x = 320, y = 208, width = 100, height = 22)

# Ventana Datos del programador

Vdat = Toplevel() # se crea ventana para el menu
Vdat.title ("Datos del programador") # cambia el nombre de la ventana
Vdat.iconbitmap("luna.ico") # Se cambia el icono de la ventana
Vdat.geometry ("800x600+100+100")
Vdat.resizable (0,0)  # No hay cambio de tamaño de la ventana
Vdat.iconify()

#se crea un canvas para dibujar
canvas4 = Canvas(Vdat, width = 800, height = 600, bg = "cornsilk2" )
canvas4.pack()

# se crean las lineas para la decoracion 
canvas4.create_rectangle(0,0,800,50, fill = "#e44f28", outline = "#e44f28")
canvas4.create_rectangle(0,0,775,50, fill = "#ffa500", outline = "#ffa500")
canvas4.create_rectangle(0,0,750,50, fill = "MistyRose4", outline = "MistyRose4")

canvas4.create_text(150,25, text = "Datos del programador", font = ("Times", 22), fill = "white")

# Se crea el texto en ventana datos programador

imagen3 = PhotoImage(file = "FotoP.gif") # Se llama a la imagen .gif
imagen_volver3 = imagen3.subsample (2,2)
etiqueta17 = Label (Vdat, image = imagen_volver3)
etiqueta17.place (x = 10, y = 60, width = 200, height = 200)
etiqueta18 = Label (Vdat, bg = "cornsilk2", font = ("times", 20), text = "Nombre:")
etiqueta18.place (x = 230, y = 60)
etiqueta19 = Label (Vdat, bg = "cornsilk2", font = ("times", 14), text = "Jose Ignacio Calderón Díaz")
etiqueta19.place (x = 230, y = 90)
etiqueta20 = Label (Vdat, bg = "cornsilk2", font = ("times", 20), text = "Carnet:")
etiqueta20.place (x = 500, y = 60)
etiqueta21 = Label (Vdat, bg = "cornsilk2", font = ("times", 14), text = "2019031750")
etiqueta21.place (x = 500, y = 90)
etiqueta22 = Label (Vdat, bg = "cornsilk2", font = ("times", 20), text = "Género:")
etiqueta22.place (x = 230, y = 120)
etiqueta23 = Label (Vdat, bg = "cornsilk2", font = ("times", 14), text = "Masculino")
etiqueta23.place (x = 230, y = 150)
etiqueta24 = Label (Vdat, bg = "cornsilk2", font = ("times", 20), text = "Edad:")
etiqueta24.place (x = 500, y = 120)
etiqueta25 = Label (Vdat, bg = "cornsilk2", font = ("times", 14), text = "18 años")
etiqueta25.place (x = 500, y = 150)
etiqueta26 = Label (Vdat, bg = "cornsilk2", font = ("times", 20), text = "Dirección:")
etiqueta26.place (x = 230, y = 180)
etiqueta27 = Label (Vdat, bg = "cornsilk2", font = ("times", 14), text = "75 mts sur del recinto de la UCR, Paraíso, Cartago")
etiqueta27.place (x = 230, y = 210)
etiqueta28 = Label (Vdat, bg = "cornsilk2", font = ("times", 20), text = "Mapa")
etiqueta28.place (x = 230, y = 250)
imagen4 = PhotoImage(file = "mapa.gif") # Se llama a la imagen .gif
imagen_volver4 = imagen4.subsample (2,2)
etiqueta29 = Label (Vdat, image = imagen_volver4)
etiqueta29.place (x = 230, y = 300, width = 520, height = 250)
etiqueta30 = Label (Vdat, bg = "cornsilk2", font = ("times", 14), text = "¡Es un lugar muy tranquilo y seguro! Con instituciones educativas cerca.")
etiqueta30.place (x = 210, y = 560)
etiqueta31 = Label (Vdat, bg = "cornsilk2", font = ("times", 16), text = "Grupo favorito:")
etiqueta31.place (x = 10, y = 270)
imagen5 = PhotoImage(file = "elo.gif") # Se llama a la imagen .gif
imagen_volver5 = imagen5.subsample (1,1)
etiqueta32 = Label (Vdat, image = imagen_volver5 )
etiqueta32.place (x = 10, y = 300, width = 200, height = 190)
etiqueta33 = Label (Vdat, bg = "cornsilk2", font = ("times", 16), text = "Banda: ELO")
etiqueta33.place (x = 70, y = 500)
etiqueta34 = Label (Vdat, bg = "cornsilk2", font = ("times", 16), text = "Género: Pop rock")
etiqueta34.place (x = 70, y = 525)

# botones ventana datos programador

imagen2 = PhotoImage(file = "atras.gif") # Se llama a la imagen .gif
imagen_volver2 = imagen2.subsample (11,11)
boton_volver2 = Button (Vdat, image = imagen_volver2, command = volver_dat)
boton_volver2.configure (bg = "cornsilk2", relief = "flat", activebackground = "cornsilk2")
boton_volver2.place (x = 750, y = 550, width = 50, height = 50)
imagen6 = PhotoImage(file = "play.gif") # Se llama a la imagen .gif
imagen_volver6 = imagen6.subsample (8,8)
boton_volver3 = Button (Vdat, image = imagen_volver6, command = play)
boton_volver3.configure (bg = "cornsilk2", relief = "flat", activebackground = "cornsilk2")
boton_volver3.place (x = 10, y = 500, width = 50, height = 50)


    
Vprincipal.mainloop()



# colores utilizados
# cornsilk2       blanco       fondo
# MistyRose4      cafe claro   
# cyan4           turquesa
# #ffa500         amarillo
# #e44f28         naranja 
