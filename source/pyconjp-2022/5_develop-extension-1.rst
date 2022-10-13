Sphinx拡張の実装アプローチ
==========================

..  15.5 / 11

基本実装〜編

.. revealjs-break::
    :notitle:

ここからはの話は、


Sphinx拡張を実装する際によく取り扱う箇所

.. revealjs-fragments::

    = ポイントとして抑えておくと良い箇所

再掲：最低限「体裁が整っている」コード
--------------------------------------

.. code-block:: python

    def setup(app):
        print("Hello world")

Sphinx拡張の実態
----------------

大雑把に書くと、以下のような要素たちの集まり

* 追加の入出力を定義するための関数/クラス群
* イベントハンドラ用の関数群
* ★Sphinx本体から呼び出される ``setup`` 関数
* 補助処理

setup を制するものはSphinxを制す？
----------------------------------

``setup()`` の役割

* | 設定項目の宣言
  | => ``app.add_config_value``
* | ディレクティブ/ビルダー等の登録
  | => ``app.add_builder`` 他
* | イベントハンドラの登録
  | => ``app.connect``

.. revealjs-fragments::

    ...これらは、いずれも「Sphinxのメイン処理開始までに完遂しないと困ること」

.. revealjs-break::

``setup()`` の役割

.. figure:: _images/setup-flow-1.svg
    :align: center

Sphinxから呼ばれるのはsetupのみ

.. revealjs-break::

``setup()`` の役割

.. figure:: _images/setup-flow-2.svg
    :align: center

メイン処理以降は、登録済みのものを扱うだけ

setup関数/設定項目の宣言
------------------------

.. code-block:: python

    def setup(app):
        app.add_config_value(
            "config_name",  # 名前
            [],             # 初期値
        )

* 拡張の「動作」を設定させるための項目を宣言。
* Sphinx全体で重複しないように注意が必要。

例)

| ``sphinxcontrib-budoux / budoux_targets``
| => BudouXに解析して欲しいタグのリスト

.. todo:: 理論上はPythonオブジェクトなら何でもイケるが、無茶はしないこと

ディレクティブ等の登録
----------------------

入力(出力)に関する拡張をしたいときに必要となるもの。

* ディレクティブ
* ノード
* ロール
* ...他にもあれこれ

.. revealjs-break::

.. code-block:: rst

    .. oembed:: https://twitter.com/attakei/status/1575887211962290176

    .. oembed:: https://www.youtube.com/watch?v=Jn2zvfDhU0w

Sphinx本体には無いディレクティブなので、自作＆登録が必要。

.. revealjs-break::

.. code-block:: python

    from sphinx.directives import SphinxDirective

    class OembedDirective(SphinxDirective):
        ...

        def run(self):
            # 略
            node = oembed()
            ...
            # 略 - nodeの属性に各種データを引き渡す
            ...
            return [node]  #  docutilsのノードを持つリストを返す

    def setup(app):
        app.add_directive("oembed", OembedDirective)

.. revealjs-break::

* ディレクティブを用意するなら、まずノードも必要。
* ノードは出力にも関わるので、出力の実装もセット。

.. figure:: _images/rst-to-docutils.svg
    :align: center

.. revealjs-break::

.. code-block:: python

    from docutils import nodes

    class oembed(nodes.General):
        # 大抵の場合は、ディレクティブ側で処理をするので
        # 何もしないことが多い
        pass

    class visit_oembed_node(self, node):
        if "content" in node and "html" in node["content"]:
            self.body.append(node["content"]["html"])

    class depart_oembed_node(self, node):
        pass

.. revealjs-break::

.. code-block:: python

    def setup(app):
        app.add_node(
            oembed,
            # ビルダー種別ごとに、どんな処理をさせたいか指定する
            html=(visit_oembed_node, depart_oembed_node)
        )

ビルダー(概要のみ)
------------------

「既存のビルダーの枠組みではどうにもならない出力」をしたいときに、
頑張って用意する存在。

Sphinxコアイベントとハンドラ
----------------------------

| コアイベント：
| 　ビルド処理内に用意された、いくつかの追加処理向けタイミング

* イベントハンドラ関数を登録して、適宜実行させられる
* 処理直後のデータが引数で渡され、その場での加工などが役割
* ドキュメントにあるだけで18箇所
* 自分でイベントを足せる

.. revealjs-break::

.. code-block:: python

    def some_func(app, config):
        ...

    def some_func2(app):
        ...

    def setup(app):
        # 本体のイベントに接続
        app.connect("config-inited", some_func)
        # イベントを独自定義した上で、接続
        app.add_event("event-for-my-extension")
        app.connect("event-for-my-extension", some_func2)

Sphinx拡張からは、 ``app.connect()`` で関数を登録するだけで良い。

.. revealjs-break::

公開されているイベント（見切れてますし、増やせます）

- ``builder-inited``
- ``config-inited``
- ``env-get-outdated``
- ``env-purge-doc``
- ``env-before-read-docs``
- ``source-read``
- ``object-description-transform``
- ``doctree-read``
- ``missing-reference``
- ``warn-missing-reference``
- ``doctree-resolved``
- ``env-merge-info``
- ``env-updated``
- ``env-check-consistency``
- ``html-collect-pages``
- ``html-page-context``
- ``linkcheck-process-uri``
- ``build-finished``

.. revealjs-break::

イベントタイミングの目安（参考）

.. figure:: _images/core-events.svg
    :align: center

.. revealjs-break::

使いがちなコアイベント

``html-page-context``

* ドキュメントごとのHTMLファイルを生成するタイミングのイベント
* 生成時のテンプレート自体を切り替えたり、テンプレートに渡す値を加工したりと大活躍
* あくまで「出力直前」であることに注意

.. revealjs-break::

使いがちなコアイベント

``config-inited``

* ``conf.py`` からConfigオブジェクトを生成した直後のイベント
* コアイベントとしては、一番最初のタイミング
* 「拡張の都合でビルダーを生成するより前にしておきたいこと」のために必要

イベントハンドラの中身を実装する
--------------------------------

「その拡張が何をしたいか」を踏まえた上で、
「どのタイミングで」「どんな処理をすべきか」を整理する。

その上で、必要な実装をする。

.. revealjs-break::

``sphinxcontrib-budoux`` の場合。

.. code-block:: python

    def apply_budoux(app, page_name, template_name, context, doctree):
        context["body"] = update_body(context["body"])

    def setup(app):
        app.ocnnect("html-page-context", apply_budoux)

.. revealjs-fragments::

    * | ページごとの出力HTMLを加工したい
      | = ``body`` をいじりたい
    * ``html-page-context`` イベントで処理する
    * 引数を調べて、実装する

ここまで整理
------------

* setup関数が第一。ここで、もろもろをSphinx本体に登録できる。
* 文法を増やしたいなら、ディレクティブ・ノードなどの設計・登録する。
* 本体の処理に割り込みたいなら、イベントハンドラの設計・登録する。
