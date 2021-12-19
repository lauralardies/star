import turtle

def star():

    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    def draw(num, angle, size):
        turtle.showturtle()
        turtle.begin_fill()

        if num == 6:
            for side in range(6):
                turtle.fd(size/3)
                turtle.rt(-60)
                turtle.fd(size/3)
                turtle.rt(angle)

        else:     
            for side in range(num):
                turtle.fd(size)
                turtle.rt(angle)

        turtle.end_fill()
        turtle.done()
    
    while True:
        turtle.colormode(255)
        turtle.getscreen().bgcolor(100,149,237)
        turtle.title("My Star Drawing")
        turtle.shape("turtle")
        turtle.color((205,190,112),(255,236,139))
        turtle.width(3)
        turtle.hideturtle()
        turtle.penup()

        num = turtle.textinput("Draw your star!", "How many points does your star have?")

        if num.isdigit() == True:
            num = int(num)
            
            if num <= 4:
                turtle.clear()   
                turtle.goto(20, 140)
                turtle.write("You can't draw a star with\na number smaller than 5.", font=("Futura", 15, "bold italic"))

            else:
                turtle.clear()   
                if num == 6:
                    angle = 120
                else:
                    for i in range(num // 2, 1, -1):
                        if gcd(num, i) == 1:
                            angle = 360 / num * i
                            break

                turtle.goto(-150,60)
                turtle.pendown()
                
                draw(num, angle, size = 300)
            
        else:
            turtle.clear()   
            turtle.goto(20, 140)
            turtle.write("This is not a number!\nPlease introduce a valid\nanswer.", font=("Futura", 15, "bold italic"))

star()