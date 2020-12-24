---
title: Liquid Template Language in Markdown on Jekyll
author: miller
date:  2020-12-23
tags: jekyll coding
render_with_liquid: false
---

As I'm trying to document my experience customizing my jekyll install to allow posts to have tags, I realize that the blocks of Liquid template langauge don't render in my `syntax` blocks.

My python and html and plain text render fine, but all the Liquid code doesn't appear.  This post is how I fixed that.

It looks like the standard way of doing syntax highlighting in markdown doesn't work for Liquid.  Instead, you must sandwhich your code between `raw` and `endraw` liquid template commands and indent (twice, maybe) the block of code you want rendered, like this [Here's where I would like to show the code, but I can't because liquid can't render literal liquid code even inside block fences.]

{% raw %}

    XXXX

{% endraw %}

I'm not going to invest much more time on this right now.

---

It would be nice to know

* how to include liquid template commands in a markdown (jekyll) page for the purpose of documentation and communication (like this)
* how to get the 'render_with_liquid: false' flag in the forward of a document to work

---

Tweet or email any answers you have, please.
