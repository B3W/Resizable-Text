import tkinter as tk
from tkinter import font
import resizabletext as rt

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('200x100')
    root.minsize(width=100, height=100)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=0)

    # NOTE Can use any font
    custom_font = font.Font(family="Times New Roman", size=12)
    text = rt.ResizableText(root,
                            font=custom_font,
                            relief=tk.FLAT,
                            wrap='word',
                            highlightbackground="light grey",
                            highlightthickness=2,
                            height=1)

    text.insert(1.0, 'This is text that will get resized as the widget does')
    text.grid(column=0, row=0, sticky=tk.EW)

    # NOTE Must use configure event of parent to notify widget of resize
    root.bind('<Configure>', text.on_configure)
    root.mainloop()
