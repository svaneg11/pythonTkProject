# 1. Pack - empaca los elementos uno al lado del otro - dificil especificar una posicion concreta
import tkinter
window = tkinter.Tk()
window.title('Mi ventana')
window.config(padx=20, pady=20)

#Label
my_label = tkinter.Label(text="Pack Label")
my_label.pack(side='bottom')

#Button
button = tkinter.Button(text="Button")
button.pack()

#Button 2
button2 = tkinter.Button(text="Button 2")
button2.pack()

#Entry
entry = tkinter.Entry(width=10)
entry.pack()


window.mainloop()