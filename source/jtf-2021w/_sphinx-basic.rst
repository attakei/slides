Sphinxと普段の役割
==================

|:arrow_right:| > |:blue_square:| > |:blue_square:|

.. 2.5+4min, Sphinxを普段使ってる人以外向けのかんたんな説明

Sphinx
------

3行で

* 複数の出力形式に対応した
* 拡張性の高い
* Python製ドキュメンテーションビルダー

ドキュメンテーションビルダー
----------------------------

ドキュメントのソースから

* ドキュメント間の相互参照
* 階層構造の構築
* ソースコードハイライト
* etc

を行い、ドキュメント全体を組み立てる

.. blockdiag::
    :alt: フロー
    :align: center
    :figclass: diag

    blockdiag {
        default_fontsize = 16
        node_width = 240
        node_height = 80

        SRC [label = "SOURCES", stacked]
        SPX [label = "Sphinx", shape = ellipse]
        DST [label = "DOCUMENTATION", stacked]

        SRC -> SPX -> DST
    }

Sphinxが取り扱うソース
----------------------

* reStructuredText
* Markdown
* (etc)

.. blockdiag::
    :alt: フロー
    :align: center
    :figclass: diag
    
    blockdiag {
        default_fontsize = 16
        node_width = 240
        node_height = 80

        MD [label = ".rst", stacked]
        RST [label = ".md", stacked]
        SPX [label = "Sphinx", shape = ellipse]
        DST [label = "DOCUMENTATION", stacked]

        MD, RST -> SPX -> DST
    }

Sphinxが取り扱うビルド先
------------------------

* HTML
* ePub
* PDF(LaTex)
* man
* (etc)

.. blockdiag::
    :alt: フロー
    :align: center
    :figclass: diag
    
    blockdiag {
        default_fontsize = 16
        node_width = 240
        node_height = 80

        SRC [label = "SOURCES(.md , .rst)", stacked]
        SPX [label = "Sphinx", shape = ellipse]
        HTML [label = "HTML,EPUB", stacked]
        PDF [label = "PDF", stacked]

        SRC -> SPX -> HTML,PDF
    }

Sphinxを使ったサイト
--------------------

いっぱいある

* | `Python documentation <https://docs.python.org/3/>`_
  | ... Python本体
* | `Django documentation <https://docs.djangoproject.com/en/3.1/>`_
  | ... Python製Webアプリケーションフレームワーク
* | `NumPy Manual <https://numpy.org/doc/stable/>`_
  | ... Python製の数値計算ライブラリ

...その他、Pythonパッケージいっぱい

.. revealjs-break::

まだまだある

* | `Ansible documentation <https://docs.ansible.com/>`_
  | ... Python製の構成管理ツール
* | `cloud-init Documentation <https://cloudinit.readthedocs.io/en/latest/>`_
  | ... Python製のインスタンス初期設定ツール
* | `phpMyAdmin documentation <https://docs.phpmyadmin.net/en/latest/>`_
  | ... PHP製のデータベース操作Webアプリ

.. revealjs-break::

まだまだある

* | `calibre User Manual <https://manual.calibre-ebook.com/>`_
  | ... 電子書籍管理ツール
* | `Flatpak <https://docs.flatpak.org/en/latest/>`_
  | ... Linux向けアプリケーションパッケージャー 
* | `Ubuntu packaging guide <https://packaging.ubuntu.com/html/>`_
  | ... 名前の通り

Sphinxを使った書籍
------------------

(書籍執筆のどこかの工程でSphinxを使っているもの)

* `Go言語による並行処理 <https://www.oreilly.co.jp/books/9784873118468/>`_
* `Pythonプロフェッショナルプログラミング第3版 <https://www.shuwasystem.co.jp/products/7980html/5382.html>`_
* `独学プログラマー <https://shop.nikkeibp.co.jp/front/commodity/0000/C92270/>`_
* `エキスパートPythonプログラミング改訂2版 <https://asciidwango.jp/post/171156307275/>`_
* `仕事ではじめる機械学習 <https://www.oreilly.co.jp/books/9784873118253/>`_
