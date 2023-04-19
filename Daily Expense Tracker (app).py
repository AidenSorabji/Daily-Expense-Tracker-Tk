import customtkinter as ctk
import keyboard, time, os
from datetime import date
from pathlib import Path

window = ctk.CTk()
window.title("Expense Tracker")
window.geometry("700x450")
window.resizable(False, False)


# ---------------- Start ---------------- #

name_label_ask = ctk.CTkLabel(window,
                              text="What Is Your Name?",
                              font=('arial',
                                    28,
                                    "bold"))
name_label_ask.place(relx=0.5, rely=0.4, anchor='center')

name_entry = ctk.CTkEntry(window,
                          placeholder_text=" ",
                          width=300,
                          height=30)
name_entry.place(relx=0.5, rely=0.56, anchor="center")




def next_function_one():
    name_label_ask.destroy()
    name_entry.destroy()

var = ctk.IntVar()

next_button_one = ctk.CTkButton(window,
                                text="Next",
                                width=50,
                                height=30,
                                command=lambda:var.set(1))
next_button_one.place(x=690, y=440, anchor="se")

next_button_one.wait_variable(var)

name = name_entry.get()

next_function_one()

var.set(0)

# ---------------- First Entry ---------------- #

if_none = ctk.CTkLabel(window,
                       text="If no information is available for a certain entry, put: none",
                       font=('arial',
                             12,
                             'normal'))
if_none.place(relx=0.5, rely=0.8, anchor='center')

entry_one_label = ctk.CTkLabel(window,
                               text="Entry 1",
                               font=('arial',
                                     28,
                                     "bold"))
entry_one_label.place(relx=0.43, rely=0.33)

cost_label_one = ctk.CTkLabel(window,
                              text="Cost:",
                              font=("arial",
                                    16,
                                    'normal'))
cost_label_one.place(relx=0.24, rely=0.49)

cost_entry_one = ctk.CTkEntry(window,
                              placeholder_text="ex. $26.11",
                              width=78,
                              height=25)
cost_entry_one.place(relx=0.3, rely=0.5)

place_label_one = ctk.CTkLabel(window,
                               text="Place:",
                               font=('Arial',
                                     16,
                                     'normal'))
place_label_one.place(relx=0.45, rely=0.49)

place_entry_one = ctk.CTkEntry(window,
                               placeholder_text="ex. Herbert's Bakery",
                               width=150,
                               height=25)
place_entry_one.place(relx=0.52, rely=0.5)

time_label_one = ctk.CTkLabel(window,
                              text='Time:',
                              font=('Arial',
                                    16,
                                    'normal'))
time_label_one.place(relx=0.24, rely=0.562)

time_entry_one = ctk.CTkEntry(window,
                              placeholder_text="ex. 5:57 PM",
                              width=84,
                              height=25)
time_entry_one.place(relx=0.304, rely=0.57)

paymenttype_label_one = ctk.CTkLabel(window,
                                     text="Payment Type:",
                                     font=('Arial',
                                           16,
                                           'normal'))
paymenttype_label_one.place(relx=0.45, rely=0.562)

paymenttype_entry_one = ctk.CTkEntry(window,
                              placeholder_text="ex. Credit Card",
                              width=120,
                              height=25)
paymenttype_entry_one.place(relx=0.61, rely=0.57)

def next_function_two():
    entry_one_label.destroy()
    cost_label_one.destroy()
    cost_entry_one.destroy()
    place_label_one.destroy()
    place_entry_one.destroy()
    time_label_one.destroy()
    time_entry_one.destroy()
    paymenttype_label_one.destroy()
    paymenttype_entry_one.destroy()
    var.set(0)

next_button_one.wait_variable(var)

# Getting Payments
cost_one = cost_entry_one.get()
place_one = place_entry_one.get()
time_one = time_entry_one.get()
payment_type_one = paymenttype_entry_one.get()

next_function_two()

# ---------------- Second Entry ---------------- #

entry_two_label = ctk.CTkLabel(window,
                               text="Entry 2",
                               font=('arial',
                                     28,
                                     "bold"))
entry_two_label.place(relx=0.43, rely=0.33)

cost_label_two = ctk.CTkLabel(window,
                              text="Cost:",
                              font=("arial",
                                    16,
                                    'normal'))
cost_label_two.place(relx=0.24, rely=0.49)

cost_entry_two = ctk.CTkEntry(window,
                              placeholder_text="ex. $26.11",
                              width=78,
                              height=25)
cost_entry_two.place(relx=0.3, rely=0.5)

place_label_two = ctk.CTkLabel(window,
                               text="Place:",
                               font=('Arial',
                                     16,
                                     'normal'))
place_label_two.place(relx=0.45, rely=0.49)

place_entry_two = ctk.CTkEntry(window,
                               placeholder_text="ex. Herbert's Bakery",
                               width=150,
                               height=25)
place_entry_two.place(relx=0.52, rely=0.5)

time_label_two = ctk.CTkLabel(window,
                              text='Time:',
                              font=('Arial',
                                    16,
                                    'normal'))
time_label_two.place(relx=0.24, rely=0.562)

time_entry_two = ctk.CTkEntry(window,
                              placeholder_text="ex. 5:57 PM",
                              width=84,
                              height=25)
time_entry_two.place(relx=0.304, rely=0.57)

paymenttype_label_two = ctk.CTkLabel(window,
                                     text="Payment Type:",
                                     font=('Arial',
                                           16,
                                           'normal'))
paymenttype_label_two.place(relx=0.45, rely=0.562)

paymenttype_entry_two = ctk.CTkEntry(window,
                              placeholder_text="ex. Credit Card",
                              width=120,
                              height=25)
paymenttype_entry_two.place(relx=0.61, rely=0.57)

def next_function_three():
    entry_two_label.destroy()
    cost_label_two.destroy()
    cost_entry_two.destroy()
    place_label_two.destroy()
    place_entry_two.destroy()
    time_label_two.destroy()
    time_entry_two.destroy()
    paymenttype_label_two.destroy()
    paymenttype_entry_two.destroy()
    var.set(0)

next_button_one.wait_variable(var)

# Getting Payments
cost_two = cost_entry_two.get()
place_two = place_entry_two.get()
time_two = time_entry_two.get()
payment_type_two = paymenttype_entry_two.get()

next_function_three()

# ---------------- Third Entry ---------------- #

entry_three_label = ctk.CTkLabel(window,
                               text="Entry 3",
                               font=('arial',
                                     28,
                                     "bold"))
entry_three_label.place(relx=0.43, rely=0.33)

cost_label_three = ctk.CTkLabel(window,
                              text="Cost:",
                              font=("arial",
                                    16,
                                    'normal'))
cost_label_three.place(relx=0.24, rely=0.49)

cost_entry_three = ctk.CTkEntry(window,
                              placeholder_text="ex. $26.11",
                              width=78,
                              height=25)
cost_entry_three.place(relx=0.3, rely=0.5)

place_label_three = ctk.CTkLabel(window,
                               text="Place:",
                               font=('Arial',
                                     16,
                                     'normal'))
place_label_three.place(relx=0.45, rely=0.49)

place_entry_three = ctk.CTkEntry(window,
                               placeholder_text="ex. Herbert's Bakery",
                               width=150,
                               height=25)
place_entry_three.place(relx=0.52, rely=0.5)

time_label_three = ctk.CTkLabel(window,
                              text='Time:',
                              font=('Arial',
                                    16,
                                    'normal'))
time_label_three.place(relx=0.24, rely=0.562)

time_entry_three = ctk.CTkEntry(window,
                              placeholder_text="ex. 5:57 PM",
                              width=84,
                              height=25)
time_entry_three.place(relx=0.304, rely=0.57)

paymenttype_label_three = ctk.CTkLabel(window,
                                     text="Payment Type:",
                                     font=('Arial',
                                           16,
                                           'normal'))
paymenttype_label_three.place(relx=0.45, rely=0.562)

paymenttype_entry_three = ctk.CTkEntry(window,
                              placeholder_text="ex. Credit Card",
                              width=120,
                              height=25)
paymenttype_entry_three.place(relx=0.61, rely=0.57)

def next_function_forth():
    entry_three_label.destroy()
    cost_label_three.destroy()
    cost_entry_three.destroy()
    place_label_three.destroy()
    place_entry_three.destroy()
    time_label_three.destroy()
    time_entry_three.destroy()
    paymenttype_label_three.destroy()
    paymenttype_entry_three.destroy()
    if_none.destroy()
    var.set(0)

next_button_one.wait_variable(var)
var.set(0)
# Getting Payments
cost_three = cost_entry_three.get()
place_three = place_entry_three.get()
time_three = time_entry_three.get()
payment_type_three = paymenttype_entry_three.get()

next_function_forth()

next_button_one.destroy()

outputting = ctk.CTkLabel(window,
                          text="Outputting...",
                          font=('arial',
                                38,
                                'bold'))
outputting.place(relx=0.35, rely=0.45)
 
def destoy():
    outputting.destroy()
    final_label = ctk.CTkLabel(window,
                           text="Expenses Outputted!",
                           font=('arial',
                                 35,
                                 'bold'))
    final_label.place(relx=0.5, rely=0.5, anchor='center')

    close_button = ctk.CTkButton(window,
                                 width=680,
                                 height=35,
                                 text='Close Program',
                                 command=lambda:exit)
    close_button.place(relx=0.5, rely=0.94, anchor='center')


window.after(3000,destoy)

today = date.today()
daty = str(today.strftime("%m-%d-%y"))

filename = (str(name) + "'s Expenses - " + daty + ".txt")

f = open(filename, 'w')
f.write(str(name) + "'s Expenses:" + '\n')
f.write("Date: " + daty + '\n')
f.write("------------------------------------------------" + '\n')
f.write("Entry 1:" + '\n')
f.write("Cost - " + str(cost_one) + '\n')
f.write("Place - " + str(place_one) + '\n')
f.write("Time - " + str(time_one) + '\n')
f.write("Payment Type - " + str(payment_type_one) + '\n')
f.write("------------------------------------------------" + '\n')
f.write("Entry 2:" + '\n')
f.write("Cost - " + str(cost_two) + '\n')
f.write("Place - " + str(place_two) + '\n')
f.write("Time - " + str(time_two) + '\n')
f.write("Payment Type - " + str(payment_type_two) + '\n')
f.write("------------------------------------------------" + '\n')
f.write("Entry 3:" + '\n')
f.write("Cost - " + str(cost_three) + '\n')
f.write("Place - " + str(place_three) + '\n')
f.write("Time - " + str(time_three) + '\n')
f.write("Payment Type - " + str(payment_type_three) + '\n')
f.write("------------------------------------------------" + '\n')
f.close()


window.mainloop()