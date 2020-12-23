---
layout: page
title: Research - Ridges
---


This page has links to resources on relative critical sets of smooth functions.

This page is under construction

## Ridges ##

My work details the local generic properties of relative critical sets and ridge-valley-connector sets. Relative critical curves of a (smooth) function are themselves smooth, and they only rarely come to an end, but when they do, the end is stable. Relative critical curves of a function intersect at the function's critical points, and they generally intersect the function's singular points transversely (_n.b._, by singular point, we mean the curve of on which the function's Hessian vanishes).

Below are three animated gifs showing some relative critical sets of a family of functions of two variable along with the function's sigular curve. The intensity image of the functions forms the background of each image in the animation. Notice how subtle changes in the function itself (evident by subtle changes in shading) give rise to dramatic changes in the relative critical sets.

In these iamges, we use red to denote the relative critical sets defined by the zero crossing of the dot product of the function's gradient with the function's Hessians "first" eignvector (as ordered by Mathematica). Points on this curve at which the "first" eigenvalue is negative will be points of the function's one dimensional ridge set. This is why it's interesting to keep track of the functions' singular sets.

We use green to denote the other relative critical curve (the one which uses the function's "second" eigenvector), and yellow to denote the function's singular curve.

It's worth pointing out that, though these relative critical curves are smooth and well behaved in general, one parameter families of these sets (such as we are looking at through these animations) can have less pleasant properties. These three animations, in fact, are examples of three ways in which the ridge set can fail to have "nice" properties; these failures, however, are generic in one-paramter families.

| Gauss-Hessian family|
|-----|
|![](assets/images/GauHess_anim.gif)|
|The first animation is of the ridges of the family of function given by f(x,y)=y+u*x^2+y^2-2x^4-x*y^2, where the family is parameterized by -1 &lt;= u &lt;= 1.  The non-generic ridge structure can be seen at the origin when u=0.|
|-----|

| Degenerate Critical Point family|
|-----|
|![](assets/images/DegCrit_anim.gif)|
|The non-generic structure occurs at the function&#8217;s critical point and, by construction, the critical point is degenerate (i.e., the function&#8217;s Hessian vanishes there). In this case, the family of functions is given by f(x,y)=u*x+y^2+x^3+2*x*y^2 with -1&lt;=u&lt;= 1. The non-generic ridge structure occurs at the origin when u=0.|
|-----|

| Morse family|
|-----|
|![](assets/images/Morse_anim.gif)|
|This family of curves given by f(x,y)=y+u*x-1/2*x^2+1/2*y^2-x^2*y, displays a most dramatic change in struture when u=0. I&#8217;ve let u run from -1/2 to 1/2 in increments of 1/8, and i&#8217;ve also slipped in u=+/-0.03125,and +/-0.015625 so we can see the detailed structure changes near the origin, near u=0.Nnotice that the vertical red line disapplear in the u=0 frame. This appears to be an artifact of the computation.|
|-----|


