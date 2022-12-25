PyPICloudからの自己紹介
=======================

PyPICloudとは
-------------

https://pypi.org/project/pypicloud/

  This package is a Pyramid web app that provides a PyPI server where the packages are stored on Amazon’s Simple Storage Service (S3), Google’s Cloud Storage (GCS) or Azure’s Blob Storage.

  ※README序文より引用

意訳すると: S3,GCS,Azure Blobでパッケージファイルを管理できるPyramid製のPyPIサーバー

.. revealjs-break::

https://pypi.org/project/pypicloud/

使用感としては、

* 最初からクラウドサービス上での運用を前提とした
* 各種IaaS向けのインターフェース設計をしている
* プライベートなPyPIサーバーアプリケーション

※もちろんローカルでの利用も可能

ちょっと使ってみる
------------------

.. container:: power-sentence center

    (デモ予定)

.. revealjs-break::

ターミナル1

.. code-block:: shell

    $ python -m venv .venv
    $ . .venv/bin/activate
    (.venv) $ pip install 'pypicloud[server]'
    (.venv) $ pypicloud-make-config config.ini
    (.venv) $ pserve config.ini

ターミナル2

.. code-block:: shell

    $ python -m venv .venv
    $ . .venv/bin/activate
    (.venv) $ pip install --index-url bottle

ところで
--------

* 最初からクラウドサービス上での運用を前提とした
* 各種IaaS向けのインターフェース設計をしている

...って何だ？

pypicloudの仕組み(図解)
-----------------------

.. container:: flex

    .. container:: two-of-third

        PyPICloudに加えて、Storage/Cacheの3層構成

    .. container:: one-of-third

        .. blockdiag::
            :width: 320
            :figwidth: 320

            blockdiag admin {
              orientation = portrait;
              PyPICloud <-> Cache <-> Storage;
            }

.. revealjs-break::

.. container:: flex

    .. container:: two-of-third

        Storageは、実際にインストールされていくパッケージファイルの管理が役割。

        * S3 in AWS
        * GCS in GCP
        * ローカルファイルシステム

    .. container:: one-of-third

        .. blockdiag::
            :width: 320
            :figwidth: 320

            blockdiag admin {
              orientation = portrait;
              PyPICloud <-> Cache <-> Storage;
              Storage [color = pink];
            }

.. revealjs-break::

.. container:: flex

    .. container:: two-of-third

        Cacheはパッケージのメタ情報をファイルから取り出してキャッシュする。
        パッケージの検索や情報閲覧をする際のKVSとして用いる。

        * RDB
        * DynamoDB

    .. container:: one-of-third

        .. blockdiag::
            :width: 320
            :figwidth: 320

            blockdiag admin {
              orientation = portrait;
              PyPICloud <-> Cache <-> Storage;
              Cache [color = pink];
            }

設定ファイルの中身紹介
----------------------

.. code-block:: ini

    [app:main]
    ; PyPICloudに指定パッケージがないときどうするか
    pypi.fallback = cache

    ; everyone = 誰でも、 authenticated = 認証済みユーザーのみ
    ; 読み取り（パッケージ情報の取得・検索など）の権限
    pypi.default_read =
        everyone
    ; 書き込み（パッケージの登録など）の権限
    pypi.default_write =
        authenticated
    ; キャッシュ関連の更新の権限
    pypi.cache_update =
        everyone

.. revealjs-break::

.. code-block:: ini

    ; Storageに何を使うか
    pypi.storage = s3
    storage.XXXXX = XXX

    ; Cacheに何を使うか
    pypi.db = dynamo
    db.region_name = ap-northeast-1
    db.namespace = mypypicloud

    ; 管理者（パッケージをアップロードする人）
    auth.admins =
      admin
    user.admin = $6$rounds=20500$Nooooooooooooooooooooooooooooooooo


構成例
------

.. container:: flex

    .. container:: two-of-third

        シンプルにローカルで動かしてみたり...

    .. container:: one-of-third

        .. blockdiag::
            :width: 320
            :figwidth: 320

            blockdiag admin {
              orientation = portrait;
              PyPICloud <-> Cache <-> Storage;
              Storage [label = "Local filesystem"];
              Cache [label = "Local sqlite3"];
            }

.. revealjs-break::

.. container:: flex

    .. container:: two-of-third

        AWSを可能な限り使ってみたり...

    .. container:: one-of-third

        .. blockdiag::
            :width: 320
            :figwidth: 320

            blockdiag admin {
              orientation = portrait;
              PyPICloud <-> Cache <-> Storage;
              Storage [label = "S3"];
              Cache [label = "DynamoDB"];
              PyPICloud [label = "AppRunner"];
            }

.. revealjs-break::

.. container:: flex

    .. container:: two-of-third

        GCP上で動かしてみたり...

    .. container:: one-of-third

        .. blockdiag::
            :width: 320
            :figwidth: 320

            blockdiag admin {
              orientation = portrait;
              PyPICloud <-> Cache <-> Storage;
              Storage [label = "GCS"];
              Cache [label = "Local sqlite3"];
            }

.. revealjs-break::

.. container:: flex

    .. container:: two-of-third

        特殊な基盤向けに、StorageもCacheを自作してみたり

    .. container:: one-of-third

        .. blockdiag::
            :width: 320
            :figwidth: 320

            blockdiag admin {
              orientation = portrait;
              PyPICloud <-> Cache <-> Storage;
              Storage [label = "Custom Storage"];
              Cache [label = "Custom Cache"];
            }
