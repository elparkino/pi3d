# Bouncing balls example using pi3d module
# ========================================
# Copyright (c) 2012 - Tim Skillman
# Version 0.03 - 29 Nov 2012 - Added DrawString2D to draw text into a 2D context
# 
# This example does not reflect the finished pi3d module in any way whatsoever!
# It merely aims to demonstrate a working concept in simplfying 3D programming on the Pi
#
# Bouncing demonstrates pi3d sprites over the desktop.
# It uses the orthographic view scaled to the size of the window;
# this means that sprites can be drawn at pixel resolution
# which is more common for 2D.  Also demonstrates a mock title bar.

import pi3d, sys, random, array

# Setup display and initialise pi3d
scnx=800
scny=600
display = pi3d.display(100,100,scnx,scny,0)
display.setOrthographic()  #we want a 2D display (as it defaults to 3D)

# Set last value (alpha) to zero for a transparent background!
display.setBackColour(0,0.2,0.6,1)    	
    
# Ball parameters
maxballs = 40
maxballsize = 60
minballsize = 30
maxspeed = 30

# Ball x,y position
bx=[]
by=[]

# Ball direction vector
dx=[]
dy=[]

# Ball size (scale), ball image reference
bs=[]
bi=[]

# Setup ball positions, sizes, directions and colours
for b in range (0, maxballs):
    bx.append(random.random() * scnx)
    by.append(random.random() * scny)
    dx.append((random.random() - 0.5) * maxspeed)
    dy.append((random.random() - 0.5) * maxspeed)
    bs.append(random.random() * maxballsize + minballsize)
    bi.append(int(random.random() * 3))

texs=pi3d.textures()
ball = []
ball.append(texs.loadTexture("textures/red_ball.png"))
ball.append(texs.loadTexture("textures/grn_ball.png"))
ball.append(texs.loadTexture("textures/blu_ball.png"))
bar = texs.loadTexture("textures/bar.png")
bbtitle = texs.loadTexture("textures/pi3dbbd.png",True)

arialFont = pi3d.font("AR_CENA","#ddff88")   #load AR_CENA font and set the font colour

# Fetch key presses
mykeys = pi3d.key()
scshots = 1

while True:
	
    display.clear()
	
    for b in range (0, maxballs):
			    
	# Draw ball (tex,x,y,z,width,height,rotation)
	pi3d.sprite(ball[bi[b]],bx[b],by[b],-2.0,bs[b],bs[b])
	
	# Increment ball positions
	bx[b]=bx[b]+dx[b]
	by[b]=by[b]+dy[b]
	
	# X coords outside of drawing area?  Then invert X direction
	if bx[b]>scnx or bx[b]<0:
		dx[b]=-dx[b]
	
	# Y coords outside of drawing area?  Then invert Y direction
	if by[b]>scny or by[b]<0:
		dy[b]=-dy[b]
    
    pi3d.drawString2D(arialFont,"Raspberry Pi ROCKS!",100,300,80)
	
    #draw a bar at the top of the screen
    pi3d.rectangle(bar,0,scny,scnx,32)
    pi3d.rectangle(bbtitle,5,scny,256+5,32)

    k = mykeys.read()
    if k >-1:
	if k==112:
	    display.screenshot("screen3D"+str(scshots)+".jpg")
	    scshots += 1
	if k==27:
		mykeys.close()
		texs.deleteAll()
		display.destroy()
		break
	

    display.swapBuffers()
