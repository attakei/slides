e2eテストを頑張るためのpytest
=============================

e2eとしてのpytest
-----------------

* 「Pythonのモジュール内動作確認」としては使わない。
* 「Pythonを使ったコマンド実行結果の検証」のラッパーとして使う。

「FastAPIのWebアプリ開発時にTestClientを使う」「スナップショットテストをする」あたりと近い。

.. revealjs-break::
   :notitle:

【NOTE】ここから先の各要素は、相互依存的な内容です。

parameterize
------------

pytest組み込みのフィクスチャ。

* テスト関数へのデコレーターとして使う。
* 引数に従って、デコレーションしているテスト関数を複数パターンで実行できる。
* とにかく同じコマンドを繰り返すので、無いと困る存在。

.. revealjs-break::

よく見る使い方

.. revealjs-code-block:: python
    :data-line-numbers: 1-99|5,8|6,8

    import pytest


    @pytest.mark.parametrize(
        "in_,out_",       # 第1引数で、テスト関数に渡す名称を決めて
        [(2, 4), (3, 9)]  # 第2引数で、渡したい値をリストで定義する
    )
    def test_it(in_, out_):
        out = in_ * in_
        assert out == out_

.. revealjs-break::

<age-cli内での使い方>

.. revealjs-code-block:: python
    :data-line-numbers: 1-99|10-13|1-7,12

    def get_env_dirs(name: str):
        # name 配下のサブフォルダを一括でテストケース化する
        paths = [p for p in (root / name).glob("*") if p.is_dir()]
        return {
            "argvalues": paths,
            "ids": [f"{p.parent.name}/{p.name}" for p in paths]
        }


    @pytest.mark.parametrize(
        "env_path",                  # 第1引数の使い方は同じ
        **get_env_dirs("return-1"),  # 可変長引数を使って、その場でリストを作る
    )
    def test_invalid_env(cmd, env_path: Path, tmp_path: Path):
        ...

.. todo:: return-1 か for-major 配下のフォルダ構成を見せる

tmp_path
--------

pytest組み込みのフィクスチャ。

* 「一時ファイル置き場」となるディレクトリを生成してくれる。
* CLIの実行時に "working directory"として使用できる。
* これを使って、「コマンドの実行前後」の想定状態を再現テストしている。

.. revealjs-break::

<age-cli内での使い方>

.. revealjs-code-block:: python
    :data-line-numbers: 1-99|7,10

    import shutil

    @pytest.mark.parametrize(
        "env_path",
        **get_env_dirs("return-1"),
    )
    def test_invalid_env(cmd, env_path: Path, tmp_path: Path):
        """Run test cases on env having invalid configuration."""
        # 生成されている一時フォルダに、まるっとテスト用ファイルをコピーしている
        shutil.copytree(env_path / "before", tmp_path, dirs_exist_ok=True)
        ...

pytest_sessionstart
-------------------

``conftest.py`` にこの関数を定義すると、
「pytestのセッション開始時」=「pytest実行の最初に1回」特定の処理を実行できる。

* テスト対象のビルドや、共有環境のクリーンアップに向いている。
* 実際に `age` 本体のビルドをここでしている。

.. revealjs-break::

<age-cli内での使い方>

.. revealjs-code-block:: python
    :data-line-numbers: 1-99|1,4-7|8-10

    def pytest_sessionstart(session):
        """Generate age binary for testing."""
        print("Now building binary from Cargo ... ", end="")
        proc = run(
            ["cargo", "build"], 
            stdout=PIPE, stderr=PIPE, cwd=project_root
        )
        if proc.returncode != 0:  # 万が一ビルドに失敗したら「e2eしない」ためにexit
            print("Failed!!")
            pytest.exit(1)
        print(" OK!")

subprocess.run
--------------

※pytestではなく、Pythonの標準ライブラリ

おなじみ、外部コマンドを実行して結果を受け取る関数。

* コマンド+引数を渡せる。
* リターンコード、標準出力、標準エラーを受け取れる。

**「End-to-End」の要と言える存在。**

.. revealjs-break::

<age-cli内での使い方>

.. revealjs-code-block:: python
    :data-line-numbers: 1-99|5-7|8-14

    def test_valid_env(cmd, env_path: Path, tmp_path: Path):
        """Run test cases on env having valid files."""
        # 環境用意
        shutil.copytree(env_path / "before", tmp_path, dirs_exist_ok=True)
        # cmd(fixture製の関数で、内部でrunしてる)でage-cliを実行
        proc: CompletedProcess = cmd("update", "0.2.0")
        assert proc.returncode == 0
        # run()でdiffを実行して、「差分がないこと」を検証
        # diff は差分がまったくないときだけリターンコードが0になる
        diff = run([
            "diff", "--recursive", 
            str(tmp_path), str(env_path / "after")
        ])
        assert diff.returncode == 0


全部まとめると
--------------

* テスト用の環境をフォルダ単位で管理して
* session_startでCLIを事前ビルドして
* parametrizeで大量のテストパターンを実行して
* 内部では、tmp_pathで都度きれいな環境を用意して
* subprocess.runを使って、テスト結果を検査する

