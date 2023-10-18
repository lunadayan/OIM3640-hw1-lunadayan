"""
Question 1
This functio calculates JOhn's random movement for n intersections. At each intersection, John randomly chooses
one of the four directions. The program calculates and returns the manhattan distance from the starting position 
to the final position. The program will print the intersection when JOhn started, how many intersection he did 
and the total blocks from where he started. 
"""

def drunkard_walk(x, y, n):
    import random
    for i in range(n): 
        #randomly pick one of four directions: 1-right, 2-left, 3-up, 4-down
        direction = random.randint(1,4)
        if direction == 1:
            x += 1 #move right
        elif direction == 2:
            x -= 1 #move left
        elif direction == 3:
            y += 1 #move up
        elif direction == 4:
            y -= 1 #move down

    blocks = abs(x)+abs(y) #calculate manhattan distance from the start position (x,y)
    return blocks


def main():
    """
    Please do not change the code below.
    """
    x_0 = 0
    y_0 = 0
    steps = 100
    print(f"The drunkard started from ({x_0}, {y_0}).")
    distance = drunkard_walk(x_0, y_0, steps)
    print(f"After {steps} intersections, he's {distance} blocks from where he started.")


if __name__ == '__main__':
    main()