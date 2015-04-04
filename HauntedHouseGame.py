import random
from java.awt import Font
from javax.swing import JFrame
from javax.swing import JPanel
from javax.swing import JLabel

#create a function that will create a custom java window whenever we want, it will expect text in the form of a global variable called "mytext" to complete the window
def hhwindow(): #creates a function called hhwindow, this is a function we will call whenever we want to create a new window
   global win,mytext #the global statement creates variables “win” and “mytext” that can be referenced outside of just this function
   win = swing.JFrame("Inside the Haunted House")  #creates a window as a variable we named “win”, the title of the window is inside the quotes
   panel = JPanel() #creates a panel inside the window for text as a variable we named “panel”
   panel.setLayout(None) #controls layout of panel
   panel.setBackground(Color(0, 0, 0)) #sets background color of window
   win.setSize(600,400) #sets window size
   win.setVisible(True) #makes window visible
   mytextLabel = JLabel(mytext) #adds text to the window in the form of a variable, yet to be defined, called “mytext”
   mytextLabel.setBounds(20, 20, 500, 400) #sets boundaries for the text, text will be centered by default within these boundaries
   panel.add(mytextLabel) #add the label to the panel
   win.add(panel) #add the panel to the window
   win.show() #show the window

#create a function that will allow the user to exit the game whenever they want
def earlyExit(): #creates a function named early exit
    win.dispose() #closes the window created by hhwindow()
    showInformation("Too bad.  Game over. "+playerName+" is a scared wimp. Goodbye!") #display a parting insult to the user who quits

#create a function that starts the game
def start(): #creates a function named start, that will all the user to start playing the game
  global mytext #create a global variable that can be used outside this function named mytext
  mytext="""<HTML> <font size="4" color="red"> <p>Welcome to The Haunted House! <br> 
  A text-based game created in COMS 1411 Spring 2013.</p> </font></HTML>"""
  hhwindow() #call the function to create the window
  global playerName #create a global variable named playerName, to store the users name
  playerName=requestString("What is your name?")
  porch()  #call the porch function after the start function

def porch(): #creates the porch function
  win.dispose() #closes the previously created window to get ready for the new window
  global mytext #recreates my text to get ready to place new text in the window
  mytext="""<HTML> <font size="4" color="red"> <p>Late one night, you are driving down a dirt road in a deserted area.<br>
  Suddenly, your car breaks down. You try several times unsuccessfully to restart you car.<br>
  You have no cellphone service.  A storm is approaching.<br>
  You see a house in the distance and run there to take shelter.<br>
  You find yourself on the front porch of a rather scary house.<br>
  It has broken windows and an overall sinister feel.</p> </font></HTML>"""
  hhwindow() 
  enterHouse() #call the enterHouse() function

def enterHouse(): #create a function that allows users to enter the house or refuse (and quit the game)
  b=requestString("Do you want to enter the house "+playerName+"? (Enter yes or no)")
  if b=="yes":
    entryway() #call the entryway() room function is users say yes
  elif b=="no":
    earlyExit() #call the earlyExit() function if users say no
  else:
    showInformation("Not a valid response.") #repeat request for input if users type something other than yes or no
    enterHouse()

def entryway():
  win.dispose()
  global mytext
  mytext="""<HTML> <font size="4" color="red"> <p>You are in the entry way of the house. There are cobwebs in the corner.<br>
  Red rum is written on the wall in what appears to be blood.<br>
  There is a passageway to the north and another to the east.</p> </font></HTML>"""
  hhwindow()
  whichDirection1()
  
def whichDirection1():
  c=requestString(playerName+", do you want to go north, east, or quit""? (Type north, east, or quit)")
  if c=="north":
    kitchen()
  elif c=="east":
    livingroom()
  elif c=="quit":
    earlyExit()
  else:
    showInformation("Not a valid response.") 
    whichDirection1()


def kitchen():
  win.dispose()
  global mytext
  mytext="""<HTML> <font size="4" color="red"> <p> You are in the kitchen.  All the surfaces are covered with pots, pans, food pieces, and pools of blood. <br>
  You think you hear something up the stairs that go to the west side of the room.<br>
  It's a scraping noise, like something being dragged along the floor. </p> </font></HTML>"""
  hhwindow()
  whichDirection2()
  
def whichDirection2():
  c=requestString(playerName+", do you want to go south, east, or quit""? (Type south, east, or quit)")
  if c=="south":
    entryway()
  elif c=="east":
    diningroom()
  elif c=="stairs":
    attic()
  elif c=="quit":
    earlyExit()
  else:
    showInformation("Not a valid response.") 
    whichDirection2()
    

def attic():
  win.dispose()
  global mytext
  mytext="""<HTML> <font size="4" color="red"> <p> You are in the attic. </p> </font></HTML>"""
  hhwindow()
  R = random.choice([1,2,3,4,5,6,7,8,9,10]) # this assigns R the value of a randomly picked number between 1 and 10
  if R<7:
     whichDirection4() #if R<7, allow the user to continue playing the game (gives a 60% chance of the game continuing)
  elif R>7: #if R>7, kill the user, end the game (30% chance of player death)
     win.dispose() 
     showInformation("Something attacks from out of the shadows.  "+playerName+" is dead. Game over.")
  elif R==7: #if R=7, the user wins the game by finding a treasure (10% chance of winning)
     win.dispose()
     showInformation("You see something you didn't see at first: a bag in the corner.  \n A note on the bag: says "+playerName+" take this money leave and never tell anyone about this house or come back. \n You open the bag and find thousands of hundred dollar bills. \n You quickly leave the house walk 20 miles through the rain and escape with the money.")
     whichDirection2()

  


def diningroom():
  win.dispose()
  global mytext
  mytext="""<HTML> <font size="4" color="red"> <p> You are in the dining room.  There is the fresh remains of dinner on a table. <br>
  You don't know what it is and your not sure you want to know.<br>
  You hear what sounds like a distant scream. </p> </font></HTML>"""
  hhwindow()
  whichDirection3()


def whichDirection3():
  c=requestString(playerName+", do you want to go south, west, or quit""? (Type south, west, or quit)")
  if c=="south":
    livingroom()
  elif c=="west":
    kitchen()
  elif c=="quit":
    earlyExit()
  else:
    showInformation("Not a valid response.") 
    whichDirection3()
    
    


def livingroom():
  win.dispose()
  global mytext
  mytext="""<HTML> <font size="4" color="red"> <p> You are in the living room.  The photos on the wall seem to be staring at you. <br>
  You feel a cold breeze and light in the room seems to change.<br>
  There something wrapped in a blanket in the corner, about the size of a person. </p> </font></HTML>"""
  hhwindow()
  R = random.choice([1,2,3,4,5,6,7,8,9,10]) # this assigns R the value of a randomly picked number between 1 and 10
  if R<7:
     whichDirection4() #if R<7, allow the user to continue playing the game (gives a 60% chance of the game continuing)
  elif R>7: #if R>7, kill the user, end the game (30% chance of player death)
     win.dispose() 
     showInformation("Something attacks from out of the shadows.  "+playerName+" is dead. Game over.")
  elif R==7: #if R=7, the user wins the game by finding a treasure (10% chance of winning)
     win.dispose()
     showInformation("You see something you didn't see at first: a bag in the corner.  \n A note on the bag: says "+playerName+" take this money leave and never tell anyone about this house or come back. \n You open the bag and find thousands of hundred dollar bills. \n You quickly leave the house walk 20 miles through the rain and escape with the money.")
  

def whichDirection4():
  c=requestString(playerName+", do you want to go north, west, or quit""? (Type south, west, or quit)")
  if c=="north":
    diningroom()
  elif c=="west":
    entryway()
  elif c=="quit":
    earlyExit()
  else:
    showInformation("Not a valid response.") 
    whichDirection4()
