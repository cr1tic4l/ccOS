#Simple login system in python with a GUI built from tkinter
# 
#   Created by Robert Zeelie         26\09\19
#
#the user names and passwords can be found in the dictionary called users in the login function

from tkinter import *
from PIL import Image, ImageTk

#--------------------------------------------------------------------------------------------------------------
#create the window and add size and title to it
window = Tk()
window.geometry("800x500+300+100")
#set size permanently   #or you can use window.resizabld(false, false)
window.minsize(800, 500)
window.maxsize(800, 500)
window.title(" RAZ Tech")
window.iconbitmap("C:\Python\Python Projects\TKINTER/login Sys/lock_v2W_icon.ico")

#---------------------------------------------------------------------------------------------------------------
#first get the picture then save it in pic and set as background
image = Image.open("C:\Python\Python Projects\TKINTER/login Sys/blueBG.jpg")
pic = ImageTk.PhotoImage(image)
#build pic and add it to window
label0 = Label(image = pic)
label0.pack(fill = BOTH, expand = 'yes')

#-------------------------------------------------------------------------------------------------------------
#functions for the buttons to perform
def login():
    users = {'admin': '1000', 'dev': '2000', 'client': '3000', 'employee': '4000'}
    username = userName.get()
    Pass = password.get()
    if username in users :
        if (users[username] == Pass):
            label4 = Label(window, text = ("Welcome " + username),width = 25, font = ("arial", 40, "bold"))
            label4.place(x = 0, y = 400)
            
        else:
            label4 = Label(window, text = ("Incorrect Password for " + username),width = 25, font = ("arial", 40, "bold"))
            label4.place(x = 0, y = 400)

    else:
        label4 = Label(window, text = (username + " does not exist"),width = 25, font = ("arial", 40, "bold"))
        label4.place(x = 0, y = 400)

#----------------------------------------------------------------------------------------------------------------
#first lable
label1 = Label(window, text = " Login System ", fg = "black", font = ("new times roman", 40, "bold"))
label1.place(x = 200, y = 15)

label2 = Label(window, text = "User Name :", font = ("arial", 16, "bold"))
label2.place(x = 110, y = 150)

userName = StringVar()
textBox1 = Entry(window, textvar = userName, width = 30, font = ("arial", 16, "bold"))
textBox1.place(x = 290, y = 150)

label3 = Label(window, text = "Password :", font = ("arial", 16, "bold"))
label3.place(x = 116, y = 250)

password = StringVar()
textBox2 = Entry(window, textvar = password, width = 30, font = ("arial", 16, "bold"))
textBox2.place(x = 290, y = 250)

button1 = Button(window, text = "   Login   ", fg = "black", bg = "white", relief = "raised", font = ("arial", 16, "bold"), command = login)
button1.place(x = 335, y = 340)

#display window
window.mainloop()
