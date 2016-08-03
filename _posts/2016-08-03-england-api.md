---
layout: post
title: England Athletics API and competition entry checks
author: Andy Robinson
---

We're starting to do stricter checks for competition entries.  This post summarises our suggested approach and some of the issues we expect to run into.  I suspect many other people are doing the same and welcome discussion 
<a href="http://forum.opentrack.run/">on our forum</a>

The story so far:

 - rules are changing, and strict checks of status are needed for many competitions.  This was supposed to start on April 1st.
 - EA allowed a "grace period" of 3 months, during which their API incorrectly would say that people were current and paid up when they were in fact lapsed.  This prevented us from testing any validation software until July because we couldn't get "the truth"!  However, since July, it has been "telling the truth" again.
 - We're now opening up entries for some county-level events where fairly strict checks are desirable, and making this available in our system generally.

It's not as simple as one would like.  There is some interplay between two factors:  your status, and how strict the competition wants to be.

## How strict is the meeting?

We're working to offer four levels:

**STRICT**: You can't get past the first step unless we have found you by your England Athletics number, or by name and date of birth, and all the data agrees.

**DRAFT**: we will let you fill in the entry, but we won't let you pay until it checks out.  You can at least then discuss the issue with the organiser and there is a possibility to handle it offline.

**WARN**: we will warn people who are lapsed or not found, and make the status highly visible to the organiser and the people entering on the start lists.  This might leave time to sort out the issue before the meeting.

**DONTCARE**: this may be appropriate for charity events, fun runs, open meetings and anything where we don't want to limit it.

Currently we are not handling road races, but as soon as we get one, we can apply the discount for people who check out OK, so they will be motivated to register.

The STRICT mode is likely to cause a few issues.  Currently we have no way to check Scottish and Northern Irish athletes (although we'd love to add this); foreign guests will be banned; people may not be able to enter if their data at EA is incorrect; and so on.  For this reason, I suspect the DRAFT one will be more popular.



## Possible status check results

The next area is what happens when we check an athlete.  We do this when they enter, but we also need ways to re-check later, as somebody might be able to sort out a problem before entries close, and because organisers still take some paper entries.  So we have a backup routine which can check every athletes that is NOT OK at any time after entry.  (If we're in the STRICT mode, this won't help much.)

We aim to have a fixed set of status values stored against each athlete, plus an optional detailed message.  We have come up with several situations:

**OK**: The API tells us that you are registered, AND at least two out of the first name, last name and date of birth agree.  

**MISMATCH**:  The API says somebody is registered, but the first name, last name and/or age which come back disagree with what was input.   What we've done here is to say "two facts out of three are good enough".  So if the only difference was *Andy* versus *Andrew*, or a woman has changed her maiden name, we'll class it as OK.  Otherwise we'll class it as a MISMATCH.  This should stop people just using someone else's number.

**LAPSED**: The API says you haven't paid your registration fee.

**NOTFOUND**: The API doesn't know you you are.

**ERROR**: Something unexpected happened - maybe in our code, maybe trying to access the API, maybe the API returned something we didn't expect.

We're basically going to do these checks for any meeting other than the *DONTCARE* ones, and store the results.  So the status will be available online and in downloaded start lists.

## Gaps and flaws

The main problem I can see now is that we have no way to check the status of Scottish and Northern Irish athletes.  Imagine a Scottish athlete whose first claim club is in Scotland, but who has been living in Surrey for a year.  They should be able to enter, but we can't check them, as there is no unified UK system.  I imagine this problem would be much more prevalent in the Northern League.

I will note that we would be very happy to provide a unified API, if Scottish Athletics or Athletics Northern Ireland pick up the phone and want to share lists of registered athletes with us.  They are already doing so with the BMAF and it's technically easy.


As noted, discussion of registration-checking issues is welcome 
<a href="http://forum.opentrack.run/">on our forum</a>




