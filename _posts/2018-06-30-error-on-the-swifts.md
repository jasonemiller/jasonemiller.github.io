---
title: Problem with the Anabat Swift
author: miller
date: 2018-06-30
category: post
tags: [bats]
---
The purpose of this post is to describe an error we're experiencing with two of our Anabat Swifts.  The third Swift in our stable works perfectly well, we think.  In this post, I'll summarize our problem.  Then I will give a detailed report on our last encounter with the problem.  If we solve the problem, I will edit this post to include an explanation of the source of the problem (as I understand it) and the solution to the problem.

## Problem Summary ##

We are getting "error" and "format error" messages from our Anabat Swift passive bat detectors/recorders.  To isolate the cause of the error, we have purchased and used new 128gb SanDisk Ultra Plus SD cards from Amazon.com.  We have verified that all the cards we use mount on our laptops, are formatted, and are empty of any data.<br><br>Our SD cards are numbered so we can keep track of which cards are in which units and have which data.  This report will refer to them as SD18 and SD21, for example.

## Notes on Errors from First Unit ##

We have two Anabat Swift units deployed in the field for testing.  We put them out yesterday afternoon, and this morning we returned to them to see if they recorded any bat activity.  I took meticulous notes of our experience replacing the SD cards with fresh SD cards.

At Site #1, our Swift (P03) is attached to a post.   We verify that the detector, mic, and cord look unmolested.

Strap off.  Detach mic from case.  Power down.  Remove 2 SD cards:  SD11 from slot 1, SD10 from slot 2.  The former opens with 12 files.  The later is empty.  Both are put in our SD card portfolio to take back to basecamp.

We put SD07 in slot 1 and SD09 in slot 2.  Attach mic. Power on.

Slot 2 displays "error".  Reformat SD09 in slot 2 using the Swift.  Main screen, see "error" on slot 2.  Waited.  Dialog box opens, "Do you want to reformat slot 1?"  Answer 'no'.  Swift asks again.  Answer 'no'.  Back to main screen.  Now see "error" on slot 1, too.  (That is, "error" on both slots.).

Wait.  Now slot 1 "error" goes away and shows that slot 1 SD card is good, but there's still an "error" on slot 2.  Power down.  Wait a long 20 seconds.  Power up.

Main screen shows "error" on both slots.  Pause.  Main screen changes to show an error only on slot 2; slot 1 looks fine, like it is working condition.  Reformat SD09 in slot 2 using the Swift.   Oddly, the device reformats slot 1 (according to the message on the display).  Then the main display shows an "error" for both slots; slot 1 reads "error, 0 GB" and slot 2 reals "error".

![Format error display on Anabat Swift](/assets/images/IMG_0833-768x1024.png)

Then reformatted both cards with the device.  Main screen shows a "format error" for slot 1 and a "reformat error" on slot 2.

![Error displayed on Anabat Swift.](/assets/images/IMG_2635-768x1024.png)

Power down.  Try new cards:  SD15 in slot 1 and SD19 in slot 2.   Power up.  Slot 1 looks like it is working normally, but slot 2 shows "error".  Reformat SD19 in slot 2 using the Swift  Get "format error" on display.  Decide to replace Swift with our spare, P02.

Power down.  Detach mic.  Remove battery pack from P03 and put it into P02.  Put SD20 into slot 1 and SD21 in slot 2 of replacement Swift.  Attach mic.  Power on.

Both cards look good.  Waiting to acquire GPS.  Signal acquired.  Closed unit.  Strapped to post.  Check that there is not play in the attachment.  Verify set-up and activity with magnet.  Light blinks.  Good to go.

## Notes on Errors with Second Unit ##

Detector, mic, and cord look unmolested.  Unchanged from when they were placed yesterday.  Strap off.  Detach Mic from case.  Power down.  Because of "error"s thrown on slot 1 when we were placing the Swift in the field, the unit has only one SD card installed, and it's in slot 2.

Remove SD08 from slot 2.  This card SD08 mounts in a laptop to show 134 files recorded, 1gb storage used.

Place SD13 in slot 1 and SD14 in slot 2.  Attach mic.  Power on.

Get "error" in slot 1.  Reformat SD13 in slot 1 using the Swift.  Main screen then shows "format error" in slot 1 which soon changes to "error" in slot 1.

Power down.  Remove SD13 from slot 1.  Replace with SD18.  Power on.

Main screen shows that both appear good.  Then screen closes on its own.  When it reopens, it shows "error" in slot 1.

Reformat SD18 in slot 1 using the Swift.  Get "format error" for slot 1 on main screen.

Power off.  Wait 20 long seconds.  Power on.  See "error" for slot 1.  Power off.  Take SD 18 out of slot 1 and put SD21 into slot 1.  Power on.

See "error" in slot 1.  Power off.  Remove SD21.  Decide to replace the unit with only one SD card.  Verify that slot 2 is still good.  Close unit.  Verify that GPS is acquired.  Strap to post.  Test with magnet - doesn't blink.

##Update 1:  For what it's worth...##

Back at basecamp, just for kicks, I opened up the Swift to check the firmware version.  Saw that it was version 1.0.  Read in the manual how to update the firmware, and I did that.  But something else remarkable happened when I powered up the Swift.  BOTH SD CARDS READ PERFECTLY!!  No errors.




