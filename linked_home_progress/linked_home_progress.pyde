# variables
homepage = True
progress_button = False
hydration_button = False
p_base_page = False
h_base_page = False
d_base_page = False
e_base_page = False
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
# progress weekly letter colour change
p_mon_text = color(0)
p_tues_text = color(0)
p_wed_text = color(0)
p_thurs_text = color(0)
p_fri_text = color(0)
p_sat_text = color(0)
p_sun_text = color(0)
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
# hydration number colour change
h_1cup_number = color(0)
h_2cup_number = color(0)
h_3cup_number = color(0)
h_4cup_number = color(0)
h_5cup_number = color(0)
h_6cup_number = color(0)
h_7cup_number = color(0)
h_8cup_number = color(0)
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
clicked_colour = color(176, 224, 230)
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
    global p_base_page, h_base_page, d_base_page, e_base_page
    global p_done_colour
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
    global p_mon_text, p_tues_text, p_wed_text, p_thurs_text
    global p_fri_text, p_sat_text, p_sun_text
    global h_1cup_number, h_2cup_number, h_3cup_number, h_4cup_number
    global h_5cup_number, h_6cup_number, h_7cup_number, h_8cup_number

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
    
    # diet image icon
    diet = loadImage("diet_2.0.png")
    image(diet, 20, 680, 80, 80)
    
    # exercise image icon
    exercise = loadImage("dumbbell_2.0.png")
    image(exercise, 137.5, 680, 80, 80)
    
    # progress image icon
    progress = loadImage("calendar_2.0.png")
    image(progress, 255, 680, 80, 80)
    
    # hydration image icon
    hydration = loadImage("hydration_3.0.png")
    image(hydration, 372.5, 680, 80, 80)
        
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
        
        # diet image icon
        diet = loadImage("diet_2.0.png")
        image(diet, 20, 680, 80, 80)
        
        # exercise image icon
        exercise = loadImage("dumbbell_2.0.png")
        image(exercise, 137.5, 680, 80, 80)
        
        # progress image icon
        progress = loadImage("calendar_2.0.png")
        image(progress, 255, 680, 80, 80)
        
        # hydration image icon
        hydration = loadImage("hydration_3.0.png")
        image(hydration, 372.5, 680, 80, 80)
        
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

        # labels 
        textSize(16)
        fill(0)
        text("DIET", 60, 660)
        text("EXERCISE", 175, 660)
        text("PROGRESS", 295, 660)
        text("HYDRATION", 410, 660)
        
    # diet base page 
    if d_base_page:
        textAlign(LEFT)
        
        # title
        textSize(55)
        fill(0)
        text(" DIET ", 15, 90)
        textSize(35)
        text("RECIPES FOR DINNER", 35, 130)
        
        textSize(14)
        fill(242, 161, 118)
        text("*click on underlined names to get recipe", 35, 150)
        
        # monday
        textSize(20)
        fill(0)
        text("MONDAY", 35, 185)
        textSize(16)
        text("sphaghetti diablo with shrimp", 35, 205)
        rect(35, 208, 238, 1)
        
        # tuesday
        textSize(20)
        text("TUESDAY", 35, 245)
        textSize(16)
        text("baked tilapia", 35, 265)
        rect(35, 268, 100, 1)
        
        # wednesday
        textSize(20)
        text("WEDNESDAY", 35, 305)
        textSize(16)
        text("spinach & sun dried tomato pasta", 35, 325)
        rect(35, 328, 265, 1)
        
        # thursday
        textSize(20)
        text("THURSDAY", 35, 365)
        textSize(16)
        text("bean quesadillas", 35, 385)
        rect(35, 388, 132, 1)
        
        # friday
        textSize(20)
        text("FRIDAY", 35, 425)
        textSize(16)
        text("toasted buckewheat tabbouleh", 35, 445)
        rect(35, 448, 240, 1)
        
        # saturday 
        textSize(20)
        text("SATURDAY", 35, 485)
        textSize(16)
        text("black bean veggie burger", 35, 505)
        rect(35, 508, 200, 1)
        
        # sunday
        textSize(20)
        text("SUNDAY", 35, 545)
        textSize(16)
        text("grilled fish tacos with chipotle-lime dressing", 35, 565)
        rect(35, 568, 352, 1)
    
    # progress base page
    if p_base_page:
        textAlign(LEFT)
        
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
            fill(p_mon_text)
            text("M", 62.5, 300)
            fill(p_tues_text)
            text("T", 170, 300)
            fill(p_wed_text)
            text("W", 265, 300)
            fill(p_thurs_text)
            text("T", 370, 300)
            fill(p_fri_text)
            text("F", 125, 520)
            fill(p_sat_text)
            text("S", 225, 520)
            fill(p_sun_text)
            text("S", 325, 520)
            
    # changing letter colours
        # monday
        if mouseX in range(45, 126) and mouseY in range(200, 401):
            p_mon_text = color(95, 158, 160)

        # tuesday 
        elif mouseX in range(145, 226) and mouseY in range(200, 401):
            p_tues_text = color(95, 158, 160)
            
        # wednesday
        elif mouseX in range(245, 326) and mouseY in range(200, 401):
            p_wed_text = color(95, 158, 160)
        
        # thursday
        elif mouseX in range(345, 426) and mouseY in range(200, 401):
            p_thurs_text = color(95, 158, 160)
 
        # friday
        elif mouseX in range(100, 181) and mouseY in range(420, 621):
            p_fri_text = color(95, 158, 160)
        
        # saturday
        elif mouseX in range(200, 281) and mouseY in range(420, 621):
            p_sat_text = color(95, 158, 160)
    
        # sunday
        elif mouseX in range(300, 381) and mouseY in range(420, 621):
            p_sun_text = color(95, 158, 160)
            
        else:
            p_mon_text = 0
            p_tues_text = 0
            p_wed_text = 0
            p_thurs_text = 0
            p_fri_text = 0
            p_sat_text = 0
            p_sun_text = 0
            
    # back buttons
    if p_pg1 or p_pg2 or p_pg3 or p_pg4 or p_pg5 or p_pg6 or p_pg7:
        fill(220)
        rect(10, 10, 50, 30, 20)
    
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
        fill(P7_button_colour3)
        rect(350, 385, 40, 40, 10)
        
    # hydration base page
    if h_base_page:
        textAlign(LEFT)

        # hydration tracker
        noStroke
        
        fill(cupC1)
        rect(34, 200, 75, 175)
        if cup1:
            cupC1 = clicked_colour 
            
        fill(cupC2)
        rect(140, 200, 75, 175)
        if cup2:
            cupC2 = clicked_colour
            
        fill(cupC3)
        rect(245, 200, 75, 175)
        if cup3:
            cupC3 = clicked_colour
            
        fill(cupC4)
        rect(350, 200, 75, 175)
        if cup4:
            cupC4 = clicked_colour
            
        fill(cupC5)
        rect(34, 400, 75, 175)
        if cup5:
            cupC5 = clicked_colour
        
        fill(cupC6)
        rect(140, 400, 75, 175)
        if cup6:
            cupC6 = clicked_colour
        
        fill(cupC7)
        rect(245, 400, 75, 175)
        if cup7:
            cupC7 = clicked_colour
        
        fill(cupC8)
        rect(350, 400, 75, 175)    
        if cup8:
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
        fill(h_1cup_number)
        text("1", 57, 300)
        fill(h_2cup_number)
        text("2", 162, 300)
        fill(h_3cup_number)
        text("3", 265, 300)
        fill(h_4cup_number)
        text("4", 370, 300)
        fill(h_5cup_number)
        text("5", 57, 500)
        fill(h_6cup_number)
        text("6", 162, 500)
        fill(h_7cup_number)
        text("7", 265, 500)
        fill(h_8cup_number)
        text("8", 370, 500)
        
    # 1
        if mouseX in range(34, 111) and mouseY in range(200, 376):
            h_1cup_number = color(95, 158, 160)
       
    # 2   
        elif mouseX in range(140, 217) and mouseY in range(200, 376):
            h_2cup_number = color(95, 158, 160)
            
    # 3
        elif mouseX in range(246, 323) and mouseY in range(200, 376):
            h_3cup_number = color(95, 158, 160)
            
    # 4
        elif mouseX in range(352, 429) and mouseY in range(200, 376):
            h_4cup_number = color(95, 158, 160)
       
    # 5     
        elif mouseX in range(34, 111) and mouseY in range(400, 576):
            h_5cup_number = color(95, 158, 160)
        
    # 6
        elif mouseX in range(140, 217) and mouseY in range(400, 576):
            h_6cup_number = color(95, 158, 160)
            
    # 7
        elif mouseX in range(246, 323) and mouseY in range(400, 576):
            h_7cup_number = color(95, 158, 160)
        
    # 8
        elif mouseX in range(352, 429) and mouseY in range(400, 576):
            h_8cup_number = color(95, 158, 160)
            
        else:
            h_1cup_number = 0
            h_2cup_number = 0
            h_3cup_number = 0
            h_4cup_number = 0
            h_5cup_number = 0
            h_6cup_number = 0
            h_7cup_number = 0
            h_8cup_number = 0
            
    
def mousePressed():
    global homepage
    global progress_button, hydration_button
    global p_pg1, p_pg2, p_pg3, p_pg4, p_pg5, p_pg6, p_pg7
    global p_back1, p_back2, p_back3, p_back4, p_back5, p_back6, p_back7
    global p_base_page, h_base_page, d_base_page, e_base_page
    global p_done_colour
    global P1_button_colour1, P1_button_colour2, P1_button_colour3
    global P2_button_colour1, P2_button_colour2, P2_button_colour3
    global P3_button_colour1, P3_button_colour2, P3_button_colour3
    global P4_button_colour1, P4_button_colour2, P4_button_colour3
    global P5_button_colour1, P5_button_colour2, P5_button_colour3
    global P6_button_colour1, P6_button_colour2, P6_button_colour3
    global P7_button_colour1, P7_button_colour2, P7_button_colour3
    global cup1, cup2, cup3, cup4, cup5, cup6, cup7, cup8

    if homepage or p_base_page or h_base_page or d_base_page or e_base_page:
        if mouseX in range(0, int(118.5)) and mouseY in range(670, 771):
            d_base_page = True
            homepage = False
            h_base_page = False
            p_base_page = False
            e_base_page = False
            
        if mouseX in range(int(117.7), 236) and mouseY in range(670, 771):
            e_base_page = True
            homepage = False
            h_base_page = False
            p_base_page = False
            d_base_page = False
            
        if mouseX in range(235, int(353.5)) and mouseY in range(670, 771):
            p_base_page = True
            homepage = False
            h_base_page = False
            d_base_page = False
            e_base_page = False
    
        if mouseX in range(int(352.5), 471) and mouseY in range(670, 771):
            h_base_page = True
            homepage = False
            p_base_page = False
            d_base_page = False
            e_base_page = False
    
    # diet page links to recipes 
    if d_base_page:
        if mouseX in range(35, 274) and mouseY in range(188, 214):
            m_recipe = link("http://allrecipes.com/recipe/222968/spaghetti-diablo-with-shrimp/?internalSource=staff%20pick&referringId=1320&referringContentType=recipe%20hub")
    
        if mouseX in range(35, 136) and mouseY in range(248, 274):
            t_recipe = link("http://allrecipes.com/recipe/70163/easy-baked-tilapia/?internalSource=hub%20recipe&referringId=1320&referringContentType=recipe%20hub")
        
        if mouseX in range(35, 301) and mouseY in range(308, 334):
            w_recipe = link("http://allrecipes.com/recipe/73208/spinach-and-sun-dried-tomato-pasta/?internalSource=hub%20recipe&referringId=1320&referringContentType=recipe%20hub")
            
        if mouseX in range(35, 168) and mouseY in range(368, 394):
            th_recipe = link("http://allrecipes.com/recipe/14144/bean-quesadillas/?internalSource=staff%20pick&referringId=14962&referringContentType=recipe%20hub")
            
        if mouseX in range(35, 276) and mouseY in range(428, 454):
            f_recipe = link("http://allrecipes.com/recipe/228526/toasted-buckwheat-tabbouleh/?internalSource=staff%20pick&referringId=1346&referringContentType=recipe%20hub")
            
        if mouseX in range(35, 236) and mouseY in range(488, 514):
            s_recipe = link("http://allrecipes.com/recipe/85452/homemade-black-bean-veggie-burgers/?internalSource=hub%20recipe&referringId=14962&referringContentType=recipe%20hub")
            
        if mouseX in range(35, 388) and mouseY in range(548, 574):
            su_recipe = link("http://allrecipes.com/recipe/142614/grilled-fish-tacos-with-chipotle-lime-dressing/?internalSource=hub%20recipe&referringId=16374&referringContentType=recipe%20hub")
        
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
        if mouseX in range(34, 110) and mouseY in range(200, 376):
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
