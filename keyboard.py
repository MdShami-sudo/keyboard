import tkinter as tk
from tkinter import ttk

def draw_gradient(canvas, color1, color2):
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    limit = height

    r1, g1, b1 = canvas.winfo_rgb(color1)
    r2, g2, b2 = canvas.winfo_rgb(color2)
    
    r_ratio = float(r2 - r1) / limit
    g_ratio = float(g2 - g1) / limit
    b_ratio = float(b2 - b1) / limit

    for i in range(limit):
        nr = int(r1 + (r_ratio * i))
        ng = int(g1 + (g_ratio * i))
        nb = int(b1 + (b_ratio * i))

        color = f'#{nr:04x}{ng:04x}{nb:04x}'
        canvas.create_line(0, i, width, i, fill=color)

def on_key_press(key):
    if key == "Cut":
        display_var.set("")
    elif key == "Space":
        display_var.set(display_var.get() + " ")
    else:
        display_var.set(display_var.get() + key)

root = tk.Tk()
root.title("Bubble Keyboard with Gradient Background")
root.geometry("600x400")

gradient_canvas = tk.Canvas(root, width=600, height=400)
gradient_canvas.pack(fill="both", expand=True)

root.update_idletasks()  
draw_gradient(gradient_canvas, "#ffcccc", "#cc99ff")

frame = ttk.Frame(gradient_canvas)
frame.place(relx=0.5, rely=0.5, anchor="center")

display_var = tk.StringVar()
display_label = ttk.Label(frame, textvariable=display_var, font=("Helvetica", 24), background="#ffffff", width=30)
display_label.pack(pady=10)

keys_frame = ttk.Frame(frame)
keys_frame.pack()

keys = [
    ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ' ']
]

keys.append(["Cut", "Space"])

for row in keys:
    row_frame = ttk.Frame(keys_frame)
    row_frame.pack(pady=5)
    for key in row:
        btn = ttk.Button(row_frame, text=key, command=lambda k=key: on_key_press(k), width=4)
        btn.pack(side="left", padx=2)

root.mainloop()
