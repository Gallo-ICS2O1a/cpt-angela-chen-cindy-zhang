homepage = True
progress_button = False
hydration_button = False
p_base_page = False
p_page1 = False
p_page2 = False
p_page3 = False
p_page4 = False
p_page5 = False
p_page6 = False
p_page7 = False
p_back1 = False
p_back2 = False
p_back3 = False
p_back4 = False
p_back5 = False
p_back6 = False
p_back7 = False
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
p_day_button_colour = color(240,248,255)
p1_all_checked = False
p2_all_checked = False
p3_all_checked = False
p4_all_checked = False
p5_all_checked = False
p6_all_checked = False
p7_all_checked = False

def setup():
    size(470, 770)
    
def draw():
    global homepage
    global progress_button, hydration_button
    global p_page1, p_page2, p_page3, p_page4, p_page5, p_page6, p_page7
    global p_back1, p_back2, p_back3, p_back4, p_back5, p_back6, p_back7
    global p_base_page
    global p_done_colour, p_day_button_colour
    global P1_button_colour1, P1_button_colour2, P1_button_colour3
    global P2_button_colour1, P2_button_colour2, P2_button_colour3
    global P3_button_colour1, P3_button_colour2, P3_button_colour3
    global P4_button_colour1, P4_button_colour2, P4_button_colour3
    global P5_button_colour1, P5_button_colour2, P5_button_colour3
    global P6_button_colour1, P6_button_colour2, P6_button_colour3
    global P7_button_colour1, P7_button_colour2, P7_button_colour3
    global p1_all_checked, p2_all_checked, p3_all_checked, p4_all_checked, p5_all_checked, p6_all_checked, p7_all_checked
    
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
        

    # base page
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
                fill(240,248,255)
                rect(x, y, 80, 200) 
                
        # title
        textSize(65)
        fill(0)
        text(" PROGRESS ", 15, 90)
        
        # week
        textSize(45)
        fill(0)
        text(" weekly view ", 40, 155)
        
        #text on page
        
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
    if p_page1 or p_page2 or p_page3 or p_page4 or p_page5 or p_page6 or p_page7:
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
    if p_page1:
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
    
    if p_page2:
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
        
    if p_page3:
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
    
    if p_page4:
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
        
    if p_page5:
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
        
    if p_page6:
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
        
    if p_page7:
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
    
def mousePressed():
    global homepage
    global progress_button, hydration_button
    global p_page1, p_page2, p_page3, p_page4, p_page5, p_page6, p_page7
    global p_back1, p_back2, p_back3, p_back4, p_back5, p_back6, p_back7
    global p_base_page
    global p_done_colour, p_done_button_colour
    global P1_button_colour1, P1_button_colour2, P1_button_colour3
    global P2_button_colour1, P2_button_colour2, P2_button_colour3
    global P3_button_colour1, P3_button_colour2, P3_button_colour3
    global P4_button_colour1, P4_button_colour2, P4_button_colour3
    global P5_button_colour1, P5_button_colour2, P5_button_colour3
    global P6_button_colour1, P6_button_colour2, P6_button_colour3
    global P7_button_colour1, P7_button_colour2, P7_button_colour3
    global p1_all_checked, p2_all_checked, p3_all_checked, p4_all_checked, p5_all_checked, p6_all_checked, p7_all_checked
    
    if homepage:
        if mouseX >= 235 and mouseX <= 352.5:
            if mouseY >= 670 and mouseY <= 770:
                p_base_page = True
                homepage = False
    
    # base page to day progress
    if p_base_page:
        # page1 / monday
        if mouseX >= 45 and mouseX <= 125:
            if mouseY >= 200 and mouseY <= 400:
                p_page1 = True
                p_base_page = False
        
        # page2 / tuesday
        if mouseX >= 145 and mouseX <= 225:
            if mouseY >= 200 and mouseY <= 400:
                p_page2 = True
                p_base_page = False
            
        # page3 / wednesday
        if mouseX >= 245 and mouseX <= 325:
            if mouseY >= 200 and mouseY <= 400:
                p_page3 = True
                p_base_page = False
        
        # page4 / thursday
        if mouseX >= 365 and mouseX <= 425:
            if mouseY >= 200 and mouseY <= 400:
                p_page4 = True
                p_base_page = False
            
        # page5 / friday
        if mouseX >= 100 and mouseX <= 180:
            if mouseY >= 420 and mouseY <= 620:
                p_page5 = True
                p_base_page = False
        
        # page6 / saturday
        if mouseX >= 200 and mouseX <= 280:
            if mouseY >= 420 and mouseY <= 620:
                p_page6 = True
                p_base_page = False
                        
        # page7 / sunday
        if mouseX >= 300 and mouseX <= 380:
            if mouseY >= 420 and mouseY <= 620:
                p_page7 = True
                p_base_page = False
            
    # back buttons  
    if p_page1 or p_page2 or p_page3 or p_page4 or p_page5 or p_page6 or p_page7:      
        if mouseX >= 10 and mouseX <= 60:
            if mouseY >= 10 and mouseY <= 40:
                p_page1 = False
                p_page2 = False
                p_page3 = False
                p_page4 = False
                p_page5 = False
                p_page6 = False
                p_page7 = False
                p_base_page = True
            
    # check box buttons
    if p_page1:
        if mouseX >= 350 and mouseX <= 390:
            if mouseY >= 265 and mouseY <= 305:
                P1_button_colour1 = p_done_colour
            elif mouseY >= 325 and mouseY <= 365:
                P1_button_colour2 = p_done_colour
            elif mouseY >= 385 and mouseY <= 425:
                P1_button_colour3 = p_done_colour
                    
                            
    if p_page2:
        if mouseX >= 350 and mouseX <= 390:
            if mouseY >= 265 and mouseY <= 305:
                P2_button_colour1 = p_done_colour
            elif mouseY >= 325 and mouseY <= 365:
                P2_button_colour2 = p_done_colour
            elif mouseY >= 385 and mouseY <= 425:
                P2_button_colour3 = p_done_colour
                
    if p_page3:
        if mouseX >= 350 and mouseX <= 390:
            if mouseY >= 265 and mouseY <= 305:
                P3_button_colour1 = p_done_colour
            elif mouseY >= 325 and mouseY <= 365:
                P3_button_colour2 = p_done_colour
            elif mouseY >= 385 and mouseY <= 425:
                P3_button_colour3 = p_done_colour
                
    if p_page4:
        if mouseX >= 350 and mouseX <= 390:
            if mouseY >= 265 and mouseY <= 305:
                P4_button_colour1 = p_done_colour
            elif mouseY >= 325 and mouseY <= 365:
                P4_button_colour2 = p_done_colour
            elif mouseY >= 385 and mouseY <= 425:
                P4_button_colour3 = p_done_colour
                
    if p_page5:
        if mouseX >= 350 and mouseX <= 390:
            if mouseY >= 265 and mouseY <= 305:
                P5_button_colour1 = p_done_colour
            elif mouseY >= 325 and mouseY <= 365:
                P5_button_colour2 = p_done_colour
            elif mouseY >= 385 and mouseY <= 425:
                P5_button_colour3 = p_done_colour
                
    if p_page6:
        if mouseX >= 350 and mouseX <= 390:
            if mouseY >= 265 and mouseY <= 305:
                P6_button_colour1 = p_done_colour
            elif mouseY >= 325 and mouseY <= 365:
                P6_button_colour2 = p_done_colour
            elif mouseY >= 385 and mouseY <= 425:
                P6_button_colour3 = p_done_colour
                
    if p_page7:
        if mouseX >= 350 and mouseX <= 390:
            if mouseY >= 265 and mouseY <= 305:
                P7_button_colour1 = p_done_colour
            elif mouseY >= 325 and mouseY <= 365:
                P7_button_colour2 = p_done_colour
            elif mouseY >= 385 and mouseY <= 425:
                P7_button_colour3 = p_done_colour
    
        
    
    
    
    
        