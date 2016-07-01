---
layout: post
title: FIWARE Orion
author: Andy Robinson
---

FIWARE's Orion Context Broker has grown to be a key part of our architecture.  Since we're trying to encourage open source developers to collaborate with OpenTrack, I'm going to try and explain what it is, why we chose it, and what it can do.

# What is FIWARE?

FIWARE is a large European Union-funded project to enable new technologies through cloud computing.  It has invented its own jargon which is very confusing to outsiders. 

Several years ago, they surveyed and tried to find technical gaps and to work out what sort of services would be needed to enable and accelerate economic growth.  Several years R&amp;D followed. In the last 2 years, hundreds of small businesses have received funding to launch innovative ideas, but only if they use FIWARE technology and/or Open Data.  We are one of them.

Here's the intro paragraph from the documentation.  Once you get into the details, it's excellent - correct and comprhenesive with good getting-started guides - but in my opinion, it gives an average developer NO CLUE what it's there for.  What do you think?

<blockquote>
<p>Orion is a C++ implementation of the NGSI9/10 REST API binding developed as a part of the FIWARE platform.</p>

<p>Orion Context Broker allows you to manage all the whole lifecycle of context information including updates, queries, registrations and subscriptions. Using the Orion Context Broker, you are able to register context elements and manage them through updates and queries. In addition, you can subscribe to context information so when some condition occurs (e.g. a context element has changed) you receive a notification. These usage scenarios and the Orion Context Broker features are described in this document.
</p>

    
</blockquote>
