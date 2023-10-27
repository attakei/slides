Pythonパッケージを開発する
==========================

.. revealjs-notes:: 14

基本的な流れ
------------

* (想起する)
* セットアップする
* 開発する
* テストをする
* ドキュメントを書く
* パッケージングする
* アップロードする

セットアップする
----------------

パッケージに必要なファイルを準備する。

必要なもの：

* Pythonパッケージ本体
* pyproject.toml

.. container:: align-right

    **以上（あくまで最小要件）**

.. revealjs-break::

pyproject.toml (Pythonパッケージのメタデータなどを管理するファイル)

.. code-block:: yaml

    # Pythonパッケージの基本情報たち
    [project]
    name = "atsphinx-buildtime"
    description = "Simple build-time logger for Sphinx."
    requires-python = ">=3.7"
    dependencies = ["Sphinx"]
    dynamic = ["version"]

    # sdist/bdistを作成する際のツール定義
    [build-system]
    requires = ["setuptools", "setuptools-scm"]
    build-backend = "setuptools.build_meta"

    # ビルドツールのオプション
    [tool.setuptools.dynamic]
    version = {attr = "atsphinx.buildtime.__version__"}

.. revealjs-break::

``[project]`` の要素例

* name                  ... パッケージ名
* version               ... バージョン情報
* description           ... パッケージの説明
* scripts               ... CLIコマンド
* dependencies          ... 依存パッケージの情報
* optional-dependencies ... 直接依存しないパッケージの情報

.. revealjs-break::

``[project]`` の要素例

* requires-python ... 必要なPython実行環境のバージョン
* license         ... 配布時のライセンス
* classifiers     ... PyPIの分類情報( `詳細 <https://pypi.org/classifiers/>`_ )
* urls            ... パッケージの関連サイト
* dynamic         ... 外部ファイルから取り込む値

※より詳しくは :pep:`621` へ

.. revealjs-break::

必要なもの(再掲)：

* Pythonパッケージ本体
* pyproject.toml

| **Q**
| これだけ？

| **A**
| 一応、あれこれ考えずに最近のPython実行環境のみを前提にすれば、ビルドツールがよしなにやってくれる。

開発する
--------

各自の環境でPythonパッケージの開発を進める。

* Editable Install ( ``pip install -e .`` 等)を利用すると楽。
* 「どのPythonバージョンまでサポートするか」「依存パッケージがどこまでサポートしているか」

  * 例：パターンマッチングを使うならPython 3.9を見捨てる。
  * 目安として、PythonのEOLを見ると良い。
  * :strike:`Python 2.xは忘れましょう`

.. revealjs-break::

なるべく早いうちに。

* フォーマッターによる記述の統一 (:pep:`8` , isort , 他 )
* 静的解析ツールによる不要な記述の除去 ( pyflake , 他)
* docstringの記述

テストする
----------

「この呼び出しをしたら、この結果が返る」を担保する行為。

* トレンド的にはpytestを推奨
* ある意味、自分の不安との戦い
* 個人的には、社内のプロダクト開発以上に重要

  * 他者（不特定多数）への動作保証のエビデンス
  * 周辺の変化に追従する指針になる

* 「好きとか嫌いとかはいい、練習してテストを書けるようになるんだ」 [#]_

.. [#] https://2023-apac.pycon.jp/timetable?id=MBSPYH

ドキュメントを書く
------------------

他者が使うことを想定して、「利用法」などをまとめる。

* テストより人に優しいので、ある方が良い。
* ツールは様々

  * Sphinx
  * MKDoc
  * (etc)

パッケージングする
------------------

ソースコードをsdist(tar.gz)にしたり、bdist(wheel)を作成したり。

* ツールは様々。 [#]_

  * setuptools, flit, poetry, rye ...
  * pyprojectがちゃんとしているなら、pyproject-buildを使うと単一コマンドにできて楽...かもしれない。

* `PyPA <https://www.pypa.io/en/latest/>`_ に感謝を。

.. [#] 何割かは最初に知ったビルドツールを親とみなす

アップロードする
----------------

PyPIにsdist,bdistを登録する。

* ビルドツール内の機能でそのままアップロードまでできるものが多い。
* 個別に実施するときでも、 twine で十分。

.. code-block:: console

    pyproject-build
    twine upload dist/*

.. revealjs-break::

この時点までに、PyPIのアカウントを作成する必要あり。

.. container:: r-stack

    .. figure:: _images/api-token-before.png
        :align: center
        :class: fragment

    .. figure:: _images/api-token-after.png
        :align: center
        :class: fragment

.. revealjs-break::

.. container:: r-fit-text

    |
    | おめでとう！あなたはPyPIデビューできました！

.. container:: align-right

    …ひとまずは。