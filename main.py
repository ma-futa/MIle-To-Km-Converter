from tkinter import *

window = Tk()
window.title('MIle to Km Converter')
# window.minsize(height=100, width=300)
window.config(padx=20, pady=20)


def convert():
    ans = int(miles_input.get()) * 1.609
    answer_label.config(text=f'{ans}')


miles_input = Entry()
miles_input.config(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text='MIles')
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text='is equal to')
is_equal_to_label.grid(column=0, row=1)

answer_label = Label(text=0)
answer_label.grid(column=1, row=1)

km_label = Label(text='Km')
km_label.grid(column=2, row=1)

calculate_button = Button(text='Calculate',command=convert)
calculate_button.grid(column=1, row=2)

window.mainloop()
