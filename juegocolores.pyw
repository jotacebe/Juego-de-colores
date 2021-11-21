from tkinter import *
from random import choice

colorPrincipal = "#FFFF77"
colorSecundario = "#BBDDFF"

def colorear():
    validar = False
    n = 0
    while validar == False:
        for i in botones:
            aleatorio = choice([0,1])
            if aleatorio == 1:
                i.config(bg=colorPrincipal)
            else:
                i.config(bg=colorSecundario)
        for i in botones:
            if i.cget("bg") == colorPrincipal:
                n += 1
        if n != 9:        
            validar = True

def ganar(): 
    n = 0
    for i in botones:
        if i.cget("bg") == colorPrincipal:
            n += 1
    if n == 9:
        mensajeGanar.config(text="¡¡HAS GANADO!!")
        for i in botones:
            i.config(state=DISABLED)
        botonReiniciar.config(state=NORMAL)
        
def contar():   
    pulsaciones = int(contador.cget("text"))
    pulsaciones +=1
    contador.config(text=str(pulsaciones))

def reiniciar():    
    for i in botones:
        i.config(state=NORMAL)
    contador.config(text="0")
    botonReiniciar.config(state=DISABLED)
    mensajeGanar.config(text="")
    colorear()

def cambiar(lista):  
    contar()
    for i in lista:
        if i.cget("bg") == colorPrincipal:
            i.config(bg=colorSecundario)
        elif i.cget("bg") == colorSecundario:
            i.config(bg=colorPrincipal)
    ganar()

ventana = Tk()
ventana.title("Juego de colores")
ventana.geometry("460x300")
ventana.resizable(False, False)
ventana.config(padx=5, pady=5)

boton1 = Button(ventana, width=10, height=4, command=lambda: cambiar([boton1, boton2, boton4]))
boton2 = Button(ventana, width=10, height=4, command=lambda: cambiar([boton1, boton2, boton3, boton5]))
boton3 = Button(ventana, width=10, height=4, command=lambda: cambiar([boton2, boton3, boton6]))
boton4 = Button(ventana, width=10, height=4, command=lambda: cambiar([boton1, boton4, boton5, boton7]))
boton5 = Button(ventana, width=10, height=4, command=lambda: cambiar([boton2, boton4, boton5, boton6, boton8]))
boton6 = Button(ventana, width=10, height=4, command=lambda: cambiar([boton3, boton5, boton6, boton9]))
boton7 = Button(ventana, width=10, height=4, command=lambda: cambiar([boton4, boton7, boton8]))
boton8 = Button(ventana, width=10, height=4, command=lambda: cambiar([boton5, boton7, boton8, boton9]))
boton9 = Button(ventana, width=10, height=4, command=lambda: cambiar([boton6, boton8, boton9]))

botonReiniciar = Button(ventana, text="Nueva partida", state=DISABLED, command=reiniciar)

boton1.grid(row=0, column=0)
boton2.grid(row=0, column=1)
boton3.grid(row=0, column=2)
boton4.grid(row=1, column=0)
boton5.grid(row=1, column=1)
boton6.grid(row=1, column=2)
boton7.grid(row=2, column=0)
boton8.grid(row=2, column=1)
boton9.grid(row=2, column=2)

botonReiniciar.place(x=205, y=250)

mensajeGanar = Label(ventana, font=("Helvetia", 16))
mensajeGanar.place(x=10, y=250)

etiquetaContador = Label(text="Contador:", font=("Helvetia")).place(x=335, y=20)

contador = Label(ventana, text="0", font=("Helvetia"))
contador.place(x=420,y=20)

botones = [boton1, boton2, boton3, boton4, boton5, boton6, boton7, boton8, boton9]

colorear()

ventana.mainloop()