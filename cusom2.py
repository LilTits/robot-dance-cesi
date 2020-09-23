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

# Position : custom 2
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
    
position_custom_2()