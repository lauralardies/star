import turtle

def star():

    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    def draw(num, angle, size):
        turtle.begin_fill()

        if num == 6:
            for side in range(3):
                turtle.fd(size)
                turtle.rt(angle)
            turtle.end_fill()

            turtle.penup()
            turtle.goto(-150, -100)
            turtle.pendown()

            turtle.begin_fill()
            for side in range(3):
                turtle.fd(size)
                turtle.lt(angle)
            turtle.end_fill()

        else:     
            for side in range(num):
                turtle.fd(size)
                turtle.rt(angle)
            turtle.end_fill()

        turtle.done()
        
    turtle.colormode(255)
    turtle.getscreen().bgcolor(100,149,237)
    turtle.title("My Star Drawing")
    turtle.shape("turtle")
    turtle.color((205,190,112),(255,236,139))
    turtle.width(1)

    while True:
        num = turtle.textinput("Draw your star!", "How many points does your star have?")
        if num.isdigit() == True:
            num = int(num)

            if num <= 4:
                print("You can't draw a star with a number smaller than 5.")

            else:
                if num == 6:
                    angle = 120
                else:
                    for i in range(num // 2, 1, -1):
                        if gcd(num, i) == 1:
                            angle = 360 / num * i
                            break

                turtle.penup()
                turtle.goto(-150,60)
                turtle.pendown()
                
                draw(num, angle, size = 300)
            
        else:
            print("This is not a number! Please introduce a valid answer.")

star()