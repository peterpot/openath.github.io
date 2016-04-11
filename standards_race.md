---
title: Open Standards - Race
layout: default
permalink: /standards/race/
tags: standards
---

# Simple Races

A "simple race" is one where a gun goes off, the runners all start at once, and the runners are all in the same competition.  It's our starting point. 

More complex races might include relays, handicaps, and messy scoring situations (e.g a club championship within a wider road race); races with options for 5k and 10k; and on and on. 


What we need to store depends on the context.  There are a few


# Race planning and timing

Here we will have a scheduled time, and a start list, and maybe finish line data.

{% highlight json linenos %}
{
    "id": 123,
    "ot_id": "1e330d72-4130-4996-9f6a-2f8458181f65",
    "name": "Dash for the Splash 10k",
    "match": "e58f579e-a573-4e63-9512-9085bbc1b0fd",
    "slug": "dfts",
    "status": "finished",
    "start_list": [
        {
          "bib": 1,
          "first_name": "Mike",
          "last_name": "Allen",
          "team": "KPMG",
          "category": "M-50+"
        },
        {
          "bib": 2,
          "given_name": "Lucinda",
          "family_name": "Al-Zoghbi",
          "team": "Clapham Pioneers",
          "category": "F-OPEN"
        },
        ...etc...
    ],

    "finish_sequence": [
        {
            "bib": 228,
            "time": "00:20:32"
        },
        {
            "bib": 103,
            "time": "00:20:37"
        },
        {
            "bib": 102,
            "time": "00:20:59"
        },
        ...etc...
    ]
    
}
{% endhighlight %}


| Attribute | Type | Required? | Notes                 |
|-----------|------|-----------|-----------------------|
| pos       | int  | yes       | Finishing position.   |
|           |      |           |                       |
|           |      |           |                       |

id | The system generating the json may use "id" for its own purposes
ot_id | OpenTrack ID for the race.  We will provide a global ID service
match  | An identifier for a larger match or meeting this race is part of. We suggest putting location and descriptive info at Match level
name | Text name for this race
slug | a short code 


## Results for scoring/checking

The detailed results include peoples' numbers, and various points.

There will also be blocks of team results.  I have no idea yet how to classify these but it will involve a bunch of names tables.


## Results for posterity
At this point, when the race is over, nobody cares what number a runner was wearing, or who was in the start list.

The important fields at finisher level are:  position, first name, last name, team/club, time.


## Results for submission to rankings / databases

For submission to results sites (e.g. Power of 10), the key thing is to have clear athlete identification and club/team identification.

We can therefore optionall add a few fields: an agreed identifier for a club, and for an athlete.

{% highlight json linenos %}
    {
            "pos": 1,
            "bib": 228,
            "time": "00:20:32",
            "first_name": "Frederick",
            "last_name": "Fast-Finisher",
            "team": "THH A",
            "club_code": "THH",
            "athlete_id": "EA2772389"
    }
{% endhighlight %}


