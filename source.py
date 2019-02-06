"""
Written by Ali Zahid Raja
6th Feb 2019


This converter simply reads and writes the data in a new file, it makes 100% working files if the extensions are of the
same type, attached are some files which were converted

The exe files are also provided if someone wants to use the program on a system which doesnot have python or tkinter
just get the whole folder
"""
from tkinter import *
from tkinter import filedialog

MainWindow = Tk() #Making a new window
MainWindow.title("Any2Any Convertor") #Putting the title
MainWindow.geometry("700x350+400+500") #Defining the size of window and place on your screen

heading = Label(MainWindow, text="Any2Any Convertor", font=("arial", 20), fg="steelblue").pack() #Header
label1 = Label(MainWindow, text="Select the File you want to Convert:", font=("arial", 13), fg="black").place(x=10, y=70) #Label to show from where to select file
label2 = Label(MainWindow, text="Enter the Output Extension(e.g: txt):", font=("arial", 13), fg="black").place(x=10, y=150) #Lable to show where to input extension


def browsefunc(): #Finding the file
    labelDone = Label(MainWindow, text="                            ", font=("arial", 20), fg="black").place(x=250, y=250)  #Clearing the done label
    global filename
    filename = filedialog.askopenfilename() #Asking for user to choose a file
    label3 = Label(MainWindow, text="    "*len(filename), font=("arial", 20), fg="black").place(x=290, y=70) #clearing the button
    browsebutton = Button(MainWindow, text=filename, font=("arial", 13), fg="black", height=1,command=browsefunc).place(x=290, y=70) #showing the name of the file on the button


browsebutton = Button(MainWindow, text="Browse", font=("arial", 13), fg="black", height=1, command=browsefunc).place(x=290, y=70) #The browse button
Query = StringVar() #Declaring a variable to get extension
Input_box = Entry(MainWindow, textvariable=Query, width=20, bg="white").place(x=290, y=150) #Input box for extension

def Work(): #Conversion of file
    in_file = open(filename, "rb")  # opening for [r]eading as [b]inary
    data = in_file.read()  # if you only wanted to read 512 bytes, do .read(512)
    in_file.close()
    newname = filename[:filename.rfind(".")+1]
    newname = newname+Query.get()
    out_file = open(newname, "wb")  # open for [w]riting as [b]inary
    out_file.write(data)
    out_file.close()
    labelDone = Label(MainWindow,text="Conversion Done!", font=("arial", 20), fg="black").place(x=250, y=250)


button = Button(MainWindow, text="Convert", width=30, height=2, bg="grey", command=Work).place(x=250, y=200) #Convert button

MainWindow.mainloop() #Main loop for tkinter window to open

