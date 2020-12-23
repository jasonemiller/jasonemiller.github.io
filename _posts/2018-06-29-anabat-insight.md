---
title:  Trouble with Anabat Insight
author: miller
date: 2018-06-29
categories: bats
---

I'm experiencing some 'bad behavior' from Analook Insight, a program I'm using to clean call files recorded with an Anabat Swift.

My goal is to remove extraneous data from a call file. Here's a call with extraneous (low frequency) noise.

![Original call file](/assets/images/Screenshot-2018-06-29-12.59.49-1024x519.png)


Read about my troubles after the jump. <!---more--->

I can select some noise for deletion.

![Noise that I want to delete](/assets/images/Screenshot-2018-06-29-13.00.03-1024x511.png)

And I can delete it using a contextual menu that appears when I right-click on the screen and select 'Hide ZC Dots'.

![Deleted noise](/assets/images/Screenshot-2018-06-29-13.00.13-1024x564.png)

When I make this selection, the dots I want to delete disappear.  Then I tell Insight that I want to save the file. This dialog box appears and I choose 'Save As' and name the file. (Or I can choose an existing file, the end result is the same.)

![Save the cleaned call file](/assets/images/Screenshot-2018-06-29-13.00.25.png)


When I save the file, Insight redraws the call file, and noise reappears.

![Noise reappears](/assets/images/Screenshot-2018-06-29-13.00.39.png)

This suggests to me that the file I save (for teaching and analysis in the future) is not the 'cleaned' file I had been working to create but a file with some noise.

Am I doing something wrong? I've tried with with Auto ZC on and with it off. Same results.