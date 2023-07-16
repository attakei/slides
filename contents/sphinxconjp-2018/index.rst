:og:image: _images/ogp/sphinxconjp-2018/index.png
:og:description: SphinxCon JP 2018 のLTセッションで発表したプレゼンテーションです

=======================================================
素材の良さを活かしつつ、reSTをReveal.jsに変換してみる話
=======================================================

.. revealjs-slide::
    :theme: css/sphinxconjp-2018.css
    :google_font: Noto Sans JP
    :conf: {"transition": "none", "controls": false}

:by: Kazuya Takei
:on: 2018-11-28
:in: SphinxCon JP 2018

話すこと
========

* 自己紹介
* 「reveal.jsに変換してみる」
* 「素材の良さを活かす」
* 変換で得た知見(3ケース)
* まとめ

Who am I?
=========

.. 目安:1分ぐらい

.. figure:: https://attakei.net/_static/images/icon-attakei.jpg
    :align: right

Kazuya Takei
------------

* Pythonista

  * Errbotプラグイン/Errcron
  * Ansibleロール

* @attakei

  * Twitter/GitLab/GitHub

* NIJIBOX Co., Ltd

  * サーバサイド領域主体(インフラがメイン)
  * アーキテクト


「reSTをReveal.jsに変換してみる」
=================================

.. 目安:2分ぐらい

Reveal.jsの特徴
---------------

  reveal.js enables you to create beautiful interactive slide decks using HTML.

  -- https://revealjs.com より

* HTMLを使ったプレゼンテーションツール
* 横だけでなく縦へのスライド進行
* プラグインによる拡張

  * Markdownサポート
  * PDF用のCSS

reSTをReveal.jsに変換するアプローチ
-----------------------------------

* ``raw:: html`` ディレクティブでゴリ押し(?)
* `rst2reveal <https://github.com/vitay/rst2reveal>`_
* `rst2slides <https://github.com/LLNL/rst2slides>`_
* `sphinxjp.themes.revealjs <https://pypi.org/project/sphinxjp.themes.revealjs/>`_

「素材の良さを活かす」
======================

.. 目安:2分ぐらい

素材としてのreStructudedText
----------------------------

* Markdownより表現できるものが多い
* セクション管理ができる
* 「コメント」を書ける
* ディレクティブを自作して、表現の拡張が可能

器具としてのSphinx
------------------

* 普通に使っても、いい感じにHTMLを出力してくれる
* テーマの変更が容易
* 出力形式の拡張も容易

希望
----

..  ビルダーまで求めた理由も説明
    * ディレクティブの挙動を差し替えたかった
    * HTMLままの表現でも出力してみたかった

* reSTの文法をそのまま使えて
* 拡張ディレクティブの追加を最低限で済ませる

を実現する

* Sphinx拡張(ビルダー, ディレクティブ, etc)
* Sphinxテーマ

が欲しい


作ってみた
----------

`sphinx-revealjs 0.3.1 <https://pypi.org/project/sphinx-revealjs/>`_

* Sphinx拡張

  * テーマ自体の内包はしている
  * Sphinxのファイルを全部、それなりにいい感じのreveal.jsに変換する

特徴
----

* reSTのセクション構造をそのままネストされたスライドにする
* reSTのコメントをスピーカーノートとする
* ``revealjs`` という別ビルダーにしたので、万が一普通のHTMLにしたいときも阻害しない

.. blockdiag::
    :align: center

    blockdiag {
        default_linecolor = olive;

        reST [stacked];
        Sphinx [shape = "ellipse"];
        HTML [stacked, shape = "roundedbox"];
        revealjs [stacked, shape = "roundedbox"];
        reST -> Sphinx [thick];
        Sphinx -> HTML [thick];
        Sphinx -> revealjs [thick];
    }


ここからは
----------

実装時に出てきた「これをこうしたい」を元に、「reSTをこう活用した」という事例をお送りします

活用1: コメントをスピーカーノートにせよ
=======================================

.. 目安:1分ぐらい

reSTのセクション構造
--------------------

.. literalinclude:: _includes/demo.rst.txt
    :language: rst
    :linenos:
    :lines: 19-20

こうなって欲しい
----------------

.. code-block:: html

    <aside class="notes">
    This is comment
    With multiline</aside>

https://github.com/hakimel/reveal.js#speaker-notes


htmlビルドでの挙動
------------------

.. code-block:: html

    ※何も出ない

pseudoxmlにする
---------------

.. code-block:: xml

    <comment xml:space="preserve">
        This is comment
        With multiline

どうする？
----------

* HTMLビルドでは、commentノードはまるごと無視している
* これを、reveal.jsのスピーカーノートに差し替える

``sphinx.writers.html5.HTML5Translator`` より

.. code-block:: python

    def visit_comment(self, node):
        # type: (nodes.Node) -> None
        raise nodes.SkipNode

こうする
--------

.. code-block:: python

    def visit_comment(self, node: comment):
        self.body.append('<aside class="notes">\n')

    def depart_comment(self, node: comment):
        self.body.append('</aside>\n')

* ``SkipNode`` を投げなくすることで、中身をそのまま出せるようにする
* ``visit_comment`` , ``depart_comment`` で中身を ``aside`` タグで囲めばスピーカーノートの出来上がり


難点
----

* これだと、「本当にコメントアウトしたいこと」が消せなくなる

  * 需要があるかはわからない
  * ``revealjs_note`` みたいなディレクティブを作れば解決する話ではある

    * 今回は「ディレクティブを少なくする」を優先


活用2: コードブロックをReveal.jsに合わせよ
==========================================

.. 目安:1分ぐらい

reSTのセクション構造
--------------------

.. literalinclude:: _includes/demo.rst.txt
    :language: rst
    :linenos:
    :lines: 22-25

こうなって欲しい
----------------

.. code-block:: html

    <pre><code class="python">
    def hello():
        return 'world'</code></pre>

https://github.com/hakimel/reveal.js#code-syntax-highlighting

htmlビルドでの挙動
------------------

.. code-block:: html

    <div class="highlight-python notranslate">
      <div class="highlight">
        <pre>
        <span></span>
        <span class="k">def</span> <span class="nf">hello</span><span class="p">():</span>
            <span class="k">return</span> <span class="s1">&#39;world&#39;</span>
        </pre>
      </div>
    </div>

pseudoxmlにする
---------------

.. code-block:: xml

    <literal_block
          force_highlighting="True"
          highlight_args="{}"
          language="python"
          linenos="False"
          xml:space="preserve">
        def hello():
            return 'world'

どうする？
----------

* ``code-block`` は ``literal_block`` を作るのだが、中はそこそこ複雑なことをしている
* reveal.js的には ``highlight.js`` に任せたいので、簡略化するのが一番速そう

``sphinx.writers.html5.HTML5Translator`` より

.. code-block:: python

    def visit_literal_block(self, node):
        # type: (nodes.Node) -> None
        if node.rawsource != node.astext():
            # most probably a parsed-literal block -- don't highlight
            return BaseTranslator.visit_literal_block(self, node)

        lang = node.get('language', 'default')
        linenos = node.get('linenos', False)
        highlight_args = node.get('highlight_args', {})
        highlight_args['force'] = node.get('force_highlighting', False)
        if lang is self.builder.config.highlight_language:
            # only pass highlighter options for original language
            opts = self.builder.config.highlight_options
        else:
            opts = {}

        highlighted = self.highlighter.highlight_block(
            node.rawsource, lang, opts=opts, linenos=linenos,
            location=(self.builder.current_docname, node.line), **highlight_args
        )
        starttag = self.starttag(node, 'div', suffix='',
                                 CLASS='highlight-%s notranslate' % lang)
        self.body.append(starttag + highlighted + '</div>\n')
        raise nodes.SkipNode

こうする
--------

* やってることはスピーカーノートのときとおおむね同じ
* ``literal_block`` は ``language`` 属性を持つので、引き継ぐとよい

.. code-block:: python

    def visit_literal_block(self, node: literal_block):
        lang = node['language']
        self.body.append(
            f'<pre><code data-trim data-noescape class="{lang}">\n')

    def depart_literal_block(self, node: literal_block):
        self.body.append('</code></pre>\n')

難点
----

* ``pygments`` を捨てた

  * ``highlight.js`` ⊂ ``pygemnts`` の場合、非対応言語が出たかも
  * reveal.jsに寄せることを重視

活用3: セクション構造をReveal.jsへ持ち込め
==========================================

.. 目安:2分ぐらい

reSTのセクション構造
--------------------

.. literalinclude:: _includes/demo.rst.txt
    :language: rst
    :linenos:
    :lines: 1-14

こうなって欲しい
----------------

.. code-block:: html

    <section>
      <h1>Title</h1>
    </section>
    <section>
      <section>
        <h2>Section 1.</h2>
      </section>
      <section>
        <h3>Section 1.1.</h3>
      </section>
      <section>
        <h3>Section 1.2.</h3>
      </section>
    </section>
    <section>
      <section>
        <h2>Section 2.</h2>
      </section>
      <section>
        <h3>Section 2.1.</h3>
      </section>
    </section>

htmlビルドでの挙動
------------------

.. code-block:: html

    <div class="section" id="title">
      <h1>Title<a class="headerlink" href="#title" title="このヘッドラインへのパーマリンク">¶</a></h1>
      <div class="section" id="section-1">
        <h2>Section 1.<a class="headerlink" href="#section-1" title="このヘッドラインへのパーマリンク">¶</a></h2>
        <div class="section" id="content-1-1">
          <h3>Content 1.1.<a class="headerlink" href="#content-1-1" title="このヘッドラインへのパーマリンク">¶</a></h3>
        </div>
        <div class="section" id="content-1-2">
          <h3>Content 1.2.<a class="headerlink" href="#content-1-2" title="このヘッドラインへのパーマリンク">¶</a></h3>
        </div>
      </div>
      <div class="section" id="section-2">
        <h2>Section 2.<a class="headerlink" href="#section-2" title="このヘッドラインへのパーマリンク">¶</a></h2>
        <div class="section" id="content-2-1">
          <h3>Content 2.1.<a class="headerlink" href="#content-2-1" title="このヘッドラインへのパーマリンク">¶</a></h3>
        </div>
      </div>
    </div>

pseudoxmlにする
---------------

.. code-block:: xml

    <section ids="title" names="title">
        <title>
            Title
        <section ids="section-1" names="section\ 1.">
            <title>
                Section 1.
            <section ids="content-1-1" names="content\ 1.1.">
                <title>
                    Content 1.1.
            <section ids="content-1-2" names="content\ 1.2.">
                <title>
                    Content 1.2.
        <section ids="section-2" names="section\ 2.">
            <title>
                Section 2.
            <section ids="content-2-1" names="content\ 2.1.">
                <title>
                    Content 2.1.

どうする？
----------

* ``title`` から次の ``section`` までを ``section`` として囲んで、スライドにしたい

``docutils.writers._html_base.HTMLTranslator``

.. code-block:: python

    def visit_section(self, node):
        self.section_level += 1
        self.body.append(
            self.starttag(node, 'div', CLASS='section'))

    def depart_section(self, node):
        self.section_level -= 1
        self.body.append('</div>\n')

こうする
--------

* `section` の入り際で「そのセクションの最初の子セクションに」を仕切りとする

.. code-block:: python

    def visit_section(self, node: section):
        self.section_level += 1
        if self.section_level == 1:
            self._proc_first_on_section = True
            self.body.append('<section>\n')
            return
        if self._proc_first_on_section:
            self._proc_first_on_section = False
            self.body.append('</section>\n')
        self.body.append(f"<section {attrs}>\n")
        if has_child_sections(node, 'section'):
            self._proc_first_on_section = True
            self.body.append('<section>\n')

難点
----

* ディレクティブ処理が若干入り組んでいる
* `section` ノードを明示的に指定する方法を探せてないため、 ``section`` に属性を追加するのが面倒

  * カスタムディレクティブでしのぎました

まとめ
======

.. 目安:1分ぐらい

振り返り
--------

Sphinxドキュメントを「なるべくそのまま」reveal.jsにするパッケージ作ってみた

* HTMLスライド用のビルダーが欲しいなら、HTML5用のビルダーをベースにできるので比較的楽
* pseudoxmlがdocutilsの構造理解に便利
* Sphinx/docutilsをちょっと理解できた気がする

参考資料など
------------

* Sphinxドキュメント
* sphinxjp.themes.revealjs
* マスタリング docutils

ご清聴ありがとうございました
----------------------------

