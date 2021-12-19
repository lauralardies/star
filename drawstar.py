import turtle

turtle.colormode(255)
turtle.getscreen().bgcolor(100,149,237)
turtle.title("My Star Drawing")
turtle.shape("turtle")
turtle.color((205,190,112),(255,236,139))
turtle.width(1)

def star(num):

    size = 300
    turtle.penup()
    turtle.goto(-150,0)
    turtle.pendown()
    
    if num % 2 == 0:
        angle = 360 / num
        turtle.begin_fill()
        for side in range(num):
            turtle.fd(size)
            turtle.rt(angle)
            
    else:
        angle = 180 - (180 / num)
        turtle.begin_fill()
        for side in range(num):
            turtle.fd(size)
            turtle.rt(angle)

    turtle.end_fill()
    turtle.done()

while True:
    num = (input("How many points do you want your star to have? (Please insert a number): "))
    if num.isdigit() == True:
        num = int(num)
        star(num)
    else:
        print("This is not a number! Please introduce a valid answer.")
