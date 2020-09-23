from pypot.creatures import PoppyErgoJr
import time
from positions import skywatching
poppy = PoppyErgoJr(
    simulator='vrep', 
    scene='poppy_ergo_jr_holder.ttt', 
    camera='dummy'
    )

#intial
poppy.m1.goto_position(0,0)
poppy.m2.goto_position(0,0)
poppy.m3.goto_position(0,0)
poppy.m4.goto_position(0,0)
poppy.m5.goto_position(0,0)
poppy.m6.goto_position(0,0)

#position imposée 1 - reverse
def Reverse() :
    '''
    poppy.m3.goto_position(0, 4, wait=True)
    poppy.m2.goto_position(0, 4, wait=True)
    poppy.m5.goto_position(0, 4, wait=True)
    time.sleep(3)
    '''
    poppy.m2.goto_position(0, 1, wait=True)
    poppy.m3.goto_position(-90, 1, wait=True)
    poppy.m5.goto_position(-90, 1, wait=True)
    
#position imposée 2 - skywatching
def skywatching():
    poppy.m1.goto_position(0,0)
    poppy.m2.goto_position(0,0)
    poppy.m3.goto_position(0,0)
    poppy.m4.goto_position(0,0)
    poppy.m6.goto_position(0,0)
    poppy.m5.goto_position(-90,5, wait=True)
    time.sleep(3)
    
#position imposée 3 - diver
def position_diver():
    poppy.m2.goto_position(-45, 0.3)
    poppy.m3.goto_position(60, 0.3)
    poppy.m5.goto_position(-70, 0.3, wait=True)
    poppy.m6.goal_position = 0
    
#routine imposée 1 - balai-brosse
def balai_brosse() :
    poppy.m5.goto_position(-90, 2)
    poppy.m2.goto_position(70, 2)
    poppy.m3.goto_position(0, 2)
    time.sleep(2)
    poppy.m1.goto_position(180, 2, wait=True)
    poppy.m1.goto_position(0, 2, wait=True)

#routine imposée 2 - shaker
def shaker() :
    poppy.m3.goto_position(0, 2, wait=True)
    poppy.m2.goto_position(0, 2, wait=True)
    poppy.m5.goto_position(0, 2, wait=True)
    poppy.m1.goto_position(1440, 6)
    for i in range(3) :
        
        poppy.m5.goto_position(90, 1, wait=True)
        poppy.m5.goto_position(0, 1, wait=True)
        
#routine imposée 3 - looping


#custom 1
def custom1():
    poppy.m1.goto_position(90,50, wait=True)
    poppy.m1.goto_position(-90,25, wait=True)
    poppy.m4.goto_position(90,25)
    poppy.m2.goto_position(90,25)
    poppy.m1.goto_position(90,25, wait=True)
    poppy.m2.goto_position(-90,25)
    poppy.m4.goto_position(-90,25)

#custom 2
def position_custom_2():
    i = 0
    while i < 3:
        poppy.m1.goto_position(-180, 0.5)
        poppy.m1.goto_position(180, 0.5, wait=True)
        
        poppy.m2.goto_position(-70, 0.5)
        poppy.m2.goto_position(-25, 0.5)
        
        poppy.m3.goto_position(70, 0.5)
        poppy.m3.goto_position(50, 0.5)
        
        poppy.m5.goto_position(-80, 0.5)
        poppy.m5.goto_position(-60, 0.5, wait=True)
        i = i + 1
        
#custom 3
