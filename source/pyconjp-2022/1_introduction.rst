はじめに
========

お前誰よ
--------

.. revealjs-notes::

    在籍的にはニジボックス。ただし、個人活動に近い領域でのPyCon JP参加。

.. container:: flex

    .. container:: two-of-third

        Kazuya Takei

        * attakei (Twitter, GitHub, etc)
        * 株式会社ニジボックス
        * **趣味系Pythonista** <= こっち

          * ライブラリ・拡張系を作りがち
          * Sphinxでプレゼンテーションしたがる人

    .. container:: one-of-third

        .. figure:: https://attakei.net/_static/images/icon-attakei@2x.png
            :alt: 著者近影

株式会社ニジボックス
--------------------

.. figure:: _images/logo-corporate.png
    :align: center

ニジボックス は「Grow all」をミッションに、企業やサービスの成長に向き合い続けるリクルートグループのデザイン会社。

お客様のビジネスの成長をUI UXのデザインプロセスから開発・運用・改善までワンストップでサポート。

興味が湧いた・問い合わせしたくなったら、 https://www.nijibox.jp へ。

.. revealjs-break::

.. revealjs-notes::

    ニジボックスが運営するエンジニアに向けたキュレーションメディア

    POSTDは、海外のエンジニアやテックアナリストが発信する上質な記事を厳選し、日本語に翻訳してお届けしています。これまで英語での閲覧を余儀なくされていた、海外テック分野の専門性の高い情報に気軽に触れることができます。

.. container:: flex

    .. container:: two-of-third

        POSTD

        * https://postd.cc
        * エンジニアに向けたキュレーションメディア
        * 海外のテック記事を日本語に翻訳して配信

    .. container:: one-of-third

        .. figure:: _images/logo-postd.png

今日話す予定のこと
------------------

* Sphinxの概要
* Sphinx拡張の概要
* Sphinx拡張の実装アプローチ
* Extra

(補足)
------

* コード周りの環境（当時情報）

  * Python 3.10.x
  * Sphinx 5.2.x

* | 体験ベースの発表であり、網羅性はありません。
  | 例えば、このあたりはあまり触れません。

  * 普段の実装で手を出していない
  * 複雑度が高く、手を出しにくい
