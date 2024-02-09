import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: While_validaciones_rising_btl
---
Enunciado:
Rising BTL. Empresa dedicada a la toma de datos para realizar estadísticas y censos nos pide realizar una carga de datos validada e ingresada 
por ventanas emergentes solamente (para evitar hacking y cargas maliciosas) y luego asignarla a cuadros de textos. 

Los datos requeridos son los siguientes:
    Apellido
    Edad, entre 18 y 90 años inclusive.
    Estado civil, ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"]
    Número de legajo, numérico de 4 cifras, sin ceros a la izquierda.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.label0 = customtkinter.CTkLabel(master=self, text="Apellido")
        self.label0.grid(row=0, column=0, padx=20, pady=10)
        self.txt_apellido = customtkinter.CTkEntry(master=self)
        self.txt_apellido.grid(row=0, column=1)

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=1, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=1, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Estado")
        self.label2.grid(row=2, column=0, padx=20, pady=10)
        self.combobox_tipo = customtkinter.CTkComboBox(
            master=self, values=["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"])
        self.combobox_tipo.grid(row=2, column=1, padx=20, pady=10)

        self.label3 = customtkinter.CTkLabel(master=self, text="Legajo")
        self.label3.grid(row=3, column=0, padx=20, pady=10)
        self.txt_legajo = customtkinter.CTkEntry(master=self)
        self.txt_legajo.grid(row=3, column=1)

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        apellido = self.txt_apellido.get()
        while not apellido:
            alert("Error", "Por favor, ingrese el apellido.")
            apellido = prompt(self, "Ingrese el Apellido")
        edad_str = self.txt_edad.get()
        while True:
            if not edad_str.isdigit():
                alert("Error", "Por favor, ingrese una edad válida.")
            else:
                edad = int(edad_str)
                if 18 <= edad <= 90:
                    break
                else:
                    alert("Error", "La edad debe estar entre 18 y 90 años.")
            edad_str = prompt(self, "Ingrese la Edad nuevamente")
        estado_civil = self.combobox_tipo.get()
        while not estado_civil:
            alert("Error", "Por favor, seleccione un estado civil.")
            estado_civil = prompt(self, "Seleccione el Estado Civil")
        legajo_str = self.txt_legajo.get()
        while True:
            if not legajo_str.isdigit():
                alert("Error", "Por favor, ingrese un número de legajo válido.")
            else:
                legajo = int(legajo_str)
                if 1000 <= legajo <= 9999:
                    break
                else:
                    alert("Error", "El legajo debe ser un número de 4 cifras sin ceros a la izquierda.")
            legajo_str = prompt(self, "Ingrese el Legajo nuevamente")
        info_message = f"Apellido: {apellido}\nEdad: {edad}\nEstado Civil: {estado_civil}\nLegajo: {legajo}"
        alert("Datos Validados", info_message)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
