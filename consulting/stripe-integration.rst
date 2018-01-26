:orphan:

.. _consulting:

Stripe Integration
==================

:doc:`About <./index>` | Stripe Integration | `Contact`_

.. _Contact: https://goo.gl/forms/K1uwUVIWOBX589Ip1

The difficulties of building a SAAS platform
--------------------------------------------

During multiple times in my history at startups, we had to setup user
subscriptions and billing. One of the most arcane API's we had to
integrate with were E-Commerce ones.

Back then, it was **much less friendly** than it is today. Today we have
libraries like `stripe-python`_ and `stripe-node` that wrap on top of
API's so you don't have to build your own API client.

At Boostable (W14), I wrote the stripe integration for node, and later for the
python version of our website. The first issue we had was **too many API
calls**. We needed a way to cache important chunks of Stripe customer data
so we weren't slowing local development or customer's down.

For both occasions, I wrote out models that acted as a parity to Stripe's data,
so info could be available locally to avoid extra API calls, and even 
*sychronized* with the freshest available data. Most importantly though,
it established a relationship between the **user's website account and the
stripe customer**. That connection is critical, if we didn't have that, we 
couldn't create a real dashboard.

Because, in Stripe, the Customer object is the key way to handle your
billing sources and their subscriptions. But actually knowing that was the
first part of the battle. We had to create a system where we protected
the connect of the user's stripe account and the stripe ID, and gave a
**registration workflow** so the user could **subscribe to plans**.

A true SAAS worth its salt is **almost completely self-service**. Users can also
**cancel and change plans from the user dashboard**. That's where it takes
it to the next level, and really boosts your image as a company.

Behind this though is a lot of protective design for handling snags that happen.
We didn't want errors propagating without proper notifications, hopefully
to our emails. Secondly, the user should be able to land softly if any
bumps in the road are hit. And most importantly, common issues should be
**recoverable** without the user perceiving it.

Later, at devel.tech, I would begin my own billing system **completely from
scratch**. Ironically enough, I still **underestimated how long it would
take and how hard it would be**. Even though I did it before.

This time though, I had a different trajectory. I'll take my domain
knowledge of Stripe and help other startups who needed help integrating
things.

.. _stripe-python: https://github.com/stripe/stripe-python
.. _stripe-node: https://github.com/stripe/stripe-node

Your Stripe integration experts
-------------------------------

Integrating billing systems can be overwhelming. Get it done
on time and get it done right! `Send a message <https://goo.gl/forms/K1uwUVIWOBX589Ip1>`_

(Back to :doc:`./index`)
