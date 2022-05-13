from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter.messagebox import showerror, showinfo, showwarning
from tkinter.scrolledtext import ScrolledText
from tkhtmlview import *
import subprocess

app=Tk()
app.title("Lunar Code")
app.geometry("1000x600")
app.iconbitmap("images/icon.ico")

editor = ScrolledText(app, font=("ariel 13"), wrap=None)
editor.pack(fill=BOTH, expand=1)
editor.focus()
editor.config(fg="#F8F8F2",bg="#272822")

menu = Menu(app)
app.config(menu=menu)
file_menu = Menu(menu, tearoff=0)
edit_menu = Menu(menu, tearoff=0)
view_menu = Menu(menu, tearoff=0)
theme_menu = Menu(menu, tearoff=0)
other_menu = Menu(menu, tearoff=0)
program_menu = Menu(menu, tearoff=0)
run_menu= Menu(menu, tearoff=0)

menu.add_cascade(label="File", menu=file_menu)
menu.add_cascade(label="Edit", menu=edit_menu)
menu.add_cascade(label ="View", menu=view_menu)
menu.add_cascade(label="Run",menu=run_menu)
menu.add_cascade(label ="Theme", menu=theme_menu)
menu.add_cascade(label="Programming Languages",menu=program_menu)
menu.add_cascade(label="Other",menu=other_menu)


########
# function to open files
def open_file(event=None):
    global code, file_path
    #code = editor.get(1.0, END)
    open_path = askopenfilename(filetypes=[("", "*")])
    file_path = open_path
    with open(open_path, "r") as file:
        code = file.read()
        editor.delete(1.0, END)
        editor.insert(1.0, code)
app.bind("<Control-o>", open_file)
######################################
# function to save files
def save_file(event=None):
    global code, file_path
    if file_path == '':
        save_path = asksaveasfilename(defaultextension = ".py", filetypes=[("Python File", "*.py")])
        file_path =save_path
    else:
        save_path = file_path
    with open(save_path, "w") as file:
        code = editor.get(2.0, END)
        file.write(code) 
app.bind("<Control-s>", save_file)
#####################################
# function to save files as specific name 
def save_as(event=None):
    global code, file_path
    #code = editor.get(1.0, END)
    save_path = asksaveasfilename(defaultextension = ".py", filetypes=[("Python File", "*.py")])
    file_path = save_path
    with open(save_path, "w") as file:
        code = editor.get(1.0, END)
        file.write(code) 
app.bind("<Control-S>", save_as)
########

def monkai():
    editor.config(fg="#F8F8F2",bg="#272822")
    output_window.config(fg="#F8F8F2",bg="#272822")
    
def light():
    editor.config(fg="black",bg="white")
    output_window.config(fg="black",bg="white")
def dark():
    editor.config(fg="white",bg="black")
    output_window.config(fg="white",bg="black")
    
theme_menu.add_command(label="Monkai(default)",command=monkai)
theme_menu.add_command(label="Light",command=light)
theme_menu.add_command(label="Dark",command=dark)
########
# function to close IDE window
def close(event=None):
    showwarning("Exit","Make sure you saved your work!")
    app.destroy()
app.bind("<Control-q>", close)
# define function to cut 
# the selected text

########

def running(event=None):
    global code    
    code = editor.get(1.0, END)
    exec(code)
    showinfo("check terminal","Python file Ran in the terminal")
app.bind("<Control-r>", running)

def run(event):
    command = output_window.get('1.0', 'end').split('\n')[-2]
    if command == 'exit':
        exit()
    output_window.insert('end', f'\n{subprocess.getoutput(command)}')


output_window = ScrolledText(app, height=5)
output_window.pack(fill=BOTH, expand=1)
output_window.insert(tk.END, "Lunar Code Terminal\n")
output_window.config(fg="#F8F8F2",bg="#272822")
output_window.bind('<Return>', run)

#########
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_command(label="Save as",command=save_as)
file_menu.add_command(label="Quit",command=close)
#########
def about():
    import About
def help():
    import Help
other_menu.add_command(label="About",command=about)
other_menu.add_command(label="Help",command=help)
run_menu.add_command(label="run",command=run)

#########

app.mainloop()