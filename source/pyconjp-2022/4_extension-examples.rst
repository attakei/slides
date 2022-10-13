Sphinx拡張 ショーケース
=======================

.. 2 / 9

この後に例示用に出てくるSphinx拡張の紹介

sphinxcontrib-oembed
--------------------

.. container:: flex

    .. container:: half

        * oEmbedを使ったコンテンツ埋め込みをサポート。
        * URLの指定だけでツイートや動画の埋め込みが可能になる。

    .. container:: half

        .. oembed:: https://twitter.com/attakei/status/1575887211962290176

.. revealjs-break::

.. code-block:: rst

    .. raw:: html

        <blockquote class="twitter-tweet">
          <p lang="en" dir="ltr">
            sphinx-revealjs v2.2.0 is released.<br>Thank you for usings, feedbacks and collaborations!<br>See PyPI: <a href="https://t.co/TCCYhLYHWl">https://t.co/TCCYhLYHWl</a><br>See GitHub: <a href="https://t.co/F59O49dwnf">https://t.co/F59O49dwnf</a>
          </p>
          &mdash; kAZUYA tAKEI (@attakei)<a href="https://twitter.com/attakei/status/1575887211962290176?ref_src=twsrc%5Etfw">September 30, 2022</a>
        </blockquote>
        <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

↓

.. code-block:: rst

    .. oembed:: https://twitter.com/attakei/status/1575887211962290176

.. revealjs-break::

分類：入力と出力に関する拡張

* | ディレクティブ（とノード）の新規作成が必要
* | ソース読み込み時にHTTP通信する
  | => ディレクティブの実装がちょっと複雑
* とはいえ、 **ディレクティブとノードで完結する**

sphinxcontrib-budoux
--------------------

BudouXを使って、日本語文の改行をいい感じに出来るようにする拡張。

.. container:: r-stack

    .. revealjs-fragments::

        .. figure:: _images/java-before.png

        .. figure:: _images/java-after.png

.. revealjs-break::

分類：出力に関する拡張

* Sphinxメイン処理内で行われた「ソースをもとにしたHTML」を再加工する
* 出力に **割り込んで** の加工が必要
