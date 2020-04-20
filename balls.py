##-----------------------------------------------------------------------##
## Covid-19 Simulator Project:                                           ##
## Code to replicate bouncing balls of Simulitis                         ##
## https://www.washingtonpost.com/graphics/2020/world/corona-simulator/  ##
##-----------------------------------------------------------------------##
##  1. Packages/Dependencies
##  2. Set basic Figure
##  3. Define Ball Class
##  4. Animate Plot
##  5. Play Plot
##--------------------------------------------------##

##--------------------------------------------------##
## 1. Packages/Dependencies                         ##
##--------------------------------------------------##
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import threading
##--------------------------------------------------##
## 2. Set basic Figure                              ##
##--------------------------------------------------##
# bounds of the room
xlim = (0,20)
ylim = (0,20)

# 1 millisecond delta t
delta_t = 0.001

# Limits of PLotGrid
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=xlim, ylim=ylim)
ax.grid()

##--------------------------------------------------##
## 3. Define Ball Class  and Helping Functions      ##
##--------------------------------------------------##
# def get_Color():
#     color1 = 'green'
#     return color1

class Ball(object):


    def __init__(self, xy, v):
        """
        :param xy: Initial position.
        :param v: Initial velocity.
        """
        self.xy = np.array(xy)
        self.v = np.array(v)
        #self.radius = 9
        #self.color = get_Color()
        self.scatter, = ax.plot([], [], 'o', markersize=20, color='green')

    # Function to accses xy Coordinates
    def get_list(self):
        return self.xy

    # Function to update Position (Bounce Back of Walls)
    def update(self):
        if self.xy[0] <= xlim[0]:
            # hit the left wall, reflect x component
            self.v[0] =  np.abs(self.v[0])

        elif self.xy[0] >= xlim[1]:
            self.v[0] = - 1 * np.abs(self.v[0])

        if self.xy[1] <= ylim[0]:
            # hit the left wall, reflect y component
            self.v[1] =  np.abs(self.v[1])

        elif self.xy[1] >= ylim[1]:
            self.v[1] = - 1 * np.abs(self.v[1])

        # Update Position of Ball
        self.xy += self.v

        # Clip off the Ball if the radius goes over the Axes
        self.xy[0] = np.clip(self.xy[0], xlim[0], xlim[1])
        self.xy[1] = np.clip(self.xy[1], ylim[0], ylim[1])

        # Set data in case of no Collusion
        self.scatter.set_data(self.xy)

    # Function to Update the Movement if Balls hit each other
    def collusion(self):

        self.v = -1 * self.v

        self.xy += self.v

        self.scatter, = ax.plot([], [], 'o', markersize=20, color='red')

        #timer = threading.Timer(2.0, )
        #timer.start()

        self.scatter.set_data(self.xy)


b0 = Ball((3.0,18.0), (0.1,0.1))
b1 = Ball((12.0,1.0), (0.1,0.1))
b2 = Ball((25.0,15.0), (0.1,0.1))
#balls = [Ball((3.0,18.0), (0.1,0.1)), Ball((12.0,1.0), (0.1,0.1)), Ball((25.0,19.0), (0.1,0.1))] ##  List Option for Balls


def init():
    return []

def animate(t):
    # t is time in secondss
    global xy, v

    # Round values for collusion check (to happen faster)
    b0_check = np.around(b0.get_list(), decimals=0)
    #print(b0_check)
    b1_check = np.around(b1.get_list(), decimals=0)
    #print(b1_check)
    b2_check = np.around(b2.get_list(), decimals=0)
    #print(b2_check)

# Code checking whether collusion function works:
    # if b1_check[1] == b2_check[1]:
    #     print('colllusion happened')
    #     b0.collusion()
    #     b1.update()
    #     b2.collusion()
    # elif b1_check[1] != b2_check[1]:
    #     print('update happened')
    #     b0.update()
    #     b1.update()
    #     b2.update()

    # Schleife die auf Gleiche Koordinaten checkt
    if b0_check[0] == b2_check[0] and b0_check[1] == b2_check[1] :
        print('colllusion happened')
        b0.collusion()
        b1.update()
        b2.collusion()
    elif b1_check[0] == b2_check[0] and b1_check[1] == b2_check[1]:
        print('colllusion happened')
        b0.update()
        b1.collusion()
        b2.collusion()
    elif b0_check[0] == b1_check[0] and b0_check[1] == b1_check[1]:
        print('colllusion happened')
        b0.collusion()
        b1.collusion()
        b2.update()
    else:
        print('update happened')
        print(b0_check)
        print(b1_check)
        print(b2_check)
        b0.update()
        b1.update()
        b2.update()

    # check for similar coordinates:
    # if b0_check[0] == b2_check[0] or b0_check[1] == b2_check[1] :
    #     if np.sum(b0_check) == np.sum(b2_check):
    #         print('colllusion happened')
    #         b0.collusion()
    #         b1.update()
    #         b2.collusion()
    # elif b1_check[0] == b2_check[0] and b1_check[1] == b2_check[1]:
    #     if np.sum(b1_check) == np.sum(b2_check):
    #         print('colllusion happened')
    #         b0.update()
    #         b1.collusion()
    #         b2.collusion()
    # elif b0_check[0] == b1_check[0] and b0_check[1] == b1_check[1]:
    #     print('colllusion happened')
    #     b0.collusion()
    #     b1.collusion()
    #     b2.update()
    # else:
    #     print('update happened')
    #     print(b0_check)
    #     print(b1_check)
    #     print(b2_check)
    #     b0.update()
    #     b1.update()
    #     b2.update()

    #for ball in balls:  ##  List Option for Balls
    #    ball.update()
    # or
    # b0.update()
    # b1.update()
    # b2.update()

    # have to return an iterable
    #return [ball.scatter for ball in balls]  ##  List Option for Balls
    return [b0.scatter, b1.scatter, b2.scatter]

# interval in milliseconds
# we're watching in slow motion (delta t is shorter than interval)
ani = animation.FuncAnimation(fig, animate, np.arange(0,100,delta_t), init_func=init, interval=10, blit=True)

plt.show()
