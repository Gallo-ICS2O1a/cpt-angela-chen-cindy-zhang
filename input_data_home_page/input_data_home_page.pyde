def setup():
    size(470, 770)
    
def draw():
    background(250)
    
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
    
    
    
         
         
         
         
    
