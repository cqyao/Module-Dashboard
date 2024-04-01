import pymongo as pym # for MongoDB
import tkinter as tk # for GUI
from tkinter import *

# -------------                -----------------
myclient = pym.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"] # Add database
mycol = mydb["customers"] # Add collection

# ------------- Create window ------------------
def opennewwindow():
	global sub_code, sub_name, sub_grade
	window = tk.Tk()
	window.geometry("600x300")
	window.title("Module Dashboard")
	
	frame_left = tk.Frame(window)
	frame_left.grid(row=0, column=0)
	
	sub_code = tk.Entry(frame_left)
	sub_name = tk.Entry(frame_left)
	sub_grade = tk.Entry(frame_left)
	submit_btn = tk.Button(frame_left, text="Submit", command=submit)

	
	sub_code.grid(row=0, column=0)
	sub_name.grid(row=1, column=0)
	sub_grade.grid(row=2, column=0)
	submit_btn.grid(row=5, column=1)
	
	# Pack all widgets below
	
	# End pack 
	
	window.mainloop()

# ------------- Submit the form ----------------
def submit():
	if mycol.count_documents({ "Subject code": sub_code.get() }, limit = 1) == 0:
		mydict = { "Subject code": sub_code.get(), "Subject name": sub_name.get(), "Grade": sub_grade.get()}
		x = mycol.insert_one(mydict)
	else: print("Subject already exists!")

opennewwindow()