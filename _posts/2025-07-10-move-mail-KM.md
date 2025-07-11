---
title: Sorting Email using Keyboard Maestro
author: Jason
layout: post
date: 2025-07-10
tags: computer mail keyboard-maestro productivity
---

I get lots of email.  It will always be an unorganized mess.  What I want is that mess to be outside my Inbox.  It would help me to have a semi-automated way to move messages around to minimize the mess.

One app I have close at hand at all times, but don't use nearly as much as I could or shoud, is [Keyboard Masetro](https://www.keyboardmaestro.com/main/).  I knew it should be able to help me.

A Google search on the topic turned up [this web page](https://www.letstalk-tech.com/how-to-use-keyboard-maestro-to-archive-email-in-mail-app/).  It has eroded a bit over time (*i.e.*, lost its code block), but there was enough there for me to get it to work.

The gist to the applescript in the example was lost to time, but the author had a screenshot that showed the whole thing.  Note that in this example, I'm moving a message to the `Archive` mailbox that sits inside the `Archive1` folder in my `Exchange` account.

First, add a `Macro Group`  so KM gives you a palette of Mail folders to which you can move a selection of messages.  Type ⇧⌘N while in the `Group` column of KM or clock on the `+` at the bottom of the column.  This will open a pan on the right end of the KM window.

We want the palette only available in the Mail app, so use the pull-down list to select `Available in these applications` and use the green `+` button to add the Mail app.  The Mail app should be in the list of applications by default.

In the next pull-down list, select `Available in all windows`.

In the third pull-down list, select `Show a palette for one action when:` and indicate that you want to use a hotkey.  In this case I use ⇧⌥A.

We are ready to populate this group with one macro for each type of move we want to make.

Press ⌘N (or click the + at the bottom of the middle pane) to create a new macro.  It will appear in the second pane.  Give it a name.  

The author gives some good tips on how to name the macros in this group.

> Note that the name you choose is important since Keyboard Maestro will sort your macros in alphabetical order. Fortunately, there is a small trick that will allow you to manually sort your actions. By simply prefixing the name with 2 digits and a closing bracket such as 00), Keyboard Maestro will hide the numbers, but still use them to sort your macros.

With the new macro selected, clock on the green `+` in the left KM pane to add a new trigger.  I use `1` because it will be my first macro action in the palette.  Seting a trigger isn't required because you can click on the palette elements to execute the macro you want.  

In the pull-down list below the triggers, choose `Or by script`.  Then click on the green `+` to add a new action; choose the `Execute` folder in the first column and `Execute an AppleScript` in the second column.  A box will appear at the bottom of the KM pane - this is where the following Applescript will go.   
There are two pull-down selections here:  select `Execute Text Script` and `Display results in a notification`.  Now copy the Applescript.

```applescript
try
	tell application "Mail"
		set msgs to selection
		if length of msgs is not 0 then
			repeat with msg in msgs
				try
					move msg to mailbox "Archive" in mailbox "Archive1" of account "Exchange"
				on error errmsg
					return errmsg
				end try
			end repeat
			return "Moved" & length of msgs & " messages to Archive subfolder of Archive1 folder in Exchange account."
		else
			return "Please select a message or messages."
		end if
	end tell
on error errmsg
	return errmsg
end try
```
That's it.  For each type of move, make a different macro action, revising the line `move msg to mailbox "Archive" in mailbox "Archive1" of account "Exchange"` to reflect the mailbox destination of choice.

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
