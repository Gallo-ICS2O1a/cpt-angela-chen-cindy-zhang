home_width = 470
home_height = 150

def setup():
    size(470, 770)
    
def draw():
    global home_width
    global home_height
    
    
    background(255)
    noStroke()
    fill(255, 147, 102)
    rect(0, 490, home_width, home_height)
    
    #logo
    textSize(85)
    fill(0)
    text(" beneFIT+ ", 20, 300)
    
    #survey
    textSize(70)
    fill(255)
    text(" Take Survey ", 15, 590)

def mouseClicked():
    if mouseY >= 490 and mouseY <= 640:

        
    
        
