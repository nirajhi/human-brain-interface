import tkinter as tk
import navigation as nv

def write_slogan():
    print("Tkinter is easy to use!")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button1 = tk.Button(frame,
                   text="QUIT",
                   fg="red",
                   command=quit)
# button1.pack(side=tk.TOP)

button2 = tk.Button(frame,
                   text="Hello",
                   command=write_slogan)
# button2.pack(side=tk.TOP)

button3 = tk.Button(frame,
                   text="Hello",
                   command=write_slogan)
# button3.pack(side=tk.TOP)

button1.pack(side=tk.TOP)
button2.pack(side=tk.TOP)
button3.pack(side=tk.TOP)

root.mainloop()


