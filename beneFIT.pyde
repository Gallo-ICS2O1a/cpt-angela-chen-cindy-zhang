home_width = 470
home_height = 150
# page1
page1 = True
pg1_orange = color(255, 147, 102)
pg1_text = color(255)
# page2
page2 = False
pg2_black = 0
pg2_grey1 = 0
pg2_grey2 = 0
pg2_grey3 = 0
pg2_white1 = 255
pg2_white2 = 255
pg2_white3 = 255
# page3
page3A = False
page3B = False
page3C = False
page3_Back = False
pg3_BeginColour = 255
pg3_BeginText = 255
pg3_diet_button = color(216, 242, 104)
survey_option = 0
# homepage
homepage = False
homepageColour = 240
# survey diet
survey_diet = False
# survey exercise
survey_exercise = False
# survey progress
survey_progress = False
# survey hydration
survey_hydration = False
# variables
progress_button = False
hydration_button = False
p_base_page = False
h_base_page = False
# 3 progress date pages
p_pg1 = False
p_pg2 = False
p_pg3 = False
p_pg4 = False
p_pg5 = False
p_pg6 = False
p_pg7 = False
# progress weekly back buttons
p_back1 = False
p_back2 = False
p_back3 = False
p_back4 = False
p_back5 = False
p_back6 = False
p_back7 = False
# progress checkboxes
p_done_colour = color(174, 252, 223)
P1_button_colour1 = 255
P1_button_colour2 = 255
P1_button_colour3 = 255
P2_button_colour1 = 255
P2_button_colour2 = 255
P2_button_colour3 = 255
P3_button_colour1 = 255
P3_button_colour2 = 255
P3_button_colour3 = 255
P4_button_colour1 = 255
P4_button_colour2 = 255
P4_button_colour3 = 255
P5_button_colour1 = 255
P5_button_colour2 = 255
P5_button_colour3 = 255
P6_button_colour1 = 255
P6_button_colour2 = 255
P6_button_colour3 = 255
P7_button_colour1 = 255
P7_button_colour2 = 255
P7_button_colour3 = 255
p_day_button_colour = color(240, 248, 255)
# hydration cup colours
cupC1 = color(255)
cupC2 = color(255)
cupC3 = color(255)
cupC4 = color(255)
cupC5 = color(255)
cupC6 = color(255)
cupC7 = color(255)
cupC8 = color(255)
# hydration cups click detection buttons
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
    global pg2_grey1, pg2_grey2, pg2_grey3
    global pg2_white1, pg2_white2, pg2_white3 
    global pg1_orange, pg1_text
    global pg3_BeginColour, pg3_BeginText
    global page3_Back, homepage
    global pg3_diet_button
    global progress_button, hydration_button
    global p_pg1, p_pg2, p_pg3, p_pg4, p_pg5, p_pg6, p_pg7
    global p_back1, p_back2, p_back3, p_back4, p_back5, p_back6, p_back7
    global p_base_page, h_base_page
    global p_done_colour, p_day_button_colour
    global P1_button_colour1, P1_button_colour2, P1_button_colour3
    global P2_button_colour1, P2_button_colour2, P2_button_colour3
    global P3_button_colour1, P3_button_colour2, P3_button_colour3
    global P4_button_colour1, P4_button_colour2, P4_button_colour3
    global P5_button_colour1, P5_button_colour2, P5_button_colour3
    global P6_button_colour1, P6_button_colour2, P6_button_colour3
    global P7_button_colour1, P7_button_colour2, P7_button_colour3
    global cup_base
    global clicked_colour
    global cup1, cup2, cup3, cup4, cup5, cup6, cup7, cup8
    global cupC1, cupC2, cupC3, cupC4, cupC5, cupC6, cupC7, cupC8

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
        if mouseX in range(30, 441) and mouseY in range(440, 591):
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
        rect(30, 100, 410, 230, 20)
        fill(255)
        font2 = loadFont("NirmalaUI-Bold-48.vlw")
        textFont(font2, 40)
        text("What is your goal?", 58, 235)
        
        # answer box 1
        fill(pg2_grey1)
        rect(30, 365, 410, 100, 20)
        font3 = loadFont("MicrosoftJhengHeiBold-48.vlw")
        fill(pg2_white1)
        textFont(font3, 30)
        text("A.", 60, 430)
        font4 = loadFont("MicrosoftJhengHeiRegular-48.vlw")
        textFont(font4, 30)
        text("Lose Weight", 150, 430)
        
        # answer box 1 when mouse hovers
        if mouseX in range(30, 440) and mouseY in range(365, 465):
            pg2_grey1 = 200
            pg2_white1 = 100
        else:
            pg2_grey1 = 100
            pg2_white1 = 255
        
        # answer box 2
        fill(pg2_grey2)
        rect(30, 500, 410, 100, 20)
        fill(pg2_white2)
        textFont(font3, 30)
        text("B.", 60, 565)
        textFont(font4, 30)
        text("Gain Muscle", 150, 565)
        
        # answer box 2 when mouse hovers
        if mouseX in range(30, 441) and mouseY in range(500, 601):
            pg2_grey2 = 200
            pg2_white2 = 100
        else:
            pg2_grey2 = 100
            pg2_white2 = 255
        
        # answer box 3
        fill(pg2_grey3)
        rect(30, 635, 410, 100, 20)
        fill(pg2_white3)
        textFont(font3, 30)
        text("C.", 60, 700)
        textFont(font4, 30)
        text("Be Fit Overall", 150, 700)
        
        # answer box 3 when mouse hovers
        if mouseX in range(30, 441) and mouseY in range(635, 736):
            pg2_grey3 = 200
            pg2_white3 = 100
        else:
            pg2_grey3 = 100
            pg2_white3 = 255
            
    if page3A or page3B or page3C:
        # logo
        background(255)
        fill(100)
        font1 = loadFont("HPSimplified-Regular-48.vlw")
        textFont(font1, 50)
        text("beneFIT+", 40, 70)
    
        # diet
        noStroke()
        fill(pg3_diet_button)
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

        # begin button
        strokeWeight(4)
        stroke(255)
        fill(pg3_BeginColour)
        rect(0, 690, 470, 80)
        fill(pg3_BeginText)
        textSize(40)
        text("BEGIN", 190, 744)
        if mouseX in range(0, 471) and mouseY in range(690, 771):
            pg3_BeginColour = 240
            pg3_BeginText = 175
        else:
            pg3_BeginColour = 175
            pg3_BeginText = 255

    if page3A:
        fill(0)
        textSize(45)
        text("A. Lose Weight", 40, 130)
    if page3B:
        fill(0)
        textSize(45)
        text("B. Gain Muscle", 40, 130)
    if page3C:
        fill(0)
        textSize(45)
        text("C. Be Fit Overall", 40, 130)
        
    if homepage: 
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
        
        # title
        textSize(70)
        fill(0)
        text("beneFIT+", 230, 200)
        
        # introduction
        textSize(18)
        textAlign(CENTER)
        fill(0)
        text("""      Welcome to the four pages in which you 
            will input your fitness data. Below are 
            four buttons that will help you nagivate 
            throughout the app. The light green is 
            the diet page, orange represents exercise, 
            the mint green is progress and the 
            turquoise tracks hydration.""", 210, 275) 

    # progress base page
    if p_base_page:
        textAlign(LEFT)
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
        
        # weekly calendar boxes
        for y in range(200, 420, 220):
            for x in range(45, 410, 100):
                stroke(235)
                fill(240, 248, 255)
                rect(x, y, 80, 200) 
            
        for y in range(420, 555, 200):
            for x in range(100, 350, 100):
                stroke(235)
                fill(240, 248, 255)
                rect(x, y, 80, 200) 
                
        # title
        textSize(65)
        fill(0)
        text(" PROGRESS ", 15, 90)
        
        # week
        textSize(45)
        fill(0)
        text(" weekly view ", 40, 155)
        
        # text on page
        
        if p_base_page:
            # text
            textSize(50)
            fill(0)
            text("M", 62.5, 300)
            text("T", 170, 300)
            text("W", 265, 300)
            text("T", 370, 300)
            text("F", 125, 520)
            text("S", 225, 520)
            text("S", 325, 520)
            
    # back buttons
    if p_pg1 or p_pg2 or p_pg3 or p_pg4 or p_pg5 or p_pg6 or p_pg7:
        fill(220)
        rect(10, 10, 50, 30, 20)
        
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
    
    # day page checkboxes
    if p_pg1:
        noStroke()
        fill(p_done_colour)
        rect(80, 95, 250, 80, 20)
        textSize(50)
        fill(0)
        text("MONDAY", 90, 150)
        
        textSize(40)
        fill(0)
        text("DIET", 90, 300)
        text("EXERCISE", 90, 360)
        text("HYDRATION", 90, 420)
        stroke(215)
        fill(P1_button_colour1)
        rect(350, 265, 40, 40, 10)
        fill(P1_button_colour2)
        rect(350, 325, 40, 40, 10)
        fill(P1_button_colour3)
        rect(350, 385, 40, 40, 10)
    
    if p_pg2:
        noStroke()
        fill(p_done_colour)
        rect(80, 95, 250, 80, 20)
        textSize(50)
        fill(0)
        text("TUESDAY", 90, 150)
        
        textSize(40)
        fill(0)
        text("DIET", 90, 300)
        text("EXERCISE", 90, 360)
        text("HYDRATION", 90, 420)
        fill(255)
        stroke(215)
        fill(P2_button_colour1)
        rect(350, 265, 40, 40, 10)
        fill(P2_button_colour2)
        rect(350, 325, 40, 40, 10)
        fill(P2_button_colour3)
        rect(350, 385, 40, 40, 10)
        
    if p_pg3:
        noStroke()
        fill(p_done_colour)
        rect(80, 95, 325, 80, 20)
        textSize(50)
        fill(0)
        text("WEDNESDAY", 90, 150)
            
        textSize(40)
        fill(0)
        text("DIET", 90, 300)
        text("EXERCISE", 90, 360)
        text("HYDRATION", 90, 420)
        fill(255)
        stroke(215)
        fill(P3_button_colour1)
        rect(350, 265, 40, 40, 10)
        fill(P3_button_colour2)
        rect(350, 325, 40, 40, 10)
        fill(P3_button_colour3)
        rect(350, 385, 40, 40, 10)
    
    if p_pg4:
        noStroke()
        fill(p_done_colour)
        rect(80, 95, 290, 80, 20)
        textSize(50)
        fill(0)
        text("THURSDAY", 90, 150)
        
        textSize(40)
        fill(0)
        text("DIET", 90, 300)
        text("EXERCISE", 90, 360)
        text("HYDRATION", 90, 420)
        fill(255)
        stroke(215)
        fill(P4_button_colour1)
        rect(350, 265, 40, 40, 10)
        fill(P4_button_colour2)
        rect(350, 325, 40, 40, 10)
        fill(P4_button_colour3)
        rect(350, 385, 40, 40, 10)
        
    if p_pg5:
        noStroke()
        fill(p_done_colour)
        rect(80, 95, 200, 80, 20)
        textSize(50)
        fill(0)
        text("FRIDAY", 90, 150)
        
        textSize(40)
        fill(0)
        text("DIET", 90, 300)
        text("EXERCISE", 90, 360)
        text("HYDRATION", 90, 420)
        fill(255)
        stroke(215)
        fill(P5_button_colour1)
        rect(350, 265, 40, 40, 10)
        fill(P5_button_colour2)
        rect(350, 325, 40, 40, 10)
        fill(P5_button_colour3)
        rect(350, 385, 40, 40, 10)
        
    if p_pg6:
        noStroke()
        fill(p_done_colour)
        rect(80, 95, 280, 80, 20)
        textSize(50)
        fill(0)
        text("SATURDAY", 90, 150)
        
        textSize(40)
        fill(0)
        text("DIET", 90, 300)
        text("EXERCISE", 90, 360)
        text("HYDRATION", 90, 420)
        fill(255)
        stroke(215)
        fill(P6_button_colour1)
        rect(350, 265, 40, 40, 10)
        fill(P6_button_colour2)
        rect(350, 325, 40, 40, 10)
        fill(P6_button_colour3)
        rect(350, 385, 40, 40, 10)
        
    if p_pg7:
        noStroke()
        fill(p_done_colour)
        rect(80, 95, 235, 80, 20)
        textSize(50)
        fill(0)
        text("SUNDAY", 90, 150)
        
        textSize(40)
        fill(0)
        text("DIET", 90, 300)
        text("EXERCISE", 90, 360)
        text("HYDRATION", 90, 420)
        fill(255)
        stroke(215)
        fill(P7_button_colour1)
        rect(350, 265, 40, 40, 10)
        fill(P7_button_colour2)
        rect(350, 325, 40, 40, 10)
        rect(350, 385, 40, 40, 10)
        
    # hydration base page
    if h_base_page:
        textAlign(LEFT)
        
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
    global pg1_orange
    global pg1_text
    global buttonPg1
    global pg2_white1, pg2_white2, pg2_white3
    global pg2_grey1, pg2_grey2, pg2_grey3 
    global survey_option, homepage
    global page1, page2, page3A, page3B, page3C
    global progress_button, hydration_button
    global p_pg1, p_pg2, p_pg3, p_pg4, p_pg5, p_pg6, p_pg7
    global p_back1, p_back2, p_back3, p_back4, p_back5, p_back6, p_back7
    global p_base_page, h_base_page
    global p_done_colour, p_done_button_colour
    global P1_button_colour1, P1_button_colour2, P1_button_colour3
    global P2_button_colour1, P2_button_colour2, P2_button_colour3
    global P3_button_colour1, P3_button_colour2, P3_button_colour3
    global P4_button_colour1, P4_button_colour2, P4_button_colour3
    global P5_button_colour1, P5_button_colour2, P5_button_colour3
    global P6_button_colour1, P6_button_colour2, P6_button_colour3
    global P7_button_colour1, P7_button_colour2, P7_button_colour3
    global cup1, cup2, cup3, cup4, cup5, cup6, cup7, cup8
    
    # button for page 1 "Take Survey"
    if page1:
        if mouseX in range(30, 441) and mouseY in range(440, 591):
            buttonPg1 = True
        else:
            buttonPg1 = False
            
    if page1:    
        if mouseX in range(30, 441) and mouseY in range(440, 591):
            page1 = False
            page2 = True
    
    elif page2:
        if mouseX in range(30, 441) and mouseY in range(365, 466):
            page2 = False
            page3A = True
            survey_option += 1

        if mouseX in range(30, 441) and mouseY in range(500, 601):
            page2 = False
            page3B = True
            survey_option += 2
            
        if mouseX in range(30, 441) and mouseY in range(635, 736):
            page2 = False
            page3C = True
            survey_option += 3
            
    elif page3A or page3B or page3C:
        if mouseX in range(0, 470) and mouseY in range(690, 771):
            page3A = False
            page3B = False
            page3C = False
            homepage = True

    elif homepage or p_base_page or h_base_page:
        if mouseX >= 235 and mouseX <= 352.5:
            if mouseY >= 670 and mouseY <= 770:
                p_base_page = True
                homepage = False
                h_base_page = False
        
        if mouseX >= 352.5 and mouseX <= 470:
            if mouseY >= 670 and mouseY <= 770:
                h_base_page = True
                homepage = False
                p_base_page = False
    
    # base page to day progress
    elif p_base_page:
        # page1 / monday
        if mouseX >= 45 and mouseX <= 125:
            if mouseY >= 200 and mouseY <= 400:
                p_pg1 = True
                p_base_page = False
        
        # page2 / tuesday
        if mouseX >= 145 and mouseX <= 225:
            if mouseY >= 200 and mouseY <= 400:
                p_pg2 = True
                p_base_page = False
            
        # page3 / wednesday
        if mouseX >= 245 and mouseX <= 325:
            if mouseY >= 200 and mouseY <= 400:
                p_pg3 = True
                p_base_page = False
        
        # page4 / thursday
        if mouseX >= 365 and mouseX <= 425:
            if mouseY >= 200 and mouseY <= 400:
                p_pg4 = True
                p_base_page = False
            
        # page5 / friday
        if mouseX >= 100 and mouseX <= 180:
            if mouseY >= 420 and mouseY <= 620:
                p_pg5 = True
                p_base_page = False
        
        # page6 / saturday
        if mouseX >= 200 and mouseX <= 280:
            if mouseY >= 420 and mouseY <= 620:
                p_pg6 = True
                p_base_page = False
                        
        # page7 / sunday
        if mouseX >= 300 and mouseX <= 380:
            if mouseY >= 420 and mouseY <= 620:
                p_pg7 = True
                p_base_page = False
            
    # back buttons  
    elif p_pg1 or p_pg2 or p_pg3 or p_pg4 or p_pg5 or p_pg6 or p_pg7:      
        if mouseX >= 10 and mouseX <= 60:
            if mouseY >= 10 and mouseY <= 40:
                p_pg1 = False
                p_pg2 = False
                p_pg3 = False
                p_pg4 = False
                p_pg5 = False
                p_pg6 = False
                p_pg7 = False
                p_base_page = True
            
    # check box buttons
    elif p_pg1:
        if mouseX >= 350 and mouseX <= 390:
            if mouseY >= 265 and mouseY <= 305:
                P1_button_colour1 = p_done_colour
            elif mouseY >= 325 and mouseY <= 365:
                P1_button_colour2 = p_done_colour
            elif mouseY >= 385 and mouseY <= 425:
                P1_button_colour3 = p_done_colour
                              
    elif p_pg2:
        if mouseX >= 350 and mouseX <= 390:
            if mouseY >= 265 and mouseY <= 305:
                P2_button_colour1 = p_done_colour
            elif mouseY >= 325 and mouseY <= 365:
                P2_button_colour2 = p_done_colour
            elif mouseY >= 385 and mouseY <= 425:
                P2_button_colour3 = p_done_colour
                
    elif p_pg3:
        if mouseX >= 350 and mouseX <= 390:
            if mouseY >= 265 and mouseY <= 305:
                P3_button_colour1 = p_done_colour
            elif mouseY >= 325 and mouseY <= 365:
                P3_button_colour2 = p_done_colour
            elif mouseY >= 385 and mouseY <= 425:
                P3_button_colour3 = p_done_colour
                
    elif p_pg4:
        if mouseX >= 350 and mouseX <= 390:
            if mouseY >= 265 and mouseY <= 305:
                P4_button_colour1 = p_done_colour
            elif mouseY >= 325 and mouseY <= 365:
                P4_button_colour2 = p_done_colour
            elif mouseY >= 385 and mouseY <= 425:
                P4_button_colour3 = p_done_colour
                
    elif p_pg5:
        if mouseX >= 350 and mouseX <= 390:
            if mouseY >= 265 and mouseY <= 305:
                P5_button_colour1 = p_done_colour
            elif mouseY >= 325 and mouseY <= 365:
                P5_button_colour2 = p_done_colour
            elif mouseY >= 385 and mouseY <= 425:
                P5_button_colour3 = p_done_colour
                
    elif p_pg6:
        if mouseX >= 350 and mouseX <= 390:
            if mouseY >= 265 and mouseY <= 305:
                P6_button_colour1 = p_done_colour
            elif mouseY >= 325 and mouseY <= 365:
                P6_button_colour2 = p_done_colour
            elif mouseY >= 385 and mouseY <= 425:
                P6_button_colour3 = p_done_colour
                
    elif p_pg7:
        if mouseX >= 350 and mouseX <= 390:
            if mouseY >= 265 and mouseY <= 305:
                P7_button_colour1 = p_done_colour
            elif mouseY >= 325 and mouseY <= 365:
                P7_button_colour2 = p_done_colour
            elif mouseY >= 385 and mouseY <= 425:
                P7_button_colour3 = p_done_colour
                
    # hydrations page
    elif h_base_page:
        if mouseX in range(34, 109) and mouseY in range(200, 375):
            cup1 = True
        
        if mouseX in range(143, 219) and mouseY in range(200, 376):
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
