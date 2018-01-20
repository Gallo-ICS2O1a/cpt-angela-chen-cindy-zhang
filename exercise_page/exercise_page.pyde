e_base_page = True

def setup():
    size(470, 770)
    

def draw():
    global e_base_page
    
    background(255)
    if e_base_page:
        
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
        textSize(55)
        fill(0)
        text(" EXERCISES ", 15, 75)
        textSize(35)
        text("WORKOUTS @ HOME", 35, 115)
        textSize(12)
        fill(14, 34, 112)
        text("*click on names to open links to exercises", 30, 135)
        
        # images
        body_workout = loadImage("body_parts.png")
        image(body_workout, 30, 150, 410, 75)
        
        # buttons
        noStroke()
        fill(242, 140, 104)
        rect(30, 245, 195, 120, 20)
        rect(245, 245, 195, 120, 20)
        rect(30, 385, 195, 120, 20)
        rect(245, 385, 195, 120, 20)
        rect(30, 525, 195, 120, 20)
        rect(245, 525, 195, 120, 20)
        
        geometric = loadImage("geometric.png")
        image(geometric, 30, 260, 175, 103)
        image(geometric, 245, 260, 175, 103)
        image(geometric, 30, 400, 175, 103)
        image(geometric, 245, 400, 175, 103)
        image(geometric, 30, 540, 175, 103)
        image(geometric, 245, 540, 175, 103)

        fill(0)
        rect(97, 297, 43, 23)
        rect(295, 273, 92, 60)
        rect(90, 432, 71, 23)
        rect(310, 432, 60, 23)
        rect(86, 571, 76, 23)
        rect(304, 570, 76, 23)
        
        # text
        fill(255)
        textSize(20)
        text("ABS", 100, 315)
        text("""BICEPS & 
TRICEPS""", 300, 295)
        text("CHEST", 95, 450)
        text("BACK", 315, 450)
        text("QUADS", 90, 590)
        text("GLUTES", 305, 590)
        

def mousePressed():
    if mouseX in range(30, 226):
        if mouseY in range(245, 366):
            link("https://www.fitnessmagazine.com/workout/abs/exercises/top-10-abs-exercises/")
        if mouseY in range(385, 506):
            link("http://www.coachmag.co.uk/exercises/chest-exercises/3523/best-home-workout-for-a-big-chest")
        if mouseY in range(525, 646):
            link("https://legionathletics.com/quads-exercises/")
    if mouseX in range(245, 441):
        if mouseY in range(245, 366):
            link("https://www.bodybuilding.com/content/beginner-arm-training-guide.html")
        if mouseY in range(385, 506):
            link("https://www.bodybuilding.com/content/10-best-muscle-building-back-exercises.html")
        if mouseY in range(525, 646):
            link("https://www.bodybuilding.com/content/glute-workout-5-moves-to-a-better-butt.html")
        
        
        
        

        
        