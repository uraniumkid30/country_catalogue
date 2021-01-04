.. image:: https://raw.githubusercontent.com/uraniumkid30/country_catalogue/master/logo/country.jpg

This is a catalogue that gives you information about any country chosen.

Currency data sources
---------------------

The default source is the `Country Code <https://github.com/datasets/country-codes/>`_. This is the list of all country facts.
It can be downloaded here: `country-codes.csv <https://github.com/datasets/country-codes/blob/master/data/country-codes.csv>`_.
The catalogue can use different sources as long as the format is the same.

Installation
------------

You can install directly after cloning:

.. code-block:: bash

 $ python setup.py install --user

Or use the Python package:

.. code-block:: bash

  $ pip install --user country_catalogue

Command line tool
-----------------

After installation, you should have ``country_catalogue`` in your ``$PATH``:


Python API
----------

Create once the currency converter object:

.. code-block:: python

    >>> from country_catalogue.country import CountryCatalogue
    >>> cc = CountryCatalogue()

Convert from ``EUR`` to ``USD`` using the last available rate:

.. code-block:: python

    >>> cc.get_country_info(name="nigeria") # doctest: +SKIP
    >>> print(cc.english_formal_name)
    Nigeria

get_country_info returns an instance of ``SimpleNamespace`` which supports .(dot) notation:


Other attributes
~~~~~~~~~~~~~~~~

+ ``english_formal_name`` ``CLDR_display_name`` ``official_name`` lets you know the name of the country

+ ``ISO3166_1_Alpha_3`` ``ISO3166_1_Alpha_2`` ``official_name`` lets you on some geos data
.. code-block:: python

    >>> cc.ISO3166_1_Alpha_3
    >>> cc.ISO3166_1_Alpha_2

+ ``currency`` ``capital`` and ``continent'' is also available


Finally, you can use other attributes to get around:

.. code-block:: python

    # Load the packaged data and reference ISO3166-1-Alpha-2 code
    cc = CountryCatalogue()
    cc.get_country_info(alpha2="NG")

    # reference ISO3166-1-Alpha-3 code is also available
    cc.get_country_info(alpha2="NIG")#geoname_id

    # lastly you can refernece by geoname_id
    cc.get_country_info(geoname_id="234567")


Tables
~~~~~~~

Tables are available based on ``Currency`` used by any country or  ``Continent`` that a country belongs to.


.. code-block:: python

    >>> from country_catalogue.country import CountryCatalogue
    >>> cc = CountryCatalogue()
    # Full name of currency can be used
    >>> cc.get_currency_table(full_name="Naira")
    # short_code can be used "numeric_code"
    >>> cc.get_currency_table(short_code="NGN")
    # numeric_code can be used aswell
    >>> cc.get_currency_table(numeric_code=2)

    # continent table, just takes the name of the company
    >>> cc.get_continent_table("Africa)
