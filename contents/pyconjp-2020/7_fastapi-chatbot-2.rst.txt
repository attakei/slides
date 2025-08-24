FastAPIでChatBotローカル開発(2)
===============================

よりChatOpsっぽいコマンド
-------------------------

.. DNSレコードの確認をするdigをChatOpsで出来るようにします

``/dig`` を作ります

※ ``dig`` = DNSの問い合わせをするツール

.. code-block:: bash

    $ dig example.com

    ;; QUESTION SECTION:
    ;example.com.                   IN      A

    ;; ANSWER SECTION:
    example.com.            48418   IN      A       93.184.216.34

Slack上のコマンドイメージ

  /dig example.com

(1)を拡張して作る、 ``/dig``
----------------------------

.. 実際にDNS問い合わせをするSlashCommandの実装

.. code-block:: python

    # import を省略
    # dns-pythonを使います

    app = FastAPI()

    @app.post("/slash-commands/dig")
    async def dig(text: str = Form("")):
        # DNSPythonを使ってDNS情報を取得する
        name = dns.name.from_text(text)
        query = dns.message.make_query(name, dns.rdatatype.A)
        msg = dns.query.udp(query, "8.8.8.8")
        return {
            "text": f"Answer for `A` of `{name}`\n```{msg}```"
        }

試してみる
----------

.. code-block:: bash

    $ http --form localhost:8000/slash-commands/dig text=example.com
    HTTP/1.1 200 OK
    content-length: 207
    content-type: application/json
    date: Fri, 28 Aug 2020 18:18:19 GMT
    server: uvicorn

    {
        "text": "Answer for `A` of `example.com.`\n```id 31266\nopcode QUERY\nrcode NOERROR\nflags QR RD RA\n;QUESTION\nexample.com. IN A\n;ANSWER\nexample.com. 20986 IN A 93.184.216.34\n;AUTHORITY\n;ADDITIONAL```"
    }

.. revealjs-break::

.. Slack上での見え方

.. code-block:: text

    Answer for `A` of `example.com.`
    ```id 31266
    opcode QUERY
    rcode NOERROR
    flags QR RD RA
    ;QUESTION
    example.com. IN A
    ;ANSWER
    example.com. 20986 IN A 93.184.216.34
    ;AUTHORITY
    ;ADDITIONAL```

3秒しか猶予がない
-----------------

..  SlashCommandsはレスポンス猶予が3秒しか無いので、時間を食うとまずい。
    題材がちょっと悪い（DNSで3秒はまず無いので）けど、めちゃくちゃ処理するなどをイメージしてもらう

.. code-block:: python

    # import を省略

    app = FastAPI()

    @app.post("/slash-commands/dig")
    async def dig(text: str = Form("")):
        name = dns.name.from_text(text)
        query = dns.message.make_query(name, dns.rdatatype.A)
        # もし、ここで想定外の時間がかかったら？
        msg = dns.query.udp(query, "8.8.8.8")
        return {
            "text": f"Answer for `A` of `{name}`\n```{msg}```"
        }

.. revealjs-break::

対策をしないといけない

Background Task機能
-------------------

FastAPIに標準提供されている機能。

レスポンスとは非同期に処理させたいことを、
バックグラウドのイベントループに引き渡すことが出来る。

これにより、 **レスポンスを早期に返してメイン処理を別途実行することが可能になる**

.. revealjs-break::

..  BG利用に置き換えた形式。引数にBGがあれば勝手に挿入される
    ルーティングはBGに処理移譲して空レスポンスを返して終わり
    BGタスクはrequest_url経由でslackにメッセージを渡す

.. code-block:: python

    # import を省略

    app = FastAPI()

    async def query_dns(name: str, url: str):
        name = dns.name.from_text(name)
        query = dns.message.make_query(name, dns.rdatatype.A)
        await asyncio.sleep(5)  # 時間のかかる仮定
        msg = dns.query.udp(query, "8.8.8.8")
        slack = slackweb.Slack(url)
        slack.notify(text=f"Answer for `A` of `{name}`\n```{msg}```")

.. code-block:: python

    @app.post("/slash-commands/dig")
    async def dig(
          bg: BackgroundTasks,
          text: str = Form(""),
          response_url: str = Form("")
    ):
        # 直接処理せずに、移譲する
        bg.add_task(query_dns, text, response_url)
        # 空のレスポンスを返せば、まずは何もしない 
        return Response()  

.. revealjs-break::

図解

.. figure:: _images/with-background.png
    :align: center
    :width: 50%

asyncioのイベントループ上で処理しているだけなので、依存関係が増えない。
(ライブラリ的にも連携サービス的にも)

デモ？(擬似的なもの)
--------------------

…これで、真っ当にミニマムなチャットボットが出来ました。
