import time
from pypot.creatures import PoppyErgoJr
poppy = PoppyErgoJr(
    simulator='vrep', 
    scene='poppy_ergo_jr_holder.ttt', 
    camera='dummy'
    )


#Routine imposée 1 : le balai-brosse  6 secondes
def balai_brosse() :
    poppy.m5.goto_position(-90, 2)
    poppy.m2.goto_position(70, 2)
    poppy.m3.goto_position(0, 2)
    time.sleep(2)
    poppy.m1.goto_position(180, 2, wait=True)
    poppy.m1.goto_position(0, 2, wait=True)




#Routine imposée 2 : le shaker    12 secondes
def shaker() :
    poppy.m3.goto_position(0, 2, wait=True)
    poppy.m2.goto_position(0, 2, wait=True)
    poppy.m5.goto_position(0, 2, wait=True)
    poppy.m1.goto_position(1440, 6)
    for i in range(3) :
        
        poppy.m5.goto_position(90, 1, wait=True)
        poppy.m5.goto_position(0, 1, wait=True)
    



# Position imposée 1 : Reverse    3 secondes
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
    
balai_brosse()
shaker()
Reverse()