---
title:  Regular Expressions and Preparing for the General Class Amateur Radio License Exam
author: Jason
layout: post
date: 2021-07-25
tags: amateur-radio script maker coding python regex markdown ham 
---

Last week I decided to study for and take the FCC Amateur Radio License exam for a General class license.  I earned the Technician class license a couple years ago, and I've been spending some time this summer learning more about my radios.  I learned that my fiddling with antennas and things has significant overlap with topics on the General exam.  So I shrugged and decided to prepare for it.

A trick I learned while preparing for the Technician's exam makes the idea of taking another exam less daunting.  I [took a class](https://www.qualitymatrix.com/hamclass/) where the instructors, Norm and Nancy Goodkin, gave us a handout that consisted of the exam's question pool.  Each question appeared with the multiple choice answer options, and the correct option was printed in bold.

"Only memorize the correct answer,"  the Goodkins told the class.  "The others are just **distractors**.  Spending any time on the incorrect answers will confuse you."

Their test-taking strategy was to condition yourself on the questions and their correct answers so that when you see them in the exam environment, the correct answer will be likely to jump out at you.  (Or your gut will direct you to "guess" the correct one.)

If they had made a study guide for the General class exam, this is how one of the questions and answers might have looked.

<p style=”color:blue”>
G1C15 (D) \[97.313\] <br>
What measurement is specified by FCC rules that regulate maximum power output?<br>
A. RMS
B. Average
C. Forward
<b>D. PEP<br>
</b>~~
</p>

Even though that strategy worked for me, as a teacher, it goes against my learning and teaching philosophy.  But for a license, my philosophy is to get the license first without dishonest work and then learn more deeply later, through practice.  And because the FCC makes the question pool available to the public, I decided to take the same approach for the General exam.

A quick Google search pointed to the official question and answer pool for the 2019-2023 exams here: [Public Domain Release 2019-2023 General Class Pool](http://www.ncvec.org/page.php?id=364).  I downloaded the document as a text file.

It took me a while to notice that the answer key is embedded in the pool document itself.  Once I noticed that, I knew it would be easy (in theory) to use regular expressions to reformat the multiple choice questions in the same way the Goodkins did.

As anyone who exists on the periphery of computer programming knows, it can take a long time to come up with a simple script.  This endeavor into reformatting was no different for me.  First, I figured how to do it in the BBEdit text editor (which has some nice tools for testing and deploying regular expressions).  Then, after recognizing a multi-step reformatting process would benefit from being scripted, I reproduced my BBEdit work in python.  This may have taken longer than just a line-by-line edit of the questions and answers, but if I do this again (in 2023) or if someone else uses this work to help them, it will be worth it.

## Reformatting in BBEdit

It took me some trial and error, aided by BBEdit's "Pattern Playground", to come up with  a regular expressions that would do what I wanted.  (This worked for all but the very last question.  I don't know why it failed on that one.)

```
(^G[0-9]\D\d\d\s*\()(?P<answer>[A-D])\)(\s.*\n|\s*\n*)(.*\?.*\n)((.*\s*){0,3})(((?P=answer)\.\s)(.*\s*))((.*\s*){0,3})(\~\~)\n
```
The "replace" expression I used was

```
\1\2)\3\4\5\6**\7**\10 \n
```

Here, I would have liked to have the opening and closing "**" commands on the same line, but I couldn't figure out how to do that.  So I rested on the knowledge that Markdown doesn't care, and I ran with it.

I also added section and subsection formatting with the following search and replace strings.

For sections, I searched with

```
(^S.*)
```

and replaced with

```
## \1
```

For subsections, I searched with

```
^G[0-9]\D\s-.*
```

and I replaced with

```
### \0
```

I could have dealt with the title by hand, but I used this for the search

```
2019-2023 General Class.*
```

```
# \0
```

With that reformatting done, I did a University search and replace to add a slash in front of every `[` because markdown reserves those for hyperlinks.  Then I added a note to the start of the document and violá!  I had a Goodkin-ized study document.  (I will link it to the end of this posting.)

Then I went down a sort of rabbit hole.

## Reformatting with Python

Because the reformatting required a series of replacement steps, I thought that it would be economical to put those in a script so they could all happen at once.  I already had the regular expressions that worked in BBEdit.  Could it be so difficult to translate that into a python script?

I had python installed, but I didn't have a good IDE.  A few minutes of [research](https://wiki.python.org/moin/IntegratedDevelopmentEnvironments) led me to [Spyder](https://www.spyder-ide.org), which I downloaded and installed.  I was attracted to it because it had a Matlab-like interface that gives me an editor along with a console of commands, a command line console, and a workspace of variables in memory.  Together, these tools would help me cobble together and troubleshoot a script.

Leaning heavily on the [Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html) at [python.org](http://www.python.org), I identified the functions I'd need and translated the regular expression syntax into python-ese.  I had to read about file handling, too.

```python=
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 08:23:00 2021

@author: Jason Miller (KM6PSZ)
"""

import re, os, sys
os.chdir('/path/to/folder/')
input = open("tmp.txt","r")
output = open("tmp.md", "w")
input_str=input.read()

# -----------------------------------
# Reformat title lines
in_title=re.compile('(\s*)(2019-2023 General Class.*)')
new_title = in_title.sub(r"\n\n# \2",input_str)
# -----------------------------------
# Reformat section lines
in_section=re.compile('^(SUBELEMENT\sG\d)',re.MULTILINE|re.DOTALL)
new_section = in_section.sub(r"## \1",new_title)
# -----------------------------------
# Reformat subsection lines
in_subsection=re.compile('^(G[0-9]\D\s-)',re.MULTILINE|re.DOTALL)
new_subsection = in_subsection.sub(r"### \1",new_section)
# -----------------------------------
# Reformat question and answer lines
in_question=re.compile('(^G[0-9]\D\d\d\s*\()(?P<answer>[A-D])\)(\s.*\n|\s*\n*)(.*\?.*\n)((.*\s*){0,3})(((?P=answer)\.\s)(.*\s*))((.*\s*){0,3})(\~\~)\n', re.MULTILINE)
new_questions = in_question.sub(r"\1\2)\3\4\5**\7**\10\12\n",new_subsection)
# -----------------------------------
# Add backslash in from of brackets
openbrackets=re.compile('(\[)', re.MULTILINE)
new_fwdbrackets = openbrackets.sub(r"\\[",new_questions)
closebrackets=re.compile('(\])', re.MULTILINE)
new_closebrackets = closebrackets.sub(r"\\]",new_fwdbrackets)

# ----------- reformatting done --------------

output.write(new_closebrackets)
input.close()
output.close()



## for troubleshooting
#found=in_question.findall(new_subsection)
#in_section.findall(input_str)
#print(found)
```

This script does *almost* all the reformatting that needs to happen.  There's a question or two that gets missed and a subsection heading or two, as well.  (These errors are likely due to inconsistencies in the original document.)

The script and the output are linked here:

* [python script](/assets/data/fcc-General-reformatting-regex.py)
* [markdown-ified output](/assets/data/fcc-General-reformatted.md)
* [edited markdown output]((/assets/data/fcc-General-reformatted-edited.pdf))
* [edited markdown output (PDF format)](/assets/data/fcc-General-reformatted-edited.pdf)

Even with the script, there are a couple other things that need to be done by hand, anyway:

* a global search and replace for a quotation character that my text editor didn't like (YMMV)
* adding the missing grahic for the questions in section G7-1
* adding a colophon (at the end) that explains what I did to reformat the question pool

A couple things I would like to add to the script include

* some formatting that will make the questions easier to read (*e.g.*, italicizing the distractors and the heading to the question)
* figuring out how to edit the content of a capturing group to add formatting (add bold face to the answer line, italicize the lead-in information for each question, *etc.*)

If I make these changes to my script, I'll append an update to this post.

