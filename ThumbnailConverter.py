from PIL import Image
import tkinter
from tkinter import messagebox
from tkinter import filedialog



def import_image():
	global img
	import_file_path = filedialog.askopenfilename()
	img = Image.open(import_file_path)



def convert_to_thumbnail():
	global img
	export_thumbnail = filedialog.asksaveasfilename(defaultextension='.png')
	img.thumbnail((400, 400))
	img.save(export_thumbnail)




GUI = tkinter.Tk()

canvas1 = tkinter.Canvas(GUI, bg = "hotpink", height=400, width=400)
canvas1.pack()
label1 = tkinter.Label(GUI, text='Convert image to thumbnail', bg='cyan')
label1.config(font=('helvetica', 20))
canvas1.create_window(170, 60, window=label1)

browseButton_image = tkinter.Button(text="    Select image    ", command=import_image, bg='red', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButton_image)

saveAsButton_thumbnail = tkinter.Button(text="Generate thumbnail", command=convert_to_thumbnail, bg='red', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButton_thumbnail)

GUI.mainloop()