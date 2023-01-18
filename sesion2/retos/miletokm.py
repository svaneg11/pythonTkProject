import tkinter

# Window
window = tkinter.Tk()
window.title('Miles to Kilometers Converter')
window.config(padx=10, pady=10)

# Entry
entry = tkinter.Entry(width=10)
entry.grid(column=1, row=0)

# Miles Label
miles_label = tkinter.Label(text='Miles')
miles_label.grid(column=2, row=0)

# Is equal to Label
is_equal_to_label = tkinter.Label(text='is equal to')
is_equal_to_label.grid(column=0, row=1)

# Km value Label
km_value_label = tkinter.Label(text='0')
km_value_label.grid(column=1, row=1)

# Km Label
km_label = tkinter.Label(text='Km')
km_label.grid(column=2, row=1)

# Calculate Button
calculate_button = tkinter.Button(text='Calculate')
calculate_button.grid(column=1, row=2)


def convert_miles_to_km():
    miles = float(entry.get())
    km = miles * 1.609
    km_value_label['text'] = f'{km:0.2f}'


calculate_button.config(command=convert_miles_to_km)


window.mainloop()
