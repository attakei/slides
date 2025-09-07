Sphinxとプレゼンテーション
==========================

.. 7min

|:ballot_box_with_check:| > |:arrow_right:| > |:blue_square:|

… 対象者：プレゼン系ソフトウェアを使いたがらない方 / プレゼン資料もGit管理してみたい方

プレゼン系ソフトウェアって？
----------------------------

いわゆるこの辺を指します

* Microsoft PowerPoint
* Keynote
* Google スライド

「プレゼン系ソフト」を使わずにプレゼンをする
--------------------------------------------

.. 全部実在します（最後のは以前の上司が作ってた）

.. revealjs-fragments::

    * **HTMLでプレゼン**
    * PDFでプレゼン
    * Unityでプレゼン
    * ターミナルでTelnet接続したらプレゼン

HTMLでプレゼンすると何がいいか
------------------------------

主なメリット

* OSを選ばない
* ファイルをGit管理しやすい

（デメリット）

* 公開・共有にひと手間かかる
* ブラウザは選ぶ

.. revealjs-break::

1:OSを選ばない

* ブラウザベースの表示なので、端末も選ばない

  * PC
  * タブレット
  * スマホ

* ただしブラウザ依存の実装した場合は要注意

  * Chromeは新しすぎ
  * IEは忘れる

.. revealjs-break::

2:ファイルをGit管理しやすい

* リソースが分離した状態なので、差し替えなどが比較的容易
* 差分がわかりやすい(別テキストからHTMLを生成する場合に顕著)
* CI/CDしやすい(GitHub Pagesなど)

Sphinxが取り扱うビルド先(再掲)
------------------------------

* **HTML**
* ePub
* **PDF**
* man
* (etc)

.. revealjs-break::

* **HTML <= こっち**
* ePub
* **PDF**
* man
* (etc)

「SphinxでHTMLプレゼンテーション」を実現するには
------------------------------------------------

基本的には、

* なにかしらのHTMLプレゼン用ライブラリを準備して
* HTML+JSを出力するテーマ・拡張を用意する

HTMLプレゼンテーション用ライブラリ
----------------------------------

* Google I/O 2012 slide
* Go talks
* Impress.js
* Reveal.js
*	Remark
* (more...)

HTMLプレゼンを使うためのSphinx拡張集
------------------------------------

* ``hieroglyph``
* ``sphinxjp.themes.gopher``
* ``sphinxjp.themes.impressjs``
* ``sphinxjp.themes.reveajs``
* ``sphinxjp.themes.s6``
* ``sphinx-revealjs``
