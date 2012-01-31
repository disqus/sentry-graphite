sentry-graphite
===============

An extension for Sentry that increments a key in graphite based on the error.

Install
-------

Install the package via ``pip``::

    pip install sentry-graphite

Add ``sentry_graphite`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        # ...
        'sentry',
        'sentry_graphite',
    )

Configuration
-------------

Go to your project's configuration page (Projects -> [Project]) and select the
Graphite tab. Fill out the host, port and desired prefix for Graphite.

Wait for new errors, and you should see keys being incremented in Graphite.
