from tkinter import *
from tkhtmlview import HTMLLabel

# Create Object
root = Tk()
root.title("About")
root.iconbitmap('images/icon.ico')

# Set Geometry
root.geometry("700x500")

# Add label
my_label = HTMLLabel(root, html= """
    <h1>User guide</h1>
    <p>Ctrl + O = Open file<br/>
    Ctrl + Shift + S = Save As<br/>
    Ctrl + S =  Save
    </p>
    <a href="https://docs.python.org/3/">Python Docs(3.10.4)</a>
    <h4>Running JS files<br/>
    Just run in the bottom window node "path to file"<br/>
    Easy!
    <h4/>   
    """)

# Adjust label
my_label.pack(pady=20, padx=20)

# Execute Tkinter
root.mainloop()
