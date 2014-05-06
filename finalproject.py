from Tkinter import *
import os
import random 
import cPickle
import codecs 
import tkMessageBox
import string

####################################
# init
####################################

def init(data):
    data.mode = "splashScreen"
    data.score = 0
    data.word = ""
    data.objects = []
    data.i = 0 
    data.background = PhotoImage(file = "background.gif",width = data.width, height = data.height)
    rHand = PhotoImage(file="righthand.gif")
    data.rightHand = rHand.subsample(3,3)
    lHand = PhotoImage(file = "lefthand.gif")
    data.leftHand = lHand.subsample(3,3)
    data.keyboard = PhotoImage(file = "keyboard.gif")
    data.leftHandCoordinates = [(286, 532),(236, 448),(184, 434),(147, 453),(115, 493)]
    data.rightHandCoordinates = [(914, 534), (961, 444), (1014, 438), (1049, 453), (1085, 496)]
    data.a = 0 
    data.b = 0 
    data.accuracy = 0 
    data.wordnum = 0 
    data.error = (0,0)
    data.backButton = False
    data.start = 0 
    data.wpm = 0
    data.textBoxColor = "white"
    data.username = ""
    data.currentUser = None
    data.usrObjects = []
    num = 0
    with codecs.open('numObjects.txt', encoding='utf-8-sig') as f:
        num = next(f)
        num = int(num)
    try:
        data.usrObjects = load(num)
    except:
        pass
    data.soundOnColor = "grey"
    data.soundOn = False
    data.currentWords = []
    data.wpmList = []
    data.done = False
    data.keyboardCoordinates = {"`":(340, 456, 368, 482),"~":(340, 456, 368, 482), "1": (376, 454, 403, 482),"!": (376, 454, 403, 482), "2": (412, 455, 438, 482),"@":(412, 455, 438, 482), "3": (447, 453, 476, 481), "#": (447, 453, 476, 481),"4": (484, 454,514, 482),"$": (484, 454,514, 482), "5":(522, 454,548, 482),"%":(522, 454,548, 482),"6":(557, 454,586, 480), "^":(557, 454,586, 480),"7":(557, 454,586, 480), "&":(557, 454,586, 480),"8":(593, 454,621, 481),"*":(593, 454,621, 481), "9":(630, 455,657, 483),"(":(630, 455,657, 483) ,"0":(667, 454,693, 483),")":(667, 454,693, 483), "-": (701, 457,730, 482),"_":(701, 457,730, 482), "=":(738, 455,767, 482),"+":(738, 455,767, 482),"Backspace":(811, 457,870, 482), "tab":(339, 491,387, 518),"q":(393, 491,421, 516), "w":(430, 491,458, 517), "e":(465, 495,492, 518), "r":(502, 492,529, 519), "t":(536, 494,564, 519), "y": (574, 494,600, 516),"u": (609, 491,638, 518), "i":(643, 492,673, 517), "o":(679, 493,710, 518),"p":(716, 492,746, 518), "{":(752, 492,781, 520),"[":(752, 492,781, 520), "}":(785, 491,818, 519),"]":(785, 491,818, 519),"|":(785, 491,818, 519),"\\":(785, 491,818, 519),"Caps": (338, 526,393, 551), "a":(400, 526,428, 553), "s": (438, 527,466, 550), "d":(474, 527,502, 552), "f":(509, 525,537, 552), "g":(545, 527,575, 553), "h":(580, 525,610, 553), "j":(616, 525,647, 552), "k":(654, 524,682, 553), "l":(687, 525,718, 551), ":":(725, 525,753, 551),";":(725, 525,753, 551), "'":(762, 529,790, 551),  "\"":(762, 529,790, 551), "Return":(794, 526,828, 552), "Shift":(338, 560,378, 589), "z":(382, 562,413, 588), "x":(421, 564,449, 590), "c":(457, 565,487, 589),"v":(492, 563,523, 589), "b":(530, 563,555, 590), "n":(565, 561,593, 590), "m":(601, 561,629, 591), ",": (638, 561,665, 588), "<": (638, 561,665, 588),".":(673, 565,698, 587),">":(673, 565,698, 587), "/": (709, 563,738, 589), "?":(738, 455,767, 482), "Shift2":(745, 563,774, 587), "Ctrl":(339, 598,377, 626), "Alt":(385, 600,423, 627)," ": (428, 598,779, 626)}
    data.placeHolder = (data.width/6+28, 135, data.width/6+49, 165)



####################################
# mode dispatcher
####################################

def mousePressed(event, data):
    if (data.mode == "splashScreen"): 
        splashScreenMousePressed(event, data)
    elif (data.mode == "Levels"):   
        levelsMousePressed(event, data)
    elif(data.mode == "Part1"):
        Part1MousePressed(event,data)
    elif(data.mode == "Part2"):
        Part2MousePressed(event,data)
    elif(data.mode == "Part3"):
        Part3MousePressed(event,data)
    elif(data.mode == "level11"):
        level11MousePressed(event,data)
    elif(data.mode == "level12"):
        level12MousePressed(event,data)
    elif(data.mode == "level13"):
        level13MousePressed(event,data)
    elif(data.mode == "level21"):
        level21MousePressed(event,data)
    elif(data.mode == "level22"):
        level22MousePressed(event,data)
    elif(data.mode == "level23"):
        level23MousePressed(event,data)
    elif(data.mode == "level31"):
        level31MousePressed(event,data)
    elif(data.mode == "level32"):
        level32MousePressed(event,data)
    elif(data.mode == "level33"):
        level33MousePressed(event,data)
    elif(data.mode == "stats"):
        statsMousePressed(event,data)




def keyPressed(event, data):
    if (data.mode == "splashScreen"): 
        splashScreenKeyPressed(event, data)
    elif (data.mode == "Levels"):   
        levelsKeyPressed(event, data)
    elif(data.mode == "Part1"):
        Part1KeyPressed(event,data)
    elif(data.mode == "Part2"):
        Part2KeyPressed(event,data)
    elif(data.mode == "Part3"):
        Part3KeyPressed(event,data)
    elif(data.mode == "level11"):
        level11KeyPressed(event,data)
    elif(data.mode == "level12"):
        level12KeyPressed(event,data)
    elif(data.mode == "level13"):
        level13KeyPressed(event,data)
    elif(data.mode == "level21"):
        level21KeyPressed(event,data)
    elif(data.mode == "level22"):
        level22KeyPressed(event,data)
    elif(data.mode == "level23"):
        level23KeyPressed(event,data)
    elif(data.mode == "level31"):
        level31KeyPressed(event,data)
    elif(data.mode == "level32"):
        level32KeyPressed(event,data)
    elif(data.mode == "level33"):
        level33KeyPressed(event,data)
    elif(data.mode == "stats"):
        statsKeyPressed(event,data)



def timerFired(data):
    if (data.mode == "splashScreen"): 
        splashScreenTimerFired(data)
    elif (data.mode == "Levels"):   
        levelsTimerFired(data)
    elif(data.mode == "Part1"):
        Part1TimerFired(data)
    elif(data.mode == "Part2"):
        Part2TimerFired(data)
    elif(data.mode == "Part3"):
        Part3TimerFired(data)
    elif(data.mode == "level11"):
        level11TimerFired(data)
    elif(data.mode == "level12"):
        level12TimerFired(data)
    elif(data.mode == "level13"):
        level13TimerFired(data)
    elif(data.mode == "level21"):
        level21TimerFired(data)
    elif(data.mode == "level22"):
        level22TimerFired(data)
    elif(data.mode == "level23"):
        level23TimerFired(data)
    elif(data.mode == "level31"):
        level31TimerFired(data)
    elif(data.mode == "level32"):
        level32TimerFired(data)
    elif(data.mode == "level33"):
        level33TimerFired(data)
    elif(data.mode == "stats"):
        statsTimerFired(data)

def redrawAll(canvas, data):
    if (data.mode == "splashScreen"): 
        splashScreenRedrawAll(canvas, data)
    elif (data.mode == "Levels"):   
        levelsRedrawAll(canvas, data)
    elif(data.mode == "Part1"):
        Part1RedrawAll(canvas,data)
    elif(data.mode == "Part2"):
        Part2RedrawAll(canvas,data)
    elif(data.mode == "Part3"):
        Part3RedrawAll(canvas,data)
    elif(data.mode == "level11"):
        level11RedrawAll(canvas,data)
    elif(data.mode == "level12"):
        level12RedrawAll(canvas,data)
    elif(data.mode == "level13"):
        level13RedrawAll(canvas,data)
    elif(data.mode == "level21"):
        level21RedrawAll(canvas,data)
    elif(data.mode == "level22"):
        level22RedrawAll(canvas,data)
    elif(data.mode == "level23"):
        level23RedrawAll(canvas,data)
    elif(data.mode == "level31"):
        level31RedrawAll(canvas,data)
    elif(data.mode == "level32"):
        level32RedrawAll(canvas,data)
    elif(data.mode == "level33"):
        level33RedrawAll(canvas,data)
    elif(data.mode == "stats"):
        statsRedrawAll(canvas,data)

def motion(event,data):
    pass

####################################
# splashScreen mode
####################################

def splashScreenMousePressed(event, data):
    global canvas 
    #Clicked in Box --> Typing in Username
    if(clickedIn(event.x,event.y,data.width/3, 300,data.width*2/3,340)):
        data.textBoxColor= "grey"
    if not (clickedIn(event.x, event.y,data.width/3,300,data.width*2/3,340) or clickedIn(event.x,event.y,data.width/3, 370, data.width*3/7, 400) or clickedIn(event.x, event.y, data.width*4/7, 370, data.width*2/3,400)):
        data.textBoxColor = "white"
    #Clicked on submit --> will load user's data, go to mode "Levels"
    elif(clickedIn(event.x,event.y,data.width/3, 370, data.width*3/7, 400)):
        switch = False
        for u in data.usrObjects:
            if u.username == data.username:
                data.currentUser = u
                data.currentUser.session +=1
                data.currentUser.statistics[data.currentUser.session] = (0,0)
                data.mode = "Levels"
                switch = True
        if(not switch):
            message = "This account does not exist. Click 'New' to create an Account with this Username"
            title = "Error!"
            tkMessageBox.showerror(title, message)
        switch = False
    #Clicked on new --> create an new usr object, appends to data.usrObjects
    elif(clickedIn(event.x, event.y, data.width*4/7, 370, data.width*2/3,400)):
        data.mode = "Levels"
        data.currentUser = User(data.username)
        data.usrObjects.append(data.currentUser)
        dump(data.usrObjects)
        numobj = None
        with codecs.open('numObjects.txt', encoding='utf-8-sig') as f:
            numobj = next(f)
            numobj = int(numobj) +1
            numobj = str(numobj)
        contentsToWrite = numobj        
        writeFile("numObjects.txt", contentsToWrite)


def splashScreenKeyPressed(event, data):
    if(data.textBoxColor == "grey"):
        if(event.keysym == "BackSpace"):
            data.username = data.username[:-1]
        elif(event.keysym == "space"):
            data.username += " "
        elif(event.keysym == "period" or event.keysym == "??"):
            data.username += ""
        else:
            data.username += event.keysym

def splashScreenTimerFired(data):
    pass

def splashScreenRedrawAll(canvas, data):
    background = data.background
    canvas.create_image(0, 0, anchor = NW, image = background)
    canvas.create_text(data.width/6-100, 100, text = "Welcome to Protyper: Typing Educational Software for All!", anchor = NW,font="Courier 30 ", fill = "white")
    canvas.create_text(data.width/6-100, 160, text = "Enter your previous username and submit or type a new username and hit 'New' to get started!", anchor = NW,font="Courier 18 ", fill = "white")
    canvas.create_rectangle(data.width/3, 300, data.width*2/3, 340, fill = data.textBoxColor)
    canvas.create_rectangle(data.width/3, 370, data.width*3/7, 400, fill = "orange", width = 0)
    canvas.create_text(data.width/3 + 15,372, anchor = NW, text = "Submit",font="Courier 22")
    canvas.create_rectangle(data.width*4/7, 370, data.width*2/3,400, fill = "orange", width = 0)
    canvas.create_text(data.width*4/7+22,372,text = "New", anchor = NW, font="Courier 22 ")
    if(data.textBoxColor == "grey"):
        canvas.create_text(data.width/3+5,305,text = data.username, font="Courier 26 ", anchor = NW, fill = "black")





####################################
# Levels Mode 
####################################

def levelsMousePressed(event, data):
    if(clickedIn(event.x, event.y,data.width/2 - 250, data.height/6-20, data.width/2+250, data.height/6+20)):
        data.mode = "Part1"
    elif(clickedIn(event.x,event.y,data.width/2 - 250, data.height*2/6-20, data.width/2+250, data.height*2/6+20)):
        data.mode = "Part2"
    elif(clickedIn(event.x, event.y,data.width/2 - 250, data.height*3/6-20, data.width/2+250, data.height*3/6+20)):
        data.mode = "Part3"
    elif(clickedIn(event.x, event.y, data.width/2 - 250, data.height*4/6-20, data.width/2+250, data.height*4/6+20)):
        data.mode = "stats"
    elif(clickedIn(event.x, event.y, 1075, 25, 1175, 75)):
        dump(data.usrObjects)
        print(data.currentUser.session)
        data.mode = "splashScreen"
        init(data)


def levelsKeyPressed(event, data):
    pass

def levelsTimerFired(data):
    pass

def levelsRedrawAll(canvas, data):
    background = data.background
    canvas.create_image(0, 0, anchor = NW, image = background)
    canvas.create_rectangle(data.width/2 - 270, data.height/6-20, data.width/2+270, data.height/6+20, fill = "grey", outline = "orange")
    canvas.create_text(data.width/2, data.height/6, text = "Beginner - Learn the Alphabet", font="Courier 22")
    canvas.create_rectangle(data.width/2 - 270, data.height*2/6-20, data.width/2+270, data.height*2/6+20, fill = "grey", outline = "orange")
    canvas.create_text(data.width/2, data.height*2/6, text ="Intermediate - Practice!",font="Courier 22")
    canvas.create_rectangle(data.width/2 - 270, data.height*3/6-20, data.width/2+270, data.height*3/6+20, fill = "grey", outline = "orange")
    canvas.create_text(data.width/2, data.height*3/6, text = "Hard - Special Keys and Accuracy Drills",font="Courier 22")
    canvas.create_rectangle(data.width/2 - 270, data.height*4/6-20, data.width/2+270, data.height*4/6+20, fill = "grey", outline = "orange")
    canvas.create_text(data.width/2, data.height*4/6, text = "Stats",font="Courier 22")
    canvas.create_rectangle(1065, 20, 1175, 55, fill  = "orange")
    canvas.create_text(1087, 27, text = "logout", anchor = NW, font = "Courier 16")
####################################
#beginner
####################################
def Part1MousePressed(event, data):
    if(clickedIn(event.x, event.y,data.width/2 - 250, data.height/6-20, data.width/2+250, data.height/6+20)):
        data.word = ""
        letterList = ["a","s","d","f","g","h","j","k","l"," "," "]
        data.word = getLetters(data.currentUser.statDic, letterList, 145)
        data.mode = "level11"
        refreshObjects(data)
    elif(clickedIn(event.x,event.y,data.width/2 - 250, data.height*2/6-20, data.width/2+250, data.height*2/6+20)):
        data.word = ""
        letterList = ["q","w","e","r","t","y","u","i","o","p"," ", " "]
        data.word = getLetters(data.currentUser.statDic, letterList, 145)
        data.mode = "level12"
        refreshObjects(data)
    elif(clickedIn(event.x, event.y,data.width/2 - 250, data.height*3/6-20, data.width/2+250, data.height*3/6+20)):
        data.word = ""
        letterList = ["z","x","c","v","b","n","m"," "," "]
        data.word = getLetters(data.currentUser.statDic, letterList, 145)
        data.mode = "level13"
        refreshObjects(data)
    elif(clickedIn(event.x, event.y,1050,50,1175,100)):
        data.mode = "Levels"


def Part1KeyPressed(event, data):
    pass

def Part1TimerFired(data):
    pass

def Part1RedrawAll(canvas, data):
    background = data.background
    canvas.create_image(0, 0, anchor = NW, image = background)
    canvas.create_rectangle(data.width/2 - 250, data.height/6-20, data.width/2+250, data.height/6+20, fill = "grey", outline = "orange")
    canvas.create_text(data.width/2, data.height/6, text = "ASDFGHJKL - Middle Row", font="Courier 26")
    canvas.create_rectangle(data.width/2 - 250, data.height*2/6-20, data.width/2+250, data.height*2/6+20, fill = "grey", outline = "orange")
    canvas.create_text(data.width/2, data.height*2/6, text ="QWERTYYUIOP - Top Row",font="Courier 26")
    canvas.create_rectangle(data.width/2 - 250, data.height*3/6-20, data.width/2+250, data.height*3/6+20, fill = "grey", outline = "orange")
    canvas.create_text(data.width/2, data.height*3/6, text = "ZXCVBNM - Bottom Row",font="Courier 26")
    canvas.create_rectangle(1050,50,1175,100,fill = "grey")
    canvas.create_text(1060,55,text = "Back", anchor = NW, font = "Courier 26", width = 0)

####################################
#intermediate
####################################
def Part2MousePressed(event, data):
    if(clickedIn(event.x, event.y,data.width/2 - 250, data.height/6-20, data.width/2+250, data.height/6+20)):
        data.word = ""
        letterList = list(string.digits + " ")
        data.word = getLetters(data.currentUser.statDic, letterList, 145)
        data.mode = "level21"
        refreshObjects(data)
    elif(clickedIn(event.x,event.y,data.width/2 - 250, data.height*2/6-20, data.width/2+250, data.height*2/6+20)):
        data.word = ""
        letterList = list(string.punctuation + " ")
        data.word = getLetters(data.currentUser.statDic, letterList, 145)
        data.mode = "level22"
        refreshObjects(data)
    elif(clickedIn(event.x, event.y,data.width/2 - 250, data.height*3/6-20, data.width/2+250, data.height*3/6+20)):
        data.word = ""
        letterList = list(string.ascii_uppercase)
        data.word = getLetters(data.currentUser.statDic, letterList, 145, False)
        data.mode = "level23"
        refreshObjects(data)
    elif(clickedIn(event.x, event.y,1050,50,1175,100)):
        data.mode = "Levels"


def Part2KeyPressed(event, data):
    pass

def Part2TimerFired(data):
    pass

def Part2RedrawAll(canvas, data):
    background = data.background
    canvas.create_image(0, 0, anchor = NW, image = background)
    canvas.create_rectangle(data.width/2 - 250, data.height/6-20, data.width/2+250, data.height/6+20, fill = "grey", outline = "orange")
    canvas.create_text(data.width/2, data.height/6, text = "Numeric Characters", font="Courier 26")
    canvas.create_rectangle(data.width/2 - 250, data.height*2/6-20, data.width/2+250, data.height*2/6+20, fill = "grey", outline = "orange")
    canvas.create_text(data.width/2, data.height*2/6, text ="Special Characters",font="Courier 26")
    canvas.create_rectangle(data.width/2 - 250, data.height*3/6-20, data.width/2+250, data.height*3/6+20, fill = "grey", outline = "orange")
    canvas.create_text(data.width/2, data.height*3/6, text = "Using the Shift",font="Courier 26")
    canvas.create_rectangle(1050,50,1175,100,fill = "grey")
    canvas.create_text(1060,55,text = "Back", anchor = NW, font = "Courier 26", width = 0)

####################################
#advanced
####################################
def Part3MousePressed(event, data):
    if(clickedIn(event.x, event.y,data.width/2 - 250, data.height/6-20, data.width/2+250, data.height/6+20)):
        data.word = ""
        data.currentWords = []
        refreshObjects(data)
        getSimpleWords(data,30, "easy")
        data.mode = "level31"
        refreshObjects(data)
    elif(clickedIn(event.x,event.y,data.width/2 - 250, data.height*2/6-20, data.width/2+250, data.height*2/6+20)):
        data.word = ""
        data.currentWords = []
        getSimpleWords(data,16, "hard")
        data.mode = "level32"
        refreshObjects(data)
    elif(clickedIn(event.x, event.y,data.width/2 - 250, data.height*3/6-20, data.width/2+250, data.height*3/6+20)):
        data.word = ""
        data.currentWords = []
        getSimpleWords(data,20, "all")
        data.mode = "level33"
        refreshObjects(data)
    elif(clickedIn(event.x, event.y,1050,50,1175,100)):
        data.mode = "Levels"


def Part3KeyPressed(event, data):
    pass

def Part3TimerFired(data):
    pass

def Part3RedrawAll(canvas, data):
    background = data.background
    canvas.create_image(0, 0, anchor = NW, image = background)
    canvas.create_rectangle(data.width/2 - 250, data.height/6-20, data.width/2+250, data.height/6+20, fill = "grey", outline = "orange")
    canvas.create_text(data.width/2, data.height/6, text = "Small Words", font="Courier 26")
    canvas.create_rectangle(data.width/2 - 250, data.height*2/6-20, data.width/2+250, data.height*2/6+20, fill = "grey", outline = "orange")
    canvas.create_text(data.width/2, data.height*2/6, text ="Larger Words",font="Courier 26")
    canvas.create_rectangle(data.width/2 - 250, data.height*3/6-20, data.width/2+250, data.height*3/6+20, fill = "grey", outline = "orange")
    canvas.create_text(data.width/2, data.height*3/6, text = "Review!",font="Courier 26")
    canvas.create_rectangle(1050,50,1175,100,fill = "grey")
    canvas.create_text(1060,55,text = "Back", anchor = NW, font = "Courier 26", width = 0)
####################################
#level11
####################################

def level11MousePressed(event, data):
    clickOut(event,data)
def level11KeyPressed(event, data):
    analyzeKey(event,data)
    
def level11TimerFired(data):
    if(not data.done):
        atTimerFired(data)

def level11RedrawAll(canvas, data):
    drawScreen(canvas,data)
    
####################################
#level12
####################################
def level12MousePressed(event, data):
    clickOut(event,data)
def level12KeyPressed(event, data):
    analyzeKey(event,data)

def level12TimerFired(data):
    if(not data.done):
        atTimerFired(data)


def level12RedrawAll(canvas, data):
    drawScreen(canvas,data)

####################################
#level13
####################################
def level13MousePressed(event, data):
    clickOut(event,data)
def level13KeyPressed(event, data):
    analyzeKey(event,data)

def level13TimerFired(data):
    if(not data.done):
        atTimerFired(data)

def level13RedrawAll(canvas, data):
    drawScreen(canvas,data)

####################################
#level21
####################################
def level21MousePressed(event, data):
    clickOut(event,data)
def level21KeyPressed(event, data):
    analyzeKey(event,data)

def level21TimerFired(data):
    if(not data.done):
        atTimerFired(data)


def level21RedrawAll(canvas, data):
    drawScreen(canvas,data)

####################################
#level22
####################################
def level22MousePressed(event, data):
    clickOut(event,data)
def level22KeyPressed(event, data):
    analyzeKey(event,data)

def level22TimerFired(data):
    if(not data.done):
        atTimerFired(data)


def level22RedrawAll(canvas, data):
    drawScreen(canvas,data)

####################################
#level23
####################################
def level23MousePressed(event, data):
    clickOut(event,data)
def level23KeyPressed(event, data):
    analyzeKey(event,data)

def level23TimerFired(data):
    if(not data.done):
        atTimerFired(data)


def level23RedrawAll(canvas, data):
    drawScreen(canvas,data)

####################################
#level31
####################################
def level31MousePressed(event, data):
    clickOut(event,data)

def level31KeyPressed(event, data):
    analyzeKey(event,data)

def level31TimerFired(data):
    if(not data.done):
        atTimerFired(data)


def level31RedrawAll(canvas, data):
    drawScreen(canvas,data) 

####################################
#leve32
####################################
def level32MousePressed(event, data):
    clickOut(event,data)
def level32KeyPressed(event, data):
    analyzeKey(event,data)


def level32TimerFired(data):
    if(not data.done):
        atTimerFired(data)

def level32RedrawAll(canvas, data):
    drawScreen(canvas,data)

####################################
#level33
####################################
def level33MousePressed(event, data):
    clickOut(event,data)
def level33KeyPressed(event, data):
    analyzeKey(event,data)

def level33TimerFired(data):
    if(not data.done):
        atTimerFired(data)

def level33RedrawAll(canvas, data):
    drawScreen(canvas,data)

###################################
#Stats Page
###################################

def statsMousePressed(event,data):
    if(clickedIn(event.x, event.y,1000,600,1125,640)):
        data.mode = "Levels"
    print(data.currentUser.statistics)

def statsKeyPressed(event,data):
    pass

def statsTimerFired(data):
    pass

def statsRedrawAll(canvas,data):
    canvas.create_rectangle(0,0,data.width,data.height,fill = "black")
    x1beginning = 50
    x1end = 550
    y1beginning = 550
    y1end = 50
    x2beginning = 650
    x2end = 1150
    y2beginning = 550
    y2end = 50

    canvas.create_line(x1beginning,y1end,x1beginning,y1beginning, fill = "white")
    canvas.create_line(x1beginning,y1beginning, x1end,y1beginning, fill = "white")
    x1prev = x1beginning
    y1prev = y1beginning
    for key in data.currentUser.statistics:
        x1= ((x1end- x1beginning)*key)/len(data.currentUser.statistics) + x1beginning
        y1 = y1beginning-((y1beginning-y1end)*data.currentUser.statistics[key][0])
        if(key == len(data.currentUser.statistics)-1):
            canvas.create_text(x1-10,y1,anchor = SW, text = "Accuracy: "+ str(round(data.currentUser.statistics[key][0], 3)*100)+ "%", fill = "white", font = "Courier 14")
        canvas.create_oval(x1-4, y1 -4, x1+4, y1+4, fill = "orange")
        canvas.create_line(x1prev,y1prev,x1,y1,fill = "white")
        x1prev = x1
        y1prev = y1
    x2prev = x2beginning
    y2prev = y2beginning
    for key in data.currentUser.statistics:
        x2 = ((x2end- x2beginning)*key)/len(data.currentUser.statistics) + x2beginning
        y2 = y2beginning-(((y2beginning-y2end)*data.currentUser.statistics[key][1])/100)
        canvas.create_oval(x2-4, y2 -4, x2+4, y2+4, fill = "orange")
        if(key == len(data.currentUser.statistics)-1):
            canvas.create_text(x2-10,y2,anchor = SW, text = "WPM:"+ str(data.currentUser.statistics[key][1]), fill = "white", font = "Courier 14")
        canvas.create_line(x2prev,y2prev,x2,y2,fill = "white")
        x2prev = x2
        y2prev = y2

    canvas.create_line(x2beginning,y2end,x2beginning,y2beginning, fill = "white")
    canvas.create_line(x2beginning,y2beginning, x2end,y2beginning,fill = "white")
    canvas.create_text(70,570, anchor = NW, text = "WPM", fill = "white",font ="Courier 20")
    canvas.create_text(650,570,anchor = NW, text = "Accuracy", fill = "white", font = "Courier 20")
    canvas.create_text(10,10, anchor = NW, text = "Hello " + data.currentUser.username+", this page indicates your progress!", font = "Courier 26", fill = "orange")
    canvas.create_rectangle(1000,600,1125,640, fill = "grey")
    canvas.create_text(1005,605, anchor = NW, text = "Main Menu", font = "Courier 18")

####################################
#Classes and Methods
####################################


##################
#Alphabet Object
##################
class Alphabet(object):
    def __init__(self,letter):
        self.letter = letter
        self.color = "white"
        rightHand1 = "yhnujm67&^"
        rightHand2 = "ik8*"
        rightHand3 = "ol9("
        rightHand4 = "p0-+[];'/.,)-_+=}]{[|:?" + "\\" + "\""
        leftHand1 = "tgbrfv45$%"
        leftHand2 = "edc3#"
        leftHand3 = "wsx2@"
        leftHand4 = "qaz1~`!"
        if(self.letter in rightHand1 or self.letter in rightHand1.upper()):
            self.hand = "right"
            self.finger = 1
            self.fingerString = rightHand1
        elif(self.letter in rightHand2 or self.letter in rightHand2.upper()):
            self.hand = "right"
            self.finger = 2
            self.fingerString = rightHand2
        elif(self.letter in rightHand3 or self.letter in rightHand3.upper()):
            self.hand = "right"
            self.finger = 3
            self.fingerString = rightHand3
        elif(self.letter in rightHand4 or self.letter in rightHand4.upper()):
            self.hand = "right"
            self.finger = 4
            self.fingerString = rightHand4
        elif(self.letter in leftHand1 or self.letter in leftHand1.upper()):
            self.hand = "left"
            self.finger = 1
            self.fingerString = leftHand1
        elif(self.letter in leftHand2 or self.letter in leftHand2.upper()):
            self.hand = "left"
            self.finger= 2
            self.fingerString = leftHand2
        elif(self.letter in leftHand3 or self.letter in leftHand3.upper()):
            self.hand = "left"
            self.finger = 3
            self.fingerString = leftHand3
        elif(self.letter in leftHand4 or self.letter in leftHand4.upper()):
            self.hand = "left"
            self.finger = 4
            self.fingerString = leftHand4
        elif(self.letter == " "):
            self.hand = "right"
            self.finger = 0
            self.fingerString = " "

    def typed(self, typed):
        if self.letter == typed:
            return True
        elif(self.letter == "??"):
            return True
        elif(typed == "space" and self.letter == " "):
            return True
        elif(typed=="comma" and self.letter == ","):
            return True
        elif(typed == "slash" and self.letter == "/"):
            return True
        elif(typed == "period" and self.letter == "."):
            return True
        elif((typed == "quoteright" or typed == "quoteleft") and self.letter == "'"):
            return True
        elif(typed == "semicolon" and self.letter == ";"):
            return True
        elif(typed == "exclam" and self.letter == "!"):
            return True
        elif(typed == "at" and self.letter == "@"):
            return True
        elif(typed == "numbersign" and self.letter == "#" ):
            return True
        elif(typed == "dollar"and self.letter == "$" ):
            return True
        elif(typed == "percent" and self.letter == "%"):
            return True
        elif(typed == "asciicircum" and self.letter == "^"):
            return True 
        elif(typed == "ampersand" and self.letter == "&"):
            return True
        elif(typed == "asterisk" and self.letter == "*"):
            return True
        elif(typed == "parenleft" and self.letter == "("):
            return True
        elif(typed == "parenright" and self.letter == ")"):
            return True
        elif(typed =="underscore" and self.letter == "_"):
            return True
        elif(typed == "plus" and self.letter == "+"):
            return True
        elif(typed == "minus" and self.letter == "-"):
            return True
        elif(typed == "equal" and self.letter == "="):
            return True
        elif(typed == "backslash" and self.letter == "\\"):
            return True
        elif(typed == "bar" and self.letter == "|"):
            return True
        elif(typed == "bracketright" and self.letter == "]"):
            return True
        elif(typed == "braceright" and self.letter == "}"):
            return True
        elif(typed == "bracketleft" and self.letter == "["):
            return True
        elif(typed == "bracketleft" and self.letter == "]"):
            return True
        elif(typed == "question" and self.letter == "?"):
            return True
        elif(typed == "colon" and self.letter == ":"):
            return True
        elif(typed == "quotedbl" and self.letter == "\""):
            return True
        elif(typed == "greater" and self.letter == ">"):
            return True
        elif(typed == "less" and self.letter == "<" ):
            return True
        elif(typed == "asciitilde" and self.letter == "~"):
            return True
        elif(typed == "quoteleft" and self.letter == "`"):
            return True
        else:
            return False

    def draw(self,canvas,x,y):
        canvas.create_text(x, y, text = self.letter, fill = self.color, font = "Courier 26")

    def drawFingerCircle(self,canvas,data):
        if(self.hand == "right"):
                canvas.create_oval(data.rightHandCoordinates[self.finger][0]-15,data.rightHandCoordinates[self.finger][1]-15,data.rightHandCoordinates[self.finger][0]+15,data.rightHandCoordinates[self.finger][1]+15, outline= "orange", width = 3)
        elif(self.hand =="left"):
            canvas.create_oval(data.leftHandCoordinates[self.finger][0]-15,data.leftHandCoordinates[self.finger][1]-15,data.leftHandCoordinates[self.finger][0]+15,data.leftHandCoordinates[self.finger][1]+15, outline = "orange",width = 3)



##############
#USER CLASS 
##############

class User(object):
    def __init__(self,username):
        self.username = username
        self.statDic = dict()
        charList = list(string.ascii_lowercase + string.digits + string.punctuation)
        for char in charList:
            self.statDic[char]=1
        self.wordDic = setSimpleWords()
        self.wordList = []
        for key in self.wordDic:
            self.wordList.append(key)
        
        self.statistics = dict()
        self.statistics[0] = (0,0)
        self.session = 0



    def updateDictionary(self,c, cBefore1, cBefore2, fingerString):
        if(c == "Space"):
            c = " "
        if(cBefore1 == "Space"):
            cBefore1 = " "
        if(cBefore2 == "Space"):
            cBefore2 = " "
        for char in fingerString:
            if(char not in self.statDic):
                self.statDic[char] = 1
            else:
                self.statDic[char] +=1
        bigram = cBefore1 + c 
        if(bigram not in self.statDic):
            self.statDic[bigram] = 2
        else:
            self.statDic[bigram] +=2
        trigram = cBefore2+cBefore1+c
        if(trigram not in self.statDic):
            self.statDic[trigram] = 3
        else:
            self.statDic[trigram] +=3


    def updateWordDictionary(self,c, word,fingerString, cBefore1 = "", cBefore2 = "", cBefore3 = ""):
        self.wordDic[word] +=1
        self.statDic[c.lower()] +=1
        updateList1 = findLikeWords(word,self.wordList,1)
        for i in updateList1:
            print(i)
            self.wordDic[i] +=30
        updateList2 = findLikeWords(word,self.wordList,2)
        for j in updateList2:
            self.wordDic[j] += 10
        updateList3 = findLikeWords(word,self.wordList,3)
        for k in updateList3:
            self.wordDic[k] +=5
        addLetters(self.wordDic, self.statDic, c)
        trigram = cBefore2+cBefore1+c
        
        for word in self.wordDic:
            if trigram in word:
                self.wordDic[word]+=10
        fourgram = cBefore3 + cBefore2 + cBefore1 + c
        for wor in self.wordDic:
            if fourgram in wor:
                self.wordDic[wor] +=30




    def updateAddDictionary(self,c,cBefore1,cBefore2,fingerString):
        if(c == "Space"):
            c = " "
        if(cBefore1 == "Space"):
            cBefore1 = " "
        if(cBefore2 == "Space"):
            cBefore2 = " "
        for char in fingerString:
            if(char in self.statDic and self.statDic[char]>20):
                self.statDic[char]-=20
        bigram = cBefore1 + c 
        if(bigram in self.statDic and self.statDic[bigram]>5):
            self.statDic[bigram] -=5

        trigram = cBefore2+cBefore1+c
        if(trigram in self.statDic and self.statDic[trigram]>5):
            self.statDic[trigram] -= 5

    def updateAddWordDictionary(self,c,word,fingerString):
        if(self.wordDic[word]>1):
            self.wordDic[word] -=1
        if(self.statDic[c.lower()]>1):
            self.statDic[c.lower()] -=1
        
        updateList = findLikeWords(word,self.wordList,2)
        for i in updateList:
            if(self.wordDic[i]>1):
                self.wordDic[i] -=1


        


###############
#OBJECT SAVING STUFF
###############
def atTimerFired(data):
    data.start+=1
    data.wpm = getWPM(data)
    data.wpmList.append(data.wpm)


def dump(myList):
    f = open('usrobj.obj', 'w')
    for obj in myList:
        cPickle.dump(obj, f, protocol=cPickle.HIGHEST_PROTOCOL)
    f.close()

def load(numObjects): #adapted from http://deeplearning.net/software/theano/tutorial/loading_and_saving.html
    f = open('usrobj.obj', 'rb')
    loaded_objects = []
    for i in range(numObjects):
        loaded_objects.append(cPickle.load(f))
    f.close()
    return loaded_objects


#Taken from Kosbie's notes 
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)



def clickedIn(x,y,x1,y1,x2,y2):
    if(x1<x<x2 and y1<y<y2):
        return True 
    else:
        return False

def getError(right, wrong):
    rr = 0 
    rc = 0 
    wr = 0 
    wc = 0 
    l = [   ["1","2","3","4","5","6","7","8","9","0","-","+"],
            ["q","w","e","r","t","y","u","i","o","p","[","]"],
            ["a","s","d","f","g","h","j","k","l",":","'"],
            ["z","x","c","v","b","n","m",",",".","/"],
            ["space"]
        ]
    for r in range(len(l)):
        x = len(l[r])
        for c in range(x):
            if(l[r][c] == right):
                rr = r 
                rc = c
            if(l[r][c]== wrong):
                wr = r
                wc = c 
    rError = rr - wr 
    cError = rc - wc 
    if(cError<0):
        cErrorS = "Right"
        cErrorNum = str(abs(cError))
    else:
        cErrorS = "Left"
        cErrorNum = str(abs(cError))
    if(rError <0):
        rErrorS = "Down"
        rErrorNum = str(abs(rError))
    else:
        rErrorS = "Up" 
        rErrorNum = str(abs(rError))
    return (rErrorS, rErrorNum, cErrorS, cErrorNum)


def drawScreen(canvas,data):
    canvas.create_rectangle(0,0,data.width, data.height,fill = "black")
    rimage = data.rightHand
    limage = data.leftHand
    kb = data.keyboard
    canvas.create_image(data.width*3/4, data.height/2+90, anchor = W, image = rimage)
    canvas.create_image(data.width/4, data.height/2+90, anchor = E, image = limage)
    canvas.create_image(data.width*3/11, data.height/2 + 90, anchor =W, image = kb)
    canvas.create_rectangle(data.width/6, 90, data.width*5/6, 440, outline = "white")
    if(data.i < len(data.word)):
        data.objects[data.i].drawFingerCircle(canvas,data)
        canvas.create_rectangle(data.keyboardCoordinates[data.objects[data.i].letter.lower()], outline = "orange", width = 3)
        if(data.objects[data.i].letter in "~!@#$%^&*()_+}{|:?><?" + "\"" + string.ascii_uppercase):
            canvas.create_rectangle(data.keyboardCoordinates["Shift"], outline = "orange", width = 3)
    canvas.create_text(data.width/3-10, data.height/10-20, text = "Accuracy: " +str(round(data.accuracy,3)*100) + "%", fill = "white",font = "Courier 26")
    canvas.create_text(data.width/2+150, data.height/10-20, text = "Speed: " + str(data.wpm), fill = "white",font = "Courier 26")
    x = data.width/6 + 40
    y = 150
    for obj in data.objects:
        obj.draw(canvas,x,y)
        x+=20
        if(x> data.width*5/6-40):
            x = data.width/6 + 40
            y+= 70
    canvas.create_rectangle(data.placeHolder, outline = "white")
    for i in range(2, 6):
        canvas.create_line(data.width/6 + 30, 70*i +25, data.width*5/6 - 30, 70*i +25, fill = "white")

    canvas.create_rectangle(1050,50,1175,100,fill = "grey")
    canvas.create_text(1060,55,text = "Back", anchor = NW, font = "Courier 26", width = 0)

    canvas.create_rectangle(25,50,150,100,fill = data.soundOnColor)
    canvas.create_text(35,55,text = "Sound", anchor = NW, font = "Courier 26", width = 0)
    if(data.done):
        
        canvas.create_rectangle(data.width/3, 100, data.width*2/3, 500, fill = "grey", width = 6)
        canvas.create_rectangle(data.width*2/5,150, data.width*3/5, 250, fill = "orange")
        canvas.create_text(data.width*2/5+39,190, anchor = NW, text = "Stats", font = "Courier 34")
        canvas.create_text(data.width/2, data.height/2-60, text = "Accuracy " + str(round(data.accuracy,4)*100) +"%", font = "Courier 20")
        avg = 0 
        avg = avgWPM(data.wpmList)
        canvas.create_text(data.width/2,data.height/2-30, text = "Average Words Per Minute: " + str(avg), font = "Courier 20")
        if(data.currentUser.session in data.currentUser.statistics and data.currentUser.statistics[data.currentUser.session] != (0,0)):
            data.currentUser.statistics[data.currentUser.session] = ((data.currentUser.statistics[data.currentUser.session][0] + data.accuracy)/2.0, (data.currentUser.statistics[data.currentUser.session][1] + avg)/2.0)
        else:
            data.currentUser.statistics[data.currentUser.session] = (data.accuracy,avg)


def avgWPM(lst):
    if(len(lst)!=0):
        total = 0 
        for x in lst:
            total +=int(x)
        return total/len(lst)
    else:
        return None



def clickOut(event,data):
    print(data.currentUser.statistics)
    if(clickedIn(event.x, event.y,1050,50,1175,100)):
        data.mode = "Levels"
        avg = avgWPM(data.wpmList)
        if(data.currentUser.session in data.currentUser.statistics and data.currentUser.statistics[data.currentUser.session] != (0,0)):
            data.currentUser.statistics[data.currentUser.session] = ((data.currentUser.statistics[data.currentUser.session][0] + data.accuracy)/2.0, (data.currentUser.statistics[data.currentUser.session][1] + avg)/2.0)
        else:
            data.currentUser.statistics[data.currentUser.session] = (data.accuracy,avg)
        data.done = False
    if(clickedIn(event.x, event.y,25,50,150,100)):
        if(data.soundOn == False):
            data.soundOn = True
            data.soundOnColor = "orange"
        else:
            data.soundOn = False
            data.soundOnColor = "grey"
    if(data.done and clickedIn(event.x, event.y, data.width*2/5,150, data.width*3/5, 250)):
        data.done = False
        data.mode = "stats"


def refreshObjects(data):
    data.objects = []
    data.i = 0
    for x in data.word:
        data.objects.append(Alphabet(x))
    data.a = 0 
    data.b = 0 
    data.start = 0
    data.placeHolder = (data.width/6+28, 135, data.width/6+49, 165)
    data.accuracy = 0
    data.wpm = 0
    data.wordnum = 0

def getWPM(data):
    if(data.wpm == None):
        return round(60.0/float(data.start))
    else:
        if(data.start == 0):
            return 
        return round((data.wpm + (60.0/float(data.start)))/2.0)

def analyzeKey(event,data):
    data.a +=1
    if(data.i >len(data.word)-1):
        data.done  = True

    elif (data.objects[data.i].typed(event.keysym)):
        data.objects[data.i].color = "green"
        data.b +=1
        if(data.soundOn):
            getNextSound(data.objects[data.i+1].letter)
        if(event.keysym == "space"): # TO GET WPM 
            data.wordnum +=1
            data.start = 0
        if(data.placeHolder[2]<data.width*5/6-40):
            data.placeHolder = (data.placeHolder[0]+20, data.placeHolder[1], data.placeHolder[2]+20, data.placeHolder[3])
        else:
            data.placeHolder = (data.width/6+28, data.placeHolder[1]+70, data.width/6+48, data.placeHolder[3]+70)
        c = data.objects[data.i].letter
        cBefore1 = data.objects[data.i-1].letter
        cBefore2 = data.objects[data.i-2].letter
        data.currentUser.updateAddDictionary(c, cBefore1,cBefore2,data.objects[data.i].fingerString)
        if(data.mode =="level32" or data.mode == "level33" or data.mode == "level31"):
            word = data.currentWords[data.wordnum]
            data.currentUser.updateAddWordDictionary(c,word,data.objects[data.i].fingerString)
        data.i +=1

    
    elif(not data.objects[data.i].typed(event.keysym)): #not correct letter
        data.objects[data.i].color = "red"
        data.error = getError(event.keysym, data.objects[data.i].letter)
        if(data.soundOn):
            updown = data.error[0]
            updowndir = data.error[1]
            leftright = data.error[2]
            leftrightdir = data.error[3]
            getNextSound("Move " + updown + " " + updowndir + " and " + leftright + " " + leftrightdir)
        c = data.objects[data.i].letter
        if(data.i>=1):
            cBefore1 = data.objects[data.i-1].letter
        if(data.i>=2):
            cBefore2 = data.objects[data.i-2].letter
        if(data.i>=3):
            cBefore3 = data.objects[data.i-3].letter
        data.currentUser.updateDictionary(c, cBefore1,cBefore2,data.objects[data.i].fingerString)
        if(data.mode =="level32" or data.mode == "level33" or data.mode == "level31"):
            word = data.currentWords[data.wordnum]
            data.currentUser.updateWordDictionary(c,  word, data.objects[data.i].fingerString, cBefore1, cBefore2, cBefore3)
    
    data.accuracy = float(data.b)/float(data.a)



def getNextSound(phrase):       
    os.system("/usr/bin/say " + phrase)


def setWord(data, letterList):
    for i in range(30):
        data.word += random.choice(letterList)

################################
#ML
################################

def getLetters(dictionary,charsToChooseFrom, num, lower = True):
    x = 0 
    randList = []
    string = ""
    lowerList = []
    for c in charsToChooseFrom:
        lowerList.append(c.lower())

    for key in dictionary:
        if(key in lowerList):
            for i in range(int(dictionary[key]*100)):
                if(lower):
                    randList.append(key)
                else:
                    randList.append(key.upper())
    
    for x in range(num):
        y = random.randrange(3,5)
        if(x%y == 0 and x!=0):
            string += " "
        else:
            string += random.choice(randList)
    return string 


##########################################################################
# Read/Write File, get random words
##########################################################################

def setSimpleWords():
    content = readFile("words.txt")
    myDic = dict()
    for line in content.splitlines():
        myDic[line] = 1

    return myDic

def getSimpleWords(data, num, level):
    chooseFrom = []
    for key in data.currentUser.wordDic:
        if(len(key)>6 and level == "hard"):
            for i in range(int(data.currentUser.wordDic[key]*10)):
                chooseFrom.append(key)
        elif(len(key)<6 and level == "easy"):
            for i in range(int(data.currentUser.wordDic[key]*10)):
                chooseFrom.append(key)
        elif(level == "all"):
            for i in range(int(data.currentUser.wordDic[key]*10)):
                chooseFrom.append(key)
    
    for x in range(num):
        newWord = random.choice(chooseFrom)
        data.word += newWord
        data.currentWords.append(newWord)

    data.word = data.word.strip()



#########################
#Getting Like-Words - Algorithm based on Keystroke
#########################
def keystroke(word):
    l = [   ["1","2","3","4","5","6","7","8","9","0","-","+"],
            ["q","w","e","r","t","y","u","i","o","p","[","]"],
            ["a","s","d","f","g","h","j","k","l",":","'"],
            ["z","x","c","v","b","n","m",",",".","/"],
            ["space"]
        ]
    strokeList = []
    for letter in word.lower()[1:]:
        strokeList.append(getCoordinates(letter, l))
    return strokeList 


def getCoordinates(l,keyboard):
    for row in range(len(keyboard)):
        for col in range(len(keyboard[row])):
            if(keyboard[row][col] ==l):
                return (row,col)

def findLikeWords(word, wordList,delta): #find words with like strokes
    result = []
    dictionary = dict()
    wordkeystroke = keystroke(word)
    addWord = None
    for wor in wordList:
        dictionary[wor] = keystroke(wor)
    for key in dictionary:
        if(len(dictionary[key])>=len(wordkeystroke)):
            for subset in range(len(dictionary[key])-len(wordkeystroke)+1):
                compare = dictionary[key][subset:subset+len(wordkeystroke)]

                for i in range(len(compare)):
                    crow = dictionary[key][i+subset][0]
                    ccol = dictionary[key][i+subset][1]
                    wrow = wordkeystroke[i][0]
                    wcol = wordkeystroke[i][1]
                    if(abs(crow-wrow)<delta and abs(wrow-wcol)<delta):
                        addWord = True
                    else:
                        addWord = None
            if(addWord):
                result.append(key)
                addWord = None
    return result

########################################################################
#Using mistakes in past words to increase likelyhood to get those words
########################################################################

def addLetters(worddictionary,letterdictionary, c):
    for word in worddictionary:
        if letterCount(word,c) == 5:
            letterdictionary[c.lower(data.currentUser.statistics[key][0])] +=5
        elif(letterCount(word,c) == 4):
            letterdictionary[c.lower()] +=4
        elif(letterCount(word,c)== 3):
            letterdictionary[c.lower()] +=3
        elif(letterCount(word,c)==2):
            letterdictionary[c.lower()] +=2
        elif(letterCount(word,c)==1):
            letterdictionary[c.lower()] +=1

def letterCount(word,c):
    count = 0
    for char in word:
        if char == c:
            count+=1

    return count

#########################################################################
# use the run function as-is, taken from Kosbie's Animation Lecture Notes
#########################################################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)

    def motionWrapper(event,canvas,data):
        motion(event,data)
        redrawAllWrapper(canvas,data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 1000 # milliseconds
    root = Tk()
    init(data)
    # create the root and the canvas
    global canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up eventss
    root.bind("<Motion>", lambda event: motionWrapper(event,canvas,data))
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.bind("<")

    root.mainloop()  # blocks until window is closez
    dump(data.usrObjects)
    print("bye!")

run(1200, 900)