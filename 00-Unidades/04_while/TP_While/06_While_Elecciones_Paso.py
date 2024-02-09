import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        candidato_mas_votos = None
        candidato_menos_votos = None
        total_edades = 0
        total_votos = 0
        cantidad_candidatos = 0

        nombre = prompt("Nombre", "Ingrese el nombre del candidato (o 'fin' para terminar):")
        while nombre.lower() != 'fin':
            edad = prompt("Edad", "Ingrese la edad del candidato (mayor a 25):")
            if not edad.isdigit() or int(edad) <= 25:
                alert("Error", "La edad debe ser un número mayor a 25.")
                nombre = prompt("Nombre", "Ingrese el nombre del candidato (o 'fin' para terminar):")
                continue

            votos = prompt("Votos", "Ingrese la cantidad de votos recibidos (mayor o igual a 0):")
            if not votos.isdigit() or int(votos) < 0:
                alert("Error", "La cantidad de votos debe ser un número mayor o igual a 0.")
                nombre = prompt("Votos", "Ingrese el nombre del candidato (o 'fin' para terminar):")
                continue

            cantidad_candidatos += 1
            total_edades += int(edad)
            total_votos += int(votos)

            if candidato_mas_votos is None or int(votos) > candidato_mas_votos['votos']:
                candidato_mas_votos = {'nombre': nombre, 'edad': int(edad), 'votos': int(votos)}

            if candidato_menos_votos is None or int(votos) < candidato_menos_votos['votos']:
                candidato_menos_votos = {'nombre': nombre, 'edad': int(edad), 'votos': int(votos)}

            nombre = prompt("Nombre", "Ingrese el nombre del siguiente candidato (o 'fin' para terminar):")

        if cantidad_candidatos == 0:
            alert("Error", "No se ingresaron candidatos.")
            return

        # a. Candidato con más votos
        alert("Resultado a", f"El candidato con más votos es {candidato_mas_votos['nombre']}.")

        # b. Candidato con menos votos
        alert("Resultado b", f"El candidato con menos votos es {candidato_menos_votos['nombre']} con {candidato_menos_votos['edad']} años.")

        # c. Promedio de edades
        if cantidad_candidatos > 0:
            promedio_edades = total_edades / cantidad_candidatos
            alert("Resultado c", f"El promedio de edades de los candidatos es: {promedio_edades:.2f} años.")
        else:
            alert("Resultado c", "No hay candidatos para calcular el promedio de edades.")

        # d. Total de votos
        alert("Resultado d", f"El total de votos emitidos es: {total_votos}.")




if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
