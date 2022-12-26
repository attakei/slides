ローカル開発する
================

.. time: 6

基本構成
--------

.. ngrok = エングロック

* Python 3.8系
* Poetryでパッケージ管理
* ngrokを使用

ngrok
-----

NATやファイヤーウォールなどを越えて、
ローカルホストを外部公開できるサービス。

**HTTPSのURLも利用可能**

※今回の例では、最初に ``ngrok`` プロセスを用意して、
ローカルサーバは常時固定ポートを使用します。

.. revealjs-break::

こんな感じに動く

.. code-block:: bash

    $ ngrok http 8000

    Session Status                online
    Account                       Kazuya Takei (Plan: Free)
    Update                        update available (version 2.3.35, Ctrl-U to update)
    Version                       2.3.35
    Region                        United States (us)
    Web Interface                 http://127.0.0.1:4040
    Forwarding                    http://8e1d754c956e.ngrok.io -> http://localhost:8000
    Forwarding                    https://8e1d754c956e.ngrok.io -> http://localhost:8000

.. revealjs-break::

補足として...

* 無料プランの場合、

  * コマンドのたびに公開URLが変わる
  * 同時に用意できるプロセスは1個まで

* 不便な場合は有料プランをどうぞ
