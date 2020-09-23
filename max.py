import time
from pypot.creatures import PoppyErgoJr
poppy = PoppyErgoJr(
    simulator='vrep', 
    scene='poppy_ergo_jr_holder.ttt', 
    camera='dummy'
    )

#position 2 : skywatching
poppy.m1.goto_position(0,0)
poppy.m2.goto_position(0,0)
poppy.m3.goto_position(0,0)
poppy.m4.goto_position(0,0)
poppy.m5.goto_position(-90,0, wait=True)
poppy.m6.goto_position(0,0, wait=True)
time.sleep(3)