FastAPIでChatBotローカル開発(1)
===============================

フォルダ構成
------------

  | + chatbot.py
  | + poetry.lock
  | + pyproject.toml

* ``pyproject.toml`` はウィザードに従い作成
* ``poetry.lock`` はそこから自動生成

``pyproject.toml``
------------------

重要なところだけ抜粋

.. code-block:: toml

    [tool.poetry]
    name = "chatbot"

    [tool.poetry.dependencies]
    python = "^3.8"
    # 本体
    fastapi = "^0.60.1"
    # POSTリクエスト時にformdataを受け付けるのに必要
    python-multipart = "^0.0.5"
    # ASGIサーバー
    uvicorn = "^0.11.7"

``chatbot.py``
--------------

.. POSTとして受け取るために、Formをデフォルト引数にしている

.. code-block:: python

    from fastapi import FastAPI, Form

    app = FastAPI()

    @app.post("/slash-commands/hello")
    async def hello(text: str = Form(...), user_name: str = Form(...)):
        return {
            "text": f"Hello {user_name}, I recieved `{text}`"
        }

ルーティング関数のデフォルト引数が ``Form`` の場合、
POSTリクエストから取る

動きを確認
----------

.. code-block:: bash

    $ http --form localhost:8000/slash-commands/hello text=Example user_name=attakei
    HTTP/1.1 200 OK
    content-length: 46
    content-type: application/json
    date: Fri, 28 Aug 2020 18:14:23 GMT
    server: uvicorn

    {
        "text": "Hello attakei, I recieved `Example`"
    }

実際に動かす
------------

- 試したいワークスペースにSlashCommandを作成して
- コマンドとURLの組み合わせを登録すれば
- |:tada:| 準備完了です |:tada:|

→→ デモ？
