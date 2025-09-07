テストツールとしてのpytest
==========================

pytest
------

.. container:: flex

    .. container:: two-of-third

        Pythonのテストライブラリ。

        * 関数とassertというシンプルな作りが基本。
        * fixtureという仕組みが便利（後述）。
        * 標準ライブラリにunittestはあるが、こっちのほうがデファクト感ある。

    .. container:: one-of-third

        .. figure:: https://docs.pytest.org/en/stable/_static/pytest1.png

サンプルコード
--------------

.. revealjs-code-block:: python
    :data-line-numbers: 1-99|1-3|6-8|11-14

    def test_foo():
        # 成功する
        assert True is True


    def test_bar():
        # 失敗する
        assert "Hello" == "hello"


    def test_buzz(capsys):  # 標準出力をテストする
        print("Hello world")
        c = capsys.readourerr()
        assert c.out.startswith("Hello")

pytestの良いところ
------------------

* | 関数ベースでのテストが基本のため、インデントが浅い。
  | TestCaseクラスのようなものは不要。（使うことは出来る）
* ドキュメントがちゃんとしてるので、自分での機能追加もしやすい。
* ↑の実装が規約ベースで書けるので、考えることがあまり多くない（はず）。

fixture
-------

テストのプロセスに割り込んだりするための仕組み。

* 多くは、「各テストの引数」の体裁で、
  テストの前処理をオブジェクトを受け取ってテストする。
* 受け取った中身はオブジェクトなので、メソッドなどを駆使して高度なことも出来る。
* scopeの概念があり処理の差し込みは、かなり柔軟。

  * 各テストの前/後
  * テストモジュール全体の前/後
  * テスト実行全体の最初/最後
