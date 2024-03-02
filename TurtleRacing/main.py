import turtle #https://docs.python.org/3/library/turtle.html
import time
import random


WIDTH, HEIGHT = 500, 500
COLORS = ['red','green','blue','orange','yellow','black','purple','pink','brown','cyan']
def get_number_of_racers():
    racers = 0;
    while True:
        racers = input("Enter the number of racers (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric... Try again!")
            continue #brings back to the beggining of the while loop
        
        if 2 <= racers <= 10:
            return racers
        else:
            print("Number must be between 2 and 10. Try again!")

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("Turtle Racing")

def create_turtles(colors):
    turtles = []
    spacingX = WIDTH // (len(colors) + 1) #// returns an integer
    for i, color in enumerate(colors):# enumerate gives the index and the values in colors
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)#points the turtle to the top
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i+1) * spacingX, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    
    return turtles

def race(colors):
    turtles = create_turtles(colors)
    
    while True:
        for racer in turtles:
            distance = random.randrange(1,20)# every time the turtle moves, it's between 1 and 20 pixels
            racer.forward(distance)
            
            x, y = racer.pos()
            #returns the winning turtle
            if y >= HEIGHT // 2 -10:
                return colors[turtles.index(racer)]


racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)# shuffles the array
colors = COLORS[:racers]# gaves the first n colors, n = number of racers

winner = race(colors)

print(f"The winner is the turtle with color: {winner}!")
time.sleep(2)
