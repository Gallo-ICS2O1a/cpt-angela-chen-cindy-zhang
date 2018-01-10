# variables
homepage = True
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
    global homepage
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
    global homepage
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

    if homepage or p_base_page or h_base_page:
        if mouseX in range(235, 353.5) and mouseY in range(670, 771):
                p_base_page = True
                homepage = False
                h_base_page = False
        
        if mouseX in range(352.5, 471) and mouseY in range(670, 771):
                h_base_page = True
                homepage = False
                p_base_page = False
    
    # base page to day progress
    if p_base_page:
        # page1 / monday
        if mouseX in range(45, 126) and mouseY in range(200, 401):
                p_pg1 = True
                p_base_page = False
        
        # page2 / tuesday
        if mouseX in range(145, 226) and mouseY in range(200, 401):
                p_pg2 = True
                p_base_page = False
            
        # page3 / wednesday
        if mouseX in range(245, 326) and mouseY in range(200, 401):
                p_pg3 = True
                p_base_page = False
        
        # page4 / thursday
        if mouseX in range(365, 426) and mouseY in range(200, 401):
                p_pg4 = True
                p_base_page = False
            
        # page5 / friday
        if mouseX in range(100, 181) and mouseY in range(420, 621):
                p_pg5 = True
                p_base_page = False
        
        # page6 / saturday
        if mouseX in range(200, 281) and mouseY in range(420, 621):
                p_pg6 = True
                p_base_page = False
                        
        # page7 / sunday
        if mouseX in range(300, 381) and mouseY in range(420, 621):
                p_pg7 = True
                p_base_page = False
            
    # back buttons  
    if p_pg1 or p_pg2 or p_pg3 or p_pg4 or p_pg5 or p_pg6 or p_pg7:      
        if mouseX in range(10, 61) and mouseY in range(10, 41):
                p_pg1 = False
                p_pg2 = False
                p_pg3 = False
                p_pg4 = False
                p_pg5 = False
                p_pg6 = False
                p_pg7 = False
                p_base_page = True
            
    # check box buttons
    if p_pg1:
        if mouseX in range(350, 391):
            if mouseY in range(265, 306):
                P1_button_colour1 = p_done_colour
            elif mouseY in range(325, 366):
                P1_button_colour2 = p_done_colour
            elif mouseY in range(385, 426):
                P1_button_colour3 = p_done_colour
                              
    if p_pg2:
        if mouseX in range(350, 391):
            if mouseY in range(265, 306):
                P2_button_colour1 = p_done_colour
            elif mouseY in range(325, 365):
                P2_button_colour2 = p_done_colour
            elif mouseY in range(385, 426):
                P2_button_colour3 = p_done_colour
                
    if p_pg3:
        if mouseX in range(350, 391):
            if mouseY in range(265, 306):
                P3_button_colour1 = p_done_colour
            elif mouseY in range(325, 365):
                P3_button_colour2 = p_done_colour
            elif mouseY in range(385, 426):
                P3_button_colour3 = p_done_colour
                
    if p_pg4:
        if mouseX in range(350, 391):
            if mouseY in range(265, 306):
                P4_button_colour1 = p_done_colour
            elif mouseY in range(325, 366):
                P4_button_colour2 = p_done_colour
            elif mouseY in range(385, 426):
                P4_button_colour3 = p_done_colour
                
    if p_pg5:
        if mouseX in range(350, 391):
            if mouseY in range(265, 306):
                P5_button_colour1 = p_done_colour
            elif mouseY in range(325, 366):
                P5_button_colour2 = p_done_colour
            elif mouseY in range(385, 426):
                P5_button_colour3 = p_done_colour
                
    if p_pg6:
        if mouseX in range(350, 391):
            if mouseY in range(265, 306):
                P6_button_colour1 = p_done_colour
            elif mouseY in range(325, 366):
                P6_button_colour2 = p_done_colour
            elif mouseY in range(385, 426):
                P6_button_colour3 = p_done_colour
                
    if p_pg7:
        if mouseX in range(350, 391):
            if mouseY in range(265, 306):
                P7_button_colour1 = p_done_colour
            elif mouseY in range(325, 366):
                P7_button_colour2 = p_done_colour
            elif mouseY in range(385, 426):
                P7_button_colour3 = p_done_colour
                
    # hydrations page
    if h_base_page:
        if mouseX in range(34, 110) and mouseY in range(375, 201):
                cup1 = True
        
        if mouseX in range(143, 219) and mouseY in range(200, 376):
                cup2 = True
                
        if mouseX in range(252, 328) and mouseY in range(200, 376):
                cup3 = True
                
        if mouseX in range(361, 437) and mouseY in range(200, 376):
                cup4 = True
                
        if mouseX in range(34, 110) and mouseY in range(445, 621):
                cup5 = True
                
        if mouseX in range(143, 219) and mouseY in range(445, 621):
                cup6 = True
        
        if mouseX in range(252, 328) and mouseY in range(445, 621):
                cup7 = True
                
        if mouseX in range(361, 437) and mouseY in range(445, 621):
                cup8 = True
