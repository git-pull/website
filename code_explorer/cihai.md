---
orphan: true

---

(cihai)=

# Cihai: China in a python package

Have you ever downloaded a foreign song and saw garbled junk?

Have you ever noticed that Chinese websites, even with english characters,
have a different looking font?

The world around revolves around codecs. Chinese is a huge language on the
internet. Python is a major implementation on computer systems world wide
and in Asia.

The current problem, underneath it all, programmers lack the tools to
handle codec issues.

The results of poor software bubble up in pesky places. Software crashes,
general slowdowns. Individual programmers and teams of programmers
delivering software in a specific codec, when they otherwise 1.) may be
ignorant of the advantages unicode holds for them 2.) may not have the
time and risks to do that for themselves.

Cihai is not a magic bullet, it doesn't translate Chinese to English, it
doesn't migrate a GBK encoded application to unicode, but finally a
utility library that fills the gap. It fixes a pain point.

It further helps us move forward to Python 3 - the next iteration of
python that uses Unicode as a default, but it not default on production
systems yet.

[1] How does Cihai help that?

The hard truth is: The world moves faster when we move to Unicode and the
old codecs are an afterthought.

- With codec issues being a realm of confusion, ambiguity, there isn't
  enough time for programmers in developing counries to focus on it.
- Python 2.x had an issue with handing strings. See:
  <https://www.youtube.com/watch?v=sgHbC6udIqc>

This issue affects people on the web. This issue affects software.

This issue affects the productivity and technical mechanics behind all
countries utilizing the Chinese language. Python may be used as a utility
script to release firmware.

The direction we're heading:

- The migration to python 3 is a world shift. Unicode is becoming a front
  stage standard.

What Cihai is:

What Cihai covers:

- It solves smooths out technical bottlenecks prohibiting python based
  projects from localizing.
- This library could be useful for non-python projects in other
  programming languages. Python is already proven as a utility language.

What would help this effort:

- Funding for me to program this.
- Legal help regarding IP of source works and data sets.

The areas that can be affected, applications:

Directly:

Down the road:

- Better documentation for Chinese software

Niches that Cihai does cover:

- Traditional Chinese Characters - Used in Taiwan and Hong Kong
- Chinese codecs - There are many codecs for Chinese Text across asia.

What Cihai does not cover:

- Cihai is not translation of Chinese to english. This is a deeper
  linguistic issue.

Could it be used as a tool to help these potentially? YES! This is a
clean abstraction of the official Unihan release by Unicode, Inc.

Background research on current means of

- Python's popularity
- Python in china
- internet usage in china

In tiny ways we may not suspect.

Clarifying Chinese unicode is a step forward in itself.

Bringing the python, the world's system utility language closer to us, is
akin to dispersing a heuristic that can benefit the many.

[1] How does Cihai help the migration from python 2.x to python 3?

Python 2.7 is a realm of ambiguity that many python developers are stuck
with. They can't articulate a problem they can't describe. A language
brought upon the philosophy "Explicit is better than implicit"
automatically picks codecs when a developer may not want to.
<https://www.youtube.com/watch?v=sgHbC6udIqc>

[2] Are there already tools that help?

Yes, and they are sorely outdated. I founded this project because cjklib,
a tool famous abstracting the chinese language has grown old, the lead
maintainer does not have the time to fix things in it.

There are smaller projects that look promising, non of which cover the
breadth and depth cjklib did.

[3] How can Cihai, a python program, be potentially helpful on the
firmware of my coffee machine?

This sounds like a stretch, since firmware isn't programmed in python, but
python is a system tool and a utility language. It is used in the ongoing
development, maintenance and QA of a project and service.

Who hasn't bought an item that says "Made in China" before. The firmware
of the application may have been built in China also.

[4] Isn't there already tools *inside* python for decoding and encoding?

Yes, and it *could* be easy as: `'thisstring'.decode('gb2312')`, but
real life is complicated. First please see [1], the bottleneck with
unicode is based off systems around the world using python 2.7, which has
a confusing way of handling encoding and decoding.

Real life is complicated because opening *ANY* data could be *ANY codec*:

- we open a file and the codec of the page may
- we rows from a database (note that mysql allows fields to have their own
  encoding in ADDITION to types like integer, VARCHAR [alphanumerics,
  spaces, symbols]. etc.
- we open a webpage.
- we GET a website sent to us.

First, any of the following systems often send us back metadata, or have a
line that lets us know what the encoding is:

- !#!encoding: lala !-
- DESCRIBE table
- <meta-encoding thistype>
- server headers

but for various reasons, in addition, we may not get any encoding
returned. The software has to assume.

This is another realm of ambiguity and a different conversation, but check
out chardet. Guessing encoding is not perfect, but there are odds of it
being correct.


