
from tkinter import*  
base = Tk()  
base.geometry('500x500')  
base.title("Registration Form")  

def save_info():
    with open('users.txt', 'a') as file:
        file.write(f"Username: {entry_1.get()}\n")
        file.write(f"E mail: {entry_02.get()}\n")
        file.write(f"contact: {entry_03.get()}\n")
        file.write(f"Adress: {entry_04.get()}\n")
        file.write("-" * 40 + "\n")
  
labl_0 = Label(base, text="Registration form",width=20,font=('bold'))  
labl_0.place(x=90,y=53)  
  
  
labl_1 = Label(base, text="FullName",width=20)  
labl_1.place(x=80,y=130)  
  
entry_1 = Entry(base)  
entry_1.place(x=240,y=130)  
  
labl_2 = Label(base, text="Email",width=20)  
labl_2.place(x=68,y=180)  
  
entry_02 = Entry(base)  
entry_02.place(x=240,y=180)  
  
labl_3 = Label(base, text="Contact no",width=20)  
labl_3.place(x=70,y=230) 
entry_03 = Entry(base)  
entry_03.place(x=240,y=230) 
 
  
labl_4 = Label(base, text="Adress",width=20)  
labl_4.place(x=70,y=280)  
  
  
entry_04 = Entry(base)  
entry_04.place(x=240,y=280)  
  
Button(base, text='Submit',width=20,bg='brown',fg='white',command=save_info).place(x=180,y=380)  
# it will be used for displaying the registration form onto the window  
base.mainloop()  
print("Registration form is created seccussfully...")  

