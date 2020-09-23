import time
from pypot.creatures import PoppyErgoJr
poppy = PoppyErgoJr(
    simulator='vrep', 
    scene='poppy_ergo_jr_holder.ttt', 
    camera='dummy'
    )


poppy.m3.goto_position(0, 4, wait=True)
poppy.m2.goto_position(0, 4, wait=True)
#poppy.m4.goto_position(180, 4, wait=True)
poppy.m5.goto_position(0, 4, wait=True)
time.sleep(3)
poppy.m3.goto_position(-90, 4, wait=True)
poppy.m5.goto_position(-90, 4, wait=True)