---
title: Calculating CW frequencies from Audio
author: Jason
layout: post
date: 2024-07-6
tags: code, python, signal  processing, data
---

The other day an amateur radio guy, @MW1CFN@mastodon.radio, poster to Mastodon a question.

> Anybody know of a straightforward way to analyse the sound recordings from SAQ transmissions and plot how the frequency varies over time?

I asked a clarifying question of two, and her write this:

> What I want to do is plot (as a graph, rather than a waterfall per se) the single carrier frequency (around 700Hz audio) against time, thus revealing how the carrier drifted - remarkably little, given the electro-mechanical feedback system feathering a 1.25t disc of metal spinning at 2115rpm!

I invited him to send the the audio recordin so I could chew on the problem a little bit.  I felt that audio recordings of CW are simple, and I know a little about analog signal analysis from my bat monitoring days with Anabat units and Zero Crossing Analysis.  He posted the recording to soundcloud ([here](https://soundcloud.com/user-722868764/cut-sdruno-20240630-082507-17200hz?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing&si=d243499349824625871adbbd43988b6e)) and I grabbed it using Audio Hijak and Fission.

It was then off to the races.

I pulled together the below python script which kicks out a visualization that doesn't look half back, merely 25% bad.  Here's the frequency-time plot I was able to create.

![image](assets/Figure1-final.png)

It looks like there's some spurrious (?) doubling or halving happening in the code.   But I'll leave that for smarter people to track down.

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 06 11:08am

@author: Jason Miller (KM6PSZ)
"""

# basic idea from https://www.kaggle.com/code/vishnurapps/dummies-guide-to-audio-analysis

import librosa
import matplotlib.pyplot as plt
import warnings

import numpy as np

warnings.filterwarnings('ignore')

# load audio file as data set
# NOTE:  loads file as a time series

# here
# y is the frequency value
# sr is the sampling rate from which we can inferr the sample times

yd, sr = librosa.load("recording.mp3")

# timestep
deltat=1/sr

#number of samples in the audio file
L=len(yd)

# array of sampling times
time = [ deltat*i for i in range( L )]
# array of sampling times for the zero crossing vector
time2=[time[i] for i in range (L-1)]

# grab a portion of the audio file for analysis (to keep the size managable as I
# work to pull together some code)
#
# Here we take the portion of data starting from the 20,000 index and going to the 20400 index.
time1=np.split(time, [20000,20400],axis=0)
yd1=np.split(yd, [20000,20400],axis=0)
# Here we determine which of the entries are zero crossings
logicyd=librosa.zero_crossings(yd)
logicyd1=np.split(logicyd, [20000,20400],axis=0)
# here we get the indices of the zero-crossings
zeros=np.nonzero(logicyd)

times=[time[i] for i in zeros[0]]
dtimes=2*np.diff(times)
yds=[yd[i] for i in zeros[0]]
yds=[yds[i] for i in range(len(yds)-1)]

freq=[1/dtimes[i] for i in range( len(dtimes) )]
#freqdata=librosa.util.stack([time2, freq1], axis=-1)

print(freq)

# 
# # visualize the data - note that all the values are binary (either 0 or 1)
# print(logicyd1)
# 
# # what follow is from
# # https://librosa.org/doc/latest/generated/librosa.zero_crossings.html#librosa.zero_crossings
# 
# # here is the time-amplitude data
# data=librosa.util.stack([time1, yd1], axis=-1)
# # here are the times of the zero crossings
# time2=time1[zeros1]
# # here are the time-amplitude pairs at the zero crossings
# yd2 = data[zeros1]
# # because time for one oscillation is twice the time between two zero crossings
# # the frequency is the inverse of this
# deltazc=2*diff(time2)
# freq1=[1/deltazc[i] for i in range( len(deltazc) )]
# freqdata=librosa.util.stack([time2, freq1], axis=-1)
# 
# 

plt.figure(figsize=(20, 4))
plt.plot(freq)
plt.grid()
plt.title('frequencies')
plt.xlabel('time')
plt.ylabel('text')
plt.show()
```


<!--
SYNTAX FOR IMAGES
* use services to create JPG and to create thumbnail that is 720px wide

[![ALT-TEXT](/assets/images/filename-thumbnail.jpg)](/assets/images/filename.jpg)
-->

<!--
SYNTAX FOR VIDEO
* convert MOV to mp4 using VLC

<video width="480" height="320" controls="controls">
  <source src="/assets/media/filename.m4v" type="video/mp4">
</video>
-->
