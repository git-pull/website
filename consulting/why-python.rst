:orphan:

Why Python? (draft)
===================

:doc:`About <./index>` |
:doc:`Stripe Integration <./stripe-integration>` | 
Why Python? |
`Contact`_

.. _Contact: https://goo.gl/forms/K1uwUVIWOBX589Ip1

.. image:: img/python.png
   :align: right
   :width: 200

.. note::
   
   This is a draft and not completed yet.
   
   Wording needs to be improved, technical things have to be double checked, and 
   statements have yet to be cited.

I'm a polyglot. I have contributed to a variety of open source projects in
everything from Ruby to C++. I fully believe I'd be competent regardless
of programming language. However, my proficiency in Python is considerable.

I had conversations with a few founders looking for work in software stacks 
outside my core competency. Ultimately, I come to the conclusion I may not
be the best pick at the time because there's no advantage to me over
another programmer if you're not using Python. I'm just going to be
average.

I don't want to put you in a position where I'm not giving you my best.
You deserve no less. Especially when time is of the essence.

It's really good over here in Python land. Reaping these benefits of the toolchain
and well-documented, permissively licensed libraries. I'm wondering why you're 
not joining the party.

Who are you to say this?
------------------------

I am a prominent Python programmer. I've released multiple end-to-end 
Python projects. Some have large userbases, even distributed on major Linux
distributions. I stand by my track record.

In my past startups, I didn't have the power to override and enforce safer 
solutions that could have led the business to a better outcome. I've also
tried various combinations of software stacks, and learn how important
it is to stick to safe, effective technologies.

I don't refuse work solely based on me not liking a programming language.
If I'm not programming Python, I'm concerned I won't meet your expectations.
That would not only make me feel bad, but worse, it could end up being
non-optimal to your objectives.

I don't know your stack, and can't judge it. But since Python suits so many 
generalist cases, I want to take this chance to convey some information on why 
I think Python is best.

Why you should move to Python
-----------------------------

I think Python is best for server, data, and script code. I think it's
overall the best programming language for startups:

Performance
"""""""""""

- Python has libraries that leverage C speedups.
- Python has C API's baked into its main implementation
- Python has C

Web frameworks
""""""""""""""

- Flask is top tier microframework

Databases
"""""""""

- Solid abstraction layer, Database API
- Solid drivers (for the abstraction layer): psycopg2
- Solid ORM's: SQLAlchemy, Django ORM, Peewee ORM

Template engines
""""""""""""""""

- Django Templates
- Jinja 2

Maturity
""""""""

- Python is older than Java
- Python 3 has been around since
- 

Prominence
""""""""""

- Google's first search. YouTube.com uses it.
- Linux's package managers use it

Talent pool
"""""""""""

- According to Stack Overflow, it's one of the most popular languages
- Second most highly sought programming language according in demand [#]_

.. [#] Misirlakis, Speros. (2017, December 13). *The 7 Most In-Demand Programming Languages of 2018* [Blog post]. Compiled from
   Indeed.com. Retrieved from http://www.codingdojo.com/blog/7-most-in-demand-programming-languages-of-2018/ 

Node.js vs Python
-----------------

One language to rule them all.

A huge amount of Node's ecosystem gets a boost from being non-blocking.
This is highly efficient.

It handles the server side / backend / scripting, and the browser side JS
and frameworks (React, Vue.js, Knockout)

JavaScript is one of the most widely discussed programming languages [#]_

JavaScript has many uses. It's also used in the browser. It's used in
abstractions like PostgresSQL's `plv8`_.

`npm`_, provides a sensible, easy, default package manager. Want super
speeds? Try `yarn`_.

*package.json* + *./node_modules* is a simple layout for handling project
resources.

BBC, LinkedIn, and USA Today use it.

Pain points
"""""""""""

.. note::

   These are my opinions from using Node.js extensively. I still use
   and enjoy Node.

Node.js is cumbersome from scripts that don't absolutely need to be
non-blocking.

In more than half of my programming code, the boost from it being
asynchronous is negligible. Not work the headaches controlling flow
in Node introduces.

Technically speaking, well written code will be throwing around a lot
of *pure* functions. The issue is, the notion of this gets skewed
in practice: objects, promises, and asynchronous functions are
being thrown around.

- It's harder to understand, write, test and debug code in Node's callback

  That's a pretty big indictment. But when you're writing a lot of code in
  this way, and not getting a proportional benefit in return, it has been
  mind numbing for me.

  Many people are apparently fine with it. There is are endless droves of
  happy node.js developers writing massive codebases. But for me,
  headaches it caused me really impacted me delivering product goals, and
  my overall feeling of writing clean, maintainable code.
  
  How do you know the type of object being thrown around?
  
  In Ruby and Python, you don't know either, but if you're passing in a
  promise, do you consider that pure?
  
  If you're passing in a specialized context object literal, how do you
  type check it?
  
  How easy is it to test and mock the response, at scale?

- Things are Async by default, when you don't benefit from it

  Java is a fantastic programming language. People sometimes get irked by the 
  amount of bureaucratic boilerplate involved.

  Node.js runs JavaScript code in an Event Loop [#]_. This style of
  programming makes scaling I/O nearly a feature of the language, and it's
  therefore a convention that Node code adopt a callback pattern [#]_.

  In most of my scripting, I found I missed Ruby and Python's succinct
  blocking, synchronous code. It's clearer and more concise.

.. [#] 2017. *Stack Overflow 2017 Developer Survey - Most Popular Technologies*
   Retrieved from https://insights.stackoverflow.com/survey/2017#technology
.. [#] *Overview of Blocking vs Non-Blocking*
   Retrieved from https://nodejs.org/en/docs/guides/blocking-vs-non-blocking/
.. [#] *Don't Block the Event Loop (or the Worker Pool)*.
   Retrieved from https://nodejs.org/en/docs/guides/dont-block-the-event-loop/

.. _plv8: https://github.com/plv8/plv8
.. _npm: https://www.npmjs.com/
.. _yarn: https://yarnpkg.com/

Ruby vs Python
--------------

Ruby is another in-demand language.

To many, it's considered the most delightful to program. I agree.

The community is brilliant. And joyous.

GitHub uses it.

Rails, one of the most legendary web frameworks uses it. Rails in itself
is the prime reason most people begin Ruby - not the other way around.

PHP vs Python
-------------

PHP's legacy is in web development. Many programmers (myself included)
were web developers using PHP in the early days, but migrated to different
programming languages.

Even then, PHP is still a force to be reckoned with.

Facebook was built on PHP. And still uses it.

Laravel, perhaps the most elite of all web frameworks, is in PHP. This in
itself is enough a reason to use PHP for many. They like Laravel that
much.

WordPress - the world's most popular and legendary blog platform, is PHP.

Drupal, a super powerful CMS with a brilliant extension community, is also
PHP.

Why I stick to Python
---------------------

You'll notice above, I have experience with all these languages. I also
actually enjoy Ruby, Node.js, and PHP. So why such a fuss?

Spreading oneself too thin
""""""""""""""""""""""""""

Each language has its own tooling, libraries, and so on to handle the same
situations.

In some of those languages, there might not even be a library, so you
could be stuck reinventing the wheel [#]_.

.. [#] Barrow, Lionel (2013, March 7) *Gotchas, Irritants, and Warts in Go Web Development* [Blog post].
   Retrieved from https://www.braintreepayments.com/blog/gotchas-irritants-and-warts-in-go-web-development/

Switching cost
""""""""""""""

For you: Depending on where you're at, you may not be able to pick a new
software stack.

For me: I would have to factor in extra time and cost into getting up to
speed with the language and libraries, in addition to your codebase and
startup.

Opportunity cost
""""""""""""""""

I'm more productive and efficient in Python. There are more and better
software libraries to leverage. Better debugging. Synchronous. All the
advantages in `Why you should move to Python`_.

Safety
------

Accurate estimates are important to a project / sprints success.

I'm better able to predict the time and effort of things in the
programming language I'm most familiar with. This creates an
additional layer of safety on top of an already safe language.

Your startup may be solving a much needed problem in a novel way. Sometimes, 
even with Python, we realize the approach we decided on is harder than we (me 
and you) realized at first. We don't always have enough information before hand,
because we're sort of in uncharted territory at times.
