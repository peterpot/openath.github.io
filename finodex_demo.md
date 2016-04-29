---
title: Finodex Demo
layout: default
permalink: /finodex_demo/
tags: finodex
css: //maxcdn.bootstrapcdn.com/font-awesome/4.6.0/css/font-awesome.min.css
---

# Finodex Demonstration
This is a script and demo guide for the FINODEX evaluators.

We are building a complex platform with several different sites and workflows, so we can't just say "do this" to understand what we have built.  There are a number of things you can try out, all listed below.

In all cases we have created as username "finodex" or "finodex@reportlab.com".  The password has been communicated separately.   You will be using a test server, so cannot affect live data.

## 1. Online entry system

We are taking entries right now for key competitions in May 14/15 (UK County Championships).


### Enter the Surrey County Championships

The event page is <a href="https://test-raceresults.reportlab.com/entries/2016/surreytf/">here.</a>

 1. See who is entered (links at top right) - this is real data
 2. Enter yourself.  Try different birth dates.   To make a payment, use card number 4242 4242 4242 4242, any future date and any CVC number).   We expect to take almost a thousand entries between April 28th and May 5th, when they close.

 3. We also made you a meeting organiser.  You can download the meeting info for planning purposes.  (Please delete the data file after - it's personal and we did not have time to generate realistic "fake people")

### Be a team manager in Portugal

See the page for the 
<a href="https://test-raceresults.reportlab.com/entries/2016/emacns/">European Masters Non-Stadia</a> on May 18-20 in Portugal.  If you log in, we have given you rights to manage/approve the Portuguese and Spanish teams.

 1. Browse through the entries

 2. Try the "team manager validation" (right side).  It's your job to tell us if the athletes entered are known to your federation, are the correct age, and have paid their federation fees.  This used to involve a lot of emailed spreadsheets, but this year, it's just a click.

### Other stories

We have several other journeys, but they need some understanding of the real-world process

 - relay team entry
 - cross country team manager: add athletes on the phone

## 2. Open Data

This summer we will release and start to crowdsource open data sets of tracks and clubs.

### Athletics Tracks data set  ("TrackAdvisor"?)
Browse our database of <a href="https://opentrack.info/v/">4000 running tracks in Europe</a>:  we have quite good coverage in UK and Spain.  Some are false positives.  The crowd can help us move pins, add missing ones and remove false alarms.  They can then begin to fill in technical information, disrepair, opening hours, when it's crowded. This will help people to
 - find a place to train
 - plan competitions
 - help governing bodies to plan where investment is needed

It will also let everyone have a clear code for every venue when exchanging results.

### Clubs and Organisations data set:  



Try our running <a href="http://www.reportlab.com/sp/agegrade.html">Age Grade calculations</a> to see how good you are for your age - try on your mobile phone - in English and Portuguese.   We got the maintainer to officially make these factors open data - see <a href="http://www.howardgrubb.co.uk/athletics/data/wavacalc15.xls">last tab of this Excel sheet</a>.  This calculation can be done automatically in any results we present.




#### Athletics tracks
 * <a href="https://opentrack.info/v/">Search for a track</a> - we have quite good coverage in UK and Spain.  Some are false positives.
 * <a href="https://opentrack.info/v/dd354e92-65f5-4ca5-9a5c-b013ac887777/">View details for a specific track<a/>

#### Competition Entries
  * <a href="https://surreyleague.org/slm/race/120/">Surrey league results/declaration page</a>
  * Competition license checker

## 3. Live Recording



The results of <a href="">this race</a> were captured live, as people crossed the line, using a mobile device.

This is the experimental portion of our system.  We handles 4 trial races in February/March for cross country.  And on 7th and 14th May, we're recording throwing and jumping competitions, under the eyes of an Olympic field judge.  The data is stored in Orion.

 * <a href="https://opentrack.info/c/"> List all competitions</a>
 * <a href="https://opentrack.info/c/edit/">Create a competition called 'finodex test'</a>
 * <a href="https://opentrack.info/c/edit/">Create a new race</a>
 * Start the race
 * Use the recording/timekeeping functionality
 * Check the race progress

### 4. Throwing and long jump competitions

Field events (throws and jumps) are hard to follow unless you are competing. 
It's hard to keep up with who is in the lead.  We're going to give everyone
a TV-like experience.

<div class="row finodex">
	<div class="col-sm-3">
		<a target="_blank" href="https://opentrack.info/c/uk2015/sm-sp/le/">Start list
		<i class="fa fa-check-square-o" aria-hidden="true"> </i></a>
		<p class="text-muted">View the main page for a field event </p>
	</div>
	<div class="col-sm-3">
		<a target="_blank" href="https://opentrack.info/c/uk2015/sm-sp/length/">Record some throws...
		<i class="fa fa-flag-checkered" aria-hidden="true"> </i></a>
		
		<p class="text-muted">Record the throws of a Shot Put demo event.
		Officials will use this on a tablet.</p>
	</div>
	<div class="col-sm-3">
		<a target="_blank" href="https://opentrack.info/c/uk2015/sm-sp/le/live/">Watch the results..
		<i class="fa fa-tv" aria-hidden="true"> </i></a>
		<p class="text-muted">See near-realtime results as they are entered.
		Great for parents, friends, team-mates and commentators.
		</p>
	</div>
	<div class="col-sm-3">
		 <a target="_blank" href="https://orion.reportlab.com:1026/v1/contextEntities/opentrack:length-event:cd5b84a3-a47f-4d32-afba-e1197ac8a4ee">Spy on FIWARE Orion...
		<i class="fa fa-gears" aria-hidden="true"> </i></a>
		<p class="text-muted">Inspect the raw data as it is registered and subscribed. </p>
	</div>
</div>
 
This will get it's first trial on May 7th (Oxford vs. Cambridge), and then in May 14th/15th (Surrey County Championships).  We're demoing to a board director of
England Athletics, who was the throwing referee at the London 2012 Olympics,
and giving the output to a top commentator.

## 4. Community resources
 * <a href="https://github.com/openath">Github openath</a>
 * <a href="http://forum.opentrack.run/">Forum pages</a>
 * News page - click menu above
 * <a href="https://twitter.com/open_trak">Twitter page</a>

## 5. Competitors

## 6. Testimonials

### Main Youtube video
<iframe width="560" height="315" src="https://www.youtube.com/embed/SdTcpxOYVxA" frameborder="0" allowfullscreen></iframe>

### Video testimonials
(upload 4 more)




