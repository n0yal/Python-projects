import turtle
import random
import time


WIDTH, HEIGHT= 500, 500
COLORS = ['red','green','blue','orange','yellow', 'black','purple', 'pink','brown','cyan']
def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title('Turtle Racing')


def get_number_of_racers():
    while True:
        racers = input('How many racers do you want?(2-10): ')
        try:
            racers = int(racers)
        except ValueError :
            print('Please type in an number')
            continue
        if 2 <= racers <= 10:
            return racers
        else:
            print('Check if you have typed in an integer that is greater than' \
                    ' 2 and less than 10')


def create_turtles(colors):
    turtles = []
    spacing = WIDTH // (len(colors) + 1)
    for index, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        # position of the racer
        racer.setpos(-WIDTH//2 + (index+1) * spacing,-HEIGHT //2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles
    

def race_turtles(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)
            x,y = racer.pos()
            if y >= HEIGHT //2 - 20:
                return colors[turtles.index(racer)]


racers = get_number_of_racers()
random.shuffle(COLORS)
colors = COLORS[:racers]
init_turtle()
winner = race_turtles(colors)
print(f'The winner color is {winner}!')
time.sleep(5)




