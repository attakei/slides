======================================
pytestでRust製CLIをe2eテストしてみよう
======================================

.. pytest-e2e-for-rust-cli

はじめに
========

このトークの概要
----------------

お前誰よ？
----------

株式会社ニジボックス
--------------------

本日の脇役: age-cli
===================

age-cliの宣伝
-------------

ライブラリのバージョンに関する記述を一括更新するCLIツール。
Rust製。

.. todo:: アイコン作る？

.. revealjs-break::

.. code-block:: toml
   :caption: .age.toml(一部略)

   current_version = "0.7.0"

   [[files]]
   path = "Cargo.toml"
   search = "version = \"{{current_version}}\""
   replace = "version = \"{{new_version}}\""
   
   [[files]]
   path = "CHANGELOG.md"
   search = "# Changelog"
   replace = """
   # Changelog
   
   ## v{{new_version}} - {{now|date}} (JST)
   """

.. revealjs-break::

.. code-block:: console

   $ time age minor
   Updated!
   age minor  0.00s user 0.00s system 90% cpu 0.003 total

   $ git status
   On branch main
   Your branch is up to date with 'origin/main'.
   
   Changes not staged for commit:
     (use "git add <file>..." to update what will be committed)
     (use "git restore <file>..." to discard changes in working directory)
           modified:   .age.toml
           modified:   .github/release-body.md
           modified:   CHANGELOG.md
           modified:   Cargo.toml
           modified:   doc/conf.py
           modified:   doc/usage/installation.rst
           modified:   pyproject.toml
   
   no changes added to commit (use "git add" and/or "git commit -a")

(余談)
------

Q: なんで作ったんですか？

* A1: 似たPythonライブラリがあるけど、世代交代についていけなくなった。
  
  * bumpversion
  * bump2version
  * bump-my-version

* A2: せっかくなので、Rustの習作にしたかった。

Pythonに慣れたあとのRust感
==========================

※個人の感想です

Rustの良いところ
----------------

Rustの辛いところ
----------------

要点
----

* Pythonistaが動作速度などを求めてRustに手を出し
* LSPなどを駆使して「やりたいこと」の実現ぐらいにはたどり着けたが
* 「動作の担保」までRustで頑張るまでが大変

.. revealjs-fragment::

   →ここはRustなくても平気なのでは？

テストツールとしてのpytest
==========================

pytest
------

サンプルコード
--------------

pytestの良いところ
------------------

e2eテストを頑張るためのpytestの機能
===================================

e2eとしてのpytest
-----------------

* 「Pythonのモジュール内動作確認」としては使わない。
* 「Pythonを使ったコマンド実行結果の検証」のラッパーとして使う。

「FastAPIのWebアプリ開発時にTestClientを使う」のに近い。

subprocess.run
--------------

※pytestではなく、Pythonの標準ライブラリ

capsysフィクスチャ
------------------

テスト時の標準入力/標準出力/標準エラーをキャプチャーして、
テスト時に検査しやすくしてくれる。

.. code-block:: python

   def test_using_capture(capsys):
       print("Hello world")
       captured = capsys.readouterror()
       assert "world" in captured.out

.. revealjs-break::

conftest.py
-----------

まとめ
======
