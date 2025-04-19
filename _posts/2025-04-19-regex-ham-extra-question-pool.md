---
title:  Regular Expressions and Preparing for the Amateur Extra Class Amateur Radio License Exam
author: Jason
layout: post
date: 2025-04-19
tags: amateur-radio script maker coding python regex markdown ham 
---

One of the best ways to prepare to take and pass an FCC amateur radio licensing exam is to get the question pool and familiarize yourselve with the questions and their answers, ignoring the distractifiers.  Of couse, if you want to understand the reasons why the correct answer is correct, that's a bonus.  In my experience, though, you'll learn the 'why' more effectively through operating and doing amateur radio.  It's not necessary for passing licensing exams.

To that end, I've created study guides for exam of the three exams.  Here they are:

1. [Tech Exam](../assets/techpool-modified-230303.pdf)
1. [General Exam](../assets/genpool-modified-240607.pdf)
1. [Extra Exam](assets/extrapool-formatted.pdf)

In each of these, for each question, I put the correct answer in bold face.  This allows the learner to ignore the distractifiers completely if they want to.

In the hope that the effort will pay off in time (if I create enough of these documents over the years), I scripted the process of reformatting into Markdown using python.  You can see a previous post on this topic <a href="https://www.jasonemiller.org/2021/07/25/regex-ham-general-question-pool.html">here</a>.

## Reformatting with Python

Here's the code I used for the Extra exam question pool.  Note that the reformatting was a but too sophisticated for me to do on my own, so I called on some help from ChatGPT.  Each of its sugestions was tested by hand before including in the larger script.

```python=
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat April 19 2025

@author: Jason Miller (KM6PSZ) assisted by ChatGPT
"""

import re, os, sys

# -----------------------------------
# input text from Amateur Extra question pool

os.chdir('/Users/jason.miller/Library/CloudStorage/OneDrive-CSUCI/DropboxData/unit - Mathematics Department/_amateur radio/FCCextraexam2028/')
input = open("extrapool28-modified.txt","r", encoding="latin-1")
output = open("extrapool28-modified250419-00.md", "w")
input_str=input.read()

# -----------------------------------
# Remove '~~' that separates questions and as markdown would create strikeout text
rm_seps=re.compile(r'(\s*)(~~)')
input_str = rm_seps.sub(r"",input_str)

# -----------------------------------
# Reformat title line
in_title=re.compile(r'(\s*)(2024-2028 Extra Class.*)')
input_str = in_title.sub(r"\n\n# \2",input_str)
 
# -----------------------------------
# Reformat section lines
in_section=re.compile(r'^(SUBELEMENT\sE\d)',re.MULTILINE|re.DOTALL)
input_str = in_section.sub(r"## \1",input_str)

# Replace [ and ] with \[ and \] on lines starting with ##
input_str = re.sub(r'^(##.*?)(\[|\])', r'\1\\\2', input_str, flags=re.MULTILINE)


# -----------------------------------
# Reformat subsection lines

# function to put text of a subclass label on a single line (removing newlines)
def remove_linebreaks(text):
	def replacer(match):
		block=match.group(0)
		block_no_breaks=block.replace('\n','')
		return block_no_breaks
	return re.sub(r'\b(E[0-9][A-Z]\b)(.+\n)?',replacer,text)
# put label on a single line of text

input_str =remove_linebreaks(input_str)

# add markdown formatting
in_subsection=re.compile(r'\b(E[0-9][A-Z]\b)',re.MULTILINE|re.DOTALL)
input_str = in_subsection.sub(r"### \1",input_str)


# -----------------------------
# On a line that starts with an 'E', replace question text (from ']' to '?') with a one-line version
def single_line_question(match):
    prefix = match.group(1)  # The E-line through the closing ]
    question = match.group(2)
    one_line = ' '.join(question.split())
    return f"{prefix}\n{one_line}?"

# Apply the regex
input_str = re.sub(r'^(E[^\n]*\])\s*((?:.|\n)*?)\?', single_line_question, input_str, flags=re.MULTILINE | re.DOTALL)

# -----------------------------
# Reformat each answer to a single line
def flatten_answers(text):
    lines = text.splitlines()
    output = []
    buffer = []
    current_label = None

    for line in lines:
        if re.match(r'^[A-D]\.\s', line):
            # Flush previous answer
            if buffer:
                output.append(current_label + ' '.join(buffer))
                buffer = []
            current_label, rest = line[:3], line[3:].strip()
            buffer.append(rest)
        elif current_label and not re.match(r'^(E|#|[A-D]\.\s|\s*$)', line):
            buffer.append(line.strip())
        else:
            if buffer:
                output.append(current_label + ' '.join(buffer))
                buffer = []
                current_label = None
            output.append(line)

    # Final flush
    if buffer:
        output.append(current_label + ' '.join(buffer))

    return '\n'.join(output)

input_str=flatten_answers(input_str)

# -----------------------------------
# Reformat question and answer lines

def highlight_correct_answer(text):
    # Match each question block starting with 'E' and capture everything until the next 'E' or end of text
    pattern = r'^(E[^\n]+?)\(([A-D])\)(.*?)((?=^E|\Z))'
    
    def bold_correct_choice(match):
        header = match.group(1).strip()
        correct_letter = match.group(2)
        rest = match.group(3)
        # Bold the correct answer choice
        rest = re.sub(rf'(^|\n)({correct_letter}\.\s[^\n]*)', r'\1**\2**', rest)
        return f"{header}({correct_letter}){rest}"

    return re.sub(pattern, bold_correct_choice, text, flags=re.MULTILINE | re.DOTALL)

input_str=highlight_correct_answer(input_str)

# -----------------------------------
# output text

#output.write(new_closebrackets)
output.write(input_str)
input.close()
output.close()


#
# NOTE:  images need to be placed by hand
#
# This is the markdown code that can be put in the Markdown output before the first question that references 
# each image.  This text is for Figure E9-3.
#
# ![Figure E9-3](./e4_2024-svgs/E9-3.svg "Figure E9-3")
# <!-- <img src="./e4_2024-svgs/E9-3.svg" alt="isolated" width="150"/>-->
#
```

This script does *almost* all the reformatting that needs to happen.  But you need to add the images into the markdown document by hand.

