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

# Position : Start and stop
def position_start_stop():
    poppy.m2.goal_position = 0
    poppy.m3.goal_position = 0
    poppy.m5.goal_position = 0
    poppy.m6.goal_position = 0
    
position_start_stop()