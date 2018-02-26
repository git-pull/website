:orphan:

.. _consulting:

Stripe Integration
==================

:doc:`About <./index>` |
Stripe Integration | 
:doc:`Why Python? <./why-python>` |
`Contact`_

.. _Contact: https://goo.gl/forms/K1uwUVIWOBX589Ip1

.. image:: img/stripe.png
   :align: right
   :width: 200

The difficulties of building a SAAS platform.

At my past companies, I had to deliver a billing and subscription system
from the ground up. Back in the day, these API's were very cumbersome and 
buggy, much less friendly than they are today.

Today, with libraries like `stripe-python`_ and `stripe-node`_ that wrap on top
of API's so you don't have to build your own API client.

At Boostable (W14), I wrote the stripe integration for node, and later :doc:`for the
python version <./why-python>` of our website. The first issue we had was
querying Stripe every time the user loaded the dashboard. We needed a way to 
cache relational bits of Stripe information and only update it when
necessary.

For both occasions, I wrote out models that acted as a parity to Stripe's data,
so info could be available locally to avoid extra API calls, and even 
*synchronized* with the freshest available data. Most importantly though,
it established a relationship between the *user's website account and the
stripe customer*. That connection is critical, if we didn't have that, we 
couldn't create a real dashboard.

Making sense of Stripe
----------------------

The first part of the battle is understanding how Stripe logically
assembles a transaction, and even goes the extra mile to store customer
information securely [1]_

The Stripe `Customer <https://stripe.com/docs/sources/customers>`_ is the
key way to handle your billing sources and their subscriptions.

If you're marketing and reaching out for customers, you'll probably also
want to create coupons, which can be used to apply discounts, as well.

.. [1] Stripe is PCI Service Provider Level 1 Certified.
   https://stripe.com/docs/security/stripe

Solutions for a robust, self-service platform
----------------------------------------------

A mature startup has billing systems automated. Users can subscribe,
change plans, and even cancel their subscriptions from the dashboard.

Behind this though is a lot of protective design for handling snags that happen.
We didn't want errors propagating without proper notifications, hopefully
to our emails. Secondly, the user should be able to land softly if any
bumps in the road are hit. And most importantly, common issues should be
*recoverable* without the user perceiving it.

Later, at devel.tech, I would begin my own billing system *completely from
scratch*. Ironically enough, I still *underestimated how long it would
take and how hard it would be*. Even though I did it before.

Built with clarity in mind
--------------------------

This time though, I had a different trajectory. I'll take my domain
knowledge of Stripe and help other startups who needed help integrating
things.

To survive in the long term, a stripe integration must make sense so
future programmers on the code can understand. With my track record in
building API's and documentation that have been implemented around the
world, you are in good hands to have the pieces fit.

.. _stripe-python: https://github.com/stripe/stripe-python
.. _stripe-node: https://github.com/stripe/stripe-node

Your Stripe integration expert
------------------------------

Integrating billing systems can be overwhelming. A seasoned developer will
be on your side to understand your billing workflow. Don't delay,
`Send a message <https://goo.gl/forms/K1uwUVIWOBX589Ip1>`_

(Back to :doc:`./index`)

*The Stripe name and logos are trademarks or service marks of Stripe, Inc. or its affiliates in the U.S. and other countries. Other names may be trademarks of their respective owners.*
