---
title: Finodex Demo
layout: default
permalink: /finodex_demo/
tags: finodex
css: //maxcdn.bootstrapcdn.com/font-awesome/4.6.0/css/font-awesome.min.css
---

# Finodex Demonstration
This is a script and demo guide for the FINODEX evaluators.

We are building a complex platform with several different sites and workflows, so we can't just say "do this" to understand what we have built.  There are a number of things you can try out, all listed below.  Click the <button data-toggle="collapse" data-target="#showme">Instructions</button> button next to each feature for a step-by-step guide.

<div id="showme">That's right!</div>

When asked to log in, you can use

 - username:  finodex@reportlab.com
 - password:  the name of Miguel's company, all lower case


## 1. Online entry system

We are taking entries right now for key competitions in May.  These are recent copies of the real entry data.  Some notes below will guide you on what to do.

<div class="row finodex">
	<div class="col-sm-6">
		<a target="_blank" href="https://test-raceresults.reportlab.com/entries/2016/surreytf/">Surrey County Championships<br>London, May 14/15 2016
		<i class="fa fa-flag-checkered" aria-hidden="true"> </i></a>
		
		<p class="text-muted">Please enter!  Real money not needed</p>

		<div id="surreytf" class="panel panel-default">
			<div class="panel-heading">
    			<h3 class="panel-title">
    				<a data-toggle="collapse" data-target="#instructions-surreytf" 
           href="#surreytf">
          Instructions</a>
    			</h3>
  			</div>
  			<div class="panel-body collapse" id="instructions-surreytf">
				<ol>
					<li>Click above to launch in a new window</li>
					<li>See who is entered (links at top right) - this is real data</li>
					<li>Enter yourself.  Try different birth dates.   To make a payment, use card number 4242 4242 4242 4242, any future date and any CVC number).   We expect to take almost a thousand entries between April 28th and May 5th, when they close.</li>
					<li>We also made you a meeting organiser.  You can download the meeting info for planning purposes using the cream links on the right.  (Please delete the data file after - it's personal and we did not have time to generate realistic "fake people")
						
					</li>
				</ol>

  			</div>
		</div>
	</div>
	<div class="col-sm-6">
		<a target="_blank" href="https://test-raceresults.reportlab.com/entries/2016/emacns/">European Masters Non-Stadia<br>Portugal, May 20-22 2016
		<i class="fa fa-check-square-o" aria-hidden="true"> </i></a>
		<p class="text-muted">Be a team manager.  Approve your squad.</p>
		<div id="surreytf" class="panel panel-default">
			<div class="panel-heading">
    			<h3 class="panel-title">
    				<a data-toggle="collapse" data-target="#instructions-emacns">
          Instructions</a>
    			</h3>
  			</div>
  			<div class="panel-body collapse" id="instructions-emacns">
  				If you log in, we have given you rights to manage/approve the Portuguese and Spanish teams.

				<ol>
					<li>Browse through the entries</li>
					<li>Try the "team manager validation" (right side). </li>
					<li>Go to Spain or Portugal.  Approve or disapprove, leave a note</li> 
				</ol>
				It's your job to tell us if the athletes entered are known to your federation, are the correct age, and have paid their federation fees.  (Sometimes the 80-year-olds
				make mistakes!) This used to involve a lot of emailed spreadsheets, sent repeatedly back and forth, but this year, it's just a click.

  			</div>
		</div>		
	</div>
</div>

### Other stories

We have several other journeys, but they need some understanding of the real-world process, so we have omitted them today

 - relay team entry - choose teams, then pay for squad
 - cross country team manager: add athletes to your squad (on the phone, before a race)

## 2. Open Data

This summer we will release and start to crowdsource open data sets of _tracks_ and _clubs/associations_.  These are important because the sport needs common IDs to build databases.  

They are a step towards getting the actual results labelled as Open Data&trade;. We will let people get used to the idea of open reference data first.

<div class="row finodex">
	<div class="col-sm-6">
		<a target="_blank" href="https://opentrack.info/v/">
		Track directory - TrackAdvisor?<br>
		<img src="/img/trackfinder.png" width="300"></a>
		
		<p class="text-muted">Click and explore. UK and Spain are best.</p>

		<div id="surreytf" class="panel panel-default">
			<div class="panel-heading">
    			<h3 class="panel-title">
    				<a data-toggle="collapse" data-target="#instructions-tracks">
          Background - how and why?</a>
    			</h3>
  			</div>
  			<div class="panel-body collapse" id="instructions-tracks">
	  			We started with OpenStreetMap, and cross-referenced to federation
	  			lists of stadia, based on geocoded addresses.

	  			Why? First of all, there's nothing like this.  The UK and USA have really old, unmaintained sites.  It's useful to runners

	  			Secondly, we'll let people choose the "usual name" and have a unique code for every track. When building databases of results
	  			or advertising fixtures, a common.

	  			Stadia can include opening hours, who manages it, what needs
	  			repair, when there are schoolkids in the way.  Anyone can contribute.

	  			We'll expand to clubhouses, regular race courses and "places groups meet".  NOT Strava or MapMyRun.

	  			This should quickly make us useful.
	  			</div>
		</div>
	</div>
	<div class="col-sm-6">
		<a target="_blank" href="https://raceresults.reportlab.com/ref/eapick/">
		Clubs and Organisations<br>
		<img src="/img/clubpicker.png" width="300"></a>
		
		<p class="text-muted"></p>

		<div id="surreytf" class="panel panel-default">
			<div class="panel-heading">
    			<h3 class="panel-title">
    				<a data-toggle="collapse" data-target="#instructions-clubs">
          Background - how and why?</a>
    			</h3>
  			</div>
  			<div class="panel-body collapse" id="instructions-clubs">
  			<ul>
  				<li>We started with 3000 organisations in the sport in the UK, and
	  			have had 250 clubs contributed from Spain.</li>

	  			<li>To take entries accurately, we need to let people CHOOSE a club,
	  			not just type in free text.  We need IDs for the clubs.</li>

	  			<li>We will let each club manage its listing, and advertise their
	  			training nights, public contacts and so on - all as Open Data</li>

	  			<li>They can "choose their code", first come first served in each country, in 
	  			results, and nice flags and logos.  Anyone gets to use these
	  			in results presentation.</li>

	  			<li>We give them nice web widgets to embed in their site, so they
	  			can present things with no web skills, and we get more data.</li>
	  			
	  		</ul>
  			</div>
		</div>
	</div>
</div>



## Competition Entries
  * <a href="https://surreyleague.org/slm/race/120/">Surrey league results/declaration page</a>
  * Competition license checker

## 3. Live Recording

FIWARE Orion lets us record data on a massive scale.  Matches on the same Saturday all over Europe, with dozens of volunteers.  



### 3A. Throwing and long jump competitions - "Internet of Throws"

Throwing and horizontal jumps are hard to follow, unless you are competing. 
It's hard to keep track of who is in the lead, or where your friend (or child!) is until it's over.  We're going to give everyone
a TV-like experience and get the results out quickly.

This is a first step towards a full track and field management system, recording
all event types and doing live match scores.

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

### 3B.  Recording running races

The results of <a href="">this race</a> were captured live, as people crossed the line, using a mobile device.

This is the experimental portion of our system.  We handles 4 trial races in February/March for cross country.  And on 7th and 14th May, we're recording throwing and jumping competitions, under the eyes of an Olympic field judge.  The data is stored in Orion.

 * <a href="https://opentrack.info/c/"> List all competitions</a>
 * <a href="https://opentrack.info/c/edit/">Create a competition called 'finodex test'</a>
 * <a href="https://opentrack.info/c/edit/">Create a new race</a>
 * Start the race
 * Use the recording/timekeeping functionality
 * Check the race progress

## 4. Community resources
 * <a href="https://github.com/openath">Github openath</a>
 * <a href="http://forum.opentrack.run/">Forum pages</a>
 * News page - click menu above
 * <a href="https://twitter.com/open_trak">Twitter page</a>

## 5. Competitors

## 6. Testimonials

<a href="/feedback/">Click here</a> to see our feedback - quotations and testimonials

### Main Youtube video
<iframe width="560" height="315" src="https://www.youtube.com/embed/_gHIwov5PKY" frameborder="1" allowfullscreen></iframe>

### Video testimonials

Mary Drysdale, Race Director, Run2Rio


<div class="row">
	<div class="col-md-4">
		<iframe width="300" height="170" 
			src="https://www.youtube.com/embed/ePha0ymNTVE" frameborder="1" allowfullscreen>
		</iframe>
		Mary Drysdale, Race Director, Run2Rio
	</div>
	<div class="col-md-4">
		<iframe width="300" height="170" 
			src="https://www.youtube.com/embed/-OUKnYZDeuI" frameborder="1" allowfullscreen>
		</iframe>
		Matthew Kiernan, Team Manager and Race Organiser
	</div>
	<div class="col-md-4">
		<iframe width="300" height="170" 
			src="https://www.youtube.com/embed/mg3i2R1Hpk4" frameborder="1" allowfullscreen>
		</iframe>
		Nicola Fleet, Surrey County senior technical official
	</div>
</div>


<div class="row">
	<div class="col-md-4">
		<iframe width="300" height="170" 
			src="https://www.youtube.com/embed/jbC9waKezI8" frameborder="1" allowfullscreen>
		</iframe>
		Pat Logan, Club coach (and multiple masters world sprint champion)
	</div>
	<div class="col-md-4">
		<iframe width="300" height="170" 
			src="https://www.youtube.com/embed/eezBbTLwLx8" frameborder="1" allowfullscreen>
		</iframe>
		Paul Weston, club coach, Croydon Harriers
	</div>
	<div class="col-md-4">
	</div>
</div>


##  Open Data Policies

http://opentrack.run/opendata/

https://raceresults.reportlab.com/page/privacy-policy/


## Market research, useful data

Sport England <a href="https://www.sportengland.org/media/3912/1x30_sport_14plus_factsheet_aps9v2.pdf">Active People Survey</a> - see page 3

KU Leuven <a href="http://faber.kuleuven.be/spm/">Sport Policy &amp; Management</a> unit - see SPM 10 (name needed to download)

<a href="http://www.playthegame.org/fileadmin/image/PtG2013/Presentations/30_October_Wednesday/Jeroen_Scheerder_30_ok_11.30_Spejlsalen.pdf">RUNNING ACROSS EUROPE - The European sports model revisited</a> - Scheerder and Breedveld.  Presentation

Demographics of runners - Competitor Group <a href="http://cdn.competitorgroup.com/wp-content/uploads/2016/04/2016_Competitor_MediaKit_Updated.pdf">Media Kit</a>
