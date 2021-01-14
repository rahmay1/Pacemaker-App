# Creating a global variable
def initialize():
    global User
    User = "" 

    # Variable which checks if pacemaker is connected
    global deviceConnected
    deviceConnected = False

    global serialport
    serialport = ""
    
    global ATRVals
    ATRVals = 100*[0.0]

    global VENTVals
    VENTVals = 100*[0.0]

    global ATRVENTVAL

    # Parameters for the serial sending
    global paceLoc
    paceLoc = 0

    global sensing
    sensing = 0

    global LRL
    LRL = 0
    
    global URL
    URL = 0

    global atrAmp
    atrAmp = 0.000

    global ventAmp
    ventAmp = 0.000

    global atrsensitivity
    atrSensitivity = 0.0

    global VENTsensitivity
    VENTsensitivity = 0.0

    global ATRpulseWidth
    ATRpulseWidth = 0.000

    global VENTpulseWidth
    VENTpulseWidth = 0.000

    global ARP
    ARP = 0.000

    global VRP
    VRP = 0.000

    global rateAdap
    rateAdap = 0

    global rateSmoothing
    rateSmothing = 0

    global reactTime
    reactTime = 0

    global respFactor
    respFactor = 0

    global recovTime
    recovTime = 0

    global MSR
    MSR = 0

    global AV_delay
    AV_delay = 0.000

    global ATT
    ATT = ""