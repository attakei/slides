Cloud Runで運用する
===================

Cloud Runとは
-------------

.. container:: flex

    .. container:: two-of-third

        ..

          コンテナ化されたアプリケーションをすばやく安全にデプロイ、スケーリングできる、フルマネージド型のコンピューティング プラットフォーム

    .. container:: one-of-third

        .. figure:: _images/logo-cloudrun.png
          :width: 50%

        (Cloud Runのトップページより)

.. revealjs-break::

* 割と気軽に
* コンテナWebアプリの実行を
* ドメイン付きで

実現するサービス

3行で説明するCloud Runの使い方
------------------------------

* GCPの契約をして、プロジェクトで必要なサービスを有効化する
* ローカルでDockerアプリを開発してから、イメージをpush
* サービスを起動する

図解
----

.. revealjs-fragments::

    .. container::

        .. container::

            .. figure:: _images/flow-deployment_basic.png

        .. container::

            全てGCPでやる感じだと、こう

            .. figure:: _images/flow-deployment_full_gcp.png

Cloud Run向けDockerfile(例)
---------------------------

.. 普段Poetryを使っているので、Wheelを作るステージと動作させるステージを分けてる

.. code-block:: dockerfile

    # ------------------
    # Build stage
    # ------------------
    FROM python:3.8-slim as buildenv

    RUN mkdir -p /build/chatbot
    COPY chatbot/* /build/chatbot/
    COPY poetry.lock pyproject.toml /build/
    WORKDIR /build
    RUN poetry build

.. code-block:: dockerfile

    # ------------------
    # Running stage
    # ------------------
    FROM python:3.8-slim
    COPY --from=buildenv /build/dist/chatbot-*-py3-none-any.whl /
    RUN pip install /chatbot-*-py3-none-any.whl

    CMD ["uvicorn", "chatbot:app", "--port", "8080"]

Cloud Runのメリット/デメリット
------------------------------

メリット:

* マシン管理が不要になる
* 従量課金
* | HTTPS+FQDNが自動で付与される
  | ( ``{指定名+ランダムな文字列}.a.run.app`` )

.. revealjs-break::

.. 従量課金の常でDDos食らうとお財布が怖い

デメリット:

* サーバー初動が遅い（微妙な頻度でタイムアウトする
* 運用にDockerの知識が少々必要
* DDoS怖い

Cloud Runの未知の部分
---------------------

請求対象期間は、

「リクエストを受け付けてインスタンスが起動した時刻」

から

「インスタンスが最後にリクエストの処理をした時刻」

* 非同期処理している間は？
* インスタンスはいつ停止になる？
