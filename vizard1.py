"""Getting Started with Virtual Reality 
By Hrithik 
29th April 2022 """

 
import viz 
viz.setMultiSample(4) # Smooths out jagged edges 

viz.go()
viz.MainWindow.fov(60) # Increase the view angle from 40 degreee to 60 degreee
piazza = viz.addChild('ground_grass.osgb')
viz.MainView.collision(viz.ON) # Gives you collision effects 

import vizshape
vizshape.addAxes() # Adds axes to the center as r-x , y-b ,z-g

plant = viz.addChild('plant.osgb') # Adds the plant object to the vr 
plant.setPosition([4,0,6]) # To set the posiuition of the plant object 


""" Moving the ViewPoint"""
viz.MainView.move([3,0,-7]) # Changes the initial Start Point 
viz.MainView.setPosition([0,15,-15])


""" Manipulating 3D Models """

plants= []
for x in [-3, -1, 1, 3]:
   for z in [4, 2, 0, -2, -4]:
        plant = viz.addChild('plant.osgb',cache=viz.CACHE_CLONE)
        plant.setEuler([0,0,0])  # Manipulate Yaw , Pitch , Roll 
        plant.setPosition([x,0,z]) # Manipulate the position in 3D coordinates 
        plant.setScale([0.5,0.5,0.5]) # Manipulate the size of the object 
        plants.append(plant)
     

import vizact 
spin = vizact.spin(0,1,0,15)

for plant in plants:
     plant.addAction(spin)


male = viz.addAvatar('vcc_male.cfg')
male.setPosition([4.5, 0, 7])
male.setEuler([0,0,0])

female = viz.addAvatar('vcc_female.cfg')
female.setPosition([4.5,0,9])
female.setEuler([180,0,0])


male.state(14)
female.state(14)

import random

pigeons = []
for i in range(10):

    #Generate random values for position and orientation
    x = random.randint(-4,3)
    z = random.randint(4,8)
    yaw = random.randint(0,360)

    #Load a pigeon
    pigeon = viz.addAvatar('pigeon.cfg')

    #Set position, orientation, and state
    pigeon.setPosition([x,0,z])
    pigeon.setEuler([yaw,0,0])
    pigeon.state(1)

    #Append the pigeon to a list of pigeons
    pigeons.append(pigeon)
    
    
def walkAvatars():
    walk1 = vizact.walkTo([4.5, 0,-40])
    vizact.ontimer2(0.5,0,female.addAction,walk1)

    walk2 = vizact.walkTo([3.5,0,-40])
    male.addAction(walk2)

def pigeonsFeed():

    random_speed = vizact.method.setAnimationSpeed(0,vizact.randfloat(0.7,1.5))
    random_walk = vizact.walkTo(pos=[vizact.randfloat(-4,4),0,vizact.randfloat(3,7)])
    random_animation = vizact.method.state(vizact.choice([1,3],vizact.RANDOM))
    random_wait = vizact.waittime(vizact.randfloat(5.0,10.0))
    pigeon_idle = vizact.sequence( random_speed, random_walk, random_animation, random_wait, viz.FOREVER)

    for pigeon in pigeons:
        pigeon.addAction(pigeon_idle)

vizact.onkeydown('p',pigeonsFeed)