import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: IF_Iluminacion
---
Enunciado:
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        precio_lamparas = 800
        marca_luz = self.combobox_marca.get()
        cantidad_lamparas = int(self.combobox_cantidad.get())
        precio_total = precio_lamparas * cantidad_lamparas
        if cantidad_lamparas >= 6:
            descuento = precio_total * 0.5
            precio_condescuento = int(precio_total - descuento)
            if precio_condescuento > 4000:
                descuento_a = precio_total * 0.05
                precio_condescuento = precio_condescuento - descuento_a
            else:
                pass
            alert("Precio", "Su precio final es de "+str(precio_condescuento))
        elif cantidad_lamparas == 5 and marca_luz == "ArgentinaLuz":
            descuento = precio_total * 0.4
            precio_condescuento = int(precio_total - descuento)
            if precio_condescuento > 4000:
                descuento_a = precio_total * 0.05
                precio_condescuento = precio_condescuento - descuento_a
            else:
                pass
            alert("Precio", "Su precio final es de "+str(precio_condescuento))
        elif cantidad_lamparas == 5 and marca_luz != "ArgentinaLuz":
            descuento = precio_total * 0.3
            precio_condescuento = int(precio_total - descuento)
            if precio_condescuento > 4000:
                descuento_a = precio_total * 0.05
                precio_condescuento = precio_condescuento - descuento_a
            else:
                pass
            alert("Precio", "Su precio final es de "+str(precio_condescuento))
        elif cantidad_lamparas == 4 and marca_luz == "ArgentinaLuz" or marca_luz == "FelipeLamparas":
            descuento = precio_total * 0.25
            precio_condescuento = int(precio_total - descuento)
            if precio_condescuento > 4000:
                descuento_a = precio_total * 0.05
                precio_condescuento = precio_condescuento - descuento_a
            else:
                pass
            alert("Precio", "Su precio final es de "+str(precio_condescuento))
        elif cantidad_lamparas == 4 and marca_luz != "ArgentinaLuz" and marca_luz != "FelipeLamparas":
            descuento = precio_total * 0.2
            precio_condescuento = int(precio_total - descuento)
            if precio_condescuento > 4000:
                descuento_a = precio_total * 0.05
                precio_condescuento = precio_condescuento - descuento_a
            else:
                pass
            alert("Precio", "Su precio final es de "+str(precio_condescuento))
        elif cantidad_lamparas == 3 and marca_luz == "ArgentinaLuz":
            descuento = precio_total * 0.15
            precio_condescuento = int(precio_total - descuento)
            if precio_condescuento > 4000:
                descuento_a = precio_total * 0.05
                precio_condescuento = precio_condescuento - descuento_a
            else:
                pass
            alert("Precio", "Su precio final es de "+str(precio_condescuento))
        elif cantidad_lamparas == 3 and marca_luz == "FelipeLamparas":
            descuento = precio_total * 0.1
            precio_condescuento = int(precio_total - descuento)
            if precio_condescuento > 4000:
                descuento_a = precio_total * 0.05
                precio_condescuento = precio_condescuento - descuento_a
            else:
                pass
            alert("Precio", "Su precio final es de "+str(precio_condescuento))
        elif cantidad_lamparas == 3 and marca_luz != "ArgentinaLuz" and marca_luz != "FelipeLamparas":
            descuento = precio_total * 0.05
            precio_condescuento = int(precio_total - descuento)
            if precio_condescuento > 4000:
                descuento_a = precio_total * 0.05
                precio_condescuento = precio_condescuento - descuento_a
            else:
                pass
            alert("Precio", "Su precio final es de "+str(precio_condescuento))
        else:
            if precio_condescuento > 4000:
                descuento_a = precio_total * 0.05
                precio_condescuento = precio_condescuento - descuento_a
            else:
                pass 
            alert("Precio", "Su precio final es de "+str(precio_total))
        

        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()