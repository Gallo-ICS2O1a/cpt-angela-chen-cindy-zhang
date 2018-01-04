# variables
cupC1 = color(255)
cupC2 = color(255)
cupC3 = color(255)
cupC4 = color(255)
cupC5 = color(255)
cupC6 = color(255)
cupC7 = color(255)
cupC8 = color(255)

clicked_colour = color(176,224,230)
cup1 = False
cup2 = False
cup3 = False
cup4 = False
cup5 = False
cup6 = False
cup7 = False 
cup8 = False

def setup():
    size(470, 770)

def draw():
    global cup_base
    global clicked_colour
    global cup1
    global cup2
    global cup3
    global cup4
    global cup5
    global cup6
    global cup7
    global cup8
    global cupC1
    global cupC2
    global cupC3
    global cupC4
    global cupC5
    global cupC6
    global cupC7
    global cupC8
    
    
    background(255)
    
    # icons at the bottom
    noStroke()
    # light green (diet)
    fill(216, 242, 104)
    rect(0, 670, 117.5, 100)
    # orange (exercise)
    fill(244, 176, 107)
    rect(117.5, 670, 117.5, 100)
    # mint green (progress)
    fill(174, 252, 223)
    rect(235, 670, 117.5, 100)
    # turquiose (hydration)
    fill(94, 193, 192)
    rect(352.5, 670, 117.5, 100)
    
    # hydration tracker
    noStroke
    
    fill(cupC1)
    rect(34, 200, 75, 175)
    if cup1 == True:
        cupC1 = clicked_colour 
        
    fill(cupC2)
    rect(140, 200, 75, 175)
    if cup2 == True:
        cupC2 = clicked_colour
        
    fill(cupC3)
    rect(245, 200, 75, 175)
    if cup3 == True:
        cupC3 = clicked_colour
        
    fill(cupC4)
    rect(350, 200, 75, 175)
    if cup4 == True:
        cupC4 = clicked_colour
        
    fill(cupC5)
    rect(34, 400, 75, 175)
    if cup5 == True:
        cupC5 = clicked_colour
     
    fill(cupC6)
    rect(140, 400, 75, 175)
    if cup6 == True:
        cupC6 = clicked_colour
     
    fill(cupC7)
    rect(245, 400, 75, 175)
    if cup7 == True:
        cupC7 = clicked_colour
    
    fill(cupC8)
    rect(350, 400, 75, 175)    
    if cup8 == True:
        cupC8 = clicked_colour
    
    
    # title
    textSize(70)
    fill(0)
    text(" hydration ", 10, 100)
    
    # original boxes
    for y in range(200, 525, 200):
        for x in range(34, 436, 105):
            stroke(155)
            noFill()
            rect(x, y, 75, 175)
            
    # numbers
    textSize(50)
    fill(0)
    text("1", 57, 300)
    text("2", 162, 300)
    text("3", 265, 300)
    text("4", 370, 300)
    text("5", 57, 500)
    text("6", 162, 500)
    text("7", 265, 500)
    text("8", 370, 500)
   
def mousePressed():
    global cup1
    global cup2
    global cup3
    global cup4
    global cup5
    global cup6
    global cup7
    global cup8
    
    
    if mouseX >= 34 and mouseX <= 109:
        if mouseY <= 375 and mouseY >= 200:
            cup1 = True
    
    if mouseX >= 143 and mouseX <= 218:
        if mouseY <= 375 and mouseY >= 200:
            cup2 = True
            
    if mouseX >= 252 and mouseX <= 327:
        if mouseY <= 375 and mouseY >= 200:
            cup3 = True
            
    if mouseX >= 361 and mouseX <= 436:
        if mouseY <= 375 and mouseY >= 200:
            cup4 = True
            
    if mouseX >= 34 and mouseX <= 109:
        if mouseY >= 445 and mouseY <= 620:
            cup5 = True
            
    if mouseX >= 143 and mouseX <= 218:
        if mouseY >= 445 and mouseY <= 620:
            cup6 = True
    
    if mouseX >= 252 and mouseX <= 327:
        if mouseY >= 445 and mouseY <= 620:
            cup7 = True
            
    if mouseX >= 361 and mouseX <= 436:
        if mouseY >= 445 and mouseY <= 620:
            cup8 = True
