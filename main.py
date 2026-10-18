from tkinter import *

window = Tk()
window.title("Kilometer to Miles")
window.config(padx=20, pady=20)

label1 = Label(text="Km ", font=("Times New Roman", 25))
label1.grid(column=2, row=0)
label2 = Label(text="Is equal to: ", font=("Times New Roman", 25))
label2.grid(column=0, row=1)
label3 = Label(text="Miles ", font=("Times New Roman", 25))
label3.grid(column=2, row=1)
label4 = Label(text=" ", font=("Times New Roman", 25))
label4.grid(column=1, row=1)

def km_to_miles():
    km = float(km_input.get())
    result = int(km) / 1.609344
    label4.config(text=round(result, 2))

button = Button(text="Calculate", font=("Times New Roman", 15), command=km_to_miles)
button.grid(column=1, row=2)

km_input = Entry(width=15)
km_input.grid(column=1, row=0)
print(km_input)
window.mainloop()