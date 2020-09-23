from pypot.creatures import PoppyErgoJr
import time
poppy = PoppyErgoJr(
    simulator='vrep', 
    scene='poppy_ergo_jr_holder.ttt', 
    camera='dummy'
    )

def looping():
    #Initial
    poppy.m1.goto_position(-180,1, wait=True)
    poppy.m4.goto_position(-180,1, wait=True)
    poppy.m5.goto_position(90,1, wait=True)
    poppy.m2.goto_position(90,1, wait=True)
    poppy.m3.goto_position(0,1, wait=True)
    poppy.m6.goto_position(0,0)
    
    #Final
    poppy.m1.goto_position(-180,1)
    poppy.m4.goto_position(-180,1)
    poppy.m5.goto_position(-90,1)
    poppy.m2.goto_position(0,1)
    poppy.m3.goto_position(90,1)
    poppy.m6.goto_position(0,0)
    
looping()