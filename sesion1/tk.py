import tkinter

#Ventana
window = tkinter.Tk()
window.title('My window')
window.minsize(width=500, height=300)

#Label - Etiqueta
label = tkinter.Label(text='Soy un Label', font=("Arial", 24, "italic"))
label.pack()

#Button
def button_clicked():
    #label['text'] = input.get()
    label.config(text=input.get())

button = tkinter.Button(text="Click me!", command=button_clicked)
button.pack()


#Entry
input = tkinter.Entry(width=10)
input.pack()


window.mainloop()