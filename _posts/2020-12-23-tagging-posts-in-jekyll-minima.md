---
title: Adding post tagging to jekyll's Minima theme
author: miller
date:  2020-12-23
tags: jekyll coding
render_with_liquid: false
---

It's almost Christmas Eve and I'm fiddling with a web page.  I moved my content from a Wordpress site to a jekyll installation that can be hosted freely by GitHub.  The 'minima' theme seems to scratch most of my itches, but there are a couple I want to address in the next couple days.  Today's is tagging.

I'd like to have a set of tags for posts that show visitors which posts are related to one another.  Maybe later I can find a way to display posts by tag, to counts by tag, etc.  Ruby's Liquid language has to make that easy, right?

For now, I'll just be happy with tags on each post.  I found a [post]() by [Long Qian]() that looks promising, so I'm going to take notes here on the steps I take to get tags working on my site.  Fingers crossed.

#### Front Matter ####

First, each tagged post needs a 'tags' line in its front matter.  Tags are signle words separated by a single space.  This is how I tagged this page:

```
---
title: Adding post tagging to jekyll's Minima theme
author: miller
date:  2020-12-23
tags: jekyll coding
---
```

#### Collecting Tags ####

Next, I made a file called `collecttags.html` and saved it in my `_includes` directory.  The contents of this file (liquid commands) are shared below.

{% raw %}

    {% assign rawtags = "" %}
    {% for post in site.posts %}
      {% assign ttags = post.tags | join:'|' | append:'|' %}
      {% assign rawtags = rawtags | append:ttags %}
    {% endfor %}
    {% assign rawtags = rawtags | split:'|' | sort %}
    
    {% assign site.tags = "" %}
    {% for tag in rawtags %}
      {% if tag != "" %}
        {% if tags == "" %}
          {% assign tags = tag | split:'|' %}
        {% endif %}
        {% unless tags contains tag %}
          {% assign tags = tags | join:'|' | append:'|' | append:tag | split:'|' %}
        {% endunless %}
      {% endif %}
    {% endfor %}

{% endraw %}


This makes a list `site.tags`.

I then added

{% raw %}

    {% if site.tags != "" %}
        {% include collecttags.html %}
      {% endif %}

{% endraw %}

to `_include/head.html` below the line that reads `{%- include custom-head.html -%}`.  Qian writes that this allows jekyll to load the new HTML file (that creates the `site.tags` list) before the `site.tags` list needs to be used.

The have the tags of a post displayed on the post, you need to modify the post layout.  I insterted

{% raw %}

    <span>[
      {% for tag in page.tags %}
        {% capture tag_name %}{{ tag }}{% endcapture %}
        <a href="/tag/{{ tag_name }}"><code class="highligher-rouge"><nobr>{{     tag_name }}</nobr></code>&nbsp;</a>
      {% endfor %}
    ]</span>

{% endraw %}

in `_layouts/post.html` starting at line 6.  This seemed like what Qian did for his site.  I'll probably mess with some of the styling later (e.g., bacground color).

At this point in his instructions, Qian says

> Note that a link is inserted to each of the tags of the post, at /tag/tag_name. We will come to that in the next step.

I don't know what that means, yet.

Next, we make a layout for a new kind of page that will display for each tag all the posts for that tag.  Here's the text for a `_layouts/tagpage.html` file:

{% raw %}

    ---
    layout: default
    ---
    <div class="post">
    <h1>Tag: {{ page.tag }}</h1>
    <ul>
    {% for post in site.tags[page.tag] %}
      <li><a href="{{ post.url }}">{{ post.title }}</a> ({{ post.date |     date_to_string }})<br>
        {{ post.description }}
      </li>
    {% endfor %}
    </ul>
    </div>
    <hr>

{% endraw %}

I'll probably want to go play with that some, too.

At this point, Qian says that you either need to create a file for each tag, into which jekyll will render you list of posts with that tag, or you can run a python script [he provides](https://github.com/qian256/qian256.github.io/blob/master/tag_generator.py) to do it each time you prepare to push your site to its production server.

A markdown template file for the tag `uffda` would look like this:

```m
---
layout: tagpage
title: "Tag: uffda"
tag: uffda
---
```

and it would be saved in a folder `tag` in the root folder of your working directory.

For posterity, I'm copying Qian's python file at the bottom of this page, too.  Please respect his ownership of the work.

After setting the execute bit on the python script, I ran it at the command link and received this error:

```zsh
 ~/path/ [main] ./tag-generator.py
Traceback (most recent call last):
  File "./tag-generator.py", line 23, in <module>
    f = open(filename, 'r', encoding='utf8')
TypeError: 'encoding' is an invalid keyword argument for this function
```

A quick Google search told me that my default install of python is probably version 2, and that I should try running python3.  That worked, and I've changed the python code below.

After a successful run of the script, I received the following terminal message

```zsh
Tags generated, count 5
```

Qian ends his great write-up with code that will create a clickable 'cloud' of tags on ths site.  He creates a file `archives.html` in the `_includes` folder of the site that has the following content:

{% raw %}

    <h2>Archive</h2>
    {% capture temptags %}
      {% for tag in site.tags %}
        {{ tag[1].size | plus: 1000 }}#{{ tag[0] }}#{{ tag[1].size }}
      {% endfor %}
    {% endcapture %}
    {% assign sortedtemptags = temptags | split:' ' | sort | reverse %}
    {% for temptag in sortedtemptags %}
      {% assign tagitems = temptag | split: '#' %}
      {% capture tagname %}{{ tagitems[1] }}{% endcapture %}
      <a href="/tag/{{ tagname }}"><code class="highligher-rouge"><nobr>{{ tagname    }}</nobr></code></a>
    {% endfor %}

{% endraw %}



Qian writes the following about this chunk of liquid code:

>This script fetches `site.tags` and sort them by the size of its referenced posts. The sorted list is in `sortedtemptags`. And it is iterated to be visualized. I am inspired by this [stackoverflow answer](http://stackoverflow.com/questions/13025281/how-to-get-a-sorted-tags-list-in-jekyll).

The following line should display the 'cloud' of tags:

{% raw %}

    {% include archive.html %}

{% endraw %}

I added this to the end of the `tagpage.html` file I created, above, according to Qian's directions.

And I gotta tell you.  This just works.  And it looks great.  Thanks [Long Qian](http://longqian.me)!

## Python Script

```python
#!/usr/bin/env python3

'''
tag_generator.py

Copyright 2017 Long Qian
Contact: lqian8@jhu.edu

This script creates tags for your Jekyll blog hosted by Github page.
No plugins required.
'''

import glob
import os

post_dir = '_posts/'
tag_dir = 'tag/'

filenames = glob.glob(post_dir + '*md')

total_tags = []
for filename in filenames:
    f = open(filename, 'r', encoding='utf8')
    crawl = False
    for line in f:
        if crawl:
            current_tags = line.strip().split()
            if current_tags[0] == 'tags:':
                total_tags.extend(current_tags[1:])
                crawl = False
                break
        if line.strip() == '---':
            if not crawl:
                crawl = True
            else:
                crawl = False
                break
    f.close()
total_tags = set(total_tags)

old_tags = glob.glob(tag_dir + '*.md')
for tag in old_tags:
    os.remove(tag)
    
if not os.path.exists(tag_dir):
    os.makedirs(tag_dir)

for tag in total_tags:
    tag_filename = tag_dir + tag + '.md'
    f = open(tag_filename, 'a')
    write_str = '---\nlayout: tagpage\ntitle: \"Tag: ' + tag + '\"\ntag: ' + tag + '\nrobots: noindex\n---\n'
    f.write(write_str)
    f.close()
print("Tags generated, count", total_tags.__len__())
```