title = 'Hello EBI/ARISE'
week = 1
year = 2023
month = 1
day = 20
tags = 'starting, new desk, month_one'
===
I started the ARISE fellowship, which runs for three years on the 16th January 2023. I'm now on the Wellcome Genome Campus in the European Bioinformatics Institute, with OpenTargets as my host group and an association with the PDB in Europe group. Having been a remote worker for much of the pandemic, having a desk and being with colleagues is lovely. It's even more wonderful to be back amongst scientists for the whole week after working as an independent researcher for the last year and a half and working in the technology sector before that.

As I'm always keen to start at ["the B of the bang"](https://en.wikipedia.org/wiki/Linford_Christie) and ARISE is a continuation and scale-up of the work already performed, I've set myself some tasks for between meetings. 

The first one is around weeknotes, both building the small software feature to display them and the practice of writing them. 

The software feature is being used to test a way of developing microservices and having them be part of an overarching product. As with the structures part of the website, the weeknotes feature will be developed in [Flask](https://flask.palletsprojects.com/)/[Zappa](https://github.com/zappa/Zappa) and deployed as an [AWS Lambda](https://aws.amazon.com/lambda/) function. However, to keep with the principle of ["small pieces, loosely joined"](https://www.smallpieces.com/) new sections of the overall product will be individual microservices which are then composited using [API Gateway](https://aws.amazon.com/api-gateway/). Search will be the next feature to get some upgrades and to become a microservice. 

The practice of writing them will be inspired by a couple of pieces of current reading:

- [Joe Roberson](https://twitter.com/workingwithjoe)'s [excellent guide](https://medium.com/wethecatalysts/weeknotes-how-to-write-one-in-30-minutes-ef3eef0e41f7) on how to write weeknotes in 30 minutes.
- [Giles Turnbull](https://twitter.com/gilest)'s very readable and incredibly insightful [The agile comms handbook](https://agilecommshandbook.com/)

Hopefully, the weeknotes will be of use to others. At the very least they will be a way of lightweight continuous reporting and reminding me of what was done when (in terms of features, experiments will obviously be in the lab notebook).

Finally, a meeting with Sameer from PDB in Europe made me think again about the need for a PID (Project Initiation Document) template which captures user-centricity and existing knowledge better and is more agile than waterfall. So that will be a task for next week.