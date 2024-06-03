import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operator = entry_operator.get()

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                result = 'Error! Division by zero.'
            else:
                result = num1 / num2
        else:
            result = 'Invalid operator'

        entry_result.delete(0, tk.END)
        entry_result.insert(0, result)
    except ValueError:
        entry_result.delete(0, tk.END)
        entry_result.insert(0, "Error! Invalid input")

root = tk.Tk()
root.title("Simple Calculator")

label1 = tk.Label(root, text="Number 1:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label_operator = tk.Label(root, text="Operator (+, -, *, /):")
label_operator.pack()
entry_operator = tk.Entry(root)
entry_operator.pack()

label2 = tk.Label(root, text="Number 2:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

entry_result = tk.Entry(root)
entry_result.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

root.mainloop()