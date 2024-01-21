import tkinter as tk


def press_key(key):
    current = display.get()
    if key == 'C':
        display.delete(0, tk.END)
    elif key == '=':
        try:
            result = eval(current)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    else:
        display.insert(tk.END, key)


root = tk.Tk()
root.title("Calculator")

display = tk.Entry(root, width=25, font=('Arial', 16), justify=tk.RIGHT)
display.grid(row=0, column=0, columnspan=4)

keys = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

row_val = 1
col_val = 0

for key in keys:
    if key != '=':
        tk.Button(root, text=key, padx=20, pady=10, font=('Arial', 12),
                  command=lambda k=key: press_key(k)).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=key, padx=20, pady=10, font=('Arial', 12),
                  command=lambda k=key: press_key(k)).grid(row=row_val, column=col_val, rowspan=2)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()