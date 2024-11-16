はじめに
========

このトークの概要
----------------

このトークでは、

* PythonistaがRustでCLIを作った際に
* 試行錯誤の結果として
* 品質担保をRustではなくPythonで実施した

という話をします。

.. revealjs-break::

このトークでは、

* Rust側の細かい話
* 作ったCLI自体の細かい話
* 「超テクニカル」な使い方

という話はしません。

（考え方とエッセンシャルな技法が中心です）

お前誰よ
--------

.. container:: flex

    .. container:: two-of-third

        Kazuya Takei

        * attakei (X, GitHub, etc)
        * 株式会社ニジボックス
        * **趣味系Pythonista** <= こっち

          * ライブラリ・拡張系を作りがち
          * Sphinx拡張生成マシーン
          * Sphinxでプレゼンテーションしたがる人

        * | Python は 2.6ぐらいから？
          | （GAE for Python出たあたり）

    .. container:: one-of-third

        .. figure:: https://attakei.net/_static/images/icon-attakei@2x.png
            :alt: 著者近影

株式会社ニジボックス
--------------------

.. figure:: ../pyconjp-2022/_images/logo-corporate.png
    :align: center

https://www.nijibox.jp

ニジボックス は「Grow all」をミッションに、企業やサービスの成長に向き合い続けるリクルートグループのデザイン会社です。

お客様のビジネスの成長をUI UXのデザインプロセスから開発・運用・改善までワンストップでサポートします。

.. revealjs-break::

.. revealjs-notes::

    ニジボックスが運営するエンジニアに向けたキュレーションメディア

    POSTDは、海外のエンジニアやテックアナリストが発信する上質な記事を厳選し、日本語に翻訳してお届けしています。
    これまで英語での閲覧を余儀なくされていた、海外テック分野の専門性の高い情報に気軽に触れることができます。

.. container:: flex

    .. container:: two-of-third

        POSTD

        * https://postd.cc
        * エンジニアに向けたキュレーションメディア
        * 海外のテック記事を日本語に翻訳して配信

    .. container:: one-of-third

        .. figure:: /_images/nijibox/logo-postd.png

.. revealjs-notes:: 3min

