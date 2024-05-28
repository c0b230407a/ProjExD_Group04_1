# 見つけろ！こうかとん

## 実行環境の必要条件
* python >= 3.10
* pygame >= 2.1

## ゲームの概要
ランダムな位置に生成された主人公キャラクター(喜ぶこうかとん)を制限時間内(5秒)に見つけるゲーム。ニセの画像ランダムにを同時に出現させ、正しいこうかとんを見つけてクリックすることでスコアが増え、次のゲームに遷移する。時間内に見つけられなかった場合、ゲームオーバーとなる。

## ゲームの実装
### 共通基本機能
* 背景画像と主人公キャラクターの描画、フェイク画像の描画

### 担当追加機能
* ランダムにこうかとん、フェイク画像の生成（担当：加藤）：正しい答えのこうかとんとフェイク画像を画面にランダムに、重ならないように配置する機能。その際、正規こうかとんの座標を取得
* 当たり判定（担当：日馬）：マウスカーソルの位置と正規のこうかとんの座標が合っていたらスコアを1増やす。
* スコア表示（担当：小山）：その時のスコアを画面に表示する機能。
* BGM(担当：栗原)：対応したBGMを流す機能
* ゲームオーバー・タイム（担当：山田）：ゲームオーバー時にゲームオーバー画面を表示する。　制限時間を表示させる機能。5秒が制限時間

### ToDo
- [ ] 各自機能を作る
- [ ] 作った機能を合わせる
- [ ] 追加機能の修正
- [ ] 動作確認


### メモ
* クラス内の変数は，すべて，「get_変数名」という名前のメソッドを介してアクセスするように設計してある
* すべてのクラスに関係する関数は，クラスの外で定義してある
