# setup
page = 1
home_width = 470
home_height = 150
# page1
pg1_orange = color(255, 147, 102)
pg1_text = color(255)
# page2
pg2_black = color(0)
pg2_grey1 = color(0)
pg2_grey2 = color(0)
pg2_grey3 = color(0)
pg2_white1 = color(255)
pg2_white2 = color(255)
pg2_white3 = color(255)
# page3-5 / survey pages
s_page = 0
# survey pages colour of buttons
surveyBeginColour = color(255)
surveyBeginText = color(255)
surveyDietButton = color(216, 242, 104)
surveyExerciseButton = color(244, 176, 107)
surveyFAQButton = color(174, 252, 223)
surveyHydrationButton = color(94, 193, 192)
survey_option = 0
# progress date page
p_page = 0
# progress weekly letter colour change
p_mon_text = color(0)
p_tues_text = color(0)
p_wed_text = color(0)
p_thurs_text = color(0)
p_fri_text = color(0)
p_sat_text = color(0)
p_sun_text = color(0)
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
P1_button_colour1 = color(255)
P1_button_colour2 = color(255)
P1_button_colour3 = color(255)
P2_button_colour1 = color(255)
P2_button_colour2 = color(255)
P2_button_colour3 = color(255)
P3_button_colour1 = color(255)
P3_button_colour2 = color(255)
P3_button_colour3 = color(255)
P4_button_colour1 = color(255)
P4_button_colour2 = color(255)
P4_button_colour3 = color(255)
P5_button_colour1 = color(255)
P5_button_colour2 = color(255)
P5_button_colour3 = color(255)
P6_button_colour1 = color(255)
P6_button_colour2 = color(255)
P6_button_colour3 = color(255)
P7_button_colour1 = color(255)
P7_button_colour2 = color(255)
P7_button_colour3 = color(255)
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
# hydration number colour change
h_1cup_number = color(0)
h_2cup_number = color(0)
h_3cup_number = color(0)
h_4cup_number = color(0)
h_5cup_number = color(0)
h_6cup_number = color(0)
h_7cup_number = color(0)
h_8cup_number = color(0)
# hydration cups click detection buttons
clickedcolor = color(176, 224, 230)
# loading images
backbutton = loadImage("backbutton.png")
LoseWeight = loadImage("LoseWeight.png")
GainMuscle = loadImage("GainMuscle.png")
BeFitOverall = loadImage("BeFitOverall.png")
breakfast = loadImage("breakfast.png")
water = loadImage("water.jpg")
unprocessed = loadImage("unprocessed.png")
sweets = loadImage("sweets.png")
diet = loadImage("diet_2.0.png")
meat = loadImage("Meat.png")
proteinshake = loadImage("ProteinShake.jpg")
carbs = loadImage("Carbs.png")
salad = loadImage("Salad.png")
peaches = loadImage("Peaches.png")
healthy = loadImage("healthy.png")
S_ExerciseLW = loadImage("LoseWeight2.jpg")
S_ExerciseGM = loadImage("GainMuscle2.jpg")
S_ExerciseBFO = loadImage("BeFitOverall2.jpg")
body_workout = loadImage("body_parts.png")
geometric = loadImage("geometric.png")


def setup():
    global LoseWeight, GainMuscle, BeFitOverall, backbutton
    global breakfast, water, unprocessed, sweets
    global diet, meat, proteinshake, carbs, salad, peaches, healthy
    global S_ExerciseLW, S_ExerciseGM, S_ExerciseBFO
    global body_workout, geometric

    # size of program
    size(470, 770)

    # loading images
    LoseWeight = loadImage("LoseWeight.png")
    GainMuscle = loadImage("GainMuscle.png")
    BeFitOverall = loadImage("BeFitOverall.png")
    diet = loadImage("diet_2.0.png")
    breakfast = loadImage("breakfast.png")
    water = loadImage("water.jpg")
    unprocessed = loadImage("unprocessed.png")
    sweets = loadImage("sweets.png")
    meat = loadImage("Meat.png")
    proteinshake = loadImage("ProteinShake.jpg")
    carbs = loadImage("Carbs.png")
    salad = loadImage("Salad.png")
    peaches = loadImage("Peaches.png")
    healthy = loadImage("healthy.png")
    backbutton = loadImage("backbutton.png")
    S_ExerciseLW = loadImage("LoseWeight2.jpg")
    S_ExerciseGM = loadImage("GainMuscle2.jpg")
    S_ExerciseBFO = loadImage("BeFitOverall2.jpg")
    body_workout = loadImage("body_parts.png")
    geometric = loadImage("geometric.png")


def draw():
    global page, s_page, p_page
    global pg2_grey1, pg2_grey2, pg2_grey3
    global pg2_white1, pg2_white2, pg2_white3
    global pg1_orange, pg1_text
    global surveyBeginColour, surveyBeginText
    global surveyDietButton, surveyExerciseButton
    global surveyFAQButton, surveyHydrationButton
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
    global cupC1, cupC2, cupC3, cupC4, cupC5, cupC6, cupC7, cupC8
    global p_mon_text, p_tues_text, p_wed_text, p_thurs_text
    global p_fri_text, p_sat_text, p_sun_text
    global h_1cup_number, h_2cup_number, h_3cup_number, h_4cup_number
    global h_5cup_number, h_6cup_number, h_7cup_number, h_8cup_number
    global LoseWeight, GainMuscle, BeFitOverall
    global breakfast, water, unprocessed, sweets
    global diet, meat, proteinshake, carbs, salad, peaches, healthy
    global backbutton
    global S_ExerciseLW, S_ExerciseGM, S_ExerciseBFO
    global body_workout, geometric
    global p_mon_text, p_tues_text, p_wed_text, p_thurs_text
    global p_fri_text, p_sat_text, p_sun_text
    global h_1cup_number, h_2cup_number, h_3cup_number, h_4cup_number
    global h_5cup_number, h_6cup_number, h_7cup_number, h_8cup_number

    # setup
    background(255)
    noStroke()

    # page 1 / homepage
    if page == 1:
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

    # page 2 / Survey question & options
    if page == 2:
        # logo
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
        # Lose Weight Icon
        image(LoseWeight, 50, 383, 65, 65)
        # Lose Weight Text
        fill(pg2_white1)
        font3 = loadFont("MicrosoftJhengHeiRegular-48.vlw")
        textFont(font3, 30)
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
        # Gain Muscle Icon
        image(GainMuscle, 50, 516, 70, 70)
        fill(pg2_white2)
        textFont(font3, 30)
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
        # Be Fit Overall icon
        image(BeFitOverall, 50, 652, 65, 65)
        fill(pg2_white3)
        textFont(font3, 30)
        text("Be Fit Overall", 150, 700)

        # answer box 3 when mouse hovers
        if mouseX in range(30, 441) and mouseY in range(635, 736):
            pg2_grey3 = 200
            pg2_white3 = 100
        else:
            pg2_grey3 = 100
            pg2_white3 = 255

    # when survey option clicked, display page with buttons
    if page in range(3, 6):
        # logo
        background(255)
        fill(100)
        font1 = loadFont("HPSimplified-Regular-48.vlw")
        textFont(font1, 50)
        text("beneFIT+", 40, 70)

        # DIET
        noStroke()
        fill(surveyDietButton)
        rect(30, 200, 200, 200, 20)
        fill(255)
        textSize(40)
        text("DIET", 94, 320)

        # Hover over DIET button
        if mouseX in range(30, 221) and mouseY in range(200, 401):
            surveyDietButton = color(196, 226, 59)
        else:
            surveyDietButton = color(216, 242, 104)

        # EXERCISE
        fill(surveyExerciseButton)
        rect(240, 200, 200, 200, 20)
        fill(255)
        textSize(40)
        text("EXERCISE", 263, 320)

        # Hover over exercise button
        if mouseX in range(240, 441) and mouseY in range(200, 401):
            surveyExerciseButton = color(237, 152, 66)
        else:
            surveyExerciseButton = color(244, 176, 107)

        # PROGRESS
        fill(surveyFAQButton)
        rect(30, 410, 200, 200, 20)
        fill(255)
        textSize(40)
        text("FAQ", 100, 530)

        # Hover over progress button
        if mouseX in range(30, 231) and mouseY in range(410, 611):
            surveyFAQButton = color(138, 247, 206)
        else:
            surveyFAQButton = color(174, 252, 223)

        # HYDRATION
        fill(surveyHydrationButton)
        rect(240, 410, 200, 200, 20)
        fill(255)
        textSize(40)
        text("HYDRATION", 245, 530)

        # Hover over hydration button
        if mouseX in range(240, 441) and mouseY in range(410, 611):
            surveyHydrationButton = color(56, 181, 179)
        else:
            surveyHydrationButton = color(94, 193, 192)

        # begin button
        strokeWeight(4)
        stroke(255)
        fill(surveyBeginColour)
        rect(0, 690, 470, 80)
        fill(surveyBeginText)
        textSize(40)
        text("BEGIN", 190, 744)

        # hover over begin button
        if mouseX in range(0, 471) and mouseY in range(690, 771):
            surveyBeginColour = 240
            surveyBeginText = 175
        else:
            surveyBeginColour = 175
            surveyBeginText = 255

    if page == 3:
        strokeWeight(2)
        fill(0)
        textSize(45)
        text("A. Lose Weight", 40, 130)
    if page == 4:
        fill(0)
        textSize(45)
        text("B. Gain Muscle", 40, 130)
    if page == 5:
        fill(0)
        textSize(45)
        text("C. Be Fit Overall", 40, 130)

    # back bottons for survey pages
    if s_page in range(1, 5):
        image(backbutton, 400, 30, 50, 50)

        # logo printed at top
        fill(100)
        font1 = loadFont("HPSimplified-Regular-48.vlw")
        textFont(font1, 50)
        text("beneFIT+", 40, 70)
        if survey_option == 1:
            fill(0)
            textSize(45)
            text("A. Lose Weight", 40, 130)

        if survey_option == 2:
            fill(0)
            textFont(font1, 45)
            text("B. Gain Muscle", 40, 130)

        if survey_option == 3:
            fill(0)
            textFont(font1, 45)
            text("C. Be Fit Overall", 40, 130)

    # if diet page is clicked according to survey option
    if s_page == 1:
        font1 = loadFont("HPSimplified-Regular-48.vlw")
        font2 = loadFont("NirmalaUI-Bold-48.vlw")
        if survey_option == 1:
            fill(100)
            textAlign(CENTER)
            textSize(30)
            text("""Here are some diet tips to help
you lose Weight.""", 235, 190)

            # Pictures
            image(water, 280, 580, 117, 153)
            image(sweets, 40, 590, 150, 150)
            image(breakfast, 130, 590, 200, 120)
            image(unprocessed, 215, 630, 228, 119)
            fill(0)
            textAlign(LEFT)
            textFont(font2, 25)
            text("""1. Cut Back on Sugars and Starches

2. Eat a High-Protein Breakfast

3. Eat Your Food Slowly

4. Eat Whole, Unprocessed Foods

5. Drink Water Before Eating.""", 20, 300)

        if survey_option == 2:
            fill(100)
            textSize(30)
            textAlign(CENTER)
            text("""Here are some diet tips to help
you gain muscles.""", 235, 190)

            # Pictures
            image(proteinshake, 230, 520, 215, 215)
            image(carbs, 40, 560, 170, 170)
            image(peaches, 160, 580, 167, 157)
            image(salad, 300, 650, 150, 108)
            image(meat, 60, 668, 150, 80)

            fill(0)
            textFont(font2, 25)
            textAlign(LEFT)
            text("""1. Eat meat for protein.

2. Eat something every 3 hours.

3. Eat carbs after workouts.

4. Drink a shake before workouts.

5. Eat more in general.""", 20, 300)

        if survey_option == 3:
            fill(100)
            textSize(30)
            textAlign(CENTER)
            text("""Here are some diet tips to help
you get in shape.""", 235, 190)

            # Pictures
            image(healthy, 80, 570, 300, 180)

            fill(0)
            textFont(font2, 25)
            textAlign(LEFT)
            text("""1. Control your portion sizes.

2. Focus on a healthy lifestyle.

3. Eat more fiber & lean protein.

4. Drink a lot of water.

5. Eat less sweets.""", 20, 300)

    if s_page == 2:
        font1 = loadFont("HPSimplified-Regular-48.vlw")
        font2 = loadFont("NirmalaUI-Bold-48.vlw")
        if survey_option == 1:
            fill(100)
            textAlign(CENTER)
            textSize(30)
            text("""Here are some exercise tips to help
you lose Weight.""", 235, 190)

            # Pictures
            image(S_ExerciseLW, int(32.5), 550, 400, 225)

            fill(0)
            textAlign(LEFT)
            textFont(font2, 25)
            text("""1. Take the stairs.

2. Forget the scale.

3. Do cardio 30 minutes a day.

4. Fluctuate intensity levels.

5. Do not fear weights.""", 20, 300)

        if survey_option == 2:
            fill(100)
            textSize(30)
            textAlign(CENTER)
            text("""Here are some exercise tips to help
you gain muscles.""", 235, 190)

            # Pictures
            image(S_ExerciseGM, 10, 550, 450, 221)

            fill(0)
            textFont(font2, 25)
            textAlign(LEFT)
            text("""1. Do squats and situps.

2. Work your biggest muscles.

3. Lift every other day.

4. Slow down each of your reps.

5. Rest after workouts.""", 20, 300)

        if survey_option == 3:
            fill(100)
            textSize(30)
            textAlign(CENTER)
            text("""Here are some exercise tips to help
you get in shape.""", 235, 190)

            # Pictures
            image(S_ExerciseBFO, int(37.5), 550, 400, 200)
            fill(0)
            textFont(font2, 25)
            textAlign(LEFT)
            text("""1. Don't waste time in workouts.

2. Warm up.

3. Engage your core.

4. Do High Interval Intense Training.

5. Don't fear weights.""", 20, 300)

    if s_page == 3:
        font1 = loadFont("HPSimplified-Regular-48.vlw")
        font2 = loadFont("NirmalaUI-Bold-48.vlw")

        if survey_option == 1:
            fill(100)
            textSize(30)
            textAlign(CENTER)
            text("What are good times to workout?", 235, 190)

            fill(0)
            textFont(font2, 25)
            textAlign(LEFT)
            text("""In the mornings when you wake up.
Working out on an empty stomach
prompts weight loss.""", 20, 250)

            fill(100)
            textFont(font1, 30)
            textAlign(CENTER)
            text("How many times should I work out?", 235, 370)

            fill(0)
            textFont(font2, 25)
            textAlign(LEFT)
            text("""You should exercise for a minimum
of 150 minutes a week (cut
calories and follow a healthy diet.)""", 20, 430)

            fill(100)
            textFont(font1, 30)
            textAlign(CENTER)
            text("""Which comes first: cardiovascular
training or weight training?""", 235, 550)

            fill(0)
            textFont(font2, 25)
            textAlign(LEFT)
            text("""To lose weight, you should do
cardiovascular exercises (i.e. run on
the treadmill) before doing weight
training.""", 20, 640)

        if survey_option == 2:
            fill(100)
            textSize(30)
            textAlign(CENTER)
            text("What are good times to workout?", 235, 190)

            fill(0)
            textFont(font2, 25)
            textAlign(LEFT)
            text("""You should workout in mornings.
testosterone is important, and there
is greater mental focus.""", 20, 250)

            fill(100)
            textFont(font1, 30)
            textAlign(CENTER)
            text("How many times should I work out?", 235, 370)

            fill(0)
            textFont(font2, 25)
            textAlign(LEFT)
            text("""You should never train for 2 days in
a row. Therefore, exercise hard for
around 3-4 days per week.""", 20, 430)

            fill(100)
            textFont(font1, 30)
            textAlign(CENTER)
            text("""Which comes first: cardiovascular
training or weight training?""", 235, 550)

            fill(0)
            textFont(font2, 25)
            textAlign(LEFT)
            text("""To gain, you should do weight
exercises (i.e. free weights) before
doing cardiovascular training.""", 20, 640)

        if survey_option == 3:
            fill(100)
            textSize(30)
            textAlign(CENTER)
            text("What are good times to workout?", 235, 190)

            fill(0)
            textFont(font2, 25)
            textAlign(LEFT)
            text("""Find what is suitable for you.
Try working out for a month in the
mornings vs. noon vs. evenings.""", 20, 250)

            fill(100)
            textFont(font1, 30)
            textAlign(CENTER)
            text("How many times should I work out?", 235, 370)

            fill(0)
            textFont(font2, 25)
            textAlign(LEFT)
            text("""You should begin slow and slowly
progress to a goal of working out
3-4 times a week. Remember to rest.""", 20, 430)

            fill(100)
            textFont(font1, 30)
            textAlign(CENTER)
            text("""Which comes first: cardiovascular
training or weight training?""", 235, 550)

            fill(0)
            textFont(font2, 25)
            textAlign(LEFT)
            text("""Alternate your workouts. You can
begin with either, but alternate what
you start with every few weeks.""", 20, 640)

    if s_page == 4:
        font1 = loadFont("HPSimplified-Regular-48.vlw")
        font2 = loadFont("NirmalaUI-Bold-48.vlw")
        fill(100)
        textFont(font1, 30)
        textAlign(CENTER)
        text("How can I stay hydrated?", 235, 190)

        fill(0)
        textFont(font2, 25)
        textAlign(LEFT)
        text("""Keep a waterbottle with you
during the day.

Add a slice of lemon or lime to
give some flavour.

Drink water before, during, and
after a workout.

Drink water when you're hungry.

Drink on a schedule to help you
remember.""", 30, 260)

    if page == 6:
        # title
        textAlign(CENTER)
        font1 = loadFont("HPSimplified-Regular-48.vlw")
        textFont(font1, 70)
        fill(0)
        text("beneFIT+", 235, 200)

        # introduction
        textSize(20)
        textAlign(CENTER)
        fill(0)
        text("""Welcome to the four pages in which you
will input your fitness data. Below are
four buttons that will help you nagivate
throughout the app.""", 235, 255)

        # explanation
        fill(100)
        textAlign(LEFT)
        font3 = loadFont("MicrosoftJhengHeiRegular-48.vlw")
        textFont(font3, 18)
        fill(224, 58, 0)
        text(""" The diet page gives you a recipe you can follow
depending on what you answered in the survey.""", 20, 365)
        fill(38, 58, 122)
        text("""The exercise page gives you examples of workouts
you can complete depending on your survey reply.""", 20, 435)
        fill(46, 203, 208)
        text("""The progress page tracks whether or not you have
completed your goal for the day on a weekly basis.""", 20, 505)
        fill(14, 166, 203)
        text("""The hydration page will track how many cups of
water you drank for a day.""", 20, 575)

        # labels
        textAlign(CENTER)
        textSize(16)
        fill(0)
        text("DIET", 60, 660)
        text("EXERCISE", 175, 660)
        text("PROGRESS", 295, 660)
        text("HYDRATION", 410, 660)

    if page == 7:
        textAlign(LEFT)

        # title
        textSize(65)
        fill(0)
        text("DIET", 25, 90)
        textSize(35)
        text("RECIPES FOR DINNER", 35, 130)
        textSize(14)
        fill(242, 161, 118)
        text("*click on underlined names to get recipe", 35, 150)

        # Recipes for 'lose weight' option
        if survey_option == 1:
            # monday
            textSize(20)
            fill(0)
            text("MONDAY", 35, 185)
            textSize(17)
            text("mediterranean stuffed chicken breast", 35, 205)
            rect(35, 208, 291, 1)

            # tuesday
            textSize(20)
            text("TUESDAY", 35, 245)
            textSize(17)
            text("herbed salmon with broccoli bulgur pilaf", 35, 265)
            rect(35, 268, 320, 1)

            # wednesday
            textSize(20)
            text("WEDNESDAY", 35, 305)
            textSize(17)
            text("crockpot sizzling chicken fajitas ", 35, 325)
            rect(35, 328, 250, 1)

            # thursday
            textSize(20)
            text("THURSDAY", 35, 365)
            textSize(17)
            text("spicy grilled tofu with szechuan veggies", 35, 385)
            rect(35, 388, 312, 1)

            # friday
            textSize(20)
            text("FRIDAY", 35, 425)
            textSize(17)
            text("artichoke & spinach penne casserole", 35, 445)
            rect(35, 448, 283, 1)

            # saturday
            textSize(20)
            text("SATURDAY", 35, 485)
            textSize(17)
            text("mexican style quinoa", 35, 505)
            rect(35, 508, 167, 1)

            # sunday
            textSize(20)
            text("SUNDAY", 35, 545)
            textSize(17)
            text("twice-baked potatoes", 35, 565)
            rect(35, 568, 170, 1)

            textSize(15)
            fill(242, 161, 118)
            text("*Customized for you to lose weight", 20, 620)

        # Recipes for 'gain muscle' option
        if survey_option == 2:
            # monday
            textSize(20)
            fill(0)
            text("MONDAY", 35, 185)
            textSize(17)
            text("high protein tuna bake pasta", 35, 205)
            rect(35, 208, 225, 1)

            # tuesday
            textSize(20)
            text("TUESDAY", 35, 245)
            textSize(17)
            text("grilled chipotle with shrimp tacos", 35, 265)
            rect(35, 268, 262, 1)

            # wednesday
            textSize(20)
            text("WEDNESDAY", 35, 305)
            textSize(17)
            text("lemon thyme roast chicken", 35, 325)
            rect(35, 328, 212, 1)

            # thursday
            textSize(20)
            text("THURSDAY", 35, 365)
            textSize(17)
            text("chicken burrito bowl", 35, 385)
            rect(35, 388, 160, 1)

            # friday
            textSize(20)
            text("FRIDAY", 35, 425)
            textSize(17)
            text("cheesy baked eggplant", 35, 445)
            rect(35, 448, 180, 1)

            # saturday
            textSize(20)
            text("SATURDAY", 35, 485)
            textSize(17)
            text("low fat chicken curry", 35, 505)
            rect(35, 508, 165, 1)

            # sunday
            textSize(20)
            text("SUNDAY", 35, 545)
            textSize(17)
            text("steak & grilled cheese sandwich", 35, 565)
            rect(35, 568, 250, 1)

            textSize(15)
            fill(242, 161, 118)
            text("*Customized for you to gain muscle", 20, 620)

        # recipe options for 'be fit overall'
        if survey_option == 3:
            # monday
            textSize(20)
            fill(0)
            text("MONDAY", 35, 185)
            textSize(17)
            text("sphaghetti diablo with shrimp", 35, 205)
            rect(35, 208, 238, 1)

            # tuesday
            textSize(20)
            text("TUESDAY", 35, 245)
            textSize(17)
            text("baked tilapia", 35, 265)
            rect(35, 268, 100, 1)

            # wednesday
            textSize(20)
            text("WEDNESDAY", 35, 305)
            textSize(17)
            text("spinach & sun dried tomato pasta", 35, 325)
            rect(35, 328, 265, 1)

            # thursday
            textSize(20)
            text("THURSDAY", 35, 365)
            textSize(17)
            text("bean quesadillas", 35, 385)
            rect(35, 388, 132, 1)

            # friday
            textSize(20)
            text("FRIDAY", 35, 425)
            textSize(17)
            text("toasted buckewheat tabbouleh", 35, 445)
            rect(35, 448, 240, 1)

            # saturday
            textSize(20)
            text("SATURDAY", 35, 485)
            textSize(17)
            text("black bean veggie burger", 35, 505)
            rect(35, 508, 200, 1)

            # sunday
            textSize(20)
            text("SUNDAY", 35, 545)
            textSize(17)
            text("grilled fish tacos with chipotle-lime dressing", 35, 565)
            rect(35, 568, 352, 1)

            textSize(15)
            fill(242, 161, 118)
            text("*Customized for you to be fit overall", 20, 620)

    # Exercise Page
    if page == 8:
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

        # geometric design
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

    # progress page
    if page == 9:
        progress = loadImage("progress.png")
        image(progress, 70, 470, 400, 250)
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
        textAlign(LEFT)
        textSize(65)
        fill(0)
        text("PROGRESS", 25, 90)
        textAlign(CENTER)
        textSize(20)
        text("""Click on each day of the week
to track your progress.""", 235, 140)

        # text
        textAlign(LEFT)
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
    if p_page in range(1, 8):
        progress = loadImage("progress.png")
        image(progress, 70, 470, 400, 250)
        fill(220)
        rect(10, 10, 50, 30, 20)

    # day page checkboxes
    if p_page == 1:
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

    if p_page == 2:
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

    if p_page == 3:
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

    if p_page == 4:
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

    if p_page == 5:
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

    if p_page == 6:
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

    if p_page == 7:
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
    if page == 10:
        textAlign(LEFT)

        # hydration tracker
        fill(cupC1)
        rect(34, 200, 75, 175)
        fill(cupC2)
        rect(140, 200, 75, 175)
        fill(cupC3)
        rect(245, 200, 75, 175)
        fill(cupC4)
        rect(350, 200, 75, 175)
        fill(cupC5)
        rect(34, 400, 75, 175)
        fill(cupC6)
        rect(140, 400, 75, 175)
        fill(cupC7)
        rect(245, 400, 75, 175)
        fill(cupC8)
        rect(350, 400, 75, 175)

        # title
        textSize(70)
        fill(0)
        text("HYDRATION", 25, 90)
        textAlign(CENTER)
        textSize(20)
        text("""When you finish drinking one cup of water,
click one of the cups to fill them up.
Your goal is to drink 8 cups a day!""", 235, 130)

        textAlign(LEFT)
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

        waves = loadImage("waves.png")
        image(waves, 0, 560, 770, 151)

    if page > 5 or p_page in range(1, 8):
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


def mousePressed():
    global page, s_page, p_page
    global survey_option
    global p_done_colour, p_done_button_colour
    global P1_button_colour1, P1_button_colour2, P1_button_colour3
    global P2_button_colour1, P2_button_colour2, P2_button_colour3
    global P3_button_colour1, P3_button_colour2, P3_button_colour3
    global P4_button_colour1, P4_button_colour2, P4_button_colour3
    global P5_button_colour1, P5_button_colour2, P5_button_colour3
    global P6_button_colour1, P6_button_colour2, P6_button_colour3
    global P7_button_colour1, P7_button_colour2, P7_button_colour3
    global cupC1, cupC2, cupC3, cupC4, cupC5, cupC6, cupC7, cupC8
    global clickedcolor

    # button for page 1 "Take Survey"
    if page == 1:
        if mouseX in range(30, 441) and mouseY in range(440, 591):
            page = 2

    elif page == 2:
        if mouseX in range(30, 441) and mouseY in range(365, 466):
            page = 3
            survey_option = 1

        if mouseX in range(30, 441) and mouseY in range(500, 601):
            page = 4
            survey_option = 2

        if mouseX in range(30, 441) and mouseY in range(635, 736):
            page = 5
            survey_option = 3

    elif page in range(3, 6):
        # DIET
        if mouseX in range(30, 221) and mouseY in range(200, 401):
            page = 0
            s_page = 1
        # EXERCISE
        if mouseX in range(240, 441) and mouseY in range(200, 401):
            page = 0
            s_page = 2
        # PROGRESS
        if mouseX in range(30, 231) and mouseY in range(410, 611):
            page = 0
            s_page = 3
        # HYDRATION
        if mouseX in range(240, 441) and mouseY in range(410, 611):
            page = 0
            s_page = 4
        # BEGIN
        if mouseX in range(0, 471) and mouseY in range(690, 771):
            page = 6

    elif page in range(6, 11):
        if mouseX in range(0, int(118.5)) and mouseY in range(670, 771):
            page = 7

        if mouseX in range(int(117.7), 236) and mouseY in range(670, 771):
            page = 8

        if mouseX in range(235, int(353.5)) and mouseY in range(670, 771):
            page = 9

        if mouseX in range(int(352.5), 471) and mouseY in range(670, 771):
            page = 10

    # note: length of links were over 80 lines (not pep8 complaint), but
    # we couldn't shorten them unless we used bit.ly. This is why there is
    # '# noqa' behind the code so pep8 wouldn't check it. This was the
    # only exception we had.

    # Diet page links
    if page == 7:
        if survey_option == 1:
            if mouseX in range(35, 327) and mouseY in range(188, 214):
                link("https://www.lecremedelacrumb.com/one-pot-lemon-herb-chicken-rice")  # noqa

            if mouseX in range(35, 356) and mouseY in range(248, 274):
                link("https://skinnyms.com/herbed-salmon-with-broccoli-bulgur-pilaf/")  # noqa

            if mouseX in range(35, 286) and mouseY in range(308, 334):
                link("https://skinnyms.com/slow-cooker-sizzling-chicken-fajitas/")  # noqa

            if mouseX in range(35, 348) and mouseY in range(368, 394):
                link("https://skinnyms.com/spicy-grilled-tofu-with-szechuan-vegetables/")  # noqa

            if mouseX in range(35, 319) and mouseY in range(428, 454):
                link("https://skinnyms.com/skinny-artichoke-spinach-penne-casserole/")  # noqa

            if mouseX in range(35, 203) and mouseY in range(488, 514):
                link("https://skinnyms.com/one-pot-mexican-style-quinoa-recipe/")  # noqa

            if mouseX in range(35, 206) and mouseY in range(548, 574):
                link("https://skinnyms.com/twice-baked-potatoes/")  # noqa

        if survey_option == 2:
            if mouseX in range(35, 261) and mouseY in range(188, 214):
                link("https://www.muscleandstrength.com/recipes/high-protein-tuna-bake-pasta")  # noqa

            if mouseX in range(35, 298) and mouseY in range(248, 274):
                link("https://www.muscleandstrength.com/recipes/grilled-chipotle-shrimp-tacos-recipe")  # noqa

            if mouseX in range(35, 248) and mouseY in range(308, 334):
                link("https://www.muscleandstrength.com/recipes/lemon-thyme-roast-chicken.html")  # noqa

            if mouseX in range(35, 196) and mouseY in range(368, 394):
                link("https://www.muscleandstrength.com/recipes/high-protein-chicken-burrito-bowl")  # noqa

            if mouseX in range(35, 216) and mouseY in range(428, 454):
                link("https://www.muscleandstrength.com/recipes/cheesy-baked-eggplant.html")  # noqa

            if mouseX in range(35, 201) and mouseY in range(488, 514):
                link("https://www.muscleandstrength.com/recipes/bodybuilders-low-fat-chicken-curry.html")  # noqa

            if mouseX in range(35, 286) and mouseY in range(548, 574):
                link("https://www.muscleandstrength.com/recipes/pepper-jack-steak-grilled-cheese")  # noqa

        if survey_option == 3:
            if mouseX in range(35, 274) and mouseY in range(188, 214):
                link("http://allrecipes.com/recipe/222968/spaghetti-diablo-with-shrimp/?internalSource=staff%20pick&referringId=1320&referringContentType=recipe%20hub")  # noqa

            if mouseX in range(35, 136) and mouseY in range(248, 274):
                link("http://allrecipes.com/recipe/70163/easy-baked-tilapia/?internalSource=hub%20recipe&referringId=1320&referringContentType=recipe%20ub")  # noqa

            if mouseX in range(35, 301) and mouseY in range(308, 334):
                link("http://allrecipes.com/recipe/73208/spinach-and-sun-dried-tomato-pasta/?internalSource=hub%20recipe&referringId=1320&referringContentType=recipe%20hub")  # noqa

            if mouseX in range(35, 168) and mouseY in range(368, 394):
                link("http://allrecipes.com/recipe/14144/bean-quesadillas/?internalSource=staff%20pick&referringId=14962&referringContentType=recipe%20hub")  # noqa

            if mouseX in range(35, 276) and mouseY in range(428, 454):
                link("http://allrecipes.com/recipe/228526/toasted-buckwheat-tabbouleh/?internalSource=staff%20pick&referringId=1346&referringContentType=recipe%20hub")  # noqa

            if mouseX in range(35, 236) and mouseY in range(488, 514):
                link("http://allrecipes.com/recipe/85452/homemade-black-bean-veggie-burgers/?internalSource=hub%20recipe&referringId=14962&referringContentType=recipe%20hub")  # noqa

            if mouseX in range(35, 388) and mouseY in range(548, 574):
                link("http://allrecipes.com/recipe/142614/grilled-fish-tacos-with-chipotle-lime-dressing/?internalSource=hub%20recipe&referringId=16374&referringContentType=recipe%20hub")  # noqa

    elif page == 8:
        if mouseX in range(30, 226):
            if mouseY in range(245, 366):
                link("https://www.fitnessmagazine.com/workout/abs/exercises/top-10-abs-exercises/")  # noqa
            elif mouseY in range(385, 506):
                link("http://www.coachmag.co.uk/exercises/chest-exercises/3523/best-home-workout-for-a-big-chest")  # noqa
            elif mouseY in range(525, 646):
                link("https://legionathletics.com/quads-exercises/")  # noqa

        elif mouseX in range(245, 441):
            if mouseY in range(245, 366):
                link("https://www.bodybuilding.com/content/beginner-arm-training-guide.html")  # noqa
            elif mouseY in range(385, 506):
                link("https://www.bodybuilding.com/content/10-best-muscle-building-back-exercises.html")  # noqa
            elif mouseY in range(525, 646):
                link("https://www.bodybuilding.com/content/glute-workout-5-moves-to-a-better-butt.html")  # noqa

    # progress
    elif page == 9:
        # page1 / monday
        if mouseX in range(45, 126) and mouseY in range(200, 401):
            p_page = 1
            page = 0

        # page2 / tuesday
        if mouseX in range(145, 226) and mouseY in range(200, 401):
            p_page = 2
            page = 0

        # page3 / wednesday
        if mouseX in range(245, 326) and mouseY in range(200, 401):
            p_page = 3
            page = 0

        # page4 / thursday
        if mouseX in range(365, 426) and mouseY in range(200, 401):
            p_page = 4
            page = 0

        # page5 / friday
        if mouseX in range(100, 181) and mouseY in range(420, 621):
            p_page = 5
            page = 0

        # page6 / saturday
        if mouseX in range(200, 281) and mouseY in range(420, 621):
            p_page = 6
            page = 0

        # page7 / sunday
        if mouseX in range(300, 381) and mouseY in range(420, 621):
            p_page = 7
            page = 0

    # hydrations page
    elif page == 10:
        if mouseY in range(200, 376):
            if mouseX in range(34, 109):
                cupC1 = clickedcolor
            elif mouseX in range(143, 219):
                cupC2 = clickedcolor
            elif mouseX in range(252, 328):
                cupC3 = clickedcolor
            if mouseX in range(361, 437):
                cupC4 = clickedcolor
        elif mouseY in range(445, 621):
            if mouseX in range(34, 110):
                cupC5 = clickedcolor
            elif mouseX in range(143, 219):
                cupC6 = clickedcolor
            elif mouseX in range(252, 328):
                cupC7 = clickedcolor
            elif mouseX in range(361, 437):
                cupC8 = clickedcolor

    # survey page back buttons
    if s_page in range(1, 5):
        if mouseX in range(400, 450) and mouseY in range(39, 73):
                s_page = 0
                page = 2 + survey_option

    # check box buttons
    if p_page in range(1, 8):
        if mouseX in range(235, int(353.5)) and mouseY in range(670, 771):
            page = 9
            p_page = 0

        if mouseX in range(int(352.5), 471) and mouseY in range(670, 771):
            page = 10
            p_page = 0

    if p_page == 1:
        if mouseX in range(350, 391):
            if mouseY in range(265, 306):
                P1_button_colour1 = p_done_colour
            elif mouseY in range(325, 365):
                P1_button_colour2 = p_done_colour
            elif mouseY in range(385, 426):
                P1_button_colour3 = p_done_colour
        if mouseX in range(10, 61) and mouseY in range(10, 41):
            p_page = 0
            page = 9

    elif p_page == 2:
        if mouseX in range(350, 391):
            if mouseY in range(265, 306):
                P2_button_colour1 = p_done_colour
            elif mouseY in range(325, 365):
                P2_button_colour2 = p_done_colour
            elif mouseY in range(385, 426):
                P2_button_colour3 = p_done_colour
        if mouseX in range(10, 61) and mouseY in range(10, 41):
            p_page = 0
            page = 9

    elif p_page == 3:
        if mouseX in range(350, 391):
            if mouseY in range(265, 306):
                P3_button_colour1 = p_done_colour
            elif mouseY in range(325, 365):
                P3_button_colour2 = p_done_colour
            elif mouseY in range(385, 426):
                P3_button_colour3 = p_done_colour
        if mouseX in range(10, 61) and mouseY in range(10, 41):
            p_page = 0
            page = 9

    elif p_page == 4:
        if mouseX in range(350, 391):
            if mouseY in range(265, 306):
                P4_button_colour1 = p_done_colour
            elif mouseY in range(325, 365):
                P4_button_colour2 = p_done_colour
            elif mouseY in range(385, 426):
                P4_button_colour3 = p_done_colour
        if mouseX in range(10, 61) and mouseY in range(10, 41):
            p_page = 0
            page = 9

    elif p_page == 5:
        if mouseX in range(350, 391):
            if mouseY in range(265, 306):
                P5_button_colour1 = p_done_colour
            elif mouseY in range(325, 365):
                P5_button_colour2 = p_done_colour
            elif mouseY in range(385, 426):
                P5_button_colour3 = p_done_colour
        if mouseX in range(10, 61) and mouseY in range(10, 41):
            p_page = 0
            page = 9

    elif p_page == 6:
        if mouseX in range(350, 391):
            if mouseY in range(265, 306):
                P6_button_colour1 = p_done_colour
            elif mouseY in range(325, 365):
                P6_button_colour2 = p_done_colour
            elif mouseY in range(385, 426):
                P6_button_colour3 = p_done_colour
        if mouseX in range(10, 61) and mouseY in range(10, 41):
            p_page = 0
            page = 9

    elif p_page == 7:
        if mouseX in range(350, 391):
            if mouseY in range(265, 306):
                P7_button_colour1 = p_done_colour
            elif mouseY in range(325, 365):
                P7_button_colour2 = p_done_colour
            elif mouseY in range(385, 426):
                P7_button_colour3 = p_done_colour
        if mouseX in range(10, 61) and mouseY in range(10, 41):
            p_page = 0
            page = 9