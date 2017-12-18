home_width = 470
home_height = 150

def setup():
    size(470, 770)
    
def draw():
    global home_width
    global home_height
    
    
    background(255)
    noStroke()
    fill(255)
    rect(0, 0, 470, 770)
    fill(255, 147, 102)
    rect(30, 490, 410, home_height, 20)
    
    
    # logo

    fill(0)
    font1 = loadFont("HPSimplified-Regular-48.vlw")
    textFont(font1, 85)
    text(" beneFIT+ ", 60, 300)
    
    # survey
    fill(255)
    font2 = loadFont("NirmalaUI-Bold-48.vlw")
    textFont(font2, 50)
    text(" Take Survey ", 70, 585)
    

    # if mouseClicked:
    #     base_color = 100
        
def mouseClicked():
    if mouseY >= 490 and mouseY <= 640:
        base_color = 100