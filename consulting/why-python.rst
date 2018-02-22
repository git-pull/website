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
tried various combinations of software stacks, and learned how important
it is to stick to one solution over another.

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
- Django (compare to Laravel, Rails)

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

- Python is older than Java (1991 and 1995, respectively) [#]_ [#]_
- Python 3 has been around 9+ years (December 3, 2008)

.. [#] Rossum, Guido. *A Brief Timeline of Python* [Blog post].
   Retrieved from https://python-history.blogspot.com/2009/01/brief-timeline-of-python.html
.. [#] Oracle. *The History of Java Technology*
   Retrieved from http://www.oracle.com/technetwork/java/javase/overview/javahistory-index-198355.html

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

While this is ultimately based on tastes, I feel many Node users
confront a sunk-cost fallacy, want to conform to Node's way of doing
things believing it'll pay off in the end, and in some cases even
misunderstand when non-blocking/async actually helps, rather than
hinders.

Node.js is cumbersome for scripts that don't sharply benefit from
non-blocking.

In more than half of my programming code, the boost from it being
asynchronous is negligible. Not worth the headaches controlling flow
Node's flow introduces.

Well written code will be throwing around a lot of *pure* functions. The notion 
of this is skewed. Since we have to follow Node's callback pattern, I've
found many developers think they're getting the benefits of pure
functions, when they're juggling around promises, object literals,
and dictionary-like objects, that add to the cognitive load
when doing the job.

- Things are async by default, when you don't benefit from it

  Java is a fantastic programming language. People sometimes get irked by the 
  amount of bureaucratic boilerplate involved.

  Node.js runs JavaScript code in an Event Loop [#]_. This style of
  programming makes scaling I/O nearly a feature of the language, and it's
  therefore a convention that Node code adopt a callback pattern [#]_.

  In most of my scripting, I found I missed Ruby and Python's succinct
  blocking, synchronous code. It's clearer and more concise.

- It's harder to understand, write, test and debug code in Node's callback
  style

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
  type check it? With Python, it's more clear through documentation and
  trackbacks I'm interacting with instance of a critical object, like
  `requests.Response
  <http://docs.python-requests.org/en/master/api/#requests.Response>`_.

  With JavaScript, you're passing around dictionary-like objects too, but
  they libraries don't crystalize them in the form of a class in the way
  Python does. Even though Python is weakly-typed and duck-typed, objects
  play part of the technical culture.

  JavaScript does have TypeScript and Flow. But I feel for something like
  JS, change needs to happen from the ground up to represent responses as
  typed objects. The existence and growth of typed javascript shows the
  need, but I'm concerned they're not grasping it from the angle I'm
  seeing, and may end up with a porous system where typed responses don't
  play a role in a language that doesn't do enough for control flow.

  I mean, I think it'd even be better to have an optional `PropTypes`_-like 
  dictionary to pass along that validates things and if something pops up,
  raises a detailed traceback.
  
  How easy is it to test and mock the response, at scale?

  .. _PropTypes: https://reactjs.org/docs/typechecking-with-proptypes.html

- Promises, Async / Await, and so on, don't help much

  This really mask the pain I feel developers are having (but not
  articulating) . It's not any easier to think about, write, or test.

  And after playing with the many (well-intentioned, and innovative)
  solutions. You begin to realize how much time gets sunk trying to
  simplify code that you otherwise wouldn't *need* asynchronous.

  You begin to miss Ruby, Python, Golang, and other languages
  for not putting you through the following:

  We need to end the callback pyramid of death. It's not an option
  to change the fundamentals of Node.js's worker system, so we need
  to create wrapper objects around functions that consume the
  callback-style node.js uses.

  But that's not enough. Because we also have to use `.then(), .catch(),
  and finally()
  <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise>`_
  to control the flow.

  I didn't want that. I want to return and resolve the variable in one
  line, as-is. Like `request.request`_ does in Python, or `fs.readFileSync`_
  (and other functions ending in ``Sync``) do.

  .. _request.request: http://docs.python-requests.org/en/master/api/#requests.request
  .. _fs.readFileSync: https://nodejs.org/api/fs.html#fs_fs_readfilesync_path_options

  And *even with* native promises in ES6, `we have programmers preferring
  Bluebird <https://stackoverflow.com/a/34961040>`_. In 2013, this meant
  some libraries were incompatible with each other's promises. Meaning
  required libraries and responses have to be adjusted in your own code,
  to work around dysfunction of code that *literally only controls flow*.

  I thought at first glance, `async / await
  <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function>`_
  would cure the pain. But should actually involve having to wrap
  promises. I'm not trying to be cynical - but it's like there's no escape
  from just getting the code to block and give me a response.

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

It's considered the most delightful to program in. I agree.

The community is brilliant. And joyous.

GitHub uses it.

Rails, one of the most legendary web frameworks uses it. Rails in itself
is the prime reason most people begin Ruby - not the other way around.

There are a lot of startups hiring Rails developers. There is a huge
talent pool to meet the demand.

Homebrew, macOS user's favorite packaage manger. Vagrant, the VM manager.
Jekyll, a blogging platform. Metasploit, a security framework.

Downsides to Ruby
"""""""""""""""""

Documentation is kind of shoddy compared to Python's Sphinx and
ReadTheDocs.

It's a generalist language, but the community has overwhelmingly
picked Python for scripting.

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
