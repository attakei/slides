Sphinx拡張 イントロダクション
=============================

.. revealjs-notes:: 3 / 6

Sphinx拡張とは何か
------------------

「Sphinxの機能を拡張」するためのPythonライブラリ。

* モジュールでも良いし、パッケージでも良い
* ローカル管理でも平気（インポートさえできればOK）
* （ちょっと雑だけど） ``conf.py`` 上で実装してもいい

.. revealjs-break::

拡張の使用方法。

.. code-block:: python

    # Optional
    import sys
    sys.path.append(PATH_TO_LOCAL_MODULE)

    extensions = [
        "my_extensoin",
    ]

* ``extensions`` にライブラリ名を追加するだけ
* 必要に応じて ``sys.path`` を編集
* 体裁が整っているなら、よしなに呼ばれる

.. revealjs-break::

.. revealjs-notes::

    引数を1個受け付ける ``setup`` 関数があれば、
    そのモジュールはSphinx拡張として成立する。

最低限「体裁が整っている」コード

.. code-block:: python

    def setup(app):
        print("Hello world")

* ``conf.py`` に記述すると、「ビルド時に ``Hello World`` とコンソール出力する」

Sphinx拡張で実現可能なこと
--------------------------

  ディレクティブの登録
  ／既存ディレクティブへの処理を変更
  ／読み取り可能なフォーマットを追加
  ／新しい出力形式（ビルダー）の追加
  ／出力処理時にデータ加工
  ／その他・Sphinxのビルド処理時の各種処理追加

.. revealjs-break::

ざっくりとした分類

* | 「入力」を拡張する
  | （フォーマットを増やす、文法を増やす）
* | 「出力」を拡張する
  | （フォーマットを増やす、自作テーマ）
* 「内部」で何かする
* (複合系)

拡張の例
--------

* | Sphinx本体にバンドルされているもの
  |  `sphix.ext.autodoc <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_, `sphinx.ext.todo <https://www.sphinx-doc.org/en/master/usage/extensions/todo.html>`_
* | サードパーティ製
  |  :pypi:`myst-parser`, :pypi:`ablog`
* | 自作のもの
  |  :pypi:`sphinx-revealjs`, :pypi:`sphinxcontrib-budoux`
