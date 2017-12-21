home_width = 470
home_height = 150
page1 = True
page2 = False
page3A = False
page3B = False
page3C = False
pg1_orange = color(255, 147, 102)
pg1_text = color(255)
pg2_black = 0
pg2_grey1 = 0
pg2_grey2 = 0
pg2_grey3 = 0
pg2_white1 = 255
pg2_white2 = 255
pg2_white3 = 255
pg3_diet_button = color(216, 242, 104)
# pg3_exercise_button = color(
# pg3_


def setup():
    size(470, 770)
    
def draw():
    
    global pg2_grey1, pg2_grey2, pg2_grey3
    global pg2_white1, pg2_white2, pg2_white3 
    global pg1_orange, pg1_text
    
    background(255)
    noStroke()
    fill(255)
    background(255)
    
    # page 1
    if page1:
        # logo
        fill(0)
        font1 = loadFont("HPSimplified-Regular-48.vlw")
        textFont(font1, 85)
        text(" beneFIT+ ", 60, 300)
        
        # survey button
        fill(pg1_orange)
        rect(30, 440, 410, 150, 20)
        fill(pg1_text)
        font2 = loadFont("NirmalaUI-Bold-48.vlw")
        textFont(font2, 55)
        text(" Take Survey ", 60, 535)
        
        # survey when hover
        if mouseY >= 440 and mouseY <= 590:
            if mouseX <=440 and mouseX >= 30:
                pg1_orange = color(255, 181, 150)
                pg1_text = color(198, 93, 49)
        else:
            pg1_orange = color(255, 147, 102)
            pg1_text = 255
        

    # page 2
    elif page2:
        fill(100)
        font1 = loadFont("HPSimplified-Regular-48.vlw")
        textFont(font1, 50)
        text("beneFIT+", 40, 70)
    
        # question box
        fill(255, 147, 102)
        triangle(80, 80, 55, 100, 105, 100)
        rect(30,100,410,230,20)
        fill(255)
        font2 = loadFont("NirmalaUI-Bold-48.vlw")
        textFont(font2, 40)
        text("What is your goal?", 58, 235)
        
        
        # answer box 1
        fill(pg2_grey1)
        rect(30, 365, 410, 100, 20)
        font3 = loadFont("MicrosoftJhengHeiBold-48.vlw")
        fill(pg2_white1)
        textFont (font3, 30)
        text("A.", 60, 430)
        font4 = loadFont("MicrosoftJhengHeiRegular-48.vlw")
        textFont (font4, 30)
        text("Lose Weight", 150, 430)
        
        # answer box 1 when mouse hovers
        if mouseX <= 440 and mouseX >= 30 and mouseY >= 365 and mouseY <= 465:
            pg2_grey1 = 200
            pg2_white1 = 100
        else:
            pg2_grey1 = 100
            pg2_white1 = 255
        
        
        # answer box 2
        fill(pg2_grey2)
        rect(30, 500, 410, 100, 20)
        fill(pg2_white2)
        textFont (font3, 30)
        text("B.", 60, 565)
        textFont (font4, 30)
        text("Gain Muscle", 150, 565)
        
        # answer box 2 when mouse hovers
        if mouseX <= 440 and mouseX >= 30 and mouseY >= 500 and mouseY <= 600:
            pg2_grey2 = 200
            pg2_white2 = 100
        
        else:
            pg2_grey2 = 100
            pg2_white2 = 255
        
        # answer box 3
        fill(pg2_grey3)
        rect(30, 635, 410, 100, 20)
        fill(pg2_white3)
        textFont (font3, 30)
        text("C.", 60, 700)
        textFont (font4, 30)
        text("Be Fit Overall", 150, 700)
        
        # answer box 3 when mouse hovers
        if mouseX <= 440 and mouseX >= 30 and mouseY >= 635 and mouseY <= 735:
            pg2_grey3 = 200
            pg2_white3 = 100
        else:
            pg2_grey3 = 100
            pg2_white3 = 255
            
    if page3A:
        # logo
        background(255)
        fill(100)
        font1 = loadFont("HPSimplified-Regular-48.vlw")
        textFont(font1, 50)
        text("beneFIT+", 40, 70)
        fill(0)
        textSize(45)
        text("A. Lose Weight", 40, 130)
        
        # diet
        noStroke()
        fill(pg3_diet_button)
        rect(30, 200, 200, 200, 20)
        fill(255)
        textSize(40)
        text("DIET", 94, 320)
        
        # diet hover
        # if mouseX >= 30 and mouseX <= 320:
        #     if mouseY >= 200 and mouseY <= 400:
                
        # EXERCISE
        fill(244, 176, 107)
        rect(240, 200, 200, 200, 20)
        fill(255)
        textSize(40)
        text("EXERCISE", 263, 320)
        
        # PROGRESS
        fill(174, 252, 223)
        rect(30, 410, 200, 200, 20)
        fill(255)
        textSize(40)
        text("PROGRESS", 43, 530)
        
        # HYDRATION
        fill(94, 193, 192)
        rect(240, 410, 200, 200, 20)
        fill(255)
        textSize(40)
        text("HYDRATION", 245, 530)
    if page3B:
        # logo
        background(255)
        fill(100)
        font1 = loadFont("HPSimplified-Regular-48.vlw")
        textFont(font1, 50)
        text("beneFIT+", 40, 70)
        fill(0)
        textSize(45)
        text("B. Gain Muscle", 40, 130)
        
        # DIET
        noStroke()
        fill(216, 242, 104)
        rect(30, 200, 200, 200, 20)
        fill(255)
        textSize(40)
        text("DIET", 94, 320)
        
        # EXERCISE
        fill(244, 176, 107)
        rect(240, 200, 200, 200, 20)
        fill(255)
        textSize(40)
        text("EXERCISE", 263, 320)
        
        # PROGRESS
        fill(174, 252, 223)
        rect(30, 410, 200, 200, 20)
        fill(255)
        textSize(40)
        text("PROGRESS", 43, 530)
        
        # HYDRATION
        fill(94, 193, 192)
        rect(240, 410, 200, 200, 20)
        fill(255)
        textSize(40)
        text("HYDRATION", 245, 530)
    
    if page3C:
        # logo
        background(255)
        fill(100)
        font1 = loadFont("HPSimplified-Regular-48.vlw")
        textFont(font1, 50)
        text("beneFIT+", 40, 70)
        fill(0)
        textSize(45)
        text("C. Be Fit Overall", 40, 130)
        
        # DIET
        noStroke()
        fill(216, 242, 104)
        rect(30, 200, 200, 200, 20)
        fill(255)
        textSize(40)
        text("DIET", 94, 320)
        
        # EXERCISE
        fill(244, 176, 107)
        rect(240, 200, 200, 200, 20)
        fill(255)
        textSize(40)
        text("EXERCISE", 263, 320)
        
        # PROGRESS
        fill(174, 252, 223)
        rect(30, 410, 200, 200, 20)
        fill(255)
        textSize(40)
        text("PROGRESS", 43, 530)
        
        # HYDRATION
        fill(94, 193, 192)
        rect(240, 410, 200, 200, 20)
        fill(255)
        textSize(40)
        text("HYDRATION", 245, 530)


def mousePressed():
    global pg1_orange
    global pg1_text
    global buttonPg1
    global pg2_white1, pg2_white2, pg2_white3
    global pg2_grey1, pg2_grey2, pg2_grey3 
    
    # button for page 1 "Take Survey"
    if page1:
        if mouseY >= 440 and mouseY <= 590:
            if mouseX <=440 and mouseX >= 30:
                buttonPg1 = True
        else:
            buttonPg1 = False
       
    
def mouseReleased():
    global page1, page2, page3A, page3B, page3C
    if page1:    
        if mouseY >= 440 and mouseY <= 590:
            if mouseX <=440 and mouseX >= 30:
                page1 = False
                page2 = True
    
    elif page2:
        if mouseY >= 365 and mouseY <= 465:
            if mouseX <= 440 and mouseX >= 30:
                page2 = False
                page3A = True


        if mouseY >= 500 and mouseY <= 600:
            if mouseX <= 440 and mouseX >= 30:
                page2 = False
                page3B = True

                
        if mouseY >= 635 and mouseY <= 735:
            if mouseX <= 440 and mouseX >= 30:
                page2 = False
                page3C = True
