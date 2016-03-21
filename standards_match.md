---
title: Open Standards - Match
layout: default
permalink: /standards/match/
tags: standards
---

# Match

A "match" is a collection of races, probably at a single location, on one day or consecutive days. 


```json
  {
      "id": 123,
      "ot_id": "4071eadc-ef82-11e5-9ce9-5e5517507c66",
      "name": "Surry League, Division 2, 3rd round",
      "series": "SURREYLG/DIV2",
      "season": "WIN1516",
      "location": [location_id],
      "host_organisation": "GBR/THH"
      "slug": "dfts",
      "status": "finished"
  }
```

```json
  {
      "id": 123,
      "ot_id": "3377a81c-ef82-11e5-9ce9-5e5517507c66",
      "name": "English Schools Athletics Championships",
      "series": "ENGSCHOOLS",
      "season": "SUM16",
      "slug": "dfts",
      "status": "finished"
  }
```

# Season


```json
  [
    {
        "id": "WIN1516",
        "ot_id": "ea4c2154-ef81-11e5-9ce9-5e5517507c66",
        "name": "Winter 2015/6",
        "start_date": "2015-01-01",
        "end_date": "2016-03-31",
        "slug": "dfts"
    },
    {
        "id": "SUM16",
        "ot_id": "4071fd38-ef82-11e5-9ce9-5e5517507c66",
        "name": "Summer 2016",
        "start_date": "2016-04-01",
        "end_date": "2016-08-31",
        "slug": "dfts"
    },
```

# Series


```json
  {
      "id": "SURREYLG/DIV2",
      "ot_id": "d2f6d7c4-ef81-11e5-9ce9-5e5517507c66",
      "name": "Surrey League, Division 2",
      "competition": "Surrey League",
      "slug": "dfts"
  }
```

# Competition


```json
  {
      "id": SURREYLG,
      "ot_id": "34aaab36-ef81-11e5-9ce9-5e5517507c66",
      "name": "Surrey League",
      "type": "Cross-country",
      "organiser": "SLG",
      "slug": "dfts"
  }
```
