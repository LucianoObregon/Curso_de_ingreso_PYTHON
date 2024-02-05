import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Luciano
apellido: Obregon
---
Ejercicio: entrada_salida_09bis
---
Enunciado:
Al presionar el botón 'Calcular', se deberán obtener los valores contenidos en las cajas de texto (txtSueldo y txtIncremento), 
transformarlos en números y mostrar el importe de sueldo actualizado con el incremento porcentual utilizando el Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Sueldo")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_sueldo = customtkinter.CTkEntry(master=self)
        self.txt_sueldo.grid(row=0, column=1)
        
        self.label2 = customtkinter.CTkLabel(master=self, text="Incremento") #acá cambié el "% de incremento" por "incremento" porque me daba error al usarlo en el self.txt
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_incremento = customtkinter.CTkEntry(master=self)
        self.txt_incremento.grid(row=1, column=1)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        sueldo_normal = int(self.txt_sueldo.get())
        incremento = int(self.txt_incremento.get())
        porcentaje = incremento / 100
        sueldo_porcentaje = porcentaje * sueldo_normal
        sueldo_total = sueldo_porcentaje + sueldo_normal
        alert("Sueldo", "El sueldo total es de "+str(sueldo_total))
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()