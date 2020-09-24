from pypot.creatures import PoppyErgoJr
import time
poppy = PoppyErgoJr(
    simulator='vrep', 
    scene='poppy_ergo_jr_holder.ttt', 
    camera='dummy'
    )

#######################################################

# Position : Start and stop
def start_stop():
    poppy.m1.goal_position = 0
    poppy.m2.goal_position = 0
    poppy.m3.goal_position = 0
    poppy.m4.goal_position = 0
    poppy.m5.goal_position = 0
    poppy.m6.goal_position = 0
    
#######################################################

#position imposée 1 - reverse
def reverse() :
    poppy.m2.goto_position(0, 2, wait=True)
    poppy.m3.goto_position(-90, 2, wait=True)
    poppy.m5.goto_position(-90, 2, wait=True)
    
#position imposée 2 - skywatching
def skywatching():
    poppy.m1.goto_position(0, 2)
    poppy.m2.goto_position(0, 2)
    poppy.m3.goto_position(0, 2)
    poppy.m4.goto_position(0, 2)
    poppy.m6.goto_position(0, 2, wait=True)
    poppy.m5.goto_position(-90, 0.1)
    
#position imposée 3 - diver
def diver():
    poppy.m2.goto_position(-45, 2)
    poppy.m3.goto_position(60, 2)
    poppy.m5.goto_position(-70, 2, wait=True)
    poppy.m6.goal_position = 0
    
#######################################################
    
#routine imposée 1 - balai-brosse
def broom() :
    poppy.m5.goto_position(-90, 2)
    poppy.m2.goto_position(70, 2)
    poppy.m3.goto_position(0, 2)
    time.sleep(2)
    poppy.m1.goto_position(180, 1, wait=True)
    poppy.m1.goto_position(0, 1, wait=True)

#routine imposée 2 - shaker
def shaker() :
    poppy.m3.goto_position(0, 2, wait=True)
    poppy.m2.goto_position(0, 2, wait=True)
    poppy.m5.goto_position(0, 2, wait=True)
    poppy.m1.goto_position(720, 3)
    poppy.m5.goto_position(90, 1.5, wait=True)
    poppy.m5.goto_position(0, 1.5, wait=True)
        
#routine imposée 3 - looping
def looping():
    #Initial
    poppy.m1.goto_position(-180, 1, wait=True)
    poppy.m4.goto_position(-180, 1, wait=True)
    poppy.m5.goto_position(90, 1, wait=True)
    poppy.m2.goto_position(90, 1, wait=True)
    poppy.m3.goto_position(0, 1, wait=True)
    poppy.m6.goto_position(0, 0)
    #Final
    poppy.m1.goto_position(-180, 1)
    poppy.m4.goto_position(-180, 1)
    poppy.m5.goto_position(-90, 1)
    poppy.m2.goto_position(0, 1)
    poppy.m3.goto_position(90, 1)
    poppy.m6.goto_position(0, 0)
    
#######################################################

#custom 1
def custom1():
    poppy.m2.goto_position(0, 0.5)
    poppy.m3.goto_position(0, 0.5)
    poppy.m4.goto_position(0, 0.5)
    poppy.m5.goto_position(0, 0.5)
    poppy.m6.goto_position(0, 0.5)
    poppy.m1.goto_position(90, 2, wait=True)
    poppy.m1.goto_position(-90, 1, wait=True)
    poppy.m4.goto_position(90, 1)
    poppy.m2.goto_position(90, 1)
    poppy.m1.goto_position(90, 2, wait=True)
    poppy.m2.goto_position(-90, 2)
    poppy.m4.goto_position(-90, 2)
    poppy.m1.goto_position(180, 2, wait=True)

#custom 2
def custom2():
    poppy.m1.goto_position(-180, 2, wait=True)
    poppy.m1.goto_position(180, 2)
    poppy.m2.goto_position(-70, 2, wait=True)
    poppy.m2.goto_position(-25, 2)
    poppy.m3.goto_position(70, 2, wait=True)
    poppy.m3.goto_position(50, 2)
    poppy.m5.goto_position(-80, 2, wait=True)
    poppy.m5.goto_position(-60, 2)
        
#custom 3
def custom3() :
    time.sleep(1.5)
    poppy.m5.goto_position(-90, 2, wait=True)
    poppy.m4.goto_position(720, 3)
    poppy.m3.goto_position(-90, 1.5, wait=True)
    poppy.m3.goto_position(90, 1.5, wait=True)

#######################################################
        
        
#function calls
start = time.time()
start_stop()
print("hello")
reverse()
print("reverse done")
custom2()       
print("custom 2 done")
skywatching()
print("skywatching done")
custom3()
print("custom 3 done")
broom()
print("broom done")
shaker()
print("shaker done")
diver()
print("diver done")
custom1()
print("custom 1 done")
looping()
print("looping done")
start_stop()
end = time.time()
print(end - start)