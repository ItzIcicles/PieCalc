# Importing the library that made GUI possible for this program
import tkinter


root = tkinter.Tk()

# Giving the windows a title
root.title("PieCalc")

#Placing the screen / typing area
screen = tkinter.Entry(root, width=45, borderwidth=5)
screen.grid(row=0, column=0, columnspan=5, padx=8, pady=10)


# Defing functions  
def button_click(number):
    current = screen.get()
    screen.delete(0, tkinter.END)
    screen.insert(0, str(current) + str(number))

def button_clear():
    screen.delete(0, tkinter.END)

def button_add():
    first_number = screen.get()
    global f_num
    f_num = int(first_number)
    screen.delete(0, tkinter.END)

def button_equal():
    second_number = screen.get()
    screen.delete(0, tkinter.END)
    screen.insert(0, f_num + int(second_number))


# Defining the buttons and placing them on the screen
button_clear = tkinter.Button(root, text="Clear", padx=125, pady=20, command=button_clear).grid(row=1, column=1, columnspan=3)
button_add = tkinter.Button(root, text="+", padx=30, pady=20, command=button_add).grid(row=1, column=4)

button_7 = tkinter.Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7)).grid(row=2, column=1)
button_8 = tkinter.Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8)).grid(row=2, column=2)
button_9 = tkinter.Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9)).grid(row=2, column=3)

button_4 = tkinter.Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4)).grid(row=3, column=1)
button_5 = tkinter.Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5)).grid(row=3, column=2)
button_6 = tkinter.Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6)).grid(row=3, column=3)

button_1 = tkinter.Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1)).grid(row=4, column=1)
button_2 = tkinter.Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2)).grid(row=4, column=2)
button_3 = tkinter.Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3)).grid(row=4, column=3)

button_0 = tkinter.Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0)).grid(row=5, column=1)
button_equal = tkinter.Button(root, text="=", padx=125, pady=20, command=button_equal).grid(row=5, column=2, columnspan=3)



root.mainloop()