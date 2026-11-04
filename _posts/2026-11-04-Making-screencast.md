---
title: Note on making a screencast for teaching
author: Jason
layout: post
date: 2026-11-4
tags: teaching
---

Each semester, I need to make a video for student asynchronous viewing.  This is a note about how I do this now.

Tools I use are:

* macOS machine
* iPad with Apple pencil
* GoodNotes iOS app
* QuickTime Player
* USB-C to USB-C cable
* Yeti microphone connected to headphones with 3.5mm cable

I record on a macOS machine running the [OBS app](https://obsproject.com/welcome).  I connect an iPad to my machine with a USB-C to USB-C cable.  I also use a Yeti microphone and a headset connected directly to the microphone with a 3.5mm cable.  (This allows me to monitor audio while I'm recording with no dependence on the software or its settings.)

After making sure the iPad 'trusts' the macOS machine, I open QuickTime Player and in the `File` menu, select `New Movie Recording`.    A small dialog will open up with a red record button in the center.  To the button's right is a small downward pointing arrow/chevron.  Click on it and a menu will appear.  In the `Screen` section of the menu, choose your iPad.

A QuickTime window will open up showing the screen of your iPad.

Open OBS.  Create and name a new Scene.  Add a new source by clicking on the `+` button; in window that appears, choose`macOS Screen Capture` in the left column and then, in the window to the right click on the `+ Add a new macOS Screen Capture`.  A window titled `Properties for macOS ScreenCapture`will open with two drop-down menus below the midline, one titled `Method` and the other titled `Window`.  In the `Method` menu, choose `Window Capture`.   In the `Window` menu, a list of your screens will show up.  Choose the option that starts with `[QuickTime Player]`.    This will cause your iPad screen to appear in the OBS app window.  Click `OK` in the `Properties for macOS ScreenCapture` window to close it.

Next, you will want to resize and crop the appearance of your iPad screen.  I use GoodNotes, so I like to crop out the GoodNotes menu.  

If the iPad screen is appearing cropped or otherwise the wrong size try this:
* control-click on the `macOS Screen Capture` item in the `Sources` list in OBS, and choose `Transform` from the menu that pops-up.  Choose `Fit to Screen` to see if the iPad image adjusts to allow you to see the whole picture.
* Option-clicking on the bounding box lines or anchors in the OBS window allow you to adjust how OBS crops the image from the iPad.

Then I like to do a quick test recording (just a few seconds) to see how the output will appear.  By default in macOS, the output is saved in your home folder's `Movies` subfolder.