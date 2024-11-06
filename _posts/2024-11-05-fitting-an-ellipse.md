---
title: How To Fit An Ellipse to Data
author: Jason
layout: post
date: 2024-11-05
use_math: true
tags: mathematics
---

Last month, Karen Kikuchi, a matheamtics teacher at Rancho Campana High School in Camarillo, CA, reached out to the Mathematics Department at CI to ask if there were a mathematician who could advise a group of students on a mathematics problem they were wrestling with.  The students were working on submitting an entry to [NASA's App Development Challenge](https://nam10.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.nasa.gov%2Flearning-resources%2Fapp-development-challenge%2Fabout-nasa-app-development-challenge-adc%2F&data=05%7C02%7Cjason.miller%40csuci.edu%7C46461cf286f74c89323508dcf3a65672%7Ce30f5bdb7f18435b84369d84aa7b96dd%7C1%7C0%7C638653142967418118%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=pVZ0n4RxcrdRaPYMP7BoGCyXVLN7vic954Z0ZS%2BrHDs%3D&reserved=0).

Here's the problem statement as she shared it with me.

<quote>
  We know that given two points with attached velocity vectors iin space, the smooth curve that connects the two will be an arc of an ellipse.  The question is, what is the equation of this ellipse?  (Note:  there are infinitely many such ellipses, we desire the ellipse with the lowest ecentricity/)
</quote>

She also referenced [a post](https://math.stackexchange.com/questions/109890/how-to-find-an-ellipse-given-2-passing-points-and-the-tangents-at-them/109927#109927) in Math StackExchange that answers the question, but the students were having trouble understanding the answer.  She also shared a [Desmos rendering](https://www.desmos.com/3d/win32s4luf) of the data they are working with.

Reviewing the problem and the links confused me; I didn't see the obvious question between what they were asking and the NASA challenge.  So I did my best, starting with translating the StackExchange post into a narrative that I thought the students (who had completed an AP Calculus BC course) could understand.  I also built a couple Desmos models to demonstrate the utility of the mathematics from a coding perspective.

This posting memorializes this work.

First, it's worth making the problem statement more precise.  Given two points and a line through each point, find the equation of an ellipse passing through the points with the lines tangent at those points.  There will be an infinite number of such ellipses, so we are interested in finding the ellipse with minimal eccentricity.

Let <span>$P_1$</span> and $P_2$ be points in <span>$\mathbb{R}^2$</span>.



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

<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>