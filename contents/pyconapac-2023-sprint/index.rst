===========================================
Relese note for |br| sphinx-revealjs v2.8.0
===========================================

.. revealjs-slide::
    :conf: {"width":1920,"height":1080}
    :theme: css/my-solarized-large.css

.. |br| raw:: html

   <br>

Demo of ``sphinx-revealjs.ext.footnotes``.

(PyConn APAC 2023 Sprint)

Introduction
============

Important
---------

* This presentation is English.
* But, talk is Japanese.

Who am I
--------

.. figure:: http://attakei.net/_static/images/icon-attakei@2x.png

Kazuya Takei

* Sphinx-extension developer
* Author of sphinx-revealjs
* Evangelist of Sphinx presentation

Overview of sphinx-revealjs
---------------------------

:pypi:`sphinx-revealjs` is Sphinx-extension to generate HTML presentation from Sphinx document.

* You can use syntax of reStructuredText.
* You can use other Sphinx extensions.
* You can generate documentation and presentation from same Sphinx project (also).

Thank you for users!

.. revealjs-break::

Source of this presentation (first section)

.. code-block:: rst

   ===========================================
   Relese note for |br| sphinx-revealjs v2.8.0
   ===========================================
   
   .. |br| raw:: html
   
      <br>
   
   Demo of ``sphinx-revealjs.ext.footnotes``.
   
   (PyConn APAC 2023 Sprint)

.. revealjs-break::

More info:

* https://github.com/attakei/sphinx-revealjs
* Full demo (using ``sphinx-intl`` )

  * English => https://attakei.github.io/sphinx-revealjs/en/
  * Jananese => https://attakei.github.io/sphinx-revealjs/ja/

.. figure:: https://attakei.github.io/sphinx-revealjs/en/_images/ogp/index.png
   :width: 50%

Released sphinx-revealjs v2.8.0
===============================

|:tada:| |:tada:| |:tada:|

Updates
-------

* Supporting Python 3.12 (passed tests)
* Use MyPy
* Custom extension about **layout of footnotes**

Footnotes of Sphinx
-------------------

reStructuredText is defined about footnote. [#]_

.. code-block:: rst

   Lorem ipsum [#f1]_ dolor sit amet ... [#f2]_
   
   .. rubric:: Footnotes
   
   .. [#f1] Text of the first footnote.
   .. [#f2] Text of the second footnote.

.. [#] https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#footnotes

Footnotes of sphinx-revealjs
----------------------------

v2.8.0 provides custom extension to layout footnotes into left-bottom of section. [#]_

.. code-block:: python

   """Your conf.py of sphinx project.
   """

   extensions = [
       "sphinx_revealjs",
       # ↓ Append this!
       "sphinx_revealjs.ext.footnotes",
   ]

.. [#] This text is rendered left-bottom of presentation.

.. revealjs-break::

By previous version ...

.. figure:: _images/footnotes-v2.7.1.png
   :class: with-border

.. revealjs-fragments::

   (You can build without ``sphinx_revealjs.ext.footnotes``)

.. revealjs-break::

Reproduction stylesheet is

.. code-block:: css

   a.footnote-reference {
     font-size: 70%;
     vertical-align: top;
   }
   
   aside.footnote-list {
     position: fixed;
     bottom: 0;
     font-size: 50%;
     width: 100%;
   }
   
   aside.footnote > span {
     float: left;
   }
   aside.footnote p {
     text-align: left;
     padding-left: 2rem;
   }

Next version
============

Reveal.js v5.0.0 is released
----------------------------

* Released at 2023/10/27 (NOW!!!)
* I am reading docs for new features and breaking-changes.


.. revealjs-fragments::

   Finish presentation. Thank you for reading!
