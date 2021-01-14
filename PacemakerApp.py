# Importing all the required modules for the program

import globals
import os
import re
import kivy
import struct
import serial
from kivy.uix.popup import Popup
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import (ScreenManager, Screen, NoTransition, SlideTransition, CardTransition,
                                    SwapTransition, FadeTransition, WipeTransition, FallOutTransition, RiseInTransition)
from kivy.lang import Builder
from kivy.garden.graph import MeshLinePlot
from kivy.uix.scrollview import ScrollView
from kivy.properties import NumericProperty,ReferenceListProperty,ObjectProperty
import json

# Choosing the proper frontend to run
kv = Builder.load_file("PacemakerApp.kv")

# Class which controls the login menu
class LoginMenuWindow(Screen):

    # Constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # Function checks if the username and password inputted is correct with the User.txt file...
    #...And outputs the corresponding prompt
    # Activates when the Login button is clicked
    def check_user(self):
        user1 = self.ids.userText
        pass1 = self.ids.passText
        errorPrompt = self.ids.infoText

        username = user1.text
        password = pass1.text

        valid = False
        with open("users.txt", "r") as f:
            for line in f:
                credentials = line.strip().split(" ")
                if username == credentials[0] and password == credentials[1]:
                    valid = True
                    break

        if valid == False:
            errorPrompt.text = '[color=#FF0000]ERROR: Please Enter a correct username/password.[/color]'
        else:
            globals.User = username
            errorPrompt.text = '[color=#00FF00]User Logged in successfully.[/color]'
            self.clearContents()
            currentMenu.current = "mainMenu"

    # Function which checks if there are 10 users in the users.txt already when...
    #...the register button is clicked
    def register_Call(self):
        numOfLines = 0
        with open("users.txt", "r") as f:
            for line in f:
                numOfLines = numOfLines + 1

        if numOfLines > 9:
            errorPrompt = self.ids.infoText
            errorPrompt.text = '[color=#FF0000]ERROR: There are already 10 registered users.[/color]'
        else:
            self.clearContents()
            currentMenu.current = "registerMenu"

    # Function that clears the contents of the infotext, username and password input boxes
    def clearContents(self):
        self.ids.userText.text = ''
        self.ids.passText.text = ''
        self.ids.infoText.text = ''

# Class which controls the Register Menu
class RegisterMenuWindow(Screen):

    # Constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # Function which registers the user into the user.txt file if there are not any naming errors
    # Activates when the Register button is clicked
    def check_user(self):
        errorPrompt = self.ids.infoText
        user1 = self.ids.userText
        pass1 = self.ids.passText
        username = user1.text
        password = pass1.text
        valid = True

        if len(username) == 0 or len(password) == 0 or username.isspace() == True or password.isspace() == True:
            errorPrompt.text = '[color=#FF0000]ERROR: Please Enter a valid username/password.[/color]'
        else:

            with open("users.txt", "r") as f:
                for line in f:
                    credentials = line.strip().split(" ")
                    if username.lower() == credentials[0].lower():
                        valid = False
                        break

            if valid == False:

                errorPrompt.text = '[color=#FF0000]ERROR: That username is already in use.[/color]'
            else:
		        
                f1 = open("users.txt", "a")
                f1.write("\n"+username+" "+password)
                globals.User = username
                f1.close()
                errorPrompt.text  = '[color=#00FF00]User Registered successfully.[/color]'
                self.clearContents()
                self.createStates()
                currentMenu.current = "mainMenu"

    # Function that returns the user into the login menu when...
    #...the login button is clicked
    def login_Call(self):
        self.clearContents()
        currentMenu.current = "loginMenu"

    # Function that clears the contents of the infotext, username and password input boxes
    def clearContents(self):
        self.ids.userText.text = ''
        self.ids.passText.text = ''
        self.ids.infoText.text = ''

    def createStates(self):
        flag = False
        if os.stat("AOO.txt").st_size == 0:
            flag = True
        f1 = open("AOO.txt", "a")
        if flag == False:
            f1.write("\n")
        f1.write(globals.User+":")
        f1.write("\n"+ "60")
        f1.write("\n"+ "120")
        f1.write("\n"+ "3.75")
        f1.write("\n"+ "0.4")
        f1.close()

        flag = False
        if os.stat("VOO.txt").st_size == 0:
            flag = True    
        f2 = open("VOO.txt", "a")
        if flag == False:
            f2.write("\n")
        f2.write(globals.User+":")
        f2.write("\n"+ "60")
        f2.write("\n"+ "120")
        f2.write("\n"+ "3.75")
        f2.write("\n"+ "0.4")
        f2.close()

        flag = False
        if os.stat("AAI.txt").st_size == 0:
            flag = True    
        f3 = open("AAI.txt", "a")
        if flag == False:
            f3.write("\n")
        f3.write(globals.User+":")
        f3.write("\n"+ "60")
        f3.write("\n"+ "120")
        f3.write("\n"+ "3.75")
        f3.write("\n"+ "0.4")
        f3.write("\n"+ "0.75")
        f3.write("\n"+ "250")
        f3.write("\n"+ "250")
        f3.write("\n"+ "0")
        f3.close()

        flag = False
        if os.stat("VVI.txt").st_size == 0:
            flag = True    
        f4 = open("VVI.txt", "a")
        if flag == False:
            f4.write("\n")
        f4.write(globals.User+":")
        f4.write("\n"+ "60")
        f4.write("\n"+ "120")
        f4.write("\n"+ "3.75")
        f4.write("\n"+ "0.4")
        f4.write("\n"+ "2.5")
        f4.write("\n"+ "320")
        f4.write("\n"+ "0")
        f4.close()

        flag = False
        if os.stat("DOO.txt").st_size == 0:
            flag = True
        f5 = open("DOO.txt", "a")
        if flag == False:
            f5.write("\n")
        f5.write(globals.User+":")
        f5.write("\n"+ "60")
        f5.write("\n"+ "120")
        f5.write("\n"+ "150")
        f5.write("\n"+ "3.75")
        f5.write("\n"+ "3.75")
        f5.write("\n"+ "0.4")
        f5.write("\n"+ "0.4")
        f5.close()

        flag = False
        if os.stat("AOOR.txt").st_size == 0:
            flag = True
        f6 = open("AOOR.txt", "a")
        if flag == False:
            f6.write("\n")
        f6.write(globals.User+":")
        f6.write("\n"+ "60")
        f6.write("\n"+ "120")
        f6.write("\n"+ "120")
        f6.write("\n"+ "3.75")
        f6.write("\n"+ "0.4")
        f6.write("\n"+ "Med")
        f6.write("\n"+ "30")
        f6.write("\n"+ "8")
        f6.write("\n"+ "5")
        f6.close()

        flag = False
        if os.stat("VOOR.txt").st_size == 0:
            flag = True
        f7 = open("VOOR.txt", "a")
        if flag == False:
            f7.write("\n")
        f7.write(globals.User+":")
        f7.write("\n"+ "60")
        f7.write("\n"+ "120")
        f7.write("\n"+ "120")
        f7.write("\n"+ "3.75")
        f7.write("\n"+ "0.4")
        f7.write("\n"+ "Med")
        f7.write("\n"+ "30")
        f7.write("\n"+ "8")
        f7.write("\n"+ "5")
        f7.close()

        flag = False
        if os.stat("AAIR.txt").st_size == 0:
            flag = True
        f8 = open("AAIR.txt", "a")
        if flag == False:
            f8.write("\n")
        f8.write(globals.User+":")
        f8.write("\n"+ "60")
        f8.write("\n"+ "120")
        f8.write("\n"+ "120")
        f8.write("\n"+ "3.75")
        f8.write("\n"+ "0.4")
        f8.write("\n"+ "0.75")
        f8.write("\n"+ "250")
        f8.write("\n"+ "250")
        f8.write("\n"+ "0")
        f8.write("\n"+ "Med")
        f8.write("\n"+ "30")
        f8.write("\n"+ "8")
        f8.write("\n"+ "5")
        f8.close()

        flag = False
        if os.stat("VVIR.txt").st_size == 0:
            flag = True
        f9 = open("VVIR.txt", "a")
        if flag == False:
            f9.write("\n")
        f9.write(globals.User+":")
        f9.write("\n"+ "60")
        f9.write("\n"+ "120")
        f9.write("\n"+ "120")
        f9.write("\n"+ "3.75")
        f9.write("\n"+ "0.4")
        f9.write("\n"+ "2.5")
        f9.write("\n"+ "320")
        f9.write("\n"+ "0")
        f9.write("\n"+ "Med")
        f9.write("\n"+ "30")
        f9.write("\n"+ "8")
        f9.write("\n"+ "5")
        f9.close()

        flag = False
        if os.stat("DOOR.txt").st_size == 0:
            flag = True
        f10 = open("DOOR.txt", "a")
        if flag == False:
            f10.write("\n")
        f10.write(globals.User+":")
        f10.write("\n"+ "60")
        f10.write("\n"+ "120")
        f10.write("\n"+ "120")
        f10.write("\n"+ "150")
        f10.write("\n"+ "3.75")
        f10.write("\n"+ "3.75")
        f10.write("\n"+ "0.4")
        f10.write("\n"+ "0.4")
        f10.write("\n"+ "Med")
        f10.write("\n"+ "30")
        f10.write("\n"+ "8")
        f10.write("\n"+ "5")
        f10.close()
        
# Class that controls the Main Menu
class MainMenuWindow(Screen):

    # Constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # Function that runs right before the Main Menu is shown,...
    #...Makes welcome text include username
    def on_pre_enter(self, *args):
        self.ids.welcomeText.text = "                                                      Welcome to the PaceMaker App, User " + globals.User +"."
    
    # Function that runs right before the Main Menu is shown,...
    # ...it checks if a device has already been registerd previously in the device.txt file....
    #...otherwise it saves the current connected USB devices
    def on_enter(self, *args):
        self.serialCheck()

    # Function that returns the user to the login menu when the logout button is pressed
    def logout_Call(self):
        currentMenu.current = "loginMenu"
    
    # Function that makes the Egram graph appear as a popup when the Show Egram button is pressed
    def Egram_Call(self):
        show = EgramWindow()
        global popupWindow
        popupWindow = Popup(title="Egram Window (Atrial on left (red), Ventricular on right (blue))", content=show,size_hint=(None,None), size=(750,500))
        popupWindow.open()

    # Function that shows the user to the AOO menu when the AOO button is pressed
    def AOO_Call(self):
        currentMenu.current = "AOOMenu"

    # Function that shows the user to the VOO menu when the VOO button is pressed
    def VOO_Call(self):
        currentMenu.current = "VOOMenu"
    
    # Function that shows the user to the AAI menu when the AAI button is pressed
    def AAI_Call(self):
        currentMenu.current = "AAIMenu"

    # Function that shows the user to the VVI menu when the VVI button is pressed
    def VVI_Call(self):
        currentMenu.current = "VVIMenu"

    # Function that shows the user to the DOO menu when the DOO button is pressed
    def DOO_Call(self):
        currentMenu.current = "DOOMenu"

    # Function that shows the user to the AOOR menu when the AOOR button is pressed
    def AOOR_Call(self):
        currentMenu.current = "AOORMenu"

    # Function that shows the user to the VOOR menu when the VOOR button is pressed
    def VOOR_Call(self):
        currentMenu.current = "VOORMenu"

    # Function that shows the user to the AAIR menu when the AAIR button is pressed
    def AAIR_Call(self):
        currentMenu.current = "AAIRMenu"

    # Function that shows the user to the VVIR menu when the VVIR button is pressed
    def VVIR_Call(self):
        currentMenu.current = "VVIRMenu"

    # Function that shows the user to the DOOR menu when the DOOR button is pressed
    def DOOR_Call(self):
        currentMenu.current = "DOORMenu"

    # Funtions which read the respective state parameters into the serial stream for communication with the pacemaker
    def serialAOO_Call(self):
        self.serialCheck()
        if (globals.deviceConnected):
            globals.paceLoc = 0
            globals.sensing = 0
            globals.rateAdap = 0
            counter = 0
            flag = False
            with open("AOO.txt", "r") as f:
                for line in f:
                    if flag == True:
                        if counter == 0:
                                globals.LRL = line.replace("\n","")
                        if counter == 1:
                                globals.URL = line.replace("\n","")
                        if counter == 2:
                                globals.atrAmp = line.replace("\n","")
                        if counter == 3:
                                globals.ATRpulseWidth = line.replace("\n","")
                                break
                        counter = counter + 1

                    if globals.User == line.strip().replace(":",""):
                        flag = True
        
            self.serialSend()

    def serialVOO_Call(self):
        self.serialCheck()
        if (globals.deviceConnected):
            globals.paceLoc = 1
            globals.sensing = 0
            globals.rateAdap = 0
            counter = 0
            flag = False
            with open("VOO.txt", "r") as f:
                for line in f:
                    if flag == True:
                        if counter == 0:
                                globals.LRL = line.replace("\n","")
                        if counter == 1:
                                globals.URL = line.replace("\n","")
                        if counter == 2:
                                globals.ventAmp = line.replace("\n","")
                        if counter == 3:
                                globals.VENTpulseWidth = line.replace("\n","")
                                break
                        counter = counter + 1

                    if globals.User == line.strip().replace(":",""):
                        flag = True

            self.serialSend()

    def serialAAI_Call(self):
        self.serialCheck()
        if (globals.deviceConnected):
            globals.paceLoc = 0
            globals.sensing = 1
            globals.rateAdap = 0
            counter = 0
            flag = False
            with open("AAI.txt", "r") as f:
                for line in f:
                    if flag == True:
                        if counter == 0:
                            globals.LRL = line.replace("\n","")
                        if counter == 1:
                            globals.URL = line.replace("\n","")
                        if counter == 2:
                            globals.atrAmp = line.replace("\n","")
                        if counter == 3:
                            globals.ATRpulseWidth = line.replace("\n","")
                        if counter == 4:
                            globals.atrsensitivity = line.replace("\n","")
                        if counter == 5:
                            globals.ARP = line.replace("\n","")
                        if counter == 6:
                            globals.PVARP = line.replace("\n","")
                        if counter == 7:
                            globals.rateSmoothing = line.replace("\n","")
                            break
                        counter = counter + 1

                    if globals.User == line.strip().replace(":",""):
                        flag = True

            self.serialSend()

    def serialVVI_Call(self):  
        self.serialCheck()
        if (globals.deviceConnected):
            globals.paceLoc = 1
            globals.sensing = 1
            globals.rateAdap = 0
            counter = 0
            flag = False
            with open("VVI.txt", "r") as f:
                for line in f:
                    if flag == True:
                        if counter == 0:
                            globals.LRL = line.replace("\n","")
                        if counter == 1:
                            globals.URL = line.replace("\n","")
                        if counter == 2:
                            globals.ventAmp = line.replace("\n","")
                        if counter == 3:
                            globals.VENTpulseWidth = line.replace("\n","")
                        if counter == 4:
                            globals.VENTsensitivity = line.replace("\n","")
                        if counter == 5:
                            globals.VRP = line.replace("\n","")
                        if counter == 6:
                            globals.rateSmoothing = line.replace("\n","")
                            break
                        counter = counter + 1

                    if globals.User == line.strip().replace(":",""):
                        flag = True

            self.serialSend()


    def serialDOO_Call(self):  
        self.serialCheck()
        if (globals.deviceConnected):
            globals.paceLoc = 2
            globals.sensing = 0
            globals.rateAdap = 0
            counter = 0
            flag = False
            with open("DOO.txt", "r") as f:
                for line in f:
                    if flag == True:
                        if counter == 0:
                                globals.LRL = line.replace("\n","")
                        if counter == 1:
                                globals.URL = line.replace("\n","")
                        if counter == 2:
                                globals.AV_delay = line.replace("\n","")
                        if counter == 3:
                                globals.atrAmp = line.replace("\n","")
                        if counter == 4:
                                globals.ventAmp = line.replace("\n","")
                        if counter == 5:
                                globals.ATRpulseWidth = line.replace("\n","")
                        if counter == 6:
                                globals.VENTpulseWidth = line.replace("\n","")
                                break
                        counter = counter + 1

                    if globals.User == line.strip().replace(":",""):
                        flag = True

            self.serialSend()

    def serialAOOR_Call(self):  
        self.serialCheck()
        if (globals.deviceConnected):
            globals.paceLoc = 0
            globals.sensing = 0
            globals.rateAdap = 1
            counter = 0
            flag = False
            with open("AOOR.txt", "r") as f:
                for line in f:
                    if flag == True:
                        if counter == 0:
                                globals.LRL = line.replace("\n","")
                        if counter == 1:
                                globals.URL = line.replace("\n","")
                        if counter == 2:
                                globals.MSR = line.replace("\n","")
                        if counter == 3:
                                globals.atrAmp = line.replace("\n","")
                        if counter == 4:
                                globals.ATRpulseWidth = line.replace("\n","")
                        if counter == 5:
                                globals.ATT = line.replace("\n","")
                        if counter == 6:
                                globals.reactTime = line.replace("\n","")
                        if counter == 7:
                                globals.respFactor = line.replace("\n","")
                        if counter == 8:
                                globals.recovTime = line.replace("\n","")
                                break
                        counter = counter + 1

                    if globals.User == line.strip().replace(":",""):
                        flag = True
            
            self.serialSend()

    def serialVOOR_Call(self):  
        self.serialCheck()
        if (globals.deviceConnected):
            globals.paceLoc = 1
            globals.sensing = 0
            globals.rateAdap = 1
            counter = 0
            flag = False
            with open("VOOR.txt", "r") as f:
                for line in f:
                    if flag == True:
                        if counter == 0:
                                globals.LRL = line.replace("\n","")
                        if counter == 1:
                                globals.URL = line.replace("\n","")
                        if counter == 2:
                                globals.MSR = line.replace("\n","")
                        if counter == 3:
                                globals.ventAmp = line.replace("\n","")
                        if counter == 4:
                                globals.VENTpulseWidth = line.replace("\n","")
                        if counter == 5:
                                globals.ATT = line.replace("\n","")
                        if counter == 6:
                                globals.reactTime = line.replace("\n","")
                        if counter == 7:
                                globals.respFactor = line.replace("\n","")
                        if counter == 8:
                                globals.recovTime = line.replace("\n","")
                                break
                        counter = counter + 1

                    if globals.User == line.strip().replace(":",""):
                        flag = True
                
            self.serialSend()

    def serialAAIR_Call(self):  
        self.serialCheck()
        if (globals.deviceConnected):
            globals.paceLoc = 0
            globals.sensing = 1
            globals.rateAdap = 1
            counter = 0
            flag = False
            with open("AAIR.txt", "r") as f:
                for line in f:
                    if flag == True:
                        if counter == 0:
                            globals.LRL = line.replace("\n","")
                        if counter == 1:
                            globals.URL = line.replace("\n","")
                        if counter == 2:
                            globals.MSR = line.replace("\n","")
                        if counter == 3:
                            globals.atrAmp = line.replace("\n","")
                        if counter == 4:
                            globals.ATRpulseWidth = line.replace("\n","")
                        if counter == 5:
                            globals.atrsensitivity = line.replace("\n","")
                        if counter == 6:
                            globals.ARP = line.replace("\n","")
                        if counter == 7:
                            globals.PVARP = line.replace("\n","")
                        if counter == 8:
                            globals.rateSmoothing = line.replace("\n","")
                        if counter == 9:
                            globals.ATT = line.replace("\n","")
                        if counter == 10:
                            globals.reactTime = line.replace("\n","")
                        if counter == 11:
                            globals.respFactor = line.replace("\n","")
                        if counter == 12:
                            globals.recovTime = line.replace("\n","")
                            break
                        counter = counter + 1

                    if globals.User == line.strip().replace(":",""):
                        flag = True

            self.serialSend()

    def serialVVIR_Call(self):  
        self.serialCheck()
        if (globals.deviceConnected):
            globals.paceLoc = 1
            globals.sensing = 1
            globals.rateAdap = 1
            counter = 0
            flag = False
            with open("VVIR.txt", "r") as f:
                for line in f:
                    if flag == True:
                        if counter == 0:
                            globals.LRL = line.replace("\n","")
                        if counter == 1:
                            globals.URL = line.replace("\n","")
                        if counter == 2:
                            globals.MSR = line.replace("\n","")
                        if counter == 3:
                            globals.ventAmp = line.replace("\n","")
                        if counter == 4:
                            globals.VENTpulseWidth = line.replace("\n","")
                        if counter == 5:
                            globals.VENTsensitivity = line.replace("\n","")
                        if counter == 6:
                            globals.VRP = line.replace("\n","")
                        if counter == 7:
                            globals.rateSmoothing = line.replace("\n","")
                        if counter == 8:
                            globals.ATT = line.replace("\n","")
                        if counter == 9:
                            globals.reactTime = line.replace("\n","")
                        if counter == 10:
                            globals.respFactor = line.replace("\n","")
                        if counter == 11:
                            globals.recovTime = line.replace("\n","")
                            break
                        counter = counter + 1

                    if globals.User == line.strip().replace(":",""):
                        flag = True

            self.serialSend()

    def serialDOOR_Call(self):  
        self.serialCheck()
        if (globals.deviceConnected):
            globals.paceLoc = 2
            globals.sensing = 0
            globals.rateAdap = 1
            counter = 0
            flag = False
            with open("DOOR.txt", "r") as f:
                for line in f:
                    if flag == True:
                        if counter == 0:
                                globals.LRL = line.replace("\n","")
                        if counter == 1:
                                globals.URL = line.replace("\n","")
                        if counter == 2:
                                globals.MSR = line.replace("\n","")
                        if counter == 3:
                                globals.AV_delay = line.replace("\n","")
                        if counter == 4:
                                globals.atrAmp = line.replace("\n","")
                        if counter == 5:
                                globals.ventAmp = line.replace("\n","")
                        if counter == 6:
                                globals.ATRpulseWidth = line.replace("\n","")
                        if counter == 7:
                                globals.VENTpulseWidth = line.replace("\n","")
                        if counter == 8:
                                globals.ATT = line.replace("\n","")
                        if counter == 9:
                                globals.reactTime = line.replace("\n","")
                        if counter == 10:
                                globals.respFactor = line.replace("\n","")
                        if counter == 11:
                                globals.recovTime = line.replace("\n","")
                                break
                        counter = counter + 1

                    if globals.User == line.strip().replace(":",""):
                        flag = True
                
            self.serialSend()

    # Function checks if the device is connected by calling the serial stream 
    def serialCheck(self):
        self.serialConnect()
        if(globals.deviceConnected):
            try:
                self.ids.prompt.text = "Device connected!"
                self.ids.SAOO.background_color = (0.3, 0.66, 0.45, 1)
                self.ids.SVOO.background_color = (0.3, 0.66, 0.45, 1)
                self.ids.SAAI.background_color = (0.3, 0.66, 0.45, 1)
                self.ids.SVVI.background_color = (0.3, 0.66, 0.45, 1)
                self.ids.SDOO.background_color = (0.3, 0.66, 0.45, 1)
                self.ids.SAOOR.background_color = (0.3, 0.66, 0.45, 1)
                self.ids.SVOOR.background_color = (0.3, 0.66, 0.45, 1)
                self.ids.SAAIR.background_color = (0.3, 0.66, 0.45, 1)
                self.ids.SVVIR.background_color = (0.3, 0.66, 0.45, 1)
                self.ids.SDOOR.background_color = (0.3, 0.66, 0.45, 1)
            except:
                self.ids.prompt.text = "Device not connected"
        else: 
            
            self.ids.prompt.text = "Device not connected"

    # Function that checks if the device is connected to a com port
    def serialConnect(self):
        notConnected = True
        port = ["COM1","COM2","COM3","COM4","COM5","COM6","COM7","COM8"]
        i = len(port)
        while notConnected:
            i = i - 1
            if (i == -1):
                break
            try:
                globals.serialport = serial.Serial(port=port[i], baudrate=115200,timeout=1)
                notConnected = False
            except:
                notConnected = True
                print(port[i] + " failed")
            if (notConnected == False): 
                globals.deviceConnected = True
                print(port[i] + " connected")
                globals.serialport.flush()
                break
    
    # Function sends the data of the DCM serially to the pacemaker that is connected
    def serialSend(self):
        serialPack = struct.pack('BBffffffffffffffff',0x16,0x55, float(globals.paceLoc), float(globals.sensing), float(globals.LRL), float(globals.URL), float(globals.atrAmp), float(globals.ventAmp), float(globals.ATRpulseWidth), float(globals.VENTpulseWidth), float(globals.ARP), float(globals.VRP), float(globals.rateAdap), float(globals.reactTime), float(globals.respFactor), float(globals.recovTime), float(globals.MSR), float(globals.AV_delay))
        globals.serialport.write(serialPack)
        print(len(serialPack))
        print([0x16,0x55, globals.paceLoc, globals.sensing, globals.LRL, globals.URL, globals.atrAmp, globals.ventAmp, globals.ATRpulseWidth, globals.VENTpulseWidth, globals.ARP, globals.VRP, globals.rateAdap, globals.reactTime, globals.respFactor, globals.recovTime, globals.MSR, globals.AV_delay])


# Class which controls the AOO Menu
class AOOWindow(Screen):
    
    # Constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # Function which gets the controlled parameters of the state from the corrisponding txt file...
    # right before the menu is shown
    def on_pre_enter(self, *args):
        counter = 0
        flag = False
        with open("AOO.txt", "r") as f:
            for line in f:
                if flag == True:
                    if counter == 0:
                            self.ids.LRLText.text = line.replace("\n","")
                    if counter == 1:
                            self.ids.URLText.text = line.replace("\n","")
                    if counter == 2:
                            self.ids.AAText.text = line.replace("\n","")
                    if counter == 3:
                            self.ids.APWText.text = line.replace("\n","")
                            break
                    counter = counter + 1

                if globals.User == line.strip().replace(":",""):
                    flag = True
                    
    # Function that returns user back to the Main Menu when the back button is pressed
    def back_Call(self):
        currentMenu.current = "mainMenu"
        self.ids.infoText.text = ""

    # Function that checks if the controlled parameters are proper values and saves them if they are...
    #...if not, prompts user about error
    # Activates when the 'Save all' button is pressed
    def save_Call(self):
        checker = 0
        errorPrompt = self.ids.infoText

        if self.ids.LRLText.text.isnumeric() and (int(self.ids.LRLText.text) > 29 and int(self.ids.LRLText.text) < 176):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Lower Rate Limit.[/color]'
            
        if self.ids.URLText.text.isnumeric() and (int(self.ids.URLText.text) > 49 and int(self.ids.URLText.text) < 176):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Upper Rate Limit.[/color]'
        
        if checker == 2 and int(self.ids.URLText.text) < (int(self.ids.LRLText.text)):

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Upper Rate Limit.[/color]'
            checker = 0

        if self.isfloat(self.ids.AAText.text) and float(self.ids.AAText.text) > 0 and float(self.ids.AAText.text) <= 5:
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Atrial Amplitude.[/color]'

        if self.isfloat(self.ids.APWText.text) and float(self.ids.APWText.text) >= 0.05 and float(self.ids.APWText.text) <= 1.9:
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Atrial Pulse Width.[/color]'

        if checker == 4:

            counter = 0
            flag = False
            get_all = ""

            with open("AOO.txt",'r') as f:
                get_all=f.readlines()

            with open("AOO.txt",'w') as f:
                for i,line in enumerate(get_all,1):   
                    if globals.User == line.strip().replace(":",""):     
                        f.write(line)
                        counter = i
                        flag = True
                    elif (counter+1) == i and flag == True:
                        f.write(self.ids.LRLText.text)
                    elif (counter+2) == i and flag == True:
                        f.write("\n"+ self.ids.URLText.text)
                    elif (counter+3) == i and flag == True:
                        f.write("\n"+ self.ids.AAText.text)  
                    elif (counter+4) == i and flag == True:
                        f.write("\n"+ self.ids.APWText.text + "\n")   
                    else:
                        f.write(line)

            errorPrompt.text  = '[color=#00FF11]Changes Saved Successfully.[/color]'

    def isfloat(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

# Class which controls the VOO Menu
class VOOWindow(Screen):
    
    # Constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # Function which gets the controlled parameters of the state from the corrisponding txt file...
    # right before the menu is shown
    def on_pre_enter(self, *args):
        counter = 0
        flag = False
        with open("VOO.txt", "r") as f:
            for line in f:
                if flag == True:
                    if counter == 0:
                            self.ids.LRLText.text = line.replace("\n","")
                    if counter == 1:
                            self.ids.URLText.text = line.replace("\n","")
                    if counter == 2:
                            self.ids.VAText.text = line.replace("\n","")
                    if counter == 3:
                            self.ids.VPWText.text = line.replace("\n","")
                            break
                    counter = counter + 1

                if globals.User == line.strip().replace(":",""):
                    flag = True
                    
    # Function that returns user back to the Main Menu when the back button is pressed
    def back_Call(self):
        currentMenu.current = "mainMenu"
        self.ids.infoText.text = ""

    # Function that checks if the controlled parameters are proper values and saves them if they are...
    #...if not, prompts user about error
    # Activates when the 'Save all' button is pressed
    def save_Call(self):
        checker = 0
        errorPrompt = self.ids.infoText

        if self.ids.LRLText.text.isnumeric() and (int(self.ids.LRLText.text) > 29 and int(self.ids.LRLText.text) < 176):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Lower Rate Limit.[/color]'
            
        if self.ids.URLText.text.isnumeric() and (int(self.ids.URLText.text) > 49 and int(self.ids.URLText.text) < 176):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Upper Rate Limit.[/color]'
        
        if checker == 2 and int(self.ids.URLText.text) < (int(self.ids.LRLText.text)):

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Upper Rate Limit.[/color]'
            checker = 0

        if self.isfloat(self.ids.VAText.text) and float(self.ids.VAText.text) > 0 and float(self.ids.VAText.text) <= 5:
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Ventricular Amplitude.[/color]'

        if self.isfloat(self.ids.VPWText.text) and float(self.ids.VPWText.text) >= 0.05 and float(self.ids.VPWText.text) <= 1.9:
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Ventricular Pulse Width.[/color]'

        if checker == 4:

            counter = 0
            flag = False
            get_all = ""

            with open("VOO.txt",'r') as f:
                get_all=f.readlines()

            with open("VOO.txt",'w') as f:
                for i,line in enumerate(get_all,1):   
                    if globals.User == line.strip().replace(":",""):     
                        f.write(line)
                        counter = i
                        flag = True
                    elif (counter+1) == i and flag == True:
                        f.write(self.ids.LRLText.text)
                    elif (counter+2) == i and flag == True:
                        f.write("\n"+ self.ids.URLText.text)
                    elif (counter+3) == i and flag == True:
                        f.write("\n"+ self.ids.VAText.text)  
                    elif (counter+4) == i and flag == True:
                        f.write("\n"+ self.ids.VPWText.text + "\n")   
                    else:
                        f.write(line)

            errorPrompt.text  = '[color=#00FF11]Changes Saved Successfully.[/color]'

    def isfloat(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

# Class which controls the AAI Menu
class AAIWindow(Screen):

    # Constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # Function which gets the controlled parameters of the state from the corrisponding txt file...
    # right before the menu is shown
    def on_pre_enter(self, *args):
        counter = 0
        flag = False
        with open("AAI.txt", "r") as f:
            for line in f:
                if flag == True:
                    if counter == 0:
                        self.ids.LRLText.text = line.replace("\n","")
                    if counter == 1:
                        self.ids.URLText.text = line.replace("\n","")
                    if counter == 2:
                        self.ids.AAText.text = line.replace("\n","")
                    if counter == 3:
                        self.ids.APWText.text = line.replace("\n","")
                    if counter == 4:
                        self.ids.ASText.text = line.replace("\n","")
                    if counter == 5:
                        self.ids.ARPText.text = line.replace("\n","")
                    if counter == 6:
                        self.ids.PVARPText.text = line.replace("\n","")
                    if counter == 7:
                        self.ids.RSText.text = line.replace("\n","")
                        break
                    counter = counter + 1

                if globals.User == line.strip().replace(":",""):
                    flag = True
                    
    # Function that returns user back to the Main Menu when the back button is pressed
    def back_Call(self):
        currentMenu.current = "mainMenu"
        self.ids.infoText.text = ""

    # Function that checks if the controlled parameters are proper values and saves them if they are...
    #...if not, prompts user about error
    # Activates when the 'Save all' button is pressed
    def save_Call(self):
        checker = 0
        errorPrompt = self.ids.infoText

        if self.ids.LRLText.text.isnumeric() and (int(self.ids.LRLText.text) > 29 and int(self.ids.LRLText.text) < 176):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Lower Rate Limit.[/color]'
            
        if self.ids.URLText.text.isnumeric() and (int(self.ids.URLText.text) > 49 and int(self.ids.URLText.text) < 176):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Upper Rate Limit.[/color]'
        
        if checker == 2 and int(self.ids.URLText.text) < (int(self.ids.LRLText.text)):

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Upper Rate Limit.[/color]'
            checker = 0

        if self.isfloat(self.ids.AAText.text) and float(self.ids.AAText.text) > 0 and float(self.ids.AAText.text) <= 5:
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Atrial Amplitude.[/color]'

        if self.isfloat(self.ids.APWText.text) and float(self.ids.APWText.text) >= 0.05 and float(self.ids.APWText.text) <= 1.9:
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Atrial Pulse Width.[/color]'

        if self.isfloat(self.ids.ASText.text) and float(self.ids.ASText.text) >= 0.25 and float(self.ids.ASText.text) <= 10:
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Atrial Sensitivity.[/color]'

        if  self.ids.ARPText.text.isnumeric() and (int(self.ids.ARPText.text) >= 150 and int(self.ids.ARPText.text) <= 500):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid ARP.[/color]'

        if self.ids.PVARPText.text.isnumeric() and (int(self.ids.PVARPText.text) >= 150 and int(self.ids.PVARPText.text) <= 500):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid PVARP.[/color]'

        if self.ids.RSText.text.isnumeric() and (int(self.ids.RSText.text) >= 0 and int(self.ids.RSText.text) <= 21):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Rate Smoothing.[/color]'

        if checker == 8:
            
            counter = 0
            flag = False
            get_all = ""

            with open("AAI.txt",'r') as f:
                get_all=f.readlines()

            with open("AAI.txt",'w') as f:
                for i,line in enumerate(get_all,1):   
                    if globals.User == line.strip().replace(":",""):     
                        f.write(line)
                        counter = i
                        flag = True
                    elif (counter+1) == i and flag == True:
                        f.write(self.ids.LRLText.text)
                    elif (counter+2) == i and flag == True:
                        f.write("\n"+ self.ids.URLText.text)
                    elif (counter+3) == i and flag == True:
                        f.write("\n"+ self.ids.AAText.text)  
                    elif (counter+4) == i and flag == True:
                        f.write("\n"+ self.ids.APWText.text)   
                    elif (counter+5) == i and flag == True:
                        f.write("\n"+ self.ids.ASText.text)
                    elif (counter+6) == i and flag == True:
                        f.write("\n"+ self.ids.ARPText.text)
                    elif (counter+7) == i and flag == True:
                        f.write("\n"+ self.ids.PVARPText.text)
                    elif (counter+8) == i and flag == True:
                        f.write("\n"+ self.ids.RSText.text + "\n")
                    else:
                        f.write(line)

            errorPrompt.text  = '[color=#00FF11]Changes Saved Successfully.[/color]'

    def isfloat(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

# Class which controls the VVI Menu            
class VVIWindow(Screen):
    
    # Constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # Function which gets the controlled parameters of the state from the corrisponding txt file...
    # right before the menu is shown
    def on_pre_enter(self, *args):
        counter = 0
        flag = False
        with open("VVI.txt", "r") as f:
            for line in f:
                if flag == True:
                    if counter == 0:
                        self.ids.LRLText.text = line.replace("\n","")
                    if counter == 1:
                        self.ids.URLText.text = line.replace("\n","")
                    if counter == 2:
                        self.ids.VAText.text = line.replace("\n","")
                    if counter == 3:
                        self.ids.VPWText.text = line.replace("\n","")
                    if counter == 4:
                        self.ids.VSText.text = line.replace("\n","")
                    if counter == 5:
                        self.ids.VRPText.text = line.replace("\n","")
                    if counter == 6:
                        self.ids.RSText.text = line.replace("\n","")
                        break
                    counter = counter + 1

                if globals.User == line.strip().replace(":",""):
                    flag = True
                    
    # Function that returns user back to the Main Menu when the back button is pressed
    def back_Call(self):
        currentMenu.current = "mainMenu"
        self.ids.infoText.text = ""

    # Function that checks if the controlled parameters are proper values and saves them if they are...
    #...if not, prompts user about error
    # Activates when the 'Save all' button is pressed
    def save_Call(self):
        checker = 0
        errorPrompt = self.ids.infoText

        if self.ids.LRLText.text.isnumeric() and (int(self.ids.LRLText.text) > 29 and int(self.ids.LRLText.text) < 176):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Lower Rate Limit.[/color]'
            
        if self.ids.URLText.text.isnumeric() and (int(self.ids.URLText.text) > 49 and int(self.ids.URLText.text) < 176):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Upper Rate Limit.[/color]'
        
        if checker == 2 and int(self.ids.URLText.text) < (int(self.ids.LRLText.text)):

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Upper Rate Limit.[/color]'
            checker = 0

        if self.isfloat(self.ids.VAText.text) and float(self.ids.VAText.text) > 0 and float(self.ids.VAText.text) <= 5:
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Ventricular Amplitude.[/color]'

        if self.isfloat(self.ids.VPWText.text) and float(self.ids.VPWText.text) >= 0.05 and float(self.ids.VPWText.text) <= 1.9:
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Ventricular Pulse Width.[/color]'

        if self.isfloat(self.ids.VSText.text) and float(self.ids.VSText.text) >= 0.25 and float(self.ids.VSText.text) <= 10:
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Ventricular Sensitivity.[/color]'

        if self.ids.VRPText.text.isnumeric() and (int(self.ids.VRPText.text) >= 150 and int(self.ids.VRPText.text) <= 500):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid VRP.[/color]'

        if self.ids.RSText.text.isnumeric() and (int(self.ids.RSText.text) >= 0 and int(self.ids.RSText.text) <= 21):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Rate Smoothing.[/color]'

        if checker == 7:
            
            counter = 0
            flag = False
            get_all = ""

            with open("VVI.txt",'r') as f:
                get_all=f.readlines()

            with open("VVI.txt",'w') as f:
                for i,line in enumerate(get_all,1):   
                    if globals.User == line.strip().replace(":",""):     
                        f.write(line)
                        counter = i
                        flag = True
                    elif (counter+1) == i and flag == True:
                        f.write(self.ids.LRLText.text)
                    elif (counter+2) == i and flag == True:
                        f.write("\n"+ self.ids.URLText.text)
                    elif (counter+3) == i and flag == True:
                        f.write("\n"+ self.ids.VAText.text)  
                    elif (counter+4) == i and flag == True:
                        f.write("\n"+ self.ids.VPWText.text)   
                    elif (counter+5) == i and flag == True:
                        f.write("\n"+ self.ids.VSText.text)
                    elif (counter+6) == i and flag == True:
                        f.write("\n"+ self.ids.VRPText.text)
                    elif (counter+7) == i and flag == True:
                        f.write("\n"+ self.ids.RSText.text + "\n")
                    else:
                        f.write(line)

            errorPrompt.text  = '[color=#00FF11]Changes Saved Successfully.[/color]'

    def isfloat(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

# Class which controls the DOO Menu
class DOOWindow(Screen):
    
    # Constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # Function which gets the controlled parameters of the state from the corrisponding txt file...
    # right before the menu is shown
    def on_pre_enter(self, *args):
        counter = 0
        flag = False
        with open("DOO.txt", "r") as f:
            for line in f:
                if flag == True:
                    if counter == 0:
                            self.ids.LRLText.text = line.replace("\n","")
                    if counter == 1:
                            self.ids.URLText.text = line.replace("\n","")
                    if counter == 2:
                            self.ids.FAVDText.text = line.replace("\n","")
                    if counter == 3:
                            self.ids.AAText.text = line.replace("\n","")
                    if counter == 4:
                            self.ids.VAText.text = line.replace("\n","")
                    if counter == 5:
                            self.ids.APWText.text = line.replace("\n","")
                    if counter == 6:
                            self.ids.VPWText.text = line.replace("\n","")
                            break
                    counter = counter + 1

                if globals.User == line.strip().replace(":",""):
                    flag = True
                    
    # Function that returns user back to the Main Menu when the back button is pressed
    def back_Call(self):
        currentMenu.current = "mainMenu"
        self.ids.infoText.text = ""

    # Function that checks if the controlled parameters are proper values and saves them if they are...
    #...if not, prompts user about error
    # Activates when the 'Save all' button is pressed
    def save_Call(self):
        checker = 0
        errorPrompt = self.ids.infoText

        if self.ids.LRLText.text.isnumeric() and (int(self.ids.LRLText.text) > 29 and int(self.ids.LRLText.text) < 176):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Lower Rate Limit.[/color]'
            
        if self.ids.URLText.text.isnumeric() and (int(self.ids.URLText.text) > 49 and int(self.ids.URLText.text) < 176):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Upper Rate Limit.[/color]'
        
        if checker == 2 and int(self.ids.URLText.text) < (int(self.ids.LRLText.text)):

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Upper Rate Limit.[/color]'
            checker = 0

        if self.ids.FAVDText.text.isnumeric() and (int(self.ids.FAVDText.text) > 69 and int(self.ids.FAVDText.text) < 301):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Fixed AV Delay.[/color]'

        if self.isfloat(self.ids.AAText.text) and float(self.ids.AAText.text) > 0 and float(self.ids.AAText.text) <= 5:
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Atrial Amplitude.[/color]'

        if self.isfloat(self.ids.VAText.text) and float(self.ids.VAText.text) > 0 and float(self.ids.VAText.text) <= 5:
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Ventricular Amplitude.[/color]'

        if self.isfloat(self.ids.APWText.text) and float(self.ids.APWText.text) >= 0.05 and float(self.ids.APWText.text) <= 1.9:
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Atrial Pulse Width.[/color]'

        if self.isfloat(self.ids.VPWText.text) and float(self.ids.VPWText.text) >= 0.05 and float(self.ids.VPWText.text) <= 1.9:
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Ventricular Pulse Width.[/color]'

        if checker == 7:

            counter = 0
            flag = False
            get_all = ""

            with open("DOO.txt",'r') as f:
                get_all=f.readlines()

            with open("DOO.txt",'w') as f:
                for i,line in enumerate(get_all,1):   
                    if globals.User == line.strip().replace(":",""):     
                        f.write(line)
                        counter = i
                        flag = True
                    elif (counter+1) == i and flag == True:
                        f.write(self.ids.LRLText.text)
                    elif (counter+2) == i and flag == True:
                        f.write("\n"+ self.ids.URLText.text)
                    elif (counter+3) == i and flag == True:
                        f.write("\n"+ self.ids.FAVDText.text)
                    elif (counter+4) == i and flag == True:
                        f.write("\n"+ self.ids.AAText.text)  
                    elif (counter+5) == i and flag == True:
                        f.write("\n"+ self.ids.VAText.text)  
                    elif (counter+6) == i and flag == True:
                        f.write("\n"+ self.ids.APWText.text)   
                    elif (counter+7) == i and flag == True:
                        f.write("\n"+ self.ids.VPWText.text + "\n")   
                    else:
                        f.write(line)

            errorPrompt.text  = '[color=#00FF11]Changes Saved Successfully.[/color]'

    def isfloat(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

# Class which controls the AOOR Menu
class AOORWindow(Screen):
    
    # Constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # Function which gets the controlled parameters of the state from the corrisponding txt file...
    # right before the menu is shown
    def on_pre_enter(self, *args):
        counter = 0
        flag = False
        with open("AOOR.txt", "r") as f:
            for line in f:
                if flag == True:
                    if counter == 0:
                            self.ids.LRLText.text = line.replace("\n","")
                    if counter == 1:
                            self.ids.URLText.text = line.replace("\n","")
                    if counter == 2:
                            self.ids.MSRText.text = line.replace("\n","")
                    if counter == 3:
                            self.ids.AAText.text = line.replace("\n","")
                    if counter == 4:
                            self.ids.APWText.text = line.replace("\n","")
                    if counter == 5:
                            self.ids.ATText.text = line.replace("\n","")
                    if counter == 6:
                            self.ids.RT1Text.text = line.replace("\n","")
                    if counter == 7:
                            self.ids.RFText.text = line.replace("\n","")
                    if counter == 8:
                            self.ids.RT2Text.text = line.replace("\n","")
                            break
                    counter = counter + 1

                if globals.User == line.strip().replace(":",""):
                    flag = True
                    
    # Function that returns user back to the Main Menu when the back button is pressed
    def back_Call(self):
        currentMenu.current = "mainMenu"
        self.ids.infoText.text = ""

    # Function that checks if the controlled parameters are proper values and saves them if they are...
    #...if not, prompts user about error
    # Activates when the 'Save all' button is pressed
    def save_Call(self):
        checker = 0
        errorPrompt = self.ids.infoText

        if self.ids.LRLText.text.isnumeric() and (int(self.ids.LRLText.text) > 29 and int(self.ids.LRLText.text) < 176):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Lower Rate Limit.[/color]'
            
        if self.ids.URLText.text.isnumeric() and (int(self.ids.URLText.text) > 49 and int(self.ids.URLText.text) < 176):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Upper Rate Limit.[/color]'
        
        if checker == 2 and int(self.ids.URLText.text) < (int(self.ids.LRLText.text)):

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Upper Rate Limit.[/color]'
            checker = 0

        if self.ids.MSRText.text.isnumeric() and (int(self.ids.MSRText.text) > 49 and int(self.ids.MSRText.text) < 176):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Maximum Response Rate.[/color]'

        if self.isfloat(self.ids.AAText.text) and float(self.ids.AAText.text) > 0 and float(self.ids.AAText.text) <= 5:
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Atrial Amplitude.[/color]'

        if self.isfloat(self.ids.APWText.text) and float(self.ids.APWText.text) >= 0.05 and float(self.ids.APWText.text) <= 1.9:
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Atrial Pulse Width.[/color]'
        
        if self.ids.ATText.text.lower() == "v-low" or self.ids.ATText.text.lower() == "low" or self.ids.ATText.text.lower() == "med-low" or self.ids.ATText.text.lower() == "med" or self.ids.ATText.text.lower() == "med-high" or self.ids.ATText.text.lower() == "high" or self.ids.ATText.text.lower() == "v-high":
            checker = checker + 1
        else:
        
            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Activity Threshold.[/color]'

        if self.ids.RT1Text.text.isnumeric() and (int(self.ids.RT1Text.text) > 9 and int(self.ids.RT1Text.text) < 51):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Reaction Time.[/color]'

        if self.ids.RFText.text.isnumeric() and (int(self.ids.RFText.text) > 0 and int(self.ids.RFText.text) < 17):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Response Factor.[/color]'

        if self.ids.RT2Text.text.isnumeric() and (int(self.ids.RT2Text.text) > 1 and int(self.ids.RT2Text.text) < 17):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Recovery Time.[/color]'

        if checker == 9:

            counter = 0
            flag = False
            get_all = ""

            with open("AOOR.txt",'r') as f:
                get_all=f.readlines()

            with open("AOOR.txt",'w') as f:
                for i,line in enumerate(get_all,1):   
                    if globals.User == line.strip().replace(":",""):     
                        f.write(line)
                        counter = i
                        flag = True
                    elif (counter+1) == i and flag == True:
                        f.write(self.ids.LRLText.text)
                    elif (counter+2) == i and flag == True:
                        f.write("\n"+ self.ids.URLText.text)
                    elif (counter+3) == i and flag == True:
                        f.write("\n"+ self.ids.MSRText.text)  
                    elif (counter+4) == i and flag == True:
                        f.write("\n"+ self.ids.AAText.text)  
                    elif (counter+5) == i and flag == True:
                        f.write("\n"+ self.ids.APWText.text)   
                    elif (counter+6) == i and flag == True:
                        f.write("\n"+ self.ids.ATText.text)   
                    elif (counter+7) == i and flag == True:
                        f.write("\n"+ self.ids.RT1Text.text)   
                    elif (counter+8) == i and flag == True:
                        f.write("\n"+ self.ids.RFText.text)   
                    elif (counter+9) == i and flag == True:
                        f.write("\n"+ self.ids.RT2Text.text + "\n")   
                    else:
                        f.write(line)

            errorPrompt.text  = '[color=#00FF11]Changes Saved Successfully.[/color]'

    def isfloat(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

# Class which controls the VOOR Menu
class VOORWindow(Screen):
    
    # Constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # Function which gets the controlled parameters of the state from the corrisponding txt file...
    # right before the menu is shown
    def on_pre_enter(self, *args):
        counter = 0
        flag = False
        with open("VOOR.txt", "r") as f:
            for line in f:
                if flag == True:
                    if counter == 0:
                            self.ids.LRLText.text = line.replace("\n","")
                    if counter == 1:
                            self.ids.URLText.text = line.replace("\n","")
                    if counter == 2:
                            self.ids.MSRText.text = line.replace("\n","")
                    if counter == 3:
                            self.ids.VAText.text = line.replace("\n","")
                    if counter == 4:
                            self.ids.VPWText.text = line.replace("\n","")
                    if counter == 5:
                            self.ids.ATText.text = line.replace("\n","")
                    if counter == 6:
                            self.ids.RT1Text.text = line.replace("\n","")
                    if counter == 7:
                            self.ids.RFText.text = line.replace("\n","")
                    if counter == 8:
                            self.ids.RT2Text.text = line.replace("\n","")
                            break
                    counter = counter + 1

                if globals.User == line.strip().replace(":",""):
                    flag = True
                    
    # Function that returns user back to the Main Menu when the back button is pressed
    def back_Call(self):
        currentMenu.current = "mainMenu"
        self.ids.infoText.text = ""

    # Function that checks if the controlled parameters are proper values and saves them if they are...
    #...if not, prompts user about error
    # Activates when the 'Save all' button is pressed
    def save_Call(self):
        checker = 0
        errorPrompt = self.ids.infoText

        if self.ids.LRLText.text.isnumeric() and (int(self.ids.LRLText.text) > 29 and int(self.ids.LRLText.text) < 176):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Lower Rate Limit.[/color]'
            
        if self.ids.URLText.text.isnumeric() and (int(self.ids.URLText.text) > 49 and int(self.ids.URLText.text) < 176):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Upper Rate Limit.[/color]'
        
        if checker == 2 and int(self.ids.URLText.text) < (int(self.ids.LRLText.text)):

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Upper Rate Limit.[/color]'
            checker = 0

        if self.ids.MSRText.text.isnumeric() and (int(self.ids.MSRText.text) > 49 and int(self.ids.MSRText.text) < 176):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Maximum Response Rate.[/color]'

        if self.isfloat(self.ids.VAText.text) and float(self.ids.VAText.text) > 0 and float(self.ids.VAText.text) <= 5:
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Ventricular Amplitude.[/color]'

        if self.isfloat(self.ids.VPWText.text) and float(self.ids.VPWText.text) >= 0.05 and float(self.ids.VPWText.text) <= 1.9:
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Ventricular Pulse Width.[/color]'

        if self.ids.ATText.text.lower() == "v-low" or self.ids.ATText.text.lower() == "low" or self.ids.ATText.text.lower() == "med-low" or self.ids.ATText.text.lower() == "med" or self.ids.ATText.text.lower() == "med-high" or self.ids.ATText.text.lower() == "high" or self.ids.ATText.text.lower() == "v-high":
            checker = checker + 1
        else:
        
            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Activity Threshold.[/color]'

        if self.ids.RT1Text.text.isnumeric() and (int(self.ids.RT1Text.text) > 9 and int(self.ids.RT1Text.text) < 51):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Reaction Time.[/color]'

        if self.ids.RFText.text.isnumeric() and (int(self.ids.RFText.text) > 0 and int(self.ids.RFText.text) < 17):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Response Factor.[/color]'

        if self.ids.RT2Text.text.isnumeric() and (int(self.ids.RT2Text.text) > 1 and int(self.ids.RT2Text.text) < 17):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Recovery Time.[/color]'

        if checker == 9:

            counter = 0
            flag = False
            get_all = ""

            with open("VOOR.txt",'r') as f:
                get_all=f.readlines()

            with open("VOOR.txt",'w') as f:
                for i,line in enumerate(get_all,1):   
                    if globals.User == line.strip().replace(":",""):     
                        f.write(line)
                        counter = i
                        flag = True
                    elif (counter+1) == i and flag == True:
                        f.write(self.ids.LRLText.text)
                    elif (counter+2) == i and flag == True:
                        f.write("\n"+ self.ids.URLText.text)
                    elif (counter+3) == i and flag == True:
                        f.write("\n"+ self.ids.MSRText.text)
                    elif (counter+4) == i and flag == True:
                        f.write("\n"+ self.ids.VAText.text)  
                    elif (counter+5) == i and flag == True:
                        f.write("\n"+ self.ids.VPWText.text)  
                    elif (counter+6) == i and flag == True:
                        f.write("\n"+ self.ids.ATText.text)  
                    elif (counter+7) == i and flag == True:
                        f.write("\n"+ self.ids.RT1Text.text)  
                    elif (counter+8) == i and flag == True:
                        f.write("\n"+ self.ids.RFText.text)  
                    elif (counter+9) == i and flag == True:
                        f.write("\n"+ self.ids.RT2Text.text + "\n")   
                    else:
                        f.write(line)

            errorPrompt.text  = '[color=#00FF11]Changes Saved Successfully.[/color]'

    def isfloat(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

# Class which controls the AAIR Menu
class AAIRWindow(Screen):
    
    # Constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # Function which gets the controlled parameters of the state from the corrisponding txt file...
    # right before the menu is shown
    def on_pre_enter(self, *args):
        counter = 0
        flag = False
        with open("AAIR.txt", "r") as f:
            for line in f:
                if flag == True:
                    if counter == 0:
                        self.ids.LRLText.text = line.replace("\n","")
                    if counter == 1:
                        self.ids.URLText.text = line.replace("\n","")
                    if counter == 2:
                        self.ids.MSRText.text = line.replace("\n","")
                    if counter == 3:
                        self.ids.AAText.text = line.replace("\n","")
                    if counter == 4:
                        self.ids.APWText.text = line.replace("\n","")
                    if counter == 5:
                        self.ids.ASText.text = line.replace("\n","")
                    if counter == 6:
                        self.ids.ARPText.text = line.replace("\n","")
                    if counter == 7:
                        self.ids.PVARPText.text = line.replace("\n","")
                    if counter == 8:
                        self.ids.RSText.text = line.replace("\n","")
                    if counter == 9:
                        self.ids.ATText.text = line.replace("\n","")
                    if counter == 10:
                        self.ids.RT1Text.text = line.replace("\n","")
                    if counter == 11:
                        self.ids.RFText.text = line.replace("\n","")
                    if counter == 12:
                        self.ids.RT2Text.text = line.replace("\n","")
                        break
                    counter = counter + 1

                if globals.User == line.strip().replace(":",""):
                    flag = True
                    
    # Function that returns user back to the Main Menu when the back button is pressed
    def back_Call(self):
        currentMenu.current = "mainMenu"
        self.ids.infoText.text = ""

    # Function that checks if the controlled parameters are proper values and saves them if they are...
    #...if not, prompts user about error
    # Activates when the 'Save all' button is pressed
    def save_Call(self):
        checker = 0
        errorPrompt = self.ids.infoText

        if self.ids.LRLText.text.isnumeric() and (int(self.ids.LRLText.text) > 29 and int(self.ids.LRLText.text) < 176):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Lower Rate Limit.[/color]'
            
        if self.ids.URLText.text.isnumeric() and (int(self.ids.URLText.text) > 49 and int(self.ids.URLText.text) < 176):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Upper Rate Limit.[/color]'
        
        if checker == 2 and int(self.ids.URLText.text) < (int(self.ids.LRLText.text)):

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Upper Rate Limit.[/color]'
            checker = 0

        if self.ids.MSRText.text.isnumeric() and (int(self.ids.MSRText.text) > 49 and int(self.ids.MSRText.text) < 176):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Maximum Response Rate.[/color]'

        if self.isfloat(self.ids.AAText.text) and float(self.ids.AAText.text) > 0 and float(self.ids.AAText.text) <= 5:
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Atrial Amplitude.[/color]'

        if self.isfloat(self.ids.APWText.text) and float(self.ids.APWText.text) >= 0.05 and float(self.ids.APWText.text) <= 1.9:
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Atrial Pulse Width.[/color]'

        if self.isfloat(self.ids.ASText.text) and float(self.ids.ASText.text) >= 0.25 and float(self.ids.ASText.text) <= 10:
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Atrial Sensitivity.[/color]'

        if  self.ids.ARPText.text.isnumeric() and (int(self.ids.ARPText.text) >= 150 and int(self.ids.ARPText.text) <= 500):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid ARP.[/color]'

        if self.ids.PVARPText.text.isnumeric() and (int(self.ids.PVARPText.text) >= 150 and int(self.ids.PVARPText.text) <= 500):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid PVARP.[/color]'

        if self.ids.RSText.text.isnumeric() and (int(self.ids.RSText.text) >= 0 and int(self.ids.RSText.text) <= 21):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Rate Smoothing.[/color]'

        if self.ids.ATText.text.lower() == "v-low" or self.ids.ATText.text.lower() == "low" or self.ids.ATText.text.lower() == "med-low" or self.ids.ATText.text.lower() == "med" or self.ids.ATText.text.lower() == "med-high" or self.ids.ATText.text.lower() == "high" or self.ids.ATText.text.lower() == "v-high":
            checker = checker + 1
        else:
        
            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Activity Threshold.[/color]'

        if self.ids.RT1Text.text.isnumeric() and (int(self.ids.RT1Text.text) > 9 and int(self.ids.RT1Text.text) < 51):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Reaction Time.[/color]'

        if self.ids.RFText.text.isnumeric() and (int(self.ids.RFText.text) > 0 and int(self.ids.RFText.text) < 17):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Response Factor.[/color]'

        if self.ids.RT2Text.text.isnumeric() and (int(self.ids.RT2Text.text) > 1 and int(self.ids.RT2Text.text) < 17):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Recovery Time.[/color]'

        if checker == 13:
            
            counter = 0
            flag = False
            get_all = ""

            with open("AAIR.txt",'r') as f:
                get_all=f.readlines()

            with open("AAIR.txt",'w') as f:
                for i,line in enumerate(get_all,1):   
                    if globals.User == line.strip().replace(":",""):     
                        f.write(line)
                        counter = i
                        flag = True
                    elif (counter+1) == i and flag == True:
                        f.write(self.ids.LRLText.text)
                    elif (counter+2) == i and flag == True:
                        f.write("\n"+ self.ids.URLText.text)
                    elif (counter+3) == i and flag == True:
                        f.write("\n"+ self.ids.MSRText.text) 
                    elif (counter+4) == i and flag == True:
                        f.write("\n"+ self.ids.AAText.text)  
                    elif (counter+5) == i and flag == True:
                        f.write("\n"+ self.ids.APWText.text)   
                    elif (counter+6) == i and flag == True:
                        f.write("\n"+ self.ids.ASText.text)
                    elif (counter+7) == i and flag == True:
                        f.write("\n"+ self.ids.ARPText.text)
                    elif (counter+8) == i and flag == True:
                        f.write("\n"+ self.ids.PVARPText.text)
                    elif (counter+9) == i and flag == True:
                        f.write("\n"+ self.ids.RSText.text)
                    elif (counter+10) == i and flag == True:
                        f.write("\n"+ self.ids.ATText.text)
                    elif (counter+11) == i and flag == True:
                        f.write("\n"+ self.ids.RT1Text.text)
                    elif (counter+12) == i and flag == True:
                        f.write("\n"+ self.ids.RFText.text)
                    elif (counter+13) == i and flag == True:
                        f.write("\n"+ self.ids.RT2Text.text + "\n")
                    else:
                        f.write(line)

            errorPrompt.text  = '[color=#00FF11]Changes Saved Successfully.[/color]'

    def isfloat(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

# Class which controls the VVIR Menu
class VVIRWindow(Screen):
    
    # Constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # Function which gets the controlled parameters of the state from the corrisponding txt file...
    # right before the menu is shown
    def on_pre_enter(self, *args):
        counter = 0
        flag = False
        with open("VVIR.txt", "r") as f:
            for line in f:
                if flag == True:
                    if counter == 0:
                        self.ids.LRLText.text = line.replace("\n","")
                    if counter == 1:
                        self.ids.URLText.text = line.replace("\n","")
                    if counter == 2:
                        self.ids.MSRText.text = line.replace("\n","")
                    if counter == 3:
                        self.ids.VAText.text = line.replace("\n","")
                    if counter == 4:
                        self.ids.VPWText.text = line.replace("\n","")
                    if counter == 5:
                        self.ids.VSText.text = line.replace("\n","")
                    if counter == 6:
                        self.ids.VRPText.text = line.replace("\n","")
                    if counter == 7:
                        self.ids.RSText.text = line.replace("\n","")
                    if counter == 8:
                        self.ids.ATText.text = line.replace("\n","")
                    if counter == 9:
                        self.ids.RT1Text.text = line.replace("\n","")
                    if counter == 10:
                        self.ids.RFText.text = line.replace("\n","")
                    if counter == 11:
                        self.ids.RT2Text.text = line.replace("\n","")
                        break
                    counter = counter + 1

                if globals.User == line.strip().replace(":",""):
                    flag = True
                    
    # Function that returns user back to the Main Menu when the back button is pressed
    def back_Call(self):
        currentMenu.current = "mainMenu"
        self.ids.infoText.text = ""

    # Function that checks if the controlled parameters are proper values and saves them if they are...
    #...if not, prompts user about error
    # Activates when the 'Save all' button is pressed
    def save_Call(self):
        checker = 0
        errorPrompt = self.ids.infoText

        if self.ids.LRLText.text.isnumeric() and (int(self.ids.LRLText.text) > 29 and int(self.ids.LRLText.text) < 176):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Lower Rate Limit.[/color]'
            
        if self.ids.URLText.text.isnumeric() and (int(self.ids.URLText.text) > 49 and int(self.ids.URLText.text) < 176):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Upper Rate Limit.[/color]'
        
        if checker == 2 and int(self.ids.URLText.text) < (int(self.ids.LRLText.text)):

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Upper Rate Limit.[/color]'
            checker = 0

        if self.ids.MSRText.text.isnumeric() and (int(self.ids.MSRText.text) > 49 and int(self.ids.MSRText.text) < 176):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Maximum Response Rate.[/color]'

        if self.isfloat(self.ids.VAText.text) and float(self.ids.VAText.text) > 0 and float(self.ids.VAText.text) <= 5:
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Ventricular Amplitude.[/color]'

        if self.isfloat(self.ids.VPWText.text) and float(self.ids.VPWText.text) >= 0.05 and float(self.ids.VPWText.text) <= 1.9:
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Ventricular Pulse Width.[/color]'

        if self.isfloat(self.ids.VSText.text) and float(self.ids.VSText.text) >= 0.25 and float(self.ids.VSText.text) <= 10:
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Ventricular Sensitivity.[/color]'

        if self.ids.VRPText.text.isnumeric() and (int(self.ids.VRPText.text) >= 150 and int(self.ids.VRPText.text) <= 500):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid VRP.[/color]'

        if self.ids.RSText.text.isnumeric() and (int(self.ids.RSText.text) >= 0 and int(self.ids.RSText.text) <= 21):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Rate Smoothing.[/color]'

        if self.ids.ATText.text.lower() == "v-low" or self.ids.ATText.text.lower() == "low" or self.ids.ATText.text.lower() == "med-low" or self.ids.ATText.text.lower() == "med" or self.ids.ATText.text.lower() == "med-high" or self.ids.ATText.text.lower() == "high" or self.ids.ATText.text.lower() == "v-high":
            checker = checker + 1
        else:
        
            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Activity Threshold.[/color]'

        if self.ids.RT1Text.text.isnumeric() and (int(self.ids.RT1Text.text) > 9 and int(self.ids.RT1Text.text) < 51):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Reaction Time.[/color]'

        if self.ids.RFText.text.isnumeric() and (int(self.ids.RFText.text) > 0 and int(self.ids.RFText.text) < 17):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Response Factor.[/color]'

        if self.ids.RT2Text.text.isnumeric() and (int(self.ids.RT2Text.text) > 1 and int(self.ids.RT2Text.text) < 17):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Recovery Time.[/color]'

        if checker == 12:
            
            counter = 0
            flag = False
            get_all = ""

            with open("VVIR.txt",'r') as f:
                get_all=f.readlines()

            with open("VVIR.txt",'w') as f:
                for i,line in enumerate(get_all,1):   
                    if globals.User == line.strip().replace(":",""):     
                        f.write(line)
                        counter = i
                        flag = True
                    elif (counter+1) == i and flag == True:
                        f.write(self.ids.LRLText.text)
                    elif (counter+2) == i and flag == True:
                        f.write("\n"+ self.ids.URLText.text)
                    elif (counter+3) == i and flag == True:
                        f.write("\n"+ self.ids.MSRText.text)
                    elif (counter+4) == i and flag == True:
                        f.write("\n"+ self.ids.VAText.text)  
                    elif (counter+5) == i and flag == True:
                        f.write("\n"+ self.ids.VPWText.text)   
                    elif (counter+6) == i and flag == True:
                        f.write("\n"+ self.ids.VSText.text)
                    elif (counter+7) == i and flag == True:
                        f.write("\n"+ self.ids.VRPText.text)
                    elif (counter+8) == i and flag == True:
                        f.write("\n"+ self.ids.RSText.text)
                    elif (counter+9) == i and flag == True:
                        f.write("\n"+ self.ids.ATText.text)
                    elif (counter+10) == i and flag == True:
                        f.write("\n"+ self.ids.RT1Text.text)
                    elif (counter+11) == i and flag == True:
                        f.write("\n"+ self.ids.RFText.text)
                    elif (counter+12) == i and flag == True:
                        f.write("\n"+ self.ids.RT2Text.text + "\n")
                    else:
                        f.write(line)

            errorPrompt.text  = '[color=#00FF11]Changes Saved Successfully.[/color]'

    def isfloat(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

# Class which controls the DOOR Menu
class DOORWindow(Screen):
    
    # Constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # Function which gets the controlled parameters of the state from the corrisponding txt file...
    # right before the menu is shown
    def on_pre_enter(self, *args):
        counter = 0
        flag = False
        with open("DOOR.txt", "r") as f:
            for line in f:
                if flag == True:
                    if counter == 0:
                            self.ids.LRLText.text = line.replace("\n","")
                    if counter == 1:
                            self.ids.URLText.text = line.replace("\n","")
                    if counter == 2:
                            self.ids.MSRText.text = line.replace("\n","")
                    if counter == 3:
                            self.ids.FAVDText.text = line.replace("\n","")
                    if counter == 4:
                            self.ids.AAText.text = line.replace("\n","")
                    if counter == 5:
                            self.ids.VAText.text = line.replace("\n","")
                    if counter == 6:
                            self.ids.APWText.text = line.replace("\n","")
                    if counter == 7:
                            self.ids.VPWText.text = line.replace("\n","")
                    if counter == 8:
                            self.ids.ATText.text = line.replace("\n","")
                    if counter == 9:
                            self.ids.RT1Text.text = line.replace("\n","")
                    if counter == 10:
                            self.ids.RFText.text = line.replace("\n","")
                    if counter == 11:
                            self.ids.RT2Text.text = line.replace("\n","")
                            break
                    counter = counter + 1

                if globals.User == line.strip().replace(":",""):
                    flag = True
                    
    # Function that returns user back to the Main Menu when the back button is pressed
    def back_Call(self):
        currentMenu.current = "mainMenu"
        self.ids.infoText.text = ""

    # Function that checks if the controlled parameters are proper values and saves them if they are...
    #...if not, prompts user about error
    # Activates when the 'Save all' button is pressed
    def save_Call(self):
        checker = 0
        errorPrompt = self.ids.infoText

        if self.ids.LRLText.text.isnumeric() and (int(self.ids.LRLText.text) > 29 and int(self.ids.LRLText.text) < 176):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Lower Rate Limit.[/color]'
            
        if self.ids.URLText.text.isnumeric() and (int(self.ids.URLText.text) > 49 and int(self.ids.URLText.text) < 176):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Upper Rate Limit.[/color]'
        
        if checker == 2 and int(self.ids.URLText.text) < (int(self.ids.LRLText.text)):

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Upper Rate Limit.[/color]'
            checker = 0

        if self.ids.MSRText.text.isnumeric() and (int(self.ids.MSRText.text) > 49 and int(self.ids.MSRText.text) < 176):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Maximum Response Rate.[/color]'

        if self.ids.FAVDText.text.isnumeric() and (int(self.ids.FAVDText.text) > 69 and int(self.ids.FAVDText.text) < 301):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Fixed AV Delay.[/color]'

        if self.isfloat(self.ids.AAText.text) and float(self.ids.AAText.text) > 0 and float(self.ids.AAText.text) <= 5:
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Atrial Amplitude.[/color]'

        if self.isfloat(self.ids.VAText.text) and float(self.ids.VAText.text) > 0 and float(self.ids.VAText.text) <= 5:
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Ventricular Amplitude.[/color]'

        if self.isfloat(self.ids.APWText.text) and float(self.ids.APWText.text) >= 0.05 and float(self.ids.APWText.text) <= 1.9:
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Atrial Pulse Width.[/color]'

        if self.isfloat(self.ids.VPWText.text) and float(self.ids.VPWText.text) >= 0.05 and float(self.ids.VPWText.text) <= 1.9:
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Ventricular Pulse Width.[/color]'

        if self.ids.ATText.text.lower() == "v-low" or self.ids.ATText.text.lower() == "low" or self.ids.ATText.text.lower() == "med-low" or self.ids.ATText.text.lower() == "med" or self.ids.ATText.text.lower() == "med-high" or self.ids.ATText.text.lower() == "high" or self.ids.ATText.text.lower() == "v-high":
            checker = checker + 1
        else:
        
            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Activity Threshold.[/color]'

        if self.ids.RT1Text.text.isnumeric() and (int(self.ids.RT1Text.text) > 9 and int(self.ids.RT1Text.text) < 51):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Reaction Time.[/color]'

        if self.ids.RFText.text.isnumeric() and (int(self.ids.RFText.text) > 0 and int(self.ids.RFText.text) < 17):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Response Factor.[/color]'

        if self.ids.RT2Text.text.isnumeric() and (int(self.ids.RT2Text.text) > 1 and int(self.ids.RT2Text.text) < 17):
            checker = checker + 1
        else:

            errorPrompt.text = '[color=#FF0000]ERROR: Invalid Recovery Time.[/color]'

        if checker == 12:

            counter = 0
            flag = False
            get_all = ""

            with open("DOOR.txt",'r') as f:
                get_all=f.readlines()

            with open("DOOR.txt",'w') as f:
                for i,line in enumerate(get_all,1):   
                    if globals.User == line.strip().replace(":",""):     
                        f.write(line)
                        counter = i
                        flag = True
                    elif (counter+1) == i and flag == True:
                        f.write(self.ids.LRLText.text)
                    elif (counter+2) == i and flag == True:
                        f.write("\n"+ self.ids.URLText.text)
                    elif (counter+3) == i and flag == True:
                        f.write("\n"+ self.ids.MSRText.text)
                    elif (counter+4) == i and flag == True:
                        f.write("\n"+ self.ids.FAVDText.text)
                    elif (counter+5) == i and flag == True:
                        f.write("\n"+ self.ids.AAText.text)  
                    elif (counter+6) == i and flag == True:
                        f.write("\n"+ self.ids.VAText.text)  
                    elif (counter+7) == i and flag == True:
                        f.write("\n"+ self.ids.APWText.text)   
                    elif (counter+8) == i and flag == True:
                        f.write("\n"+ self.ids.VPWText.text)   
                    elif (counter+9) == i and flag == True:
                        f.write("\n"+ self.ids.ATText.text)  
                    elif (counter+10) == i and flag == True:
                        f.write("\n"+ self.ids.RT1Text.text)  
                    elif (counter+11) == i and flag == True:
                        f.write("\n"+ self.ids.RFText.text)  
                    elif (counter+12) == i and flag == True:
                        f.write("\n"+ self.ids.RT2Text.text + "\n")  
                    else:
                        f.write(line)

            errorPrompt.text  = '[color=#00FF11]Changes Saved Successfully.[/color]'

    def isfloat(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

# Class which controls the Egram Menu
class EgramWindow(FloatLayout):

    # Constructor
    def __init__(self, **kwargs):
        super(EgramWindow, self).__init__()
        self.atrplot = MeshLinePlot(color=[1, 0, 0, 1])
        self.ventplot = MeshLinePlot(color=[0.06, 0.50, 0.75, 1])

    # Function which starts the Egram with updating values from the serial stream
    def start(self):
        if (globals.deviceConnected):
            self.ids.egramATRGraph.add_plot(self.atrplot)
            Clock.schedule_interval(self.ATRReceive, 0.001)

            self.ids.egramVENTGraph.add_plot(self.ventplot)
            Clock.schedule_interval(self.VENTReceive, 0.001)
    
    # Functions which continously graph the updating values of ATR and VENT pacings
    def ATRReceive(self, dt):
        globals.ATRVENTVAL = struct.unpack('<dddddd',globals.serialport.read(48))
        globals.ATRVals.pop(0)
        x = globals.ATRVENTVAL[0]
        globals.ATRVals.append((x-0.5)*-2*3.3)
        self.atrplot.points = [(i, j) for i, j in enumerate(globals.ATRVals)]

    def VENTReceive(self, dt):
        globals.VENTVals.pop(0)
        x = globals.ATRVENTVAL[1]
        globals.VENTVals.append((x-0.5)*-2*3.3)
        self.ventplot.points = [(i, j) for i, j in enumerate(globals.VENTVals)]

    # Function which stops the graphs when the stop button is called
    def stop(self):
        Clock.unschedule(self.ATRReceive)
        Clock.unschedule(self.VENTReceive)

# Class which controls all other classes (Menu Manager)
class WindowManager(ScreenManager):
    pass

# Creating a variable to store the current menu (also setting the transition animation between menus)
currentMenu = WindowManager(transition=RiseInTransition())

# Adding all classes to the currentmenu variable
currentMenu.add_widget(LoginMenuWindow(name="loginMenu"))
currentMenu.add_widget(RegisterMenuWindow(name="registerMenu"))
currentMenu.add_widget(MainMenuWindow(name="mainMenu"))
currentMenu.add_widget(AOOWindow(name="AOOMenu"))
currentMenu.add_widget(VOOWindow(name="VOOMenu"))
currentMenu.add_widget(AAIWindow(name="AAIMenu"))
currentMenu.add_widget(VVIWindow(name="VVIMenu"))
currentMenu.add_widget(DOOWindow(name="DOOMenu"))
currentMenu.add_widget(AOORWindow(name="AOORMenu"))
currentMenu.add_widget(VOORWindow(name="VOORMenu"))
currentMenu.add_widget(AAIRWindow(name="AAIRMenu"))
currentMenu.add_widget(VVIRWindow(name="VVIRMenu"))
currentMenu.add_widget(DOORWindow(name="DOORMenu"))

# Setting the current menu of the currentmenu variable to the Login Menu
currentMenu.current = "loginMenu"

# Class which controls the whole program (Startup Class)
class PacemakerApp(App):

    # Constructor (Initializing the currentmenu global variable)
    def build(self):
        return currentMenu

# Running the Startup Class
if __name__=="__main__":
    globals.initialize() 
    lm = PacemakerApp()
    lm.run()
