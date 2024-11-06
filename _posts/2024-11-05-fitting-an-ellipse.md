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

Let $P_1$ and $P_2$ be points in $\mathbb{R}^2$ and let $\ell_i$ be a line through $\P_i$.  We are interested in finding the equation of the ellipses that pass through these points and have the $\ell_i$ as tangent line at $P_i$.  There are infinitely many such ellipses, so we will conclude with an observation on finding that ellipse with least eccentricity.

There are two cases to consider:  first, the case where the $\ell_i$ intersect and, second, the case that the $\ell_i$ are parallel.  We will consider the former.

Denote the point of intersection of the $\ell_i$ as $O$.  Without loss of generality, we can assume $O$ sits at the origin.  Define vectors $\vec{p}_i=\overrightarrow{OP_i}$, the vector from the origin to the point $\P_i$.  Since the $\ell_i$ are not parallel lines, the cevtors $\vec{p}_i$ are linearly independent, so they form a basis for the plane.  This means each point $\vec{x}$ in the plane has a coordinate representation with respect to $\{\vec{p}_1,\vec{p}_2\}$, written $\vec{x}=[u,v]^T$ meaning $u$ and $v$ are real numbers such that $\vec{x}=u\vec{p}_1+v\vec{p}_2$.

In this coordinate system, our ellipses have the form
\[ (u-1)^2+(v-1)^2+2 \alpha u v =1 \]
where $\alpha$ is a real number with $|\alpha|<1$.  You can see a model of such a family of ellipses rendered in Desmos [here](https://www.desmos.com/3d/9rnkptnxx0).  (Ignore the 'center' for now.  Where it comes from will become clear.)

Next, we locate the center of the ellipse.  Let $\vec{q}_1$ and $\vec{q}_2$ be the basis dual to our basis $\{\vec{p}_1,\vec{p}_2\}$ for the plane.  This means that 
\[
\vec{p}_i \cdot \vec{q}_j = \delta_{ij} = \left\{
  \begin{align*}
  0 & \, \mbox{if } i \neq j \\
  1 & \, \mbox{if } i=j
  \end{align*}
\]

\[ \begin{cases} 
      0 & \, \mbox{if } i \neq j \\
      1 & \, \mbox{if } i=j 
   \end{cases}
\]



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