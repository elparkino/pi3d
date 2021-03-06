## **Pi3D ReadMe**

![Pi3D logo](http://www.skillmanmedia.com/pi3d/images/rpi3dlogo256.png)

**Pi3D (vsn 0.07) written by Tim Skillman, Copyright (c) 2012**

**EGG & OBJ file loader written by Paddy Gaunt, Copyright (c) 2012**

# Description

There's plenty of 3D code flying around at the moment for the Raspberry Pi, but much of it is rather complicated to understand and most of it can sit under the bonnet!

pi3d is a Python module that aims to greatly simplify writing 3D in Python whilst giving access to the power of the Raspberry Pi GPU. It enables both 3D and 2D rendering and aims to provide a host of exciting commands to load in textured/animated models, create fractal landscapes, shaders and much more.

This is the third release of the pi3d module which has various demo's of built-in shapes, landscapes, model loading, walk-about camera and much more! See the demos included with this code and experiment with them ..


# Demo's included with Pi3D

1) **ForestWalk.py** Walk about a forest on a landscape generated from a bitmap

![Forest Walk](http://www.skillmanmedia.com/pi3d/images/ForestWalk_sml.png)

2) **Triceratops.py** Large model loading with several bitmaps

![Triceratops](http://www.skillmanmedia.com/pi3d/images/Triceratops_sml.png)

3) **BuckfastAbbey.py** Explore a model of the beautiful Buckfast Abbey in Buckfastleigh, Devon

![Buckfast Abbey](http://www.skillmanmedia.com/pi3d/images/BuckfastAbbey_sml.png)

4) **Earth.py** Demonstrates semi-transparent clouds and hierarchical rotations 

![Earth](http://www.skillmanmedia.com/pi3d/images/earthPic_sml.png)

5) **BouncingBalls.py** 2D rendering with a title bar and 2D text 

![Bouncing Balls](http://www.skillmanmedia.com/pi3d/images/bouncingballs_sml.jpg)

6) **Raspberry_Rain.py** Raining Raspberries,  full-screen, over the desktop 

![Raspberry_Rain](http://www.skillmanmedia.com/pi3d/images/raspberryRain_sml.png)

7) **Clouds3D.py** Blended sprites in perspective view 

![Clouds 3D](http://www.skillmanmedia.com/pi3d/images/clouds3D_sml.png)

8) **CollisionBalls.py** More bouncing balls across the screen - this time bouncing off each other on the desktop

![Collision Balls](http://www.skillmanmedia.com/pi3d/images/collisionballs.jpg)

9) **EnvironmentCube.py** New environment cubes to try out in texture/ecubes - some high quality ones!

![Environment Cube](http://www.skillmanmedia.com/pi3d/images/envcube_sml.png)

10) **RobotWalkabout.py** Another off-planet example of a basic avatar robot drifting about

![Robot Walkabout](http://www.skillmanmedia.com/pi3d/images/walkaboutRobot_sml.png)

11) **Shapes.py** Demos available shapes and text in a 3D context

![Shapes](http://www.skillmanmedia.com/pi3d/images/shapes_sml.png)

12) **MarsStation.py** Navigate around an abandoned Mars base-station with open/shut doors. 
Implements a new Level-Of-Detail (LOD) feature and TKwindow interface

![Mars Station](http://www.skillmanmedia.com/pi3d/images/MegaStation_sml.png)

13) **TigerTank.py** Ever played World Of Tanks (WOT)? This tank emulates how a WOT tank works. 
Uses realistic modelling and LODing in a TKwindow

![Tiger Tank](http://www.skillmanmedia.com/pi3d/images/TigerTank_sm.png)

14) **Amazong.py** Can you find yourself around the amazing maze?  Written by Paddy Gaunt.

![Amazing](http://www.skillmanmedia.com/pi3d/images/amazing_sml.png)

15) **Pong.py**  A snazzy 3D version of landscape pinball and pong against a Raspberry!   Written by Paddy Gaunt.

![Pong](http://www.skillmanmedia.com/pi3d/images/pong_sml.png)

16) **HelloWorldWindow.py** A simple demo showing how to add a window to your Pi3D project

![HelloWorldWindow](http://www.skillmanmedia.com/pi3d/images/earthPic_sml.png)

17) **ConferenceHall.py** Walkabout a realistic baked-texture conference hall

![Conference Hall](http://www.skillmanmedia.com/pi3d/images/confHall_sml.jpg)


# Files and folders in this repository


1. **pi3d.py** The main pi3d module
2. **include** Contains pi3d support files
3. **textures** Various textures to play with
4. **models** Demo egg models
5. **fonts** Bitmap fonts that can be using for drawing text
6. **screenshots** Example screenshots of the demos included
7. **images** used for ReadMe.html
8. **ChangeLog.txt** Latest changes of Pi3D
9. **ReadMe.md** This file
10. **ReadMe.html** HTML readme


# Setup on the Raspberry Pi


1) **Memory Split setup**

Although most demos work on 64MB of memory, you are strongly advised to have a 128MB of graphics memory split, especially for full-screen 3D graphics.  In the latest Raspbian build you need to edit the config.txt file (in the boot directory) and set the variable 'gpu_mem=128' for 128MB of graphics memory.
 

2) **Install Python Imaging**

Before trying any of the demos or Pi3D, you must download the Python Imaging Library as this is needed for importing any graphics used by Pi3. To install on the terminal, type: 

      sudo apt-get install python-imaging python-imaging-tk


3) **Install Geany to run Pi3D**

Geany is by far the easiest and most compatible application to use for creating and running Python scripts. Download and install it with:

      sudo apt-get install geany xterm

4) **Load and run**


Load any of the demos into Geany and run (using the cogs icon)



# Pi3D Website


Models, code, news and resources are continually updated on http://www.pi3d.net (or .co.uk,.org)


# Documentation


A short 'manual' on using pi3d can be found on this github. Please note that Pi3D functions may change significantly during it's development.

Bug reports, comments, feature requests and fixes are most welcome!

Please email on timskillman@gmail.com or contact me through the Raspberry Pi forums.

# Acknowledgements

Pi3D started with code based on Peter de Rivaz 'pyopengles' (https://github.com/peterderivaz/pyopengles) with some tweaking from Jon Macey's code (jonmacey.blogspot.co.uk/2012/06/). 

The Panda3D loaderEgg.py and LoaderObj.py modules are written by Paddy Gaunt (Copyright (c) 2012)

Many Thanks, especially to Paddy Gaunt, Peter de Rivaz, Tom Swirly, Jon Macey and others who have contributed to Pi3D - keep up the good work!

A new version of Pi3D implementing Shaders will be available in the near future. Keep watch!


**PLEASE READ LICENSING AND COPYRIGHT NOTICES IF USING FOR COMMERCIAL PURPOSES ESPECIALLY**


