Sphinx イントロダクション
=========================

アンケート
----------

.. revealjs-fragments::

   * Sphinx、知ってますか？
   * Sphinx、使ってますか？

Sphinxとはなにか
----------------

.. revealjs-notes::

    SphinxはPython製のドキュメンテーションビルダーです。
    reStructuredTextで書かれたソースを中心に複数のリソースを「ドキュメント」として管理し、
    HTMLやPDFなどに変換する機能を持っています。

Python製のドキュメンテーションビルダー

* ソーステキストを束ねて「ドキュメント」として扱う
* メインソースはreStructuredTextし、内部でdocutilsを利用
* 「ドキュメント」からHTML・PDFなどを生成する

.. revealjs-break::

Python製のドキュメンテーションビルダー

.. figure:: _images/about-sphinx.svg
    :align: center

.. revealjs-break::

.. revealjs-notes::

    reStructuredTextは軽量マークアップ言語の一種です。
    マークアップとしての標準的な文法の他に、仕様として「ディレクティブ」という概念があり、表現力の向上を支えています。
    ディレクティブは自作することも可能で、Sphinxでも活用されています。
    Sphinxでのディレクティブ例だと、toctreeが挙げられます。
    ドキュメントの親子関係を記述するのに使われます。

reStructuredText

* 軽量マークアップ言語
* 「ディレクティブ」の概念（表現力・拡張力の基盤）

.. code-block:: rst

    Document title
    ==============

    概要
    ----

    .. toctree::

        overview
        installation

.. revealjs-break::

.. revealjs-notes::

    Sphinxが出力できる形式は様々です。
    バンドルされているものだと、前述のようなHTMLやPDFだけでなく、
    「電子書籍形式のEPUB」「Unix系のmanコマンド向けのman page」といったものも対応しています。

アウトプット形式様々

* HTML
* PDF
* EPUB
* man page

Sphinxで出来ているサイト
------------------------

Python関連

* Python本体
* Sphinx
* Ansible
* 様々なPythonパッケージ

.. revealjs-break::

.. revealjs-notes::

    https://www.phpmyadmin.net/ Django
    Linux Kernelは少なくともv4からSphinx

Python以外

* `Fortran <https://fortran-lang.org/>`_
* `phpMyAdmin <https://docs.phpmyadmin.net/en/latest/>`_
* `Linux kernel <https://www.kernel.org/doc/html/v5.9/>`_
* (このスライド)

Sphinxで書かれた書籍
--------------------

(書籍執筆のどこかの工程でSphinxを使っているもの)

* `Go言語による並行処理 <https://www.oreilly.co.jp/books/9784873118468/>`_
* `Pythonプロフェッショナルプログラミング第3版 <https://www.shuwasystem.co.jp/products/7980html/5382.html>`_
* `独学プログラマー <https://shop.nikkeibp.co.jp/front/commodity/0000/C92270/>`_
* `エキスパートPythonプログラミング改訂2版 <https://asciidwango.jp/post/171156307275/>`_
* `仕事ではじめる機械学習 <https://www.oreilly.co.jp/books/9784873118253/>`_

おさらい：Sphinx単体で出来ること
--------------------------------

* reStructuredTextでドキュメントを管理できる
* HTMLを生成できる・テーマを切り替えられる
* PDFを生成できる（要LaTex）

.. revealjs-fragments::

    ちょっと物足りない？

ありがちな「物足りなさ」
------------------------

* Markdownでドキュメント管理したい
* 動画やツイートなどを、なるべく楽に埋め込みたい
* HTMLでの折り返しが気に食わないので、いい感じに改行したい

.. revealjs-fragments::

    **Sphinxは「拡張」が出来るようになっている**
