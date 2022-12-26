Slack Commands
==============

.. time: 3

Slash Commandsって？
--------------------

``/`` から始まるショートカットコマンドを定義して、
特定のアクションを実行できるようにしたもの。

ビルトインのSlash Commands
--------------------------

普段、自分がよく使っているもの

- ``/feed`` : RSSフィードを使用する
- ``/remind`` : リマインダー機能を使用する
- ``/invite`` : チャンネルに招待する
- ``/archive`` : チャンネルをアーカイブする

自作Slash Commandの仕組み
-------------------------

.. ざっくり全体の流れとサーバー側がやること

※基本的なもの

- コマンドを実行する
- 指定されたURLへリクエストを行う
- URLは3秒以内にレスポンスを返す
- レスポンスを元に、メッセージとして表示する

.. revealjs-break::

.. container:: flex

    .. container:: half

        レスポンスボディが...

        * | 空(0byte)
          | => 何もしない
        * | テキスト
          | => テキストのまま表示
        * | json
          | => Webhookと同じ

    .. container:: half

        .. figure:: _images/simple-flow.png

.. revealjs-break::

リクエストの中身（一部）

.. csv-table::
    :header: 名前,中身,例

    team_domain,チーム名,pyconjp-fellow
    user_name,ユーザー,attakei
    text,コマンドの引数,--
    response_url,Webhook用URL,--
