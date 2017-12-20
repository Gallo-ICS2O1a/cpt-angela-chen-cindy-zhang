def setup():
    size(470, 770)

def draw():
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
    
    # calendar
    for y in range(200, 420, 220):
        for x in range(45, 410, 100):
            stroke(200)
            fill(225)
            rect(x, y, 80, 200) 
        
    for y in range(420, 555, 200):
        for x in range(100, 350, 100):
            stroke(200)
            fill(225)
            rect(x, y, 80, 200) 
            
    # title
    textSize(70)
    fill(0)
    text("  progress ", 10, 75)
    
    # week
    textSize(50)
    fill(0)
    text(" week ", 40, 155)
    
    
