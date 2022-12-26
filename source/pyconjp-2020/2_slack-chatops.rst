SlackのChatOps事情
==================

.. time: 4

よくある、SlackのChatOps
------------------------

- Slackbot/ワークフロー
- サードパーティのSlackアプリ
- 各種カスタムIntegration

Slackbot/ワークフロー
---------------------

.. Slackbotの例だと、＃jp-2020-random でomikuji

Slackbot

- 特定のメッセージに反応するもの
- 反応内容を複数用意すると、ランダムで選ばれる

ワークフロー

- 各種トリガーに、フォーム表示とメッセージ送信をする
- 「チャンネルにメンバーが増えた時にメッセージ」ぐらいの簡単なやつ向け

サードパーティのSlackアプリ
---------------------------

Appディレクトリに登録されている様々なコラボレーション用アプリ

- Googleカレンダー

  * 当日の予定の案内
  * 予定の時間帯にステータス変更

- Polly

  * 簡単なアンケート

- GitHub/BitBucket/etc

  * Issue/PRの連携

各種カスタムIntegration
-----------------------

.. 当然、既存のものをやるわけでな無いので、これを利用する

混み入ったことをしたいなら

- カスタムBot
- Incoming/Outgoing Webhooks
- Slash Commands

.. revealjs-break::

混み入ったことをしたいなら

- カスタムBot
- Incoming/Outgoing Webhooks
- **Slash Commands <= 今回はこれ**

なぜSlash Commands？
--------------------

.. 重要なのが、コマンドごとにURLを指定できることと、実装が楽なこと

- Slackをトリガーに出来る
- アプリケーションの実装が楽
- Incoming Webhookを含んでる
- 単体でもいいし、カスタムBotにも組み込める

= ミニマムスタートに丁度いい
