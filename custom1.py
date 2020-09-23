from pypot.creatures import PoppyErgoJr
poppy = PoppyErgoJr(
    simulator='vrep', 
    scene='poppy_ergo_jr_holder.ttt', 
    camera='dummy'
    )

#custom 1

poppy.m1.goto_position(0,0)
poppy.m2.goto_position(0,0)
poppy.m3.goto_position(0,0)
poppy.m4.goto_position(0,0)
poppy.m5.goto_position(0,0)
poppy.m6.goto_position(0,0)

poppy.m1.goto_position(90,50, wait=True)
poppy.m1.goto_position(-90,25, wait=True)
poppy.m4.goto_position(90,25)
poppy.m2.goto_position(90,25)
poppy.m1.goto_position(90,25, wait=True)
poppy.m2.goto_position(-90,25)
poppy.m4.goto_position(-90,25)