Sphinx拡張を実装アプローチ+
===========================

.. 4 / 26.5

品質向上〜編

ローカル利用の場合
------------------

トライ＆エラーで十分。

* 困るのは自分だけで済む。
* 実装に失敗していれば、Pythonのスタックトレースが出る。
* 即時対応が難しいけど無視は可能なら、「仕様」と言い張る。

とはいえ…
----------

（特に公開する場合は）考えておいたほうがいい箇所。

* ロギングとエラーハンドリング
* 関数単位でのテスト
* ビルド想定のe2eテスト

ロギング
--------

``sphinx.util.logging`` を利用することで、
Sphinxのビルド時に本体の出力と統一感があるロギングが出来る。

.. code-block:: python

    import sys
    from sphinx.util import logging

    logger = logging.getLogger(__name__)


    def setup(app):
        if sys.version_info.minor < 7:
            logger.info("NOTICE: 動きはするけど、今後サポートから外れます")

エラーハンドリング
------------------

.. container:: emoji-only

    |:thinking_face:|

.. revealjs-break::
  
* 実はあまり気にしていない。

  * 基本的に「拡張利用時の不足のエラー時には速やかにビルド失敗」させるスタンス。
  * 素のエラーだと分かりづらそうなら、適宜解説を差し込む。

* どちらかというと、エラーを必要に応じて握りつぶす傾向。

関数単位でのテスト
------------------

* こちらも「やるに越したことはない」が、複雑そうなときのみ実施。

  * 基本的には単なるPythonモジュールでしかない。
  * 適切な機能分離をして、必要に応じたテストを用意しておけばよい。

* なお、後述の理由からpytestの利用を推奨。

ビルド想定のe2eテスト
---------------------

``sphinx.testing`` を利用できる。

.. code-block:: python

    import pytest
    from bs4 import BeautifulSoup
    from bs4.element import NavigableString, Tag
    from sphinx.testing.util import SphinxTestApp
    
    
    @pytest.mark.sphinx("html")
    def test_default(app: SphinxTestApp, status: StringIO, warning: StringIO):
        app.build()
        out_html = app.outdir / "index.html"
        soup = BeautifulSoup(out_html.read_text(), "html.parser")
        contents = list(soup.h1.children)
        assert len(contents) > 1
        assert isinstance(contents[0], NavigableString)
        assert isinstance(contents[1], Tag)
        assert contents[1].name == "wbr"

公開する？
----------

* 「自分以外にも使いそうじゃない？」と思ったらPyPIに公開してみる。
* 今回は公開手法については省略

  * 単なるPythonパッケージでしか無いので、情報は出回ってる。
  * Search: ``PyPI デビュー``
