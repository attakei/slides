本日の脇役: age-cli
===================

age-cliの宣伝
-------------

ライブラリのバージョニングを補助するCLIツール。Rust製。

* 管理用ファイルに「現在のバージョン」と「更新対象とルール」を記述。
* ``age mijor|minor|patch`` で一括でルールに基づいて更新。
* 今のところ、コミットなどはしない。

.. todo:: アイコン作る？

.. revealjs-break::

.. code-block:: toml
    :caption: .age.toml(一部略)

    # バージョン情報
    current_version = "0.7.0"

    # 更新対象（いっぱい）
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
    :caption: 実行例

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

.. revealjs-notes:: 6min
