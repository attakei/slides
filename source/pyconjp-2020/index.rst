=====================================================
Cloud RunとFastAPIで、ChatBotをミニマムスタートしよう
=====================================================

.. revealjs-slide::
    :theme: css/my-solarized.css

:date: 2020-08-29
:author: Kazuya Takei
:location: PyCon JP 2020
:links: `#pyconjp_4 <https://twitter.com/hashtag/pyconjp_4?src=hashtag_click&f=live>`_

イントロ
========

今回のお題
----------

* Google Cloud Run上に
* FastAPIをベースにしたWebアプリケーションとして
* Slackで簡易なをボットを提供する

という話をします。

.. revealjs-break::

* Google Cloud Run上に
* | **FastAPIをベースにしたWebアプリケーションとして**
  | **↑ここがメイン予定**
* Slackで簡易なをボットを提供する

という話をします。

.. include:: 1_whoami.rst

免責
----

* | 「ミニマムスタート」を主眼にしているため、
  | 一部の実装などを意図的に省いています。
* | 所属とは無関係の発表です。
  | 個人の嗜好性を多分に含んだ内容となっています。

.. ここまでで3分ぐらい想定

.. include:: 2_slack-chatops.rst

.. include:: 3_slack-slashcommand.rst

-> Next ->
==========

.. ここまでで8分ぐらいが理想

.. include:: 4_fastapi-localenv.rst

.. include:: 5_fastapi-introduction.rst

.. include:: 6_fastapi-chatbot-1.rst

.. include:: 7_fastapi-chatbot-2.rst

-> Next ->
==========

.. ここまでで20分ぐらいが理想

.. include:: 8_cloudrun.rst

まとめ
======

.. ここまでで25分ぐらいが目安

発表振り返り
------------

* FastAPIの標準機能は強力で、ChatBotの実装を機能面・制約面に対する対応が比較的容易でした
* Cloud Runベースの運用も比較的容易。ただし、この種のサービスは初動がネック

※やりきってみたい
------------------

ブラウザやCLIで確認してたネット系コマンドをSlashCommandsで提供するSlack App

* ``dig``
* ``whois``
* ``openssl`` (HTTPS validation)

.. include:: 9_links.rst
