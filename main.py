import tkinter as tk
from tkinter import font
import resizabletext as rt

if __name__ == '__main__':
    root = tk.Tk()
    root.minsize(width=100, height=100)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=0)

    # NOTE Need monospaced font
    fixed_font = font.Font(family="Courier", size=12)
    text = rt.ResizableText(root,
                            fixed_font,
                            relief=tk.FLAT,
                            wrap='word',
                            highlightbackground="light grey",
                            highlightthickness=2,
                            height=1)

    text.insert(1.0, 'This is text that will get resized as the widget does')
    text.grid(column=0, row=0, sticky=tk.EW)

    # NOTE Must use configure event of master to resize widget width
    root.bind('<Configure>', text.on_configure)
    root.mainloop()
