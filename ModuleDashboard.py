import pandas as pd
import re
import tkinter as tk #for GUI

# Function that takes number grade and converts it to a letter grade
def convertToLetter(number):
	if number <= 50:
		letter = 'F'
	elif number <= 64:
		letter = 'P'
	elif number <= 74:
		letter = 'C'
	elif number <= 84:
		letter = 'D'
	else: letter = 'HD'
	
	return letter
	
def saveinfo():
	valor1 = sub_code.get()
	valor2 = sub_name_box.get("1.0", 'end-1c')
	valor3 = sub_grade.get()
	valor4 = convertToLetter(int(valor3))
	df.loc[len(df.index)] = [valor1.upper(), valor2.title(), valor3, valor4]
	# Remove the first row (empty)
	#df = df.iloc[1:, :]
	df.to_csv("pandas.csv", sep=',', index=False)
	
# Function that checks for a regex match -- Currently not in use
def checkRegex(user_input):
	pattern = r'^[A-Z]{4}\d{3}$'
	if not re.match(pattern, user_input):
		return False
	else: return True

def opennewwindow():	
	global sub_code, sub_name, sub_grade, sub_name_box
	# tkinter window details
	window = tk.Tk()
	window.geometry("600x300")
	window.title("Module Dashboard")
	sub_name_box = tk.Text(window, height=1, width=50)
	sub_name_box.grid(column=1, row=4)
	
	b1 = tk.Button(window, text="Add", command=lambda: [saveinfo(), clearboxes()]).grid(column=3, row=2)
	b2 = tk.Button(window, text="Show database", command=displaypopup).grid(column=3, row=3)
	b3 = tk.Button(window, text="Search", command=search).grid(column=2, row=2)
	tk.Label(window, text="Enter the subject code:").grid(column=1, row=1)
	sub_code = tk.Entry(window) # on row 2
	
	tk.Label(window, text="Subject Name:").grid(column=1, row=3)
	
	#sub_name = tk.Entry(window) # on row 4
	tk.Label(window, text="Enter the grade achieved:").grid(column=1, row=5)
	sub_grade = tk.Entry(window)
	
	sub_code.grid(column=1, row=2)
	#sub_name.grid(column=1, row=4)
	sub_grade.grid(column=1, row=6)
	window.mainloop()

def clearboxes():
	# Clear all entry boxes
	sub_code.delete(0, 'end')
	sub_name_box.delete('1.0', 'end')
	sub_grade.delete(0, 'end')
	sub_code.focus()
	
def displaypopup():
	
	window2 = tk.Toplevel()
	window2.geometry('1000x300')
	window2.title("Display Database")
	
	text_box = tk.Text(window2, height=10, pady=4)
	wam_box = tk.Text(window2, height=2, pady=4)
	df2 = pd.read_csv("pandas.csv")
	df2 = df2.iloc[1:, :]
	text_box.insert(tk.END, df2.to_string())
	wam_box.insert(tk.END, "Current WAM: {}".format(df2["Subject Grade"].sum()/len(df2)))
	text_box.pack()
	wam_box.pack()
	
def search():
	to_search = sub_code.get()
	a = subject_db.loc[subject_db['Subject Code']==to_search.upper()]
	b = a.iloc[0]["Subject Name"]
	sub_name_box.insert(tk.END, b)

	
# ------------ MAIN ---------------

#df = pd.DataFrame({"Subject Code": [None], "Subject Name": [None], "Subject Grade": 0, "Letter": [None]})
pd.read_csv("pandas.csv")
subject_db = pd.read_csv("subjects_database.csv")
opennewwindow()

#print(df)
#total = df["Grade"].sum()
#print(total)

