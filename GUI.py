# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 21:34:46 2018

@author: surafel
"""

import Tkinter as tk
from Tkinter import *
import serial

#Myserial = serial.Serial('/dev/ttyACM3',9600)
window = tk.Tk()
window.title("Thesis Project")
window.geometry("1280x680")

####-------Go button function----------####

def go_button(*args):
 #   print (selected_height.get())
    if selected_height.get() == "1 meter":
        print ("Printing One meter")
 #       Myserial.write('A')
    elif selected_height.get() == "2 meter":
        print ("Printing Two meter")
        #Myserial.write('B')
    elif selected_height.get() == "3 meter":
        print ("Printing Three meter")
        #Myserial.write('C')

#####------Emergency button function-----#######

def emergency_button():
    print ("You have pressed the emergency button")
  #  Myserial.write('E')
       
##########--------------FRAME------------------##############

TopFrame = Frame(window, width=720, height=200)
TopFrame.pack(side=TOP)

LeftFrame = Frame(window, width=720, height=400, bd=8, relief='ridge')
LeftFrame.pack(side=LEFT)

BottomFrame = Frame(window, width=480, height=400)
BottomFrame.pack(side=BOTTOM)

##########-------------Text_Label---------########################
school = Label(TopFrame,text="\n ADDIS ABABA SCIENCE AND TECHNOLOGY UNIVERSITY\n \n DEPARTMENT OF MECHANICAL ENGINEERING \n \n \n DESIGN AND FABRICATION OF WALL PLASTERING MACHINE\n ", font=("arial",30,"bold"))
school.grid(row=0,column=0)

Input_label = Label(LeftFrame,text="Select the Height: ", font=("arial",20,"bold"))
Input_label.grid(row=0,column=1)

##########-------------Dropdown_Menu---------########################
Height_options = ["","1 meter","2 meter","3 meter"]
selected_height = StringVar()
selected_height.set(Height_options[0])
Height_dropdown = OptionMenu(LeftFrame, selected_height, *Height_options)
Height_dropdown.grid(row=0,column=2)

##########-------------Button---------########################
Emergencybutton = Button(BottomFrame, text="EMERGENCY STOP",padx=4, pady=4,fg="red",bg="gray",font=("arial",25,"bold"), command=emergency_button)
Emergencybutton.grid(row=1,column=1)

Gobutton = Button(LeftFrame, text="Go",padx=2, pady=2,font=("arial",15,"bold"), command = go_button)
Gobutton.grid(row=0,column=3)

window.mainloop()