---
title: How To Fit An Ellipse to Data
author: Jason
layout: post
date: 2024-11-05
use_math: true
tags: mathematics
---

Last month, Karen Kikuchi, a mathematics teacher at Rancho Campana High School in Camarillo, CA, reached out to the Mathematics Department at CI to ask if there were a mathematician who could advise a group of students on a mathematics problem they were wrestling with.  The students were working on submitting an entry to [NASA's App Development Challenge](https://nam10.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.nasa.gov%2Flearning-resources%2Fapp-development-challenge%2Fabout-nasa-app-development-challenge-adc%2F&data=05%7C02%7Cjason.miller%40csuci.edu%7C46461cf286f74c89323508dcf3a65672%7Ce30f5bdb7f18435b84369d84aa7b96dd%7C1%7C0%7C638653142967418118%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=pVZ0n4RxcrdRaPYMP7BoGCyXVLN7vic954Z0ZS%2BrHDs%3D&reserved=0).

Here's the problem statement as she shared it with me.

<quote>
  We know that given two points with attached velocity vectors iin space, the smooth curve that connects the two will be an arc of an ellipse.  The question is, what is the equation of this ellipse?  (Note:  there are infinitely many such ellipses, we desire the ellipse with the lowest ecentricity/)
</quote>

I responded that I'd be willing to help.  I like space curves!  And I'm on sabbatical, so I can do Good Deeds like this.

Ms. Kikuchi also referenced [a post](https://math.stackexchange.com/questions/109890/how-to-find-an-ellipse-given-2-passing-points-and-the-tangents-at-them/109927#109927) in Math StackExchange that answers the question, but the students were having trouble understanding the answer.  She also shared a [Desmos rendering](https://www.desmos.com/3d/win32s4luf) of the data they are working with.

Reviewing the problem and the links confused me; I didn't see the obvious question between what they were asking and the NASA challenge.  So I did my best, starting with translating the StackExchange post into a narrative that I thought the students (who had completed an AP Calculus BC course) could understand.  I also built a couple Desmos models to demonstrate the utility of the mathematics from a coding perspective.

This posting memorializes this work.


## The Problem Statement

First, it's worth making the problem statement more precise.  Given two points and a line through each point, find the equation of an ellipse passing through the points with the lines tangent at those points.  There will be an infinite number of such ellipses, so we are interested in finding the ellipse with minimal eccentricity.

## Describing the Ellipses

Let $P_1$ and $P_2$ be points in $\mathbb{R}^2$ and let $\ell_i$ be a line through $P_i$.  We are interested in finding the equation of the ellipses that pass through these points and have the $\ell_i$ as tangent line at $P_i$.  There are infinitely many such ellipses, so we will conclude with an observation on finding that ellipse with least eccentricity.

There are two cases to consider:  first, the case where the $\ell_i$ intersect and, second, the case that the $\ell_i$ are parallel.  We will consider the former.

Denote the point of intersection of the $\ell_i$ as $O$.  Without loss of generality, we can assume $O$ sits at the origin.  Define vectors $\vec{p}_i=\overrightarrow{OP_i}$, the vector from the origin to the point $P_i$.  Since the $\ell_i$ are not parallel lines, the vectors $\vec{p}_i$ are linearly independent, so they form a basis for the plane.  This means each point $\vec{x}$ in the plane has a coordinate representation with respect to $\{\vec{p}_1,\vec{p}_2\}$, written $\vec{x}=[u,v]^T$ meaning $u$ and $v$ are real numbers such that $\vec{x}=u\vec{p}_1+v\vec{p}_2$.

In this coordinate system, our ellipses have the form

$$
 (u-1)^2+(v-1)^2+2 \alpha u v  = 1.
$$

Here $\alpha$ is a real number with $\|\alpha\|<1$.  You can see a model of such a family of ellipses rendered in Desmos [here](https://www.desmos.com/3d/9rnkptnxx0).  (Ignore the 'center' for now.  Where it comes from will become clear, below.)

Next, we locate the center of the ellipse.  Let $\vec{q}_1$ and $\vec{q}_2$ be the basis dual to our basis $\{\vec{p}_1,\vec{p}_2\}$ for the plane.  This means that 

$$
\vec{p}_i \cdot \vec{q}_j = \delta_{ij} = 
  \begin{cases} 
      0 & \, \mbox{if } i \neq j \\
      1 & \, \mbox{if } i=j. 
   \end{cases}
$$

Consequently, if $\vec{x}=u\vec{p}_1+v\vec{p}_2$, then 

$$
u=\vec{x} \cdot \vec{q}_1 \mbox{ and } v=\vec{x} \cdot \vec{q}_2.
$$

Later, when we want to translate our general equation into our original coordinate system (the one that describes $P_1$, $P_2$, $\ell_1$, and $\ell_2$) we're going to need to know what $\vec{q}_1$ and $\vec{q}_2$ are.  Here's how we do it.  First, make the matrix $P$ that has $\vec{p}_i$ as its $i$th column vector:

$$
P=\begin{bmatrix}
a_1 & a_2 \\ b_1 & b_2
\end{bmatrix}.
$$

The matrix inverse $P^{-1}$ is the matrix that has the property that $PP^{-1}=I$, the identity matrix.  Since $P$ is a $2 \times 2$ matrix, the formal for $P^{-1}$ is straightforward:

$$
P^{-1}=\frac{1}{D}\begin{bmatrix}
b_2 & -a_2 \\ -b_1 & a_1
\end{bmatrix}.
$$

where $D=a_1 b_2 - a_2 b_1$.  The definition of matrix multipication tell us that the dual basis vectors are the row vectors of $P^{-1}$.  That is

$$
\begin{align*}
\vec{q}_1  & = 
\begin{bmatrix}
\frac{b_2}{D} \\ \frac{-a_2}{D} 
\end{bmatrix}\\
& = 
\frac{1}{D} \begin{bmatrix}
b_2 \\ -a_2 
\end{bmatrix}
\end{align*}
$$

and

$$
\begin{align*}
\vec{q}_2  & = 
\begin{bmatrix}
-\frac{b_1}{D} \\ \frac{-a_1}{D} 
\end{bmatrix}\\
& = 
\frac{1}{D} \begin{bmatrix}
-b_1 \\ a_1 
\end{bmatrix}.
\end{align*}
$$

This gives us the formulas

$$
\begin{align*}
u & = \vec{q}_1 \cdot \vec{x} \\
& = \frac{1}{D}[b_2, -a_2] \cdot [x,y] \\
& = \frac{1}{D}(xb_2-ya_2)
\end{align*}
$$

$$
\begin{align*}
v & = \vec{q}_2 \cdot \vec{x} \\
& = \frac{1}{D}[-b_1, a_1] \cdot [x,y] \\
& = \frac{1}{D}(-xb_1+ya_1)
\end{align*}.
$$

We will return to this shortly.  First, we use the dual basis to find the center of one of our ellipses.

Using the fact that $u=\vec{p}_1 \cdot \vec{q}_1$ and $v=\vec{p}_2 \cdot \vec{q}_2$ we can rewrite the expression for our ellipses as follows. 

$$
(\vec{x} \cdot \vec{q}_1-1)^2+(\vec{x} \cdot \vec{q}_2)^2 + 2 \alpha (\vec{x} \cdot \vec{q}_1)(\vec{x} \cdot \vec{1}_1) =1.
$$

Before we express this in $xy$-coordinates, we want to use this expression to find the center of such an ellipse.  It is known that the ellipse's center is the critical point of the expression on the left-hand side (LHS) of the above.  The gradient of the LHS is

$$
\vec{q}_1 (\vec{x} \cdot \vec{q}_1+\alpha \vec{x} \cdot \vec{q}_2-1)+\vec{q}_2 (\vec{x} \cdot \vec{q}_2+\alpha \vec{x} \cdot \vec{q}_1-1).
$$

Since $\{\vec{q}_1,\vec{q}_2\}$ form a basis, they are linearly independent.  Therefore the above expression vanishes if and only if

$$
\vec{x} \cdot \vec{q}_i+\alpha \vec{x} \cdot \vec{q}_j-1=0
$$

for $i\neq j$.  Notice that $\vec{x} \cdot \vec{q}_1=\vec{x} \cdot \vec{q}_2 =\frac{1}{1+\alpha}$ solves both equations.  This means the critical point of the ellipse equation is 

$$
\begin{align*} \vec{x} & = \frac{1}{1+\alpha} \vec{p}_1 + \frac{1}{1+\alpha} \vec{p}_2 \\
& = [\frac{1}{1+\alpha},\frac{1}{1+\alpha}]
\end{align*}
$$

where the latter is the expression of the former in $uv$-coordinates.  This gives is the center of the ellipse described by our first equation, above.  (And this explains that addition in the Desmos notebook shared above.)

Now we have an expression for our candidate ellipses and their centers in $uv$-coordinates!

## Theory to Implementation

Let's pause for a moment and review what we've been doing.  We were given data (two point, two lines) in $xy$-coordinates and asked to find the family of ellipses that pass through those points with those tangencies.  We did that by changing to a new $uv$-coordinate system.  To implement that solution, we need to change **back** to our original $xy$-coordinate system.  Here's now we do that.

In a new $uv$-coordinate system, our ellipses have the form 

$$
 (u-1)^2+(v-1)^2+2 \alpha u v =1
$$

Using a dual basis, we determined $u=\vec{x}\cdot \vec{q}_1=\frac{1}{D}(xb_2-ya_2)$ and $v=\vec{x}\cdot \vec{q}_2=\frac{1}{D}(-xb_1+ya_1)$.  These expressions are in terms of $x$ and $y$, which is **almost** our original coordinate system. But remember that we assumed that the intersection of lines $\ell_1$ and $\ell_2$ to be the origin.  This assumption is valid when we're doing an analysis of the system, but as we try to implement what we've learned, we need respect the coordinates of that intersection point as it is given to us.  Let's call our very original coorinate system the $\tilde{x}$ and $\tilde{y}$ coordinate system, and let's suppose $O$ is at $(a_0,b_0)$.

To get from this original coordinate system to the $xy$-coordinate system we used in the analysis, we need to translate $O$ to the origin (in $xy$-space).  We do this by writing $x=\tilde{x}-a_0$ and $y=\tilde{y}-b_0$, and now we can unpack our formulas.  We started with 

$$
 (u-1)^2+(v-1)^2+2 \alpha u v =1
$$

which becomes

$$
 (\frac{1}{D}(xb_2-ya_2)-1)^2+(\frac{1}{D}(-xb_1+ya_1)-1)^2+2 \alpha \frac{1}{D}(xb_2-ya_2) \frac{1}{D}(-xb_1+ya_1) =1
$$

in $xy$-coordinates and

$$
\begin{multline}
 (\frac{1}{D}((\tilde{x}-a_0)b_2-(\tilde{y}-b_0))a_2)-1)^2+(\frac{1}{D}(-(\tilde{x}-a_0)b_1+(\tilde{y}-b_0)a_1)-1)^2+ \\
 2 \alpha \frac{1}{D}((\tilde{x}-a_0)b_2-(\tilde{y}-b_0)a_2) \frac{1}{D}(-(\tilde{x}-a_0)b_1+(\tilde{y}-b_0)a_1)=1.
\end{multline}
$$

in our very original coordinates.  Note that these ellispes have a center at

$$
\begin{align*}
\vec{x} & =\frac{1}{1+\alpha}\vec{p}_1+\frac{1}{1+\alpha}\vec{p}_2 \\
& = \frac{1}{1+\alpha}[a_1,b_1]+\frac{1}{1+\alpha}[a_2,b_2]\\
& = [\frac{a_1+a_2}{1+\alpha},\frac{b_1+b_2}{1+\alpha}]
\end{align*}
$$

## Eccentricity

The last bit of business is finding the ellipse that has minimal eccentricity.  I'm not going to review what eccentricity is because there are ample references for that.  (See [here](*https://en.wikipedia.org/wiki/Eccentricity_(mathematics)) or [here](https://www.mathopenref.com/ellipseeccentricity.html), for example.)  I'm not even going to derive the $\alpha$-value that gives the ellipse with the least eccentricity.  [This Math Stack Exchange article](https://math.stackexchange.com/questions/109890/how-to-find-an-ellipse-given-2-passing-points-and-the-tangents-at-them/109927#109927) does that.  It's author says that the $\alpha$-valye that minimizes the ellipse is

$$
\begin{align*}
\alpha_{min} & = \frac{2 \vec{p}_1 \cdot \vec{p}_2}{|\vec{p}_1|^2+|\vec{p}_2|^2} \\
 & = \frac{2 a_1 a_2 + b_1 b_2}{a_1^2+a_2^2+b_1^2+b_2^2}.
\end{align*}
$$

This value is expressed entirely in terms of data given at the start of the problem.  [Here is a Desmos workbook](https://www.desmos.com/3d/iucgp05yzo) that shows the implementation of the above math.

## Conclusion

The astute reader will notice that I have not written up what we do in the event that $\ell_1$ and $\ell_2$ are parallel.  You can do this yourself, using the narrative in the [Math Stack Exchange article as a guide](https://math.stackexchange.com/questions/109890/how-to-find-an-ellipse-given-2-passing-points-and-the-tangents-at-them/109927#109927).

Happy computing!


## Coda

The above wasn't helpful to the students.  As it turns out, they were given points in 3-space that lie on the path of a moon orbiter, and they wanted to fit a differentiable curve to those points.    That's a very different problem.  They ended up using cubic splines to get a differentiable path.


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