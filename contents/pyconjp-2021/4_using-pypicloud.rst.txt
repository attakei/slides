PyPICloudの使い方あれこれ
=========================

大まかに3種類の使い方を考える
-----------------------------

* LAN内のPyPIプロキシサーバー
* 個人パッケージの公開用サーバー
* 組織用プライベートレジストリ

LAN内のPyPIプロキシサーバー
---------------------------

構成

.. blockdiag::

    blockdiag admin {
      group {
        color = olive;
        shape = line;
        PyPICloud <- Client1;
        PyPICloud <- Client2;
      }
      PyPICloud[color = aqua];
      PyPI <- PyPICloud;
      PyPI[color = lime];
    }

* LAN内(AWS-VPC内)などのパターン
* Clientらは外部アクセスをせず、PyPICloudだけが通信するイメージ

.. revealjs-break::

設定例(抜粋)

.. code-block:: ini

    ; 自身が知らないパッケージはfallback先からダウンロードしてキャッシュする
    pypi.fallback = cache
    ; 上記キャッシュの更新を誰でも出来るようにする
    pypi.cache_update =
      everyone

.. revealjs-break::

特徴とか

* |:o:| 通信経路の限定化が出来る
* |:o:| パッケージがLAN内に残るので、2台目以降が高速
* |:x:| PyPICloudである必要性がない
* |:x:| ゴールデンイメージで十分

個人パッケージの公開用サーバー
------------------------------

構成

.. blockdiag::

    blockdiag admin {
      PyPICloud <- Client;
      PyPI <- Client;
      PyPICloud[color = aqua];
      PyPI[color = lime];
    }

* | 外部公開されたWebアプリケーション
  | (heroku, EC2, docker services)
* Storage, Cacheにはローカル以外を使う（ことが良い）

.. revealjs-break::

設定例(抜粋)

.. code-block:: ini

    ; 自身が知らないパッケージはfallback先へリダイレクトする
    pypi.fallback = redirect
    ; (初期設定)認証済みユーザーによってパッケージをアップロードできる
    pypi.default_write =
      authenticated

.. revealjs-break::

特徴とか

* |:o:| 自分の好きなパッケージを登録できる
* |:o:| 公開サービスなので、READMEの案内がしやすくなる
* |:x:| 他人が利用する可能性があるため、サービス維持を意識する必要がある

組織用プライベートレジストリ
----------------------------

構成

.. blockdiag::

    blockdiag admin {
      PyPICloud <- Client;
      PyPI <- Client;
      PyPICloud[color = aqua];
      PyPI[color = lime];
    }

* | Webアプリケーション(heroku, EC2, docker services)
  | アクセス制限はあったほうが良い（なくても一応平気） 
* Storage, Cacheにはローカル以外を使う（ことが良い）

.. revealjs-break::

設定例(抜粋)

.. code-block:: ini

    ; 自身が知らないパッケージはfallback先へリダイレクトする
    pypi.fallback = redirect
    ; アクセス自体も認証状態であることを求める
    pypi.default_read =
      authenticated

.. revealjs-break::

特徴とか

* |:o:| アクセス制限のあるPyPIを提供できるので、プライベートなパッケージを気兼ねなく登録できる
* |:x:| 組織内で積極利用することが前提になり、きちんとしたサービス維持を要求される
