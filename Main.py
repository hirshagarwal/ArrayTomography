from Crop import Crop
import tkinter as tk
import tkinter.filedialog as tkf

def chooseInputFile():
	fn = tkf.askopenfilename()
	print(fn)

display = tk.Tk()
chooseInput = tk.Button(display, text="Choose Input File", command = chooseInputFile)

chooseInput.place(x = 0, y = 0)
display.mainloop()

