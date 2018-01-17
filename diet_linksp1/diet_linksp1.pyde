d_base_page1 = True

def setup():
    size(470, 770)


def draw():
    global d_base_page1
    
    background(255)
# diet base page 
    if d_base_page1:
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
        text("mediterranean stuffed chicken breast", 35, 205)
        rect(35, 208, 291, 1)
        
        # tuesday
        textSize(20)
        text("TUESDAY", 35, 245)
        textSize(16)
        text("herbed salmon with broccoli bulgur pilaf", 35, 265)
        rect(35, 268, 320, 1)
        
        # wednesday
        textSize(20)
        text("WEDNESDAY", 35, 305)
        textSize(16)
        text("crockpot sizzling chicken fajitas ", 35, 325)
        rect(35, 328, 250, 1)
        
        # thursday
        textSize(20)
        text("THURSDAY", 35, 365)
        textSize(16)
        text("spicy grilled tofu with szechuan veggies", 35, 385)
        rect(35, 388, 312, 1)
        
        # friday
        textSize(20)
        text("FRIDAY", 35, 425)
        textSize(16)
        text("artichoke & spinach penne casserole", 35, 445)
        rect(35, 448, 283, 1)
        
        # saturday 
        textSize(20)
        text("SATURDAY", 35, 485)
        textSize(16)
        text("mexican style quinoa", 35, 505)
        rect(35, 508, 167, 1)
        
        # sunday
        textSize(20)
        text("SUNDAY", 35, 545)
        textSize(16)
        text("twice-baked potatoes", 35, 565)
        rect(35, 568, 170, 1)
    
def mousePressed():
    global d_base_page1, d_base_page2
        
 # diet page links to recipes 
    if d_base_page1:
        if mouseX in range(35, 327) and mouseY in range(188, 214):
            link("https://www.lecremedelacrumb.com/one-pot-lemon-herb-chicken-rice")
    
        if mouseX in range(35, 356) and mouseY in range(248, 274):
            link("https://skinnyms.com/herbed-salmon-with-broccoli-bulgur-pilaf/")
        
        if mouseX in range(35, 286) and mouseY in range(308, 334):
            link("https://skinnyms.com/slow-cooker-sizzling-chicken-fajitas/")
            
        if mouseX in range(35, 348) and mouseY in range(368, 394):
            link("https://skinnyms.com/spicy-grilled-tofu-with-szechuan-vegetables/")
            
        if mouseX in range(35, 319) and mouseY in range(428, 454):
            link("https://skinnyms.com/skinny-artichoke-spinach-penne-casserole/")
            
        if mouseX in range(35, 203) and mouseY in range(488, 514):
            link("https://skinnyms.com/one-pot-mexican-style-quinoa-recipe/")
            
        if mouseX in range(35, 206) and mouseY in range(548, 574):
            link("https://skinnyms.com/twice-baked-potatoes/")
        