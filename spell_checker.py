from textblob import TextBlob
from tkinter import *


def correct_spelling():
    global input_entry, output_entry

    # Obtiene el texto ingresado en el campo de entrada
    input_text = input_entry.get()

    # Corrige la ortografía del texto ingresado
    corrected_text = TextBlob(input_text).correct()

    # Borra el contenido del campo de salida y agrega el texto corregido
    output_entry.delete(0, END)
    output_entry.insert(0, corrected_text)


def create_main_window():
    global input_entry, output_entry

    # Crea la ventana principal
    window = Tk()
    window.geometry("500x400")
    window.resizable(False, False)
    window.config(bg="Green")
    window.title("Corrector de Ortografía")

    # Etiqueta para el texto con ortografía incorrecta
    incorrect_label = Label(window, text="Insert your word", font=(
        "Time New Roman", 20, "bold"), bg="Green", fg="white")
    incorrect_label.place(x=100, y=20, height=50, width=300)

    # Campo de entrada para el texto con ortografía incorrecta
    input_entry = Entry(window, font=("Time New Roman", 20))
    input_entry.place(x=50, y=80, height=50, width=400)

    # Etiqueta para el texto con ortografía corregida
    corrected_label = Label(window, text="The correct form is:", font=(
        "Time New Roman", 20, "bold"), bg="Green", fg="white")
    corrected_label.place(x=50, y=140, height=50, width=400)

    # Campo de entrada para el texto con ortografía corregida
    output_entry = Entry(window, font=("Time New Roman", 20))
    output_entry.place(x=50, y=200, height=50, width=400)

    # Botón para corregir la ortografía
    correction_button = Button(window, text='Corregir', font=(
        'Time New Roman', 25, 'bold'), bg="tomato", command=correct_spelling)
    correction_button.place(x=150, y=280, height=50, width=200)

    # Ejecuta el bucle principal de la ventana
    window.mainloop()


# Llama a la función para crear la ventana principal
create_main_window()
