---
title: Report on testing APRS and emergency comunication options on Santa Rosa Island
author: jason
date: 2025-07-14
tags: amateur-radio, santa-rosa-island, undergraduate-research
---

This post is an update on some amateur radio work I did at the Santa Rosa Island Research Station in July 2025.  I'll talk about my attempts to reach the mainland on VHF and my use of APRS.

I didn't plan to be on Santa Rosa Island this weekend.  On Friday, I was walking across campus and I ran into Dr. Ahmed Awad, a Chemist and the Director of the [Undergrtaduate Research program](https://www.csuci.edu/studentresearch/) at CSUCI.  "Jason", he exclaimed when he saw me, "do you want to come to Santa Rosa this weekend?"  He was inviting me to join a group of students in the Summer Undergraduate Research Fellowship (SURF) program on their annual summer retreat to our [Santa Rosa Island Research Station](https://www.csuci.edu/srirs/) in the [Channel Islands National Park](https://www.nps.gov/chis/index.htm).

I could not say no.  I did not say no.

Santa Rosa Island is a beautiful wilderness area just off the coast of California, and the campus has a research station there that I've visited about a dozen times over the years.  It's always a joy to visit that station with young men and women who are excited about learning and deeply curious about some very specific topic.  It is removed from the hustle and bombast of civilization.  Instead, we enjoy communal dining, group hikes, and game nights that last well into the darkness, all unsullied by internet access.  It's always a great time for everyone.

(Sure, there's often a student that pushes it too hard on a hike and suffers the effects of dehydration or heat exhaustion.  But we all rally around them to help them recover, and all becomes well.)

I wouldn't come to the Santa Rosa Island Resarch Station without some sort of mini-project.  This time, I brought radio gear with the goal of making some HF contacts and trying to find a minimal set-up that would allow consistent contact with people on the CSUCI campus.  The latter would form the basis of an emergency commucations plan for the research station.

## My Amateur Radio Kit

In my kit was a Buddipole, a Comet CX-333 dual band antenna with mast and tripod, a Yaesu FTM-991 mobile all band radio, and a small Bioenno (12 amp hour) battery.  I had considered bringing a larger battery from the campus club kit, but its bulk made me think twice.  (Narrator:  he shouldn't have thought twice.)

In addition, I had three handheld transcievers:  a marine band radio and both a Kenwood TH-D72 and TH-D72.  The former was for fun (to listen to traffic betwwen the park and boat captains as Channel Islands Packers shuttles visitors to and from the island), and the latter were for monitoring NPS radio traffic and beaconing my position via [APRS](https://en.wikipedia.org/wiki/Automatic_Packet_Reporting_System).

On island, I added an additional hand transciever to my kit:  a Baofeng issued by the research station that had been programmed to operate on NPS channels.  I was designated to be 'Operator 958' for traffic on that radio during my time at the station.  For activites on the East side of Santa Rosa Island, we used the [NPS repeater](https://www.radioreference.com/db/aid/4513) on Diablo Peak.

(My TH-D72 has the NPS frequencies programmed into its memory, but because they are not amateur radio frequencies, I can only monitor traffic and not transmit.)

## APRS
My HTs are set up to beacon APRS, one identifying me as KM6PSZ-7 (the TH-D72) and the other KM6PSZ-2 (the TH-D74).  By checking on [aprs.fi](https://aprs.fi) as we were leaving Ventura Harbor on Saturday morning, I was able to verify that my beacon was making it into the APRS network through some nearby gateway.

My beaconing continued to be picked up as our boat motored to Santa Rosa until my battery died.

I next played with APRS while sitting at the picnic table by the Santa Rosa schoolhouse.  Here I used by TH-D74.  To get my APRS beacon into the network, I had to raise my radio up high when I pressed the `BCON` button.  The route of the APRS packet is recorded as `[STPPTU via K6ERN*,WIDE2-1,qAR,XE2SI-10]`.

On the boat ride home, I beaconed again and set my radiot to beacon every five minutes.  Shortly after Prisoners Harbor, my beacon made it into the system and its route was recorded as `[S4PTYS via  K6ERN*,WIDE2-1,qAO,KN6OUU-2]`.  At the other end of the track that's still in aprs.fi, the last recoded beacon location had this route `[S4QRVT via K6ERN*,WIDE2-1,qAR,CAMRIO]`, which is slightly different.


[![APRS tracks of my travels](/assets/images/srirs-amateur-radio-250714-aprsmap-thumbnail.jpg)](/assets/images/srirs-amateur-radio-250714-aprsmap.jpg)

![APRS tracks of my travels](srirs-amateur-radio50-7214aprsmap.png)

I've copied all the APRS packet routes from the aprs.fi record of my route to and from the island and added thenm to an appendix of this post, below.

## Making VHF contacts

On Sunday morning, while the students and two other faculty members went out on their *a pied* excursions, it was my job to sit near the bunkhouse and use the station HT to monitor the Diablo NPS repeater for traffic from the excursionists.    So I set up my Yaesu FT-991 at the picnic table outside the old school house with the dual band antenna hoisted to a great height (maybe 25-20 feet), and set out to make some contacts on the mainland.

I started with some Santa Barbara repeaters, and I had success with one.  Then I moved to the BOZO repeaters in Ventura County (on 147.885 with PL tone of 127.8).  I was pleased to be able to open the BOZO repeater right away, and I made a contact with someone in Thousand Oaks who reported that my signal was strong.  I then reduced my signal strength from 50W to 25W and then to 10W, and he affirmed that I was still keeping the repeater open and my signal was strong.

This is very good information.  It means that the Santa Rosa Island Research Station has a very simple emergency communication plan to reach the mainland.  Because campus can reach the BOZO repeaters easily, the Research Station can reach campus easily in an emergency.  So long as someone is monitoring the BOZO repeaters.

Happy with this, set up the HF antenna (Buddipole) without turning off my radio.  This means that my radio continued to operate without me monitoring it, which isn't a big deal until you note that the Yaesu FT-991 has a standard 1 amp draw.  While I worked, the radio was draining the battery to nobody's benefit.

Later that everning, I worked some HF bands.  At one point, trip colleagues came up to learn about the process, which was lots of fun.  I didn't make any contact while they were listening, but we heard transmissions from New Zealand, Washington, and Texas.  My colleagues were delighted to have heard that!  At one point, though, the radio abruptly shut off.  The battery died, unexpectedly.  My operations during the day came at a cost!

When I went in for the night, I plugged the battery into the charger to juice it up over night.  But in the morning the Yaesu worked for a very very short time before cutting out.  The charge didn't take.  It appears I drained the battery so much that the internal BMS might require special treatment to allow a recharge.  I need to learn more about that.

The battery crapping out kept me from testing transmission on 5W.

## Simplex Communication with the Mainland

On Monday morning, with a battery that was charged less than I knew, I set up the dual band antenna and made contact with my students who were in the campus radio room, waiting for me.  (We coordianted this via email.). before teh battery crapped out on me, I was able to verify that they could receive transmissions from me at 50W, 25W, and 10W. The battery crapped out before I could make a meaningful transmission at 5W.

The experiment I had *wnted* to run would test simplex communication with the radio room.  Could I communicate directly with my students on simplex using VHF or UHF.  I would have used the national calling frequencies.

Sadly, lacking power meant the test was impossible.  Put it on the list for enxt experiments to run.

It's worth noting that 'crapping out' is 100% deactivation of the radio.  There's nothing gradual about the failure.  No fading.  Just going from being on one moment to off the next, and that failure would happen with the PTT was pressed (note: transmission soikes the draw on the battery).

## Next Experiments

The next time we can get people to the island, we will test the following:

1. Ability to contact the radio room on simplex with a dual band antenna (e.g., Comet CX-333) and the lowest required transmission power for doing so.
2. Repeat the above, replacing the CX-333 with a directional Yagi.
3. Repeating the above, replacing the Yaesu with a HT radio.
4. Exploring connectivity using the 220MHz repeater on Diablo and the 220MHz radio in the radio room.  (We'd need a 220MHz transciever on the island, and a HT that can transmit on 220MHz.)




### Appendix:  APRS Paths

Here are the APRS paths on the route from the harbor to the island.

```
[STQSPV via K6ERN*,WIDE2-1,qAR,CAMRIO]
[STQQWQ via K6ERN*,WIDE2-1,qAR,CAMRIO]
[STPXVQ via K6ERN*,WIDE2-1,qAR,CAMRIO]
[STPVVX via K6ERN*,WIDE2-1,qAR,CAMRIO]
[STPUUR via K6ERN*,WIDE2-1,qAR,CAMRIO]
[STPUQV via K6ERN*,WIDE2-1,qAR,CAMRIO]
[STPPTU via K6ERN*,WIDE2-1,qAR,XE2SI-10]
```

Here are the APRS paths on the route from the island to the mainland.

```
[STPPTU via K6ERN*,WIDE2-1,qAR,XE2SI-10]
[S4PPYP via K6SYV-10,WIDE1*,WIDE2-1,qAO,AI6NE-1]
[S4PSPX via K6SYV-10,WIDE1*,WIDE2-1,qAR,KF6NYM-15]
[S4PTWY via K6SYV-10,WIDE1*,WIDE2-1,qAR,KF6NYM-15]
[S4PTYQ via K6SYV-10,WIDE1*,WIDE2-1,qAR,K7AZ-11]
[S4PTUX via K6ERN*,WIDE2-1,qAR,CAMRIO]
[S4PTRT via K6ERN*,WIDE2-1,qAR,CAMRIO]
[S4PTTS via K6ERN*,WIDE2-1,qAR,CAMRIO]
[S4PTUX via K6SYV-10,WIDE1*,WIDE2-1,qAR,KF6NYM-15]
[S4PTRP via K6SYV-10,WIDE1*,WIDE2-1,qAR,KF6NYM-15]
[S4PSVT via K6ERN*,WIDE2-1,qAR,XE2SI-10]
[S4PQVS via K6ERN*,WIDE2-1,qAR,CAMRIO]
[S4PQRS via K6ERN*,WIDE2-1,qAR,CAMRIO]
[S4PTYS via K6ERN*,WIDE2-1,qAO,KN6OUU-2]
[S4PURY via K6ERN*,WIDE2-1,qAR,CAMRIO]
[S4PVPW via K6ERN*,WIDE2-1,qAR,CAMRIO]
[S4PWPT via K6ERN*,WIDE2-1,qAR,CAMRIO]
[S4PXPV via K6SYV-10,WIDE1*,WIDE2-1,qAR,KF6NYM-15]
[S4PYQW via K6ERN*,WIDE2-1,qAR,CAMRIO]
[S4PYYQ via K6ERN*,WIDE2-1,qAR,CAMRIO]
[S4QPYQ via K6ERN*,WIDE2-1,qAR,CAMRIO]
[S4QRVT via K6ERN*,WIDE2-1,qAR,CAMRIO]
```

Knowing the route that APRS beacons travel when on the island will help us understand efficient ways to use APRS on the island (*e.g.*, how much power do we need to use while beaconing).



