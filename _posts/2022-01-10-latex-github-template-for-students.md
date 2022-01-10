---
title:  Helping students use LaTeX for class
author: Jason
layout: post
date: 2022-01-10
tags: teaching math latex
---

I'm teaching mathematical modeling in the spring.  This is an upper-level (senior) course, and I think I'm going to take the opportunity to have students use LaTeX to typeset some of their work.

Some of my colleagues have students learn LaTeX in mid-level mathematics major courses like *Transitions to Higher Mathematics* and *Modern Algebra*, I think.  Some might even ask students in *Linear Algebra*, a course for minors, to use LaTeX.  I share this for two reasons.  First, it makes my thought of requiring my modeling students to do some LaTeX-ing seem reasonable.  Second, I want to make it clear that I *do not* make students LaTeX in any course I've taught.  LaTeX is beautiful, but I feel the pain-to-pleasure ratio for new learners is too high for me to add it to a course requirement for mid-level or lower classes.

Twitter colleaguesSteven Clontz (@StevenXClontz) and Drew Lewis (@siewlwerd) have shared how they use [Overleaf](https://www.overleaf.com) to deliver LaTeX templates to students, and I think this is something I'm going to try in my modeling class.

Drew sets up a git repository of LaTeX templates on [GitHub](https://github.com).  Then in Overleaf, they create a `Open in Overleaf` link that points to the files on GitHub.  A student clicks on the link and a copy of the templates opens for the student in Overleaf!  Easy peasy!

The syntax for such a link looks like this.  To open in Overleaf a file hosted at `http://www.example.org/file.tex` use the URL `https://www.overleaf.com/docs?snip_uri=https://www.example.org/file.tex`.

In a day or two, I'll update this post to include a concrete example using my GitHub account.  And maybe I'll include more details about how to create a repo on GitHub for the files.

It's also worth noting that is there are template LaTeX files on GitHub, students can download them directly and work on them in their LaTeX environment of choice.

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
