from tkinter import *
from random import randint
from random import choice

window = Tk()
window.title('Strong Password Generator')
window.geometry("500x300")
window.configure(bg="#B5EAEA")
#icon = PhotoImage(file = "cool-background1.png")
#window.configure(background=icon)


# Generate Random Strong Password
def generate_password():
	# Clear Our Entry Box
	pwd_entry.delete(0, END)

	# Get PW Length and convert to integer
	pwd_length = int(length.get())

	# create a variable to hold our password
	my_password = ''

	# Loop through password length
	for x in range(pwd_length):
		out=[]
		sele_1=chr(randint(33,39))
		sele_2=chr(randint(48,91))
		sele_3=chr(randint(94,126))
		out.append(sele_1)
		out.append(sele_2)
		out.append(sele_3)
		my_password+=(choice(out))


	# Output password to the screen
	pwd_entry.insert(0, my_password)


# Copy to clipboard
def copy():
	# Clear the clipboard
	window.clipboard_clear()
	# Copy to clipboard
	window.clipboard_append(pwd_entry.get())

# Label Frame
lf = LabelFrame(window, text="How Many Characters?",bg="#77ACF1")
lf.pack(pady=20)
# Create Entry Box To Designate Number of Characters
length= Entry(lf, font=("Helvetica", 24))
length.pack(pady=20, padx=20)

# Create Entry Box For Our Returned Password
pwd_entry = Entry(window, text='', font=("Helvetica", 24), bd=0, bg="#B5EAEA")
pwd_entry.pack(pady=20)

# Create a frame for our Buttons
my_frame = Frame(window,bg="#B5EAEA")
my_frame.pack(pady=20)

# Create our Buttons
my_button = Button(my_frame, text="Get Password", command=generate_password)
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text="Copy To Clipboad", command=copy)
clip_button.grid(row=0, column=1, padx=10)


window.mainloop()
