# 3.Place - especifica con coordenadas (x,y) - Molesto a la hora de ubicar muchos componentes
import tkinter
window = tkinter.Tk()
window.title('Mi ventana')
window.config(padx=20, pady=20)

#Label
my_label = tkinter.Label(text="Pack Label")
my_label.place(x=200, y=200)
window.minsize(width=500, height=300)

#Button
button = tkinter.Button(text="Button")
button.grid(column=1, row=1)

#Button 2
button2 = tkinter.Button(text="Button 2")
button2.grid(column=2, row=2)


#Entry
entry = tkinter.Entry(width=10)
entry.grid(column=3, row=3)


window.mainloop()