
import crc8_calc
from tkinter import *
from tkinter.ttk import Combobox 
from pyperclip import copy


def lbl_any(text_label, row_number, column_number=1):
    global window
    lbl = Label(window, text=text_label, font=("Arial Bold", 11))
    lbl.grid(row=row_number, column=column_number)


def button_clicked():
    global combo
    global txt_input
    
    code = crc8_calc.code_generation(combo.get(), txt_input.get())
    txt_output.delete(0, END)
    txt_output.insert(0, code)
    copy(code) #pyperclip.copy


window = Tk()
window.title("wconvert 0.1")
window.geometry('250x200')

combo = Combobox(window)  
combo['values'] = (
    '1 - код 10й формат',
    '2 - код 16й формат',
    '3 - PIN код',
    '4 - код -> серия, номер'
    )  
combo.current(0)
combo.grid(row=1, column=1) 

txt_input = Entry()
txt_input.insert(0, "000 00000")
txt_input.grid(row=2, column=1, padx=35, pady=5)

txt_output = Entry()
txt_output.insert(0, "3D00000000000001")
txt_output.grid(row=6, column=1, padx=35, pady=5)

lbl_any(' ', 0)
lbl_any(' ', 4)
lbl_any('Результат:', 5)

btn = Button(window, text="Конвертировать", bg="white", fg="blue", command=button_clicked)
btn.grid(row=3, column=1)

window.mainloop()





