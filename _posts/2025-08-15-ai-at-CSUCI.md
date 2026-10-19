---
title: Generative AI in Mathematics?  Some thoughts.
author: Jason
layout: post
date: 2025-08-15
tags: teaching AI
---

In early 2025, the California State University system officiall [dove into the deep end of that AI pool](https://www.calstate.edu/csu-system/news/Pages/CSU-AI-Powered-Initiative.aspx) by declaring itself the country's first and largest "AI-empowered higher education system."  This system-wide adoption surprised most of us in the system, and it took me a while to start to understand its implications.  To try to understand how this will effect me as an educator, I enrolled in a summer faculty development course aimed at helping faculty incorporate AI into their teaching.  This post shares a couple things I learned.

**TL;DR:**  Generative AI can be a valuable aid when working with lots of data or in tedious and repetive tasks, so it doesn't do mathematics well.  (Mathematics is a creative act.)  Generative AI can make images, but you can't exert fine control over their content.   And the art of writing a prompt for AI might give us a way to use AI to help students be more effective learners.

## Tedious and Repetitive

At the start of the course, I learned that our leaders in the campus Learning Resource Center (where our tutors are trained and supported) are *trying* to drink the AI coolaid, but they are informed enough to see the challenges teachers will have to grapple with.  Throughout the summer experience, our facilitator acknowledged the limitations of generative AI and encouraged us to explore AI tools to find those limitations ourselves.  The AI industry wants us to believe that AI is evolving quickly, leaving past problems behind.  We need to test those claims ourselves by using the tools and seeing AI capabilities with our own eyes.

I've fiddled with AI in a few ways over the last couple years.  I've used it to summarize large documents, suggest titles for an initiative, draft logos, and explain mathematical concepts.  Generative AI does better with some things (summarizing and brainstorming) than others (mathematics).  If educators are looking for a way to automate tedious repetitive tasks, AI might provide a solution.  Unfortunately, faculty members don't have many tasks like that.  Most require individual, creative attention at some level.  Instruction is like that.

## Beware Mathematics

Generative AI hasn't been very good at mathematics.  It's getting better at solving mathematical problems and showing the steps that lead to a solution.  This makes generative AI a great tool for students who want technology to do their thinking for them.  Educators need to find ways to teach that either embrace this reality or protect against it.

Students strugle with coming up with examples of functions that have prescribed properties.  During this AI course, I had the idea of using generative AI to generate examples of functions with properties that students are learning about for the first time in Calculus.  This is a matheamtical task that requires a limited amount of creativity.  

I asked ChatGPT EDU to "give me an example of a function that is continuous everywhere but not differentiable."  The prompt was a bit open ended, but ChatGPT responded [like a champ](https://chatgpt.com/s/t_689f385a5ae48191a4d3501a35e754ee), giving me the absolute value function.  Perhaps also hoping to earn brownie points, it also gave me the canonical example of a function that is everywhere continuous but nowhere differentiable.

I tried again, using a more specific prompt.  I asked it for an example of a function that was continuous on [0,1) and (1,2] but not differentiable at x=1.  Again, it won a prize with [this answer](https://chatgpt.com/s/t_689f385a5ae48191a4d3501a35e754ee).  It gave me an appropriate proper piece-wise defined function.  I was impressed until I asked ChatGPT to graph the function.  It failed at this.

[![Plot of two parallel increasing lines.](/assets/images/image-ChatGPTbadgraph.png)](/assets/images/image-ChatGPTbadgraph.png)

I attempted to coax ChatGPT with feedback aimed at helping it correct its error.  After a couple failed attempts, I wrote, "Yeah, sorry buddy. Your function is correct, but you're not graphing it correctly."  After submitting this to the chat, ChatGPT tried again and [got the graph right](https://chatgpt.com/s/t_689f39c326488191b5c7fbf7721052c4).

This suggests to me that the value in ChatGPT generating examples for students might be limited, and I shouldn't use it as an instructional tool.

I tried the same requests with another generative AI agent, [Claude](http://calude.ai) and had better mathematical results.  It didn't typeset the mathematics as nicely (which might confuse students), but it didn't make the same dumb graphing mistakes as ChatGPT.  I need to play with Claude a little more to see if it's better at generating examples for my Calculus students.

## Images

Generative AI likes to boast that it can generate images as well as text.  As part of an assignment in my summer course, I asked ChatGPT to generate a social media post (for LinkedIn) that talked about the summer course and how I hoped to integrate AI into my Calculus courses this Fall.  ChatGPT easily produced a 150 uninspiring words.  I then asked ChatGPT to generate an image to go along with the post.

It gave me this image:

[![ALT-TEXT](/assets/images/image-coursera-1.png)](/assets/images/image-coursera-1.png)

It has visual appeal, but I wanted the mathematics to be more visible.  So I asked ChatGPT to revise the image with that in mind.  It gave me this revision.

[![ALT-TEXT](/assets/images/image-coursera-2.png)](/assets/images/image-coursera-2.png)

I initially liked this one more.  It had a stronger 'mathematical' appearance.  Then I looked closer and noticed that what looked mathematical was nonsense.  This wouldn't be acceptable, so I asked ChatGPT to review the image.  To my surprise, it said that the task was impossible for it to fulfill, and it suggested that I overlay mathematical expressions that I generate with LaTeX!

This generative limitation of ChatGPT is interesting, and it's good news for creative types!

## Prompts

A person interacts with generative AI through written prompts.  How you write a prompt influences what the AI tool generates for you.  In my summer course, we spent a bunch of time thinking about this and practicing prompt writing.

About half-way through the summer course, it occured to me that I could use the importance of prompts to help students improve on a skill that has always challenged them:  asking questions.  Students have a hard time asking questions about new (and old) mathematical concepts and techniques.  They struggle to articulate what is creating confusion for them.  Students who are better at asking questions will be more effective learners.

Since a prompt to a genrative AI agent is essentially the expression of a question, perhaps spending some time asking students to work on writing effective prompts for AI tools will translate to them asking better questions in class?

Watch this space for any updates on how this works out for me.

## Conclusion

Generative AI has arrive, is available to students, and we educators need to figure out how to adapt.  We adapted how we taught mathematics when affordable graphing calculators hit the market in the early 1990s.  While some instructors 'adapted' by prohibilting their use, other instructors saw the new technology as making some old skills irrelevant (e.g., numerical computation) and creating new opportunities for understanding mathematics possible.  For example, graphing calculators made generating plots of function fast and easy because computing and drawing were two things that computers did faster than a human.  Mathematics educators are still wrestling with the impact of pervasive computing on learning, and generative AI is just a new facet of this old reality.  We'll figure out how to adapt and teach students what they need to know to be mathematically literate in the 21st century.

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
