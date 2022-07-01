import viz , vizact , vizshape
viz.setMultiSample(4)
viz.fov(60)
viz.go()
viz.MainView.move([0,0,-1])


# Lighting
viz.MainView.getHeadLight().disable()
sky_light = viz.addLight(euler=(0,90,0))
sky_light.color(viz.WHITE)
sky_light.ambient([0,0,-1])

# Additional Add-ons for Later
gallery = viz.addChild('gallery.osgb')

music = viz.addAudio("bach_air.mid",loop=1)

video = viz.addVideo('vizard.mpg',loop=1,play=1)

painting = gallery.getTexture('painting_starry-night')
2
# Avatar 
avatar = viz.addChild('vcc_male2.cfg',pos=[0,0,1])
avatar.state(1)

# Shadow of Avatar 
shadow_texture = viz.addTexture('shadow.png')
shadow = vizshape.addQuad(parent=avatar,axis=vizshape.AXIS_Y)
shadow.texture(shadow_texture)
shadow.zoffset()

vizshape.addAxes()
Randomwaittime = vizact.waittime(vizact.randfloat(5,10))

actions=[]
loc = [[-3.7,2.2,0],[-3.7,6.6,0],[0,8,0],[3.7,6.4,0],[3.7,2.3,0]]

for x,y,a in loc:
	actions.append(vizact.method.playsound('footsteps.wav',viz.LOOP))
	actions.append(vizact.walkTo([x,0,y],turnSpeed=250))
	actions.append(vizact.method.playsound('footsteps.wav',viz.STOP))
	actions.append(vizact.turn(a,250))
	actions.append(Randomwaittime)

avatar.addAction(vizact.sequence(actions,viz.FOREVER))

plantPositions = [[-3.5,0,0],[4,0,0],[4,0,7],[-3.5,0,7]]
plants = []
plant_root = viz.addGroup()
plant_root.visible(False)

for pos in plantPositions:
	plant = viz.addChild('plant.osgb',parent=plant_root,pos=pos ,cache =viz.CACHE_CLONE)
	plants.append(plant)
	
pigeon = viz.addAvatar('pigeon.cfg',pos=(1,8.1,5.9),euler=(180,0,0))
pigeon.state(1)

def scalePlants(val):
    for plant in plants:
        plant.setScale([val]*3)


vizact.onkeydown('p',plant_root.visible,viz.TOGGLE)
vizact.onkeydown('s',scalePlants,vizact.choice([0.5,1.5,2]))
vizact.onkeydown('m',vizact.choice([music.play,music.stop]))
vizact.onkeydown('v',gallery.texture,vizact.choice([video,painting]),'painting_starry-night')