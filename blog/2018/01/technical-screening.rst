Technical Screening
===================

If my experience and observations is any guide, as a programmer,

Interviewing can be likened to a rollercoaster that dunks you underwater and 
drowns you. To take you up relaxingly to see the most beautiful sights, to dunk 
you in again, It's seriously messed. That's my analogy.

And, perhaps, based on what I've seen from other's - they have similar experiences
to report. I see patterns it could more than my own A/B trials of faceplants from
"Juggernauting" into interviews with no idea what their culture is.

There is indictation small businesses and startups with flat organizational 
structures are becoming increasingly bureaucratic.


This strikes me as ironic, since the whole idea of the startup ethos is 
shunning *Dilbert* bozocraft for common sense. Importantly, we at startups
are teams focused intensely on products and users - not things involving
process.

Can you think of any time in recent history, where people have decided to take
culture, or technology, and then tried to draft a specification for who you
should be, how you should talk, act, and the ramifications of it? Did you ever
get the feeling those who wrote it may not be qualified, or even know what
they're talking about to understand the ramifications of enforcing what
they think is necessary?

Well, one of those are job requirements and interviews for programmers.

Because you can't be too cocky or have too many achievements. Never outshine the 
master. (So many VP's viewed my LinkedIn... And I view their profile... You 
begin to develop a feeling of why you're ghosting not *solely* being perceived
as a rabble-rouser)

Yet, you must be competetant, sufficiently, in whatever trivia the screener
may fire off. It's as if interviews are some alternate reality, like our 
trade doesn't involve having StackOverflow opened all day.

Or maybe, the feeling I'm having, could have some grounding in reality at times.


.. note::

   To be fair, before I move on. I'm at fault for screwing up many interviews.
   For my first jobs - while I cared about products and team immensely - I put 
   technical skill at the expense of everything else. I errored greatly. I 
   suffered for it in these past few years (2016/2017).

I'm in a unique position when it comes to technical screenings. There's
clear and unambiguous public evidence that I can program.

Yet, recruiters with no technical ability, and programmers and managers
with less programming experience than me frequently place me into
trivia and codegolf, trying to stump someone who is an expert.

That mindset of knowing beforehand someone can do something, but trying to trick
them, rather than trying in earnest to understand their capabilities and 
qualifications, is a concerning trend in technical screening.

Disclaimer, before I dig in:

1. This is just about *technical screens*. **General interviews are
   fine!**
2. There *are* exceptions to this. But the good companies that have sensible
   tech screenings are too humble to shine and be a beacon for others.
3. Half the time, I'm the one who messes up the interview, not getting
   enough sleep, someone better comes along, or it's just not a fit. So let's 
   set a margin of error.

To begin, don't you think tech screeners look people up first?

They always do. Even when they don't admit it.

Did they take into account my work history? Open source
contributions? Projects? My book? Publicly viewable
updates across my projects? Overall track record?

Are they saying they could be inauthentic?

Are they not enough to substantiate that somebody could work, *immediately*?

If someone can't answer trivia off the top of their head, are we
now to assume they never knew it, or they just didn't recollect it?

If someone demonstrates clear expertise in a specific arena, but hasn't used
exact, cherry-picked libraries out of chance yet, are we to believe they're
*unteachable*? They can't learn it in 5 minutes? A day? A week? Some
workplaces train for months.

Performance issues? In a unique way, they can publicly see I get stuff done, 
and have basically zero downtime.

Fear they can't finish things? I've released 5+ completed open source projects, with
packages, documentation, tests, continuous integration, end-to-end.

If someone can't handle on-demand, randomized programming puzzles under
pressure, does that mean they can't hack? How do they explain all my
open source code? Did a magical elf appear and ask me to do Fibonacci when I
wrote the `WorkspaceBuilder`_ for `tmuxp`_?

What are they trying to prove?

Maybe these kinds of tests are only good for one thing: Finding people who
say the right words, conditioned to do puzzles, even memorize them, to no
demonstrable, beneficial effect. The ability to be obsessed with nonsense.

So you get a person with a useless skill, with a possible inference they'd do
nonsensical things, when ordered, without question. While more and more
finally come to the personal epiphany: *wow, organizations really create 
systems that cargocult waste at scale, like Dilbert*.

That is the exact problem agile / startups tries to solve. We cut the red tape,
leverage cutting-edge frontend frameworks to get to market fast, pull in
permissively licensed libraries from the internet, black swans. That kind of
thing.

But more and more often, startups are cargoculting Dilbert-style bozo
interviews for programmers, too.

(The last time I felt such frustration and tilting was when I played
MoBA's.)

Regardless, senior level employees have more agency, there's no way around it.
Some technical screenings aren't helping find ones that'd actually *help* the
company

.. _WorkspaceBuilder: https://github.com/tmux-python/tmuxp/blob/master/tmuxp/workspacebuilder.py
.. _tmuxp: https://tmuxp.git-pull.com

Let's open up the conversation. Forget open source. Any programmer
with 8+ years of real professional programming. Subjecting a candidate with
seniority to random, non-standardized shotguns of trivia or pressured
refactorings isn't just rude, but fallacious. The cadence of the job is
nothing like that.

And they know it.

In the current situation, both the company *and* the candidate are losing.
Some of us have a sense of pride and care for the company we work for,
and our colleagues, too.

In so many ways, I've seen technical screenings fail to confirm in the
affirmative or the negative I could program or truly perform a role. 

I've been dragged around to places that lack the basal honesty to explain the
role demands flexibility, passion, focus, teamwork, but maybe the skills
*just a touch* more modest than their post's requirements. Maybe it's just
CRUD, ETL, React.js, with some Pandas here and there. Not rewriting language
primitives from the ground up in assembly. Like that.

Even when it comes to basic programming API's and standard libraries, I
don't remember every one, and regularly look up documentation for it.
Even for my own libraries like `libtmux`_. There's too much to remember, and since
there's no standardization across companies of what they ask, it's a shot in
the dark whether I'm going to flunk and casted as a poser.

.. _libtmux: https://libtmux.git-pull.com/en/latest/api.html

For this post, I'm going to give my anecdotes of times I believe screening
itself was at fault for roles I would have been awesome at.

Before I continue, let's leave margin of error for when I come off wrong
and flop interviews, when there's a better choice than me, and so on.
Let's try to dive into some of the chemistry and dynamics of the modern
programmer interview flunking solid prospects, regularly, *at scale*.

Some screenings ask you to do tricks that have no basis or grounding in
*anything*. Questioning or denying the premise can really sour things. So we're
passive and "just deal with it" to not appear as prima donnas.

.. admonition:: Story
   
   An interviewer showed a code snippet of a `Django model`, and wanted
   me to describe the schemas it would create. I correctly explained that
   `ManyToManyField`_ creates an intermediary table to ``JOIN``.
   
   Then, he wrote a `QuerySet`_ and wanted me to write the SQL. *crunch*

   .. _Django model: https://docs.djangoproject.com/en/2.0/topics/db/models/

   Provided I have documentation, I'm able to write my own own SQL queries and
   navigate SQL CLI through the terminal. What did being able to write the exact
   query intend to prove? In my current work, I rarely touch raw SQL unless I
   have a specific need to. In fact, `ORMs are good
   <https://news.ycombinator.com/item?id=14661391>`_.

   I actually ended up getting an offer from this place. They let me
   screenshare and show my code. But I don't know where the trivia came
   from - why being able to craft perfect SQL by hand at parity with an
   ORM mattered. Intuition of JOINs, INDEXs, and when queries are
   cached / rerunning wastefully, paired with profiling, is sufficient.

.. _ManyToManyField: https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.ManyToManyField
.. _QuerySet: https://docs.djangoproject.com/en/2.0/ref/models/querysets/#django.db.models.query.QuerySet

Even when I reach out and ask, it's difficult to get honest answers of what to
expect in a screen. So, when I come in with Language A on my mind,
I get something else. This causes things to fall apart, because being
rusty is going to spoil the interview.

.. admonition:: Story

   One time, I was in an in talks for a Python and Django gig, and
   agreed to be screened. Which is a bit strange for consulting work, at the
   time, I went through with it. I double checked to see what the interview
   would be, and felt OK the person had a process. When I entered the
   interview, I was presented with *JavaScript* and *Underscore.js*.
   Something I haven't touched in 4 years.
   
   Back when I did, it was with successful social media campaigns at Social Amp
   for 1-800-Flowers, Elle, and Marie Claire. But now, with no warning, I'm faced
   with JavaScript as a total surprise when I had Python on my mind. I looked as
   if I couldn't grasp JS.

   Had I have known, I could have studied a few hours the evening before.
   It was clear, this wasn't an active discovery of whether I could perform a
   role. When I told him I haven't seen JS like this in four years, he
   didn't say, "Oh, go back and study this, and come back this evening."
   It was a carnival game of odds and chance.

   The interviewer did one of those things where they put words in your mouth.
   At the very last minute, he asked if I had questions. Since he decided
   to flip the script and do a different programming language, I asked how
   much of this project promised to be in Django was actually JavaScript.

   His answer was something about mathematics. For no reason. I think he was
   unconsciously trying to fabricate that I was concerned about doing algebra
   calculations. But who knows. At that point, you're talking with a
   person who made it pretty apparent they wouldn't be cooperative as a
   colleague.

Claiming screeners deliberately sabotage interviews is enough to question your
sanity. You're kind of on your own.

If onlookers see you upset, they `may misinterpret your irritation afterward to 
be the cause of your problem, rather than a reaction to unfair treatment
<https://en.wikipedia.org/wiki/Fundamental_attribution_error>`_. You
have to adjust your view of the world and people, it's not as just and
meritocratic as you thought it may have been.

You go through a phase of imposter syndrome that lingers for years, because you 
think it's your own limitations or faults. Or you're just "bad". Until you
realize the lengths interviewers go to not hire the person that replaces them.

It's rare. Subject to interpretation. But it happens. Another example of what I 
perceive to be bait and switching and sabotage:

.. admonition:: Story

   I submitted an application for an instructor role at a code camp. I got a
   call from the founder within < 15min. I was told by the CEO in NYC - which
   I had a delightful conversation with - I'd be giving a presentation at
   their Chicago office to *instructors*. And specifically, it should be a
   challenging one intended for the faculty. I took the Metra down there. 

   I opted to go into some of the innards and build system of `tmux`_. This
   fit with me well, since I just got done publishing the first
   edition of `The Tao of tmux`_. I didn't get much sleep the night before,
   but was able to wrap up some of the slides when I arrived at the incubator.

   .. _tmux: https://en.wikipedia.org/wiki/Tmux

   I am ushered in, prepared to give my speech, to first see a group of
   5-10 students. OK, so where's the empty room so I can get plugged in
   before the faculty arrives? Then, through one more door. I see a huge
   class, 6+ rows deep, with 20, maybe even 30 students. My heart sank.

   I'm directed to a podium.

   Some people would have just walked out of there. If it were me doing
   it again, I would have. While I ended up giving a good speech, the
   student's expressions were... bewildered to say the least. They found it
   too sophisticated and not web development related.

   After that, I'm put into a conversation with an instructor that's
   very junior to me. While he was impressed by my technical background
   and didn't require screening me (I was promised I'd be able to show some
   of my open source code off, I love doing that). He keeps asking me about
   my teaching experience.

   I do have teaching experience. I've taught people at work. I'm a former
   Google Summer of Code mentor. I give support in open source. I have
   great intuition for this. I talk about the whole open source way of
   how we learn, get mentored, then assume core roles.

   The person refused to accept my answers. He read my resume and understood
   beforehand I was never a literal professor. Nor was he before this, and he
   was a junior programmer, what's he doing teaching people anyway? He
   doesn't have any accomplishments. The students are paying $15k+ per
   seat.

   I leave, and the words the instructor mumbles is something about my
   "philosophy". Ugh, what? I wasn't egging on, I just candidly
   answered questions. That's when I perceived they were portraying me a
   certain way and trying to hold on to their job.

   .. _The Tao of tmux: https://leanpub.com/the-tao-of-tmux

Who hasn't encountered a non-techie who thought they knew tech better than
them? Sometimes they may even fib they've done it before, and proceed to 
"weed out a poser candidate":

.. admonition:: Story

   I walk in to my first startup in the suburbs, cool. The first
   interviewer that comes is very chill. He even admits to me he looked
   me up beforehand. I show him `unihan-etl
   <https://unihan-etl.git-pull.com/>`_ which clearly leaves him
   impressed about my experience working with complex data being
   readily available.

   It's the first time an interviewer ever let me demo my open source projects, 
   and at that point, he said I was senior, and had no interest in technical 
   screening trivia. One of the things that made me believe he was credible was 
   his vulnerability. He talked about his past working at a cell phone company, 
   not being able to do open source, and also that the job was there to support 
   him.

   Eventually, he leaves, and a new person comes in. A CPO.

   He shuffles in with his open laptop, clasped between his palm and thumbs;
   a big smirk on his face. He claims before he worked these various
   non-tech jobs, *he himself was a programmer*. And begins directing the
   conversations more and more into trivia. I make broad statements about
   concurrency vs parallelism, and am honest if what I've done and haven't
   done before.

   When I mention my projects and evidence that I have a track record
   in Python, he ignores it, and proceeds with questions.

   As of February 2018, I've never used `multiprocessing`_, `threading`_, or
   `concurrent.futures`_. Now, if I were to try these, would I be good at
   them?  If my track record with Python was any guess - probably. But I
   haven't had the need to use them in the course of my natural duties.

   I was expecting the founder would come in and talk to me. But you
   could see the CPO type 3 keys. He has some sort of interactivity
   happening on that screen. We shake hands, and I leave. Not seeing
   the CEO? He didn't come in? (I know their faces from LinkedIn)  

   And I am left walking out, right past the CEO as he forcefully stares down
   at his phone as if I'm not there. Awkward.

   I looked up the CPO once more, and see no hint he ever did
   programming or Python. And don't know why any so-called programmer
   wouldn't just look up the documentation. 

   I find this style of interview extremely weasley and a bit creepy. Before
   I answered any questions, he introduced himself with a lie. And chatted with 
   people out of my sight, without telling me. Here I am, thinking you're 
   looking at my portfolio and abilities in earnest. And all the while, this 
   covert judging is taking place. Possibly under faulty premises; which is... 
   Kafkaesque? I never realize it at the time, only in hindsight.

For two remaining cases, there would be a programmer interviewing.

An interviewer may project what *they* feel any programmer worth their salt
would know. For instance, for me to write an ETL script (which I do well), but
then asking me to optimize it, when I see no route to do so at the moment. I
gently say  I can't. Then they continue to lean in. *crunch*

Web development roles for Django, Laravel, and Rails that insist on doing data
structures and algorithms. Unless you're specifically planning on scaling data
into terabytes or petabytes, or receiving millions of connections, or some
mix of that. Here's why that doesn't work:

1. Data structures and algorithms are cargo-culted as a way to "prove" a
   programmer has deep understanding of CS concepts.
   
   But, they can be memorized without internalizing them. This creates false 
   positives.

   The test is kind of useless at this point.

   Further analysis finds someone can have lookup times, reads, writes, types of
   searches internalized, but not be able to perform a test on command like a
   fresh graduate would. This creates false negatives.

   At this point, it's considered harmful.

2. Many startups are naive and grandiose about scaling

   This is why it's important for founders to lend their ear to senior
   programmers.
   
   You can be a successful and profitable business, like McDonalds, but they're 
   not going to fluctuate between 0 and one billion restaurants every
   millisecond. Things are predictable and stable enough to where you can 
   partition and introduce constraints pragmatically. Similar to the way 
   their corporate  management structure works - country, region, so on.
   
   There's no need to start with a blank canvas and assemble things in 1's
   and 0's. The intuition of most programmers is to break big chunks of data up, 
   cache, and profile, is satisfactory.

   Get it? There are various reasons why this stuff isn't communicated, but if 
   you don't need something - trying to play a prophet is just as bad as 
   premature opimization sometimes. You don't even have information on the ground
   to understand your own problem, but you want to bring the scaling squad
   into every front on the line of battle, until you're spread thin
   supplying non-existant fronts. You don't have enough substance to justify it.
   Sorry, but it's true. You need infantry (full stack devs / generalists)
   for most stuff so you can actually have a product and users first.

   Even businesses that requires this kind of scaling only need it in narrow 
   aspects of their applications. Not every role requires going back to basics 
   and giving asymptotic level of care, ever, period.

The runaway fascination with scaling and unchecked buzzwords appears to have 
created a marketplace for purely hypothetical job requirements, to match their 
mistaken conceptualization of how scaling works. Stuff like:
   
You must have direct experience with Spark and Hadoop - it doesn't matter if you
have 10 years programming experience and have solved data problems before.
You must talk and act in a certain way - vague and obscure enough to hide
it's all just ETL, yet scholarly and esteemed enough for it to be rude to
press for explanations. Keywords for ML/AI/Big data must be peppered on 
resume, alongside a PhD, in order to be fully qualified under the laws of
Physics as a data scientist and start a Jupyter notebook.

Most business problems aren't asymptotic - bound to infinity. The
applicant can decide to correct the interviewer (ending the hiring process, 
Never Outshine the Master), or be taken as an offense to infer the company 
"won't scale" (be successful). Or, the applicant could go along with it when 
they're not fresh on the subject. Being subjected to this wears many people out.

Some hiring managers proclaim they want the best skill and talent, but in the
end, are scared of trusting experts. Or thanks to Dunning-Kruger, think they can
get around it.

Would you "test" your doctor by giving them trivia? You could probably throw
them off on a definition; embarrass them. They're not there to be play
*Jeopardy!* on-demand. They studied the material for years, been immersed in 
the field long  enough to have *experience*. They can make educated decisions 
and analyze, synthesize information, help treat a problem, or defer to someone else.

When dealing with experts, you trust them in good faith, and put your best
foot forward with them. If it doesn't work out, you find a second opinion.

It's all about mindset. Screening today is about stumping applicants, rather
than an earnest effort to see if someone understands something, or could
learn it on the job if accommodated. That means any evidence the applicant has
experience with something in the past has to be weighed. If a test is done, it 
has to have an articulable reason and the applicant should know beforehand.

Instead, the screening process actively ignores evidence of aptitude that
doesn't follow the prescribed testing style used by the company at the
time. That is something that can be performed by a non-programmer against a pool
of thousands, ensuring false negatives.

This, coupled with interviewers ghosting and misrepresenting requirements
for the job, shows a lack of respect for the candidate's time. But if my 
anecdotes and Glassdoor are anything to go by: they don't care much about
candidate's feelings either.

Screening can work both ways - because that's the kind colleague that'd be
passive aggressive, or a boss or organization that'd terminate you at-will on a
whim, burn every bridge, only to have the business tank due to engineering waste
and ineptness. Bad bosses are highly dangerous.

When you're an expert and the boss doesn't let you assume that position,
you can't work with them. By extension, *they* may not be able to work with
talent that'd *help* the company. The course of the company turns to
devaluing tech, instead hiring middle manager bozos that worship the
ground they walk on, never giving sound technical advice, nor acting contrarian.

A solid way to hold power, but not a good way to build a competitive business in
tech, where the mantra is clear: innovate, adapt/pivot, or perish.

Parting observations on technical screens:

- current system has no respect for seniority
- no standardized test(s)
- there's no indication technical screening determines excellent
  candidates for a role to be people who fail the screen
- there's no proof of what technical screening even proves
- workplaces are looking for hypothetical skills for a role instead of what's
  needed on the job
- are subject to cargoculting by organizations without a care for
  pragmatism
- if the interviewer is more junior, they may project their
  own knowledge, often of what is fresh on *their* mind
- it's on the spot,  under pressure, and random, which is not like the
  job, and
- contrary to the opinion of many, if I am any example, open source isn't enough
  evidence for interviews at most places

Improving

A lot of the ideas require effort on part of employers that are 
interviewing to *themselves* be more honest, ethical, professional,
and put more active thought into their process and candidate's time.

For example, teams could explain candidly what the daily course of duty is,
instead of fantasizing hypotheticals of an ideal candidate materializing and
"scaling" with the latest buzzword(s). You're probably turning down 10-100
candidates that'd fulfill the role excellently, and end up hiring a streetwise
careerist/bozo who's a professional interviewer, not someone who can hack.

Another example: If the organization values software developers enough, have
senior engineers (not managers) fill in as recruiters for programmer roles. 
They're not going to hang the process on a gimmick or trick, but probe and give
the applicant a chance to fill in the blank if they know something, or could
learn it. This avoids false negatives.

I am going to be stern on this: as of 2018, there's *zero* respect for
programmers in interviews. Companies aren't helping us help them. To me,
programming is an honorable trade, and the duties need to be recognized for how
challenging they are, and the career path deserves more dignity and respect than
it's currently getting.

.. _concurrent.futures: https://docs.python.org/3/library/concurrent.futures.html
.. _multiprocessing: https://docs.python.org/3/library/multiprocessing.html
.. _threading: https://docs.python.org/3/library/threading.html
