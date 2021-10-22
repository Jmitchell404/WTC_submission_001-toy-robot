# TODO: Decompose into functions

def dir_square(size = 10):
    """
    This is the direction_square.
    step(1/4)
    """
    print("Moving in a square of size "+str(size))
    for i in range(4):
        degrees = 90
        print("* Move Forward "+str(size))
        print("* Turn Right "+str(degrees)+" degrees")

def dir_squaredancing(size = 20):
    """
    This is the direction_squaredancing.
    step(1/4)
    """
    print(f"Square dancing - 3 squares of size {size}")
    for i in range(3):
        print("* Move Forward "+str(size))
        print(f"Moving in a square of size {size}")
        for j in range(4):
            degrees = 90
            print("* Move Forward "+str(size))
            print("* Turn Right "+str(degrees) + " degrees")

def dir_rectangle(length = 20, width = 10):
    """
    This is the direction_rectangle.
    step(1/4)
    """
    print("Moving in a rectangle of "+str(length)+" by "+str(width))
    for i in range(2):
        degrees = 90
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
        print("* Move Forward "+str(width))
        print("* Turn Right "+str(degrees)+" degrees")

def dir_circle():
    """
    This is the direction_circle.
    step(1/4)
    """
    print("Moving in a circle")
    degrees = 1
    for i in range(360):
        length = 1
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")

def dir_cropcircle(length = 20):
    """
    This is the direction_cropcircle.
    step(1/2/4)
    """
    print("Crop circles - 4 circles")
    for i in range(4):   
        print("* Move Forward "+str(length))
        dir_circle()

def move():
    """
    step(3)
    """
    dir_square()
    dir_rectangle()
    dir_circle()
    dir_squaredancing()
    dir_cropcircle()

def robot_start():
    move()

if __name__ == "__main__":
    robot_start()
