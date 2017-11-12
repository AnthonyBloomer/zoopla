zoopla
======

|Build Status|

A python wrapper for the Zoopla API.

Zoopla has launched an open API to allow developers to create
applications using hyper local data on 27m homes, over 1m sale and
rental listings, and 15 years of sold price data.

`Register`_ for a user account and apply for an instant API key.

Browse the `documentation`_ to understand how to use the API and the
specifications for the individual APIs.

Installation
------------

::

    $ pip install zoopla

Tests
-----

Install the dev requirements:

.. code:: sh

    $ pip install -r requirements.txt

| Run py.test with your developer key (otherwise you won’t be able to
  hit the live
| API upon which these tests depend).

.. code:: sh

    $ py.test --api_key=<your-api-key> tests/ # pytest under Python 3+

Examples
--------

Retrieve property listings for a given area.

.. code:: python

    from zoopla import Zoopla

    zoopla = Zoopla(api_key='your_api_key')

    search = zoopla.property_listings({
        'maximum_beds': 2,
        'page_size': 100,
        'listing_status': 'sale',
        'area': 'Blackley, Greater Manchester'
    })

    for result in search.listing:
        print(result.price)
        print(result.description)
        print(result.image_url)


Retrieve a list of house price estimates for the requested area.

.. code:: python

    zed_indices = zoopla.area_zed_indices({
        'area': 'Blackley, Greater Manchester',
        'output_type': 'area',
        'area_type': 'streets',
        'order': 'ascending',
        'page_number': 1,
        'page_size': 10
    })

    print(zed_indices.town)
    print(zed_indices.results_url)

Generate a graph of values for an outcode over the previous 3 months and
return the URL to the generated image.

.. code:: python

    area_graphs = zoopla.area_value_graphs({'area': 'SW11'})

    print(area_graphs.average_values_graph_url)
    print(area_graphs.value_trend_graph_url)

Retrieve the average sale price for houses in a particular area.

.. code:: python

    average = zoopla.average_area_sold_price({'area': 'SW11'})

    print(average.average_sold_price_7year)
    print(average.average_sold_price_5year)


Submit a viewing request to an agent regarding a particular listing.
 
.. code:: python

    session_id = zoopla.get_session_id()

    arrange_viewing = zoopla.arrange_viewing({
        'session_id': session_id,
        'listing_id': 44863256,
        'name': 'Tester',
        'email': "zoopla_developer@mashery.com",
        'phone': '01010101',
        'phone_type': 'work',
        'best_time_to_call': 'anytime',
        'message': 'Hi, I seen your listing on zoopla.co.uk and I would love to arrange a viewing!'

    })
    
Contributing
------------

- Fork the project and clone locally.
- Create a new branch for what you're going to work on. 
- Push to your origin repository.
- Include tests and update documentation if necessary.
- Create a new pull request in GitHub.

.. _Register: http://developer.zoopla.com/member/register/
.. _documentation: http://developer.zoopla.com/docs/


.. |Build Status| image:: https://travis-ci.org/AnthonyBloomer/zoopla.svg?branch=master
   :target: https://travis-ci.org/AnthonyBloomer/zoopla
