Changelog
=========

[Unreleased]
------------

v0.7.0 (2021-02-23)
-------------------

Bug Fixes
~~~~~~~~~

-  [streaming quotes] fixed to handle multiple messages bundled in 1
   websocket message

   BREAKING CHANGE: decode\_ws\_msg() is now a generator returning 1 or
   more decoded messages. See documentation for details.

Documentation Changes
~~~~~~~~~~~~~~~~~~~~~

-  [decode\_ws\_msg] updated for change

v0.6.0 (2019-09-16)
-------------------

New Features
~~~~~~~~~~~~

-  [order endpoints] added support for the ManualOrder attribute

   BREAKING CHANGE: SAXO OpenApi will require this attribute in the
   orderbodies, see:
   https://www.developer.saxo/excel/blog/updated-requirements-for-order-placement?phrase=ManualOrder

Style Fixes
~~~~~~~~~~~

-  fixed flake8 style issues

Documentation Changes
~~~~~~~~~~~~~~~~~~~~~

-  [sphinx config] fixed typo

v0.5.0 (2019-09-10)
-------------------

New Features
~~~~~~~~~~~~

-  [endpoints] chart endpoints

   addition of all chart endpoint classes

Documentation Changes
~~~~~~~~~~~~~~~~~~~~~

-  [endpoints] chart endpoints documentation

   all chart endpoint classes documentation
-  various doc/docstring updates

v0.4.1 (2019-05-23)
-------------------

New Features
~~~~~~~~~~~~

-  [endpoints] eventnotificationservices

   addition all eventnotificationservices endpoint classes
-  [definitions] activities and reportformats

   addition of definitions for 'activities' and 'reportformats'

Bug Fixes
~~~~~~~~~

-  corrected config causing broken build

   replace auto-changelog

Documentation Changes
~~~~~~~~~~~~~~~~~~~~~

-  [endpoints] eventnotificationservices

   addition all eventnotificationservices endpoint classes

v0.3.1 (2019-05-04)
-------------------

v0.3.0 (2019-05-04)
-------------------
