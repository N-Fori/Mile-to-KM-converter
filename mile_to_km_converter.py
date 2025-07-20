import tkinter


def button_clicked():
    new_text = float(input.get()) * 1.609
    result_label.config(text=f"{new_text:.2f}")


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)


#Label
is_equal_label = tkinter.Label(text="is equal to", font=("Arial", 16, "bold"))
is_equal_label.grid(column=0, row=1)

miles_label = tkinter.Label(text="Miles", font=("Arial", 16, "bold"))
miles_label.grid(column=2, row=0)

km_label = tkinter.Label(text="Km", font=("Arial", 16, "bold"))
km_label.grid(column=2, row=1)

result_label = tkinter.Label(text="0", font=("Arial", 16, "bold"))
result_label.grid(column=1, row=1)

#Entry
input = tkinter.Entry(width=10)
input.insert(0, "0")
#print(input.get())
input.grid(column=1, row=0)

#Button
button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


window.mainloop()