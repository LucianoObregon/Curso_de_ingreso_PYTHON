import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        suma_positivos = 0
        suma_negativos = 0
        contador_positivos = 0
        contador_negativos = 0
        contador_ceros = 0

        
        while True:
            numero_a = prompt("Numero", "Ingrese un número:")
            if(numero_a == None):
                break
            else:
                numero_a = int(numero_a)
                if numero_a > 0:
                    numero = int(numero_a)
                    suma_positivos += numero
                    contador_positivos += 1
                elif numero_a == 0:
                    contador_ceros +=1
                else:
                    numero_b = int(numero_a)
                    suma_negativos += numero_b
                    contador_negativos += 1
        mensaje ="Suma positivos = "+str(suma_positivos)+"\nSuma negativos = "+str(suma_negativos)+"\nCantidad de positivos = "+str(contador_positivos)+"\nContador de negativos = "+str(contador_negativos)+"\nla cantidad de ceros es = "+str(contador_ceros)+"\nla diferencia entre la cantidad de negativos y positivos es = "+str(contador_positivos-contador_negativos)
        alert("Numeros", mensaje)
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
