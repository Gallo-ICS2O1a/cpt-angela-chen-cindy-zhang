d_base_page2 = True

def setup():
    size(470, 770)


def draw():
    global d_base_page2
    
    background(255)
# diet base page 
    if d_base_page2:
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
        text("high protein tuna bake pasta", 35, 205)
        rect(35, 208, 225, 1)
        
        # tuesday
        textSize(20)
        text("TUESDAY", 35, 245)
        textSize(16)
        text("grilled chipotle with shrimp tacos", 35, 265)
        rect(35, 268, 262, 1)
        
        # wednesday
        textSize(20)
        text("WEDNESDAY", 35, 305)
        textSize(16)
        text("lemon thyme roast chicken", 35, 325)
        rect(35, 328, 212, 1)
        
        # thursday
        textSize(20)
        text("THURSDAY", 35, 365)
        textSize(16)
        text("chicken burrito bowl", 35, 385)
        rect(35, 388, 160, 1)
        
        # friday
        textSize(20)
        text("FRIDAY", 35, 425)
        textSize(16)
        text("cheesy baked eggplant", 35, 445)
        rect(35, 448, 180, 1)
        
        # saturday 
        textSize(20)
        text("SATURDAY", 35, 485)
        textSize(16)
        text("low fat chicken curry", 35, 505)
        rect(35, 508, 165, 1)
        
        # sunday
        textSize(20)
        text("SUNDAY", 35, 545)
        textSize(16)
        text("steak & grilled cheese sandwich", 35, 565)
        rect(35, 568, 250, 1)
    
def mousePressed():
    global d_base_page2
        
 # diet page links to recipes 
    if d_base_page2:
        if mouseX in range(35, 261) and mouseY in range(188, 214):
            link("https://www.muscleandstrength.com/recipes/high-protein-tuna-bake-pasta")
    
        if mouseX in range(35, 298) and mouseY in range(248, 274):
            link("https://www.muscleandstrength.com/recipes/grilled-chipotle-shrimp-tacos-recipe")
        
        if mouseX in range(35, 248) and mouseY in range(308, 334):
            link("https://www.muscleandstrength.com/recipes/lemon-thyme-roast-chicken.html")
            
        if mouseX in range(35, 196) and mouseY in range(368, 394):
            link("https://www.muscleandstrength.com/recipes/high-protein-chicken-burrito-bowl")
            
        if mouseX in range(35, 216) and mouseY in range(428, 454):
            link("https://www.muscleandstrength.com/recipes/cheesy-baked-eggplant.html")
            
        if mouseX in range(35, 201) and mouseY in range(488, 514):
            link("https://www.muscleandstrength.com/recipes/bodybuilders-low-fat-chicken-curry.html")
            
        if mouseX in range(35, 286) and mouseY in range(548, 574):
            link("https://www.muscleandstrength.com/recipes/pepper-jack-steak-grilled-cheese")
        