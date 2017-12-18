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
    
    # hydration tracker
    for y in range(200, 525, 200):
        for x in range(34, 436, 105):
            stroke(155)
            noFill()
            rect(x, y, 75, 175)
            
    # title
    textSize(70)
    fill(0)
    text(" hydration ", 10, 100)
    
    
    