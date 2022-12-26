FastAPIでSlashCommandを作る
===========================

.. time: 5

FastAPIとは
-----------

.. ASGI云々については、「ASGIの概要」のアーカイブをどうぞ

.. container:: flex

    .. container:: two-of-third

        Python製Webアプリケーションフレームワーク

        * 名前の通り「高速なAPIサーバー」向け
        * ``Starlette`` というASGIフレームワークを土台にしている

          * 特に何も考えずに、 ``async/await`` 構文が使える

        * ``Flask`` や ``Bottle`` っぽい

    .. container:: one-of-third

        .. figure:: _images/logo-fastapi.png

最小の構成
----------

..
    FastAPI で動作するサーバーの最小構成について。
    ほとんどFlaskあたりと変わってない

ミニマムな ``main.py``

.. code-block:: python

    from fastapi import FastAPI

    app = FastAPI()

    @app.get("/")
    async def hello_world():
        return {"msg": "Hello, World!"}

.. revealjs-break::

.. チュートリアルどおりにuvicornというASGIサーバーで起動

.. container:: flex

    .. container:: half

        サーバーを起動する

        .. code-block:: bash

            $ pip install fastapi uvicorn
            $ uvicorn main:app

            INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
            INFO:     Started reloader process [2719205] using statreload
            INFO:     Started server process [2719212]
            INFO:     Waiting for application startup.
            INFO:     Application startup complete.
            INFO:     127.0.0.1:46564 - "GET / HTTP/1.1" 200 OK

    .. container:: half

        動作確認
        
        .. code-block:: bash

            $ http localhost:8000

            HTTP/1.1 200 OK
            content-length: 23
            content-type: application/json

            {
                "msg": "Hello, World!"
            }

最小の構成との比較
------------------

.. Flask側は若干雑

.. container:: flex

    .. container:: half

        Flask

        .. code-block:: python

            from flask import Flask

            app = Flask(__name__)

            @app.route('/')
            def hello_world():
                return json.dumps({
                    "msg":"Hello, World!"
                })

    .. container:: half

        Fast API

        .. code-block:: python

            from fastapi import FastAPI

            app = FastAPI()

            @app.get("/")
            async def hello_world():
                return {"msg": "Hello, World!"}

※見た目の関係で、意図的にコードを省いています

機能サンプル
------------

.. クエリパラメータ/ポストは全部引数のTypingでバリデーションされる

ページネーション用のクエリパラメータ

.. code-block:: python

    from fastapi import FastAPI

    app = FastAPI()

    @app.get("/items/")
    async def get_items(p: int = 1):
        """ ``/items/``         => ``p`` = 1 
            ``/items/?p=3``     => ``p`` = 3 
            ``/items/?p=three`` => バリデーションエラー
        """
        return {"msg": "Hello World"}

.. revealjs-break::

.. 前述のソースをもとにしたサーバーの動作例

.. container:: flex

    .. container:: half

        .. code-block:: bash

            $ http localhost:8000/items/ p==3
            HTTP/1.1 200 OK

            {
                "msg": "Hello World"
            }

    .. container:: half

        .. code-block:: bash

            $ http localhost:8000/items/ p==three
            HTTP/1.1 422 Unprocessable Entity

            {
                "detail": [
                    {
                        "loc": [
                            "query",
                            "p"
                        ],
                        "msg": "value is not a valid integer",
                        "type": "type_error.integer"
                    }
                ]
            }

その他機能
----------

* OpenAPIの提供
* Pydanticによる恩恵各種
* ミドルウェア
* 各種セキュリティ要求機能（Basic認証,OAuth2）
* Dependency Injection
* Background Task機能
* Starletteが出来ること
