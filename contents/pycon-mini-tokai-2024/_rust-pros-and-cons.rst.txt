Pythonに浸かった人から見たRust
==============================

※個人の感想です

Rustの良いところ
----------------

* 最終生成物の動作速度が軽快。
* バイナリ配布がしやすい。
* | LSPもlinterもRustの公式Orgが提供しており、
  | 「とりあえずこれ」がしやすい。
* 本体ソースにテストコードを同居させられる。
* | コンパイルエラーがあるから（？）、
  | 不安定なコードを潰しやすい　※ただし体感しづらい

Rustの辛いところ
----------------

* いくつかの要素に慣れるまでが大変。

  * 「借用」まわり。
  * データ構造に柔軟性がない。
* | 標準ライブラリがそんなに多くない
  | ↓ありそうでないもの（クレートはあるのでなんとかなる）

  * regex
  * toml

(テストの一例)
--------------

.. code-block:: rust

    // モジュール内の関数
    pub fn up_major(base: &Version) -> Version {

        Version {
            major: base.major + 1,
            minor: 0,
            patch: 0,
            pre: Prerelease::EMPTY,
            build: BuildMetadata::EMPTY,
        }
    }

    // ここから先が↑のテスト（同一コード内）
    #[cfg(test)]
    mod tests {
        use super::*;

        #[test]
        fn test_up_major() {
            let before = Version::parse("1.2.3").unwrap();
            let after = up_major(&before);
            assert_eq!(after.major, before.major + 1);
            assert_eq!(after.minor, 0);
            assert_eq!(after.patch, 0);
        }
    }

.. revealjs-break::

* 関数等のユニットテスト自体は頑張れる。
* 習作フェーズで網羅するのしんどい。（というか面倒）

要点
----

* Pythonistaが動作速度などを求めてRustに手を出し
* LSPなどを駆使して「やりたいこと」の実現ぐらいにはたどり着けたが
* 「動作の担保」までRustで頑張るまでが大変

.. revealjs-fragments::

   →ここはRustなくても平気なのでは？

   →じゃあ、pytest使うか！

