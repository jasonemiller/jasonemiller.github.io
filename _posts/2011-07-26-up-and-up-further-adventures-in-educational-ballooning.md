---
author: jason
date: 2011-07-26 19:30:52+00:00
layout: post
title: 'Up and Up:  Further adventures in educational ballooning'
tags: higher-education STEM hackedu
---


![Kauffman_balloon_-_tiltshift](/assets/images/kauffman_balloon_-_tiltshift.JPG.scaled1000.jpg)

 Today, I made significant progress in the alpha testing of my instantiation of _Make Magazine_'s "Helium Balloon Imaging Satellite" project (from volume 24). I was ably and enthusiastically assisted by Christian Johns, a college student who will be a Youth Leader for the three-day summer program that's motivating my efforts. Even though we started the day with all materials assembled (_e.g._, PICAXE microcontrollers, modified Aries cameras, the payload platform), ironing out the kinks took about four hours. I'll leave the gory details until another post (if there's interest) including our protocol for launching and downloading pics. For now, I'll share pics of what we're doing, and a couple videos.<!-- more -->Here's a pic of the payload platform we're using. The 12 gauge wire that connects the CD to the pill bottle is secured through their holes with bent wire and and glue so there's less in-flight play in the materials. The 'plug' that connects the Aries camera to the PICAXE microcontroller comes apart too easily, so we decided to tape the connectors together and take the wires to the platform.

![Kauffman_balloon_-_gondola_110725](/assets/images/kauffman_balloon_-_gondola_110725.JPG.scaled1000.jpg)

We learned, after launching our rig a couple times and only getting two pics each time (instead of 25), that the two initial delay values used in the PICAXE program (p.85, the narrative description of the code does not reflect the true timing in the code) were too long for the Aries camera. The program picture in the instructions shows a delay of 30000 microseconds, but that's the same delay the Aries camera uses to decide to power down. So we tweaked the values to 25000 microseconds. That fixed things. Note that the example code downloadable from [here](http://makezine.com/24/ballooncam/) does work as described int he narrative.

![Balloon_ready_to_launch](/assets/images/balloon_ready_to_launch.JPG.scaled500.jpg)

We also decided that connecting the battery to the PICAXE controller is a big PITA, and we'd like to find a way to put a switch between the power and the microcontroller. This would make launch considerably easier. That modification will wait until I can identify a good switch to use.

Our first real test of the balloon assembly used a Flip MinoHD video recorder instead of the Aries camera + PICAXE system. Here are videos of the rig on it's pre-alpha flight: one is from the ground, and one is from the rig itself. They are gently edited for length. The first is a ground-based view of our antics. The second is from the balloon-cam.

![](/assets/images/frame_00002.png)

[Kauffman Balloon](/assets/media/kauffman_balloon_-_ground_110725_for_web.m4v)

![](/assets/images/frame_00003-300x169.png)

[Kauffman Balloon](/assets/media/Balooning_-_first_flight.mov)

Later, we tested the Aries + PICAXE system. Below are some pics we took. For these, we moved our position so we could capture Universities facilities that support a new locavore initiative (_e.g._, plots of pepper plants, tomato plants, corn, and herbs gardens along with a food prep building with refrigeration.) The pics were taken at the camera's default resolution and compression.

![Buildings_and_rows](/assets/images/buildings_and_rows.JPEG.scaled500.jpg)
![Greenhouse_and_rows](/assets/images/greenhouse_and_rows.JPEG.scaled1000.jpg)
![Papper_and_tomato_plants](/assets/images/papper_and_tomato_plants.JPEG.scaled1000.jpg)
![Prep_buildings](/assets/images/prep_buildings.JPEG.scaled1000.jpg)

All in all, this was a successful test of Make Magazine's Helium Balloon Imaging Satellite.  Hopefully the kids in next week's summer program will think it's cool.
