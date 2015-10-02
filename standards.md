---
title: Open Standards
layout: default
permalink: /standards/
tags: standards
---

# Open Standards


# Preface

We'd like to evolve agreed standards for interchange between systems.  This will hopefully involve both system-to-system standards (e.g JSON document formats), and human-friendly ones.  The human-friendly ones will largely relate to what headings and values to use in spreadsheets; we can provide tools to check these and convert.

The biggest challenge, to tackle first, is about codes and terminology:  how do we refer to things?

This document is not aiming for the levels of precision of an ISO or Internet standard.  In the words of the Internet Engineering Task Force, we want "rough consensus and running code".  To this end we do NOT need to agree now exactly how to repesent unusual or historic events such as the six mile track record, or quibble too much about recording the exact weight of the javelin used; these are important, but we can achieve other things while these are being discussed.

If you disagree with the standards, join the forum (coming soon) and argue, or make counter-suggestions, so we can reach the best solution quickly.  The OpenTrack project wants to set its standards quickly.   If yu are happy to follow these standards, let us know and we'll add your name to a list to put pressure on others.

# Codes and representation

We want to set unambiguous codes for the "things" use to build databases and systems.  It is useful if these codes are safe for use in URL parameters (avoiding '?' and '/'), markup ('<, & and &'), and in filenames.  There are workarounds for all of these things, but let's just avoid as many as we can.  


## Gender ##

Let's warm up with something simple:

    M = Male
    F = Female

If the 1976 Olympic Decathlon champion decides to make a comeback, we can discuss complicating things then.


## Dates

We aim to be guided by <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a>

Databases have rich ways to store dates, date-times and times, complete with time zone information.  In athletics this can be troublesome, unless you are very careful.  For example, you set up your county championships timetable in some detail in March, then the clocks change, and you find the computer assumed GMT when you entered in, and everyone shows up an hour off; or that you are advertising the wrong start time for an early-autumn cross country race.



    "2015-10-17"  - use for dates, the ISO standard.  (Excel will differ)
    "14:35" - use for the start time of an event, for historic or programme purposes

When describing programmes or sets of results, we recommend separating the dates and times.  If you are going to use exact datetime variables, you have to get the time zone right (both when the input was done and when the event is taking place.)

### Dates in Excel and user interfaces
Pasting or importing of dates and times from Excel is risky.  Spreadsheets understand dates, but if you go via a clipboard or to CSV/text, there is the risk of muddling days and months.   Within a spreadsheet, dates should be proper dates.


## Performances, time and distance

In results, we need to record the time or distance.  This is different from recording the start time of an event.  

Times should be passed in a decimalized text format and interpreted as a number of seconds, so we know the precision that was given. If one colon is present, it denotes minutes and seconds; two colons are hours/minutes/seconds.  Ultra runners going beyond 24 hours will have to count in hours to keep life simple for the rest of us!

    9.58
    58.5
    63.5
    1:03.5     - equivalent to 63.5, first digit assumed to be minutes
    2:03   - assumed to be an 800m time of 2 minutes, and not a Marathon, because only one colon
    2:02:57 - the marathon world record, two colons so contains hours
    73:15 - a half marathon time, equivalent to 1:03:15

Distances for jumps and throws can be stored as decimal numbers.



## Disciplines

We are deliberately avoiding the word 'event', which has too many connotations within athletics, as well as in IT generally.  For the purpose of this document, we will call 'High Jump' or '100m' <em>disciplines</em>.

We would like to have unambiguous short codes which can be used internally, or as search criteria.
Our "first stab" is to use the codes from Power of Ten, which appear in the URL search parameters.  Here are most of the standard athletics events:

    60,100,200,400,800,1500,3000,5000,10000
    2000SC, 3000SC - steeplechase
    60H, 100H, 400H   (and other distances for junior hurdles)
    HJ, PV, LJ, TJ
    SP, DT, HT, JT  - discuss
    Dec, Hep, HepI  - multi-events
    20KW, 50KW - walks
    4x100, 4x400 - track relays

    ZXC - used for cross country, over distances which may not be accurate or comparable.

The <a href="http://www.iaaf.org/records/toplists/">IAAF web site</a> uses 'slugs' - URL components - such as 'one-mile' and 'high-jump'.  These are certainly useful.



### Unusual distances

Now it gets interesting as there are many ways to do it.

    Mile  - one mile (assume track)
    3M, 5M, 10M - precise distance in miles - assume road
    5K, 10K - assumed to be road; if it was track, we'd use '5000'


## Disability Categories ##

Need a list and a link to a good explanation




