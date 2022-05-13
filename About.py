from tkinter import *
from tkhtmlview import HTMLLabel

# Create Object
root = Tk()
root.title("About")
root.iconbitmap('images/icon.ico')

# Set Geometry
root.geometry("450x450")

# Add label
my_label = HTMLLabel(root, html= """
	<ul>
    	<li><a href='https://github.com/superpythonguy/Lunar-Code'>My Github</a></li>
     	<p>Thanks for using my Code editor</p>
	</ul>
	<div>
		<p>Lunar code</p>
	</div>
	<h3>V0.1.0<br/>
    Made with Tkinter
    </h3>
 
    """)

# Adjust label
my_label.pack(pady=20, padx=20)

# Execute Tkinter
root.mainloop()
