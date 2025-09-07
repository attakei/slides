:og:image: _images/ogp/pyconjp-2019/index.png
:og:description: PyCon JP 2019 のトークセッションで発表したプレゼンテーションです

===========================================
Ansibleを通じて「べき等性」を理解してみよう
===========================================

.. revealjs-slide::
    :theme: css/my-solarized-nijibox-tr.css
    :conf: {"width":1024,"height":768}

:date: 2019-09-17
:author: Kazuya Takei
:location: PyCon JP 2019

イントロ
========

.. 90sec

.. include:: 1_whoami-201909-public.rst.txt

.. include:: 2_whoami-201909-private.rst.txt


話すこと(目標)
--------------

* 冪等性の概要

  * あっさり

* Ansibleについて

  * 前置き

* Ansibleはどうやって「冪等性」を担保しているか

  * メイン予定

冪等性の概要
==============

※超概要です

「冪等性」とは
----------------

.. 30sec

冪等 = べきとう

ある操作を何度実施しても、同じ結果になる性質を持つこと。

  f(x) = f(f(x)) = f(f(f(x))) ...

「冪等性」の例
----------------

.. 30sec

.. code-block:: python

    >>> def add_zero(x):
    >>>     return x + 0
    >>>
    >>> x = 2019
    >>> x = add_zero(x)
    >>> x
    2019
    >>> x = add_zero(x)
    >>> x
    2019
    >>> add_zero(add_zero(add_zero(add_zero(x))))
    2019

.. revealjs-break::

.. 30sec

.. code-block:: python

    >>> def multi_one(x):
    >>>     return x * 1
    >>>
    >>> x = 2019
    >>> x = multi_one(x)
    >>> x
    2019
    >>> x = multi_one(x)
    >>> x
    2019
    >>> multi_one(multi_one(multi_one(multi_one(x))))
    2019


Ansibleについて
===============

Ansibleとは
-----------

.. 60sec

* Python製の「構成管理ツール」
* 「動作」ではなく「状態」を定義して適用する
* 主にサーバーのセットアップなどに使われる
* etc

  * クライアントPC
  * ネットワーク機器
  * クラウドサービス

コミュニティあります
--------------------

.. 30sec

.. figure:: _images/ansible-jp.png
    :scale: 50%
    :align: center

* サイト: https://ansiblejp.github.io/
* Connpass: https://ansible-users.connpass.com/
* Slack: https://bit.ly/ansiblejp-slack

Ansibleの動き(概要)
-------------------

.. 30sec

.. figure:: _images/ansible-playbook-demo.png
    :align: center

Ansibleの動き(中身)
-------------------

.. 60sec

.. .. todo:: 上記デモのPlaybook

インベントリファイル

* 処理実行先のサーバー一覧や簡単な情報を定義

.. literalinclude:: _includes/ansible-playbook-demo.inventory

.. revealjs-break::

Playbook

.. literalinclude:: _includes/ansible-playbook-demo.yml

.. revealjs-break::

Playbook

* 実際にAnsibleが操作したい状態を定義したもの
* **動作ではなく状態**

  * 「httpdをインストールする」という動作ではない
  * 「httpdをインストールされていること」という状態

処理の流れ
----------

.. 60sec

* Playbookに定義された状態になるように、各モジュールがよしなに処理する
* 処理の結果、「状態に変化があったか」の報告を受ける。

  * 変化があれば ``changed``
  * 変化がなければ ``ok``

同じPlaybookを実行すると、2回め以降は状態に変化がないのでOKとしかでない

= **ある操作を何度実施しても、同じ結果になる**

= **冪等性がある**


Ansibleが担保する冪等性
-------------------------

.. 20sec

定義された **「状態に対する冪等性」** を担保するように設計されている

※ログ出力があるので、マシン全体の冪等性は無理

Ansibleはどうやって、冪等性を担保するか？(1)
============================================

pip モジュール
--------------

.. 30sec

* ``pip`` コマンド経由で、Pythonパッケージの状態を管理するモジュール
* ``virtualenv`` の指定や作成もできる
* ``extra_args`` 経由で全部のオプションを指定可能

.. code-block:: yaml

    - hosts: local
      tasks:
        pip:
          name: django
          executable: pip3
          extra_args: --user

モジュールの全体像
------------------

.. 60sec

..
    * これは、Ansibleサイトにあるモジュールdocのソースを含むため
    * 説明、実行例、実行結果のパターンなどが一通り揃ってる

.. figure:: _images/github-ansible-pip.png
    :scale: 20%
    :align: center


.. revealjs-break::

`※GitHubより <https://github.com/ansible/ansible/blob/v2.8.0/lib/ansible/modules/packaging/language/pip.py>`_

* 全771行!
* 前半の約半分はドキュメント
* 残りのソースには、処理に必要な全内容がコードで書かれがち
* そのため、モジュールのソースは長めにになる傾向が強い

.. revealjs-break::

.. 45sec

大まかな流れ

* 実行環境の設定
* 実行コマンドの組み立て
* コマンドの実行
* 実行結果の検査
* モジュールとしての結果を返す

モジュールから抜粋
------------------

.. figure:: _images/pip-module_1-1.png
    :align: center

.. revealjs-break::

.. 30sec

.. figure:: _images/pip-module_1-2.png
    :align: center

.. revealjs-break::

.. 20sec

.. figure:: _images/pip-module_2-2.png
    :align: center

.. revealjs-break::

.. 20sec

.. figure:: _images/pip-module_3-2.png
    :align: center

.. revealjs-break::

.. figure:: _images/pip-module_4-1.png
    :align: center

.. revealjs-break::

.. 30sec

.. figure:: _images/pip-module_4-2.png
    :align: center

.. revealjs-break::

.. 30sec

.. figure:: _images/pip-module_4-3.png
    :align: center

.. revealjs-break::

.. 30sec

.. figure:: _images/pip-module_4-4.png
    :align: center

モジュールの単体実行の様子
--------------------------

.. 60sec

1回目

.. figure:: _images/ansible-django-changed.png
    :scale: 50%
    :align: center

.. revealjs-break::

2回目

.. figure:: _images/ansible-django-ok.png
    :scale: 50%
    :align: center


ここまで
--------

* パラメーターに従って、 ``pip`` コマンドをただただ実行
* 実行結果（リターンコード、標準出力、標準エラー）をもとに、どうなったかを判定
* ``pip`` コマンド自体が冪等性を持っているため、割とそれに信頼性を委任

Ansibleはどうやって、冪等性を担保するか？(2)
==============================================

amazon-linux-extras モジュール
------------------------------

* Amazon Linux 2が持つパッケージリポジトリの状態を管理できるもの
* コマンド自体が割と冪等性を持っているけど、 ``command`` モジュールで呼ぶのもあれなので自作してみた

※前述のpipモジュールなどを見る前に、ドキュメントだけ読んで作ってみたものです

.. code-block:: yaml

    - hosts: local
      tasks:
        - amazon2extras: name=php7.3
        - yum: name=php7.3

モジュールの全体像
------------------

.. 60sec

..
    * これは、Ansibleサイトにあるモジュールdocのソースを含むため
    * 説明、実行例、実行結果のパターンなどが一通り揃ってる


.. figure:: _images/github-ansible-amazon-linux-extras.png
    :scale: 20%
    :align: center


.. revealjs-break::

* 全771行!
* 前半の約半分はドキュメント
* 残りのソースには、処理に必要な全内容がコードで書かれがち
* そのため、モジュールのソースは長めにになる傾向が強い

.. revealjs-break::

.. 45sec

やってること

* トピックの検索
* 状態の確認（有効/無効の判定）
* 状態と設定をもとにしたコマンドの実行
* コマンド実行の際には結果を確認

モジュールのコード(抜粋)
------------------------

.. figure:: _images/amzn2extras-module_1.png
    :align: center

.. revealjs-break::

.. 30sec

.. figure:: _images/amzn2extras-module_2.png
    :align: center

ここまで
--------

* 必ず状態をチェックして、「コマンドの実行可否」を決めている

  * ``present`` なのに、「まだ有効になってない」なら有効にするコマンドを実行
  * ``absent`` なのに、「すでに有効になっている」なら無効にするコマンドを実行
  * 「状態を変える必要がない」なら、なにもしない

「余計なことはしない」ことで冪等性を担保している

おわりに
========

まとめ
------

.. 60sec

* | 冪等性とAnsibleの概要をふまえて、
  | モジュルールのコードを追ってみました
* | 冪等性の担保には、「現在と目標とのズレ」や
  | 「初期状態x処理のパターン把握」が重要
* 冪等性を担保するソフトを利用してても、それは変わらない
* 冪等性はどこにでもいる

おまけ：他にもある「冪等性」
----------------------------

.. 45sec

* git pull

  * リモートが変化しない間の正常なpullは何度やっても結果が同じ

* データベースマイグレーション

  * スキーマの状態に対して、冪等性を担保する

* Let's Encrypt

  * 「FQDNへの証明書があること」に対して、冪等性を担保する

(終)
