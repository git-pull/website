Technical Screening
===================

I'm in a unique position when it comes to technical screenings. There's
clear and unambiguous public evidence that I can program.

Yet, recruiters with no technical ability, and programmers and managers
with less programming experience than me frequently try to drag me into
trivia and golf, acting like they can stump someone who is an expert.

That mindset, of knowing before hand someone can probably do something,
but trying to trick them, is what technical screening has devolved to.

Two initial points before I dig in:

1. There *are* exceptions to this. But the good companies that have sensible
   tech screenings *are too humble* to shine and be a beacon for others.
2. Half of the time, I'm the one who messes up the interview, not getting
   enough sleep, someone better comes along, it's just not a fit. So let's set 
   a margin of error.

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

.. _WorkspaceBuilder: https://github.com/tony/tmuxp/blob/master/tmuxp/workspacebuilder.py
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
affirmative or the negative I could program or truly perform a role. I've
been dragged around to places that lack the basal honesty to explain the
role demands flexibility, passion, focus, teamwork, but maybe the skills
*just a touch* more modest than their post's requirements. Maybe it's just
CRUD, ETL, React.js, with some Pandas here and there. Not rewriting language
primitives from the ground up in assembly. That kinda thing.

Sometimes, I'm flunked based on stuff I've done before, but haven't practiced
in ages, or that's researchable and I'd be good at. It's safe to say, that
effects how competetent you come off as.

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

Some screenings even go so far as to ask you to do tricks that have no basis or
grounding in *anything*, and can cause serious friction with the
interviewer when you accidentally, reflexively, yet gently question or
deny the premise:

.. admonition:: Story
   
   An interviewer wrote an ORM snippet of models from Django, and wanted
   me to describe the schemas it would create. I correctly explained that
   `ManyToManyField`_ creates an intermediary table to ``JOIN``. Then, he
   wrote a `QuerySet`_ and wanted me to exactly write the SQL. *crunch*

   I'm fully capable to writing my own SQL Queries / navigating SQL CLI in
   the terminal *provided I have documentation*. But, what did me being able to
   write the exact query intend to prove? In my current work, I rarely touch raw
   SQL unless I have a specific need to. In fact, `ORMs are good
   <https://news.ycombinator.com/item?id=14661391>`_.

   I actually ended up getting an offer from this place. They let me
   screenshare and show my code. But I don't know where the trivia came
   from, and why specifically being able to write SQL at a parity of an
   ORM mattered. A mental mapping of JOINs, INDEXs, when queries are
   cached / rerunning wastefully, and profiling is sufficient.

.. _ManyToManyField: https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.ManyToManyField
.. _QuerySet: https://docs.djangoproject.com/en/2.0/ref/models/querysets/#django.db.models.query.QuerySet

The other is, most technical interviews never let me know what
specifically is being tested. So, when I come in with Language A on my mind,
I get something else, I come off as rusty. Which makes me look like far
weaker of a horse than I am.

.. admonition:: Story

   One time, I was in an in talks for a Python and Django gig, and
   agreed to be screened. Which is a bit strange for consulting work, at the
   time, I went through with it. I double checked to see what the interview
   would be, and felt OK the person had a process. When I entered the
   interview, I was presented with *JavaScript* and *Underscore.js*.
   Something I have programmed in 4 or so years. Of course, even though I did
   social media campaigns at Social Amp for 1-800-Flowers, Elle, and Marie
   Claire, I looked as if I couldn't grasp JS. I hadn't touched a real JS
   script handling data in that long of a time, and I was expecting Python.

   Interviewers, when they protect their job, can get cringely Machiavellian and
   desperate. I've had them outright put words in my mouth. This interviewer,
   when I asked how much of the code is in Python vs JavaScript (since he
   decided to flip the script and do a different programming language), began
   talking about mathematics, for no reason. Likely to fabricate an excuse that
   I was concerned about doing algebra. But who knows, it could be unconscious on
   his part.

So to take that last part further: The other thing is, sometimes you'll get
cringy interviews of two types:

1. Bait and switch. Sabotaging.

   The thing with claiming someone deliberately sabotages your interview
   is enough have you question your mental health. Seriously, because you think
   it's your own lackings and faults. You go through a phase of imposter
   syndrome that lingers for years until you realize the lengths people go to
   not hire the person that replaces them.

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

      Fantastic. I can officially add public humiliation to my list of
      disrespect. Which actually sets me apart from the general disrespect
      programmers get at-large when interviewing! Can I apply for a special
      discount on my Spotify/Netflix subscription now?

      After that, I'm put into a conversation with an instructor that's
      very junior to me. While he was impressed by my technical background
      and didn't require screening me (I was expected to show some of my
      open source code off, I love doing that). He keeps asking me about my
      teaching experience.

      I do have teaching experience. I teach people at work. I'm a former
      Google Summer of Code mentor. I give support in open source. I have
      great intuition for this. I talk about the whole open source way of
      how we learn, get mentored, then assume core roles.

      The person refused to accept the answers. He read my resume, and understood
      *literal* teacher. And he wasn't either, and he was a junior programmer,
      what is he doing teaching people anyway? He doesn't have any
      accomplishments. Turf protection.

      I leave, and the words the instructor mumbles is something about my
      "philosophy". Ugh, what? I wasn't egging on, I just candidly
      answered questions. That's when I perceived they were portraying me a
      certain way and trying to hold on to their job.

      .. _The Tao of tmux: https://leanpub.com/the-tao-of-tmux

2. The interviewer isn't a techie, but tries to play like they know better
   as they're own way to "weed out a poser candidate".

   .. admonition:: Story

      I walk in to my first startup in the suburbs, cool. The first
      interviewer that comes is very chill. He even admits to me he looked
      me up before hand. I show him `unihan-etl
      <https://unihan-etl.git-pull.com/>`_ which clearly leaves him
      impressed about my experience working with complex data being
      readily available.

      The other thing is, it's the first time an interviewer ever let me
      demo my open source projects, and at that point, he said I was
      senior, and had no interest in technical screening trivia. One of
      the things that made me believe he was credible was his
      vulnerability. He talked about his past working at a cell phone
      company, not being able to do open source, and also that the job was
      there to support him.

      Eventually, he leaves, and a new person comes in. A CPO.

      He shuffles in with his open laptop, clasped between his palm and thumbs;
      a big smirk on his face. He claims before he worked these various
      non-tech jobs, *he himself was a programmer*. And begins directing the
      conversations more and more into trivia. I make broad statements about
      concurrency vs parallelism, and am honest if what I've done and haven't
      done before.

      When I mention my projects and evidence that I have a track record
      in Python, he ignores it, and proceeds with questions.

      As of Feburary 2018, I've never used `multiprocessing`_, `threading`_, or
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

      I find this style of interview extremely weasley and a bit creepy. You're
      chatting with people out of my sight, without telling me. Here I am,
      thinking you're looking at my portfolio and abilities in earnest. And all the
      while, this covert judging is taking place. Possibly under faulty
      premises; which is... Kafkaesque? I never realize it at the time, only in
      hindsight.

So consider that last camp, there's also a group of people who don't want
to trust experts. Would you start giving trivia to your doctor? I
bet you could probably throw them off on a definition, but you'd probably
tick them off. They're not there to be play Jeopardy! on demand - they're
experts. We know they studied the material for years, that they've been immersed
in the field long enough to have *experience* to make educated decisions and
analyze, synthesize information, and help treat / defer to someone else in a
variety of situations.

The other thing is, sometimes the interviewer is projecting what *they*
feel any programmer worth their salt would know. For instance, for me to
write an ETL script (which I do well), but then asking me to optimize it,
when I see no route to do so at the moment. I gently say  I can't. Then they
continue to lean in. *crunch*

There's also a kind that's looking around for Django, Laravel, Rails, and
so on developers that insist on doing data structures and algorithms. I
can't explain why, because in all these years, it hasn't come up once at
work. *Unless you're specifically working on a large data set, the problem
isn't asymptotic - bound to infinity.* So, this puts me in a position where
I could be an expert and correct the interviewer (which ends the
interview, Never Outshine the Master), or I have to go along with it when
I'm not fresh on the subject.

It's all about mindset. Screening today, is about stumping applicants, rather
than an earnest effort to see if someone understands something. That means
any evidence the applicant has experience with something in the past has
to be weighed. If a test is done, it has to have an articulable reason and
the applicant should know before hand.

Instead, the screening process actively ignores evidence of aptitude that
doesn't follow the prescribed testing style used by the company at the
time.

This, coupled with interviewers ghosting and misrepresenting requirements
for the job, shows a lack of respect for the candidate's time. But if my 
anecdotes and Glassdoor are anything to go by: they don't care much about
candidate's feelings either.

Screening can work both ways - because that's the kind colleague that'd be
passive aggressive, or a boss or organization that'd terminate you at-will on a
whim, burn every bridge, only to have the business tank due to engineering waste
and ineptness. Bad bosses are about as plentiful as bad employees.

When you're an expert and the boss doesn't let you assume that position,
you can't work with them. By extension, *they* may not be able to work with
talent that'd *help* the company. The course of the company turns to
devaluing tech, instead hiring middle manager bozos that worship the
ground they walk on, never giving sound technical advice, nor acting contrarian.

A solid way to hold power, but not a good way to build a competitive business in
tech, where the mantra is clear: innovate, adapt/pivot, or perish.

Parting observations:

- the current system has no respect for seniority
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
  evidence for interviews

Ideas for improving?

I do have ideas, but a lot of them require effort on part of employers
that are interviewing to *themselves* be more honest, ethical, professional,
and put more active thought into their process and candidate's time.

For example, teams could explain candidly what the daily course of duty is,
instead of fantasizing hypotheticals of an ideal candidate materializing and
"scaling" with the latest buzzword(s). You're probably turning down 10-100
candidates that'd fulfill the role excellently, and end up hiring a streetwise
careerist/bozo who's a professional interviewer, not someone who can hack.

Another example: If the organization values software developers enough, have
senior engineers (not managers) be recruiters for programmers. They're not
going to hang the process on a gimmick or trick, but probe and give the
applicant a chance to fill in the blank if they know something, or could
learn it. This avoids false negatives.

I am going to be stern on this - as of 2018, there's *zero* respect for
programmers in interviews. Companies aren't helping us help them. To me,
programming is an honorable trade, and the duties need to be recognized for how
challenging they are, and the career path deserves more dignity and respect than
it's currently getting.

Outsiders truly underestimate the rigors of this trade. I think this is
true for any trade. We make it look easy. We take these photos at work of us
smiling at these startups like we're in paradise. Are we really happy
inside? Or are we really hurting ourselves by our values conflicting with what's
really happening. When we create false social proofs of success and
survivorship bias, it cheapens the trade. It's psychologically unhealthy. It
gets us further away from righting the course of things - and getting back to
hacking.

.. _concurrent.futures: https://docs.python.org/3/library/concurrent.futures.html
.. _multiprocessing: https://docs.python.org/3/library/multiprocessing.html
.. _threading: https://docs.python.org/3/library/threading.html
