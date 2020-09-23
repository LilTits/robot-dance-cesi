from pypot.creatures import PoppyErgoJr
poppy = PoppyErgoJr(
    simulator='vrep', 
    scene='poppy_ergo_jr_holder.ttt', 
    camera='dummy'
    )

# Block the motor to move by hand
poppy.m1.compliant = False
poppy.m2.compliant = False
poppy.m3.compliant = False
poppy.m4.compliant = False
poppy.m5.compliant = False
poppy.m6.compliant = False

# Position : Diver
def position_diver():
    poppy.m2.goto_position(-45, 0.3)
    poppy.m3.goto_position(60, 0.3)
    poppy.m5.goto_position(-70, 0.3, wait=True)
    poppy.m6.goal_position = 0
    
position_diver()