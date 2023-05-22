# インストール手順

以下は，Dockerを用いたretrieval-based-voice-conversion-webuiの環境構築の手順についてです．

## ファイル配置
1. 以下のようなファイル構成を持つディレクトリを作成します．この際に`datasets`ディレクトリ，`input`ディレクトリ，`models`ディレクトリを作成します．
    ```
    .
    ├── datasets
    ├── docker-compose
    │   ├── .env
    │   └── docker-compose.yml
    ├── Dockerfile
    │   └── Dockerfile
    ├── input
    ├── models
    ├── .gitignore
    └── README.md
    ```

## Dockerイメージのビルド

1. コマンドプロンプト（またはターミナル）でディレクトリ内の`docker-compose`ディレクトリに移動します．移動するためには，以下のようなコマンドを使用します．
    ```
    cd docker-compose
    ```

2. Dockerイメージを作成するため，以下のコマンドを実行します．
    ```
    docker-compose build
    ```
    実行結果として，必要なDockerイメージがビルドされます．

## 起動と設定
1. Dockerコンテナを起動するため，以下のコマンドを実行します．
    ```
    docker-compose up -d
    ```
    実行結果として，retrieval-based-voice-conversionのDockerコンテナがバックグラウンドで実行されます．<br>
    以下のコマンドを実行することで，稼働中のコンテナのログがリアルタイムで表示されます．これにより，アプリケーションの動作状況やエラーの発生を確認することができます．
    ```
    docker-compose logs -f
    ```

2. ブラウザから`localhost:7865`にアクセスします．<br>
もし`localhost:7865`にアクセスできない場合は，Dockerコンテナが正常に動作しているか，または他のアプリケーションが`7865`ポートを使用していないか確認してください．


# 使い方

## 学習
1. 音声ファイル（`.wav`，`.mp3`など）を`datasets`ディレクトリに配置してください．これらが学習データとなります．

2. retrieval-based-voice-conversion-webui画面で`Train`タブを選択します．

3. `Input experiment name`に出力される学習モデルの名前を入力します．

4. `Target sample rate`で`40k`を選択します．

5. `Does the model have pitch guidance (singing must, voice can not.)`にて`否`に設定すると「ピッチレス」モデルとなり，リアルタイム音声変換をする際に，音声変換精度がやや劣るようです．音声変換精度を向上させたい場合には，`是`を選択してみてください．VC Clientを利用する際に，お使いのパソコンの負荷を減らしたい場合には，「ピッチレス」モデルが候補の1つとなる様です．お使いのパソコンのスペックにお応じて調整してみてください．<br>
ただし，学習音声ファイルが楽曲の場合は，`是`で行ってください．

6. `Input training folder path`に`/datasets`を入力します．

7. `Save frequency`，`Total training epochs (total_epoch)`，`batch_size`に適切な値を設定します．

8. `One-click training.`をクリックして学習を開始します．

## 推論
1.  変換したい音声ファイルを`input`ディレクトリに配置します．

2. `Refresh timbre list`をクリックします．

3. 使用したい学習モデルを選択するために，`Inferencing timbre`から該当のモデルを選びます．

4. `transpose(integer, number of semitones, octave sharp 12 octave flat -12)`の値を設定します．例えば，男性から女性に変換する場合は`12`，女性から男性に変換する場合は`-12`，それ他の場合は`0`と入力します．

5. `Enter the path of the audio file to be processed (the default is the correct format example)`に変換したい音声ファイルのパスを入力します．`1.`にて`test.wav`という名前の音声ファイルを配置した場合は，`/input/test.wav`と入力してください．

6. `Feature search database file path`については，`/Retrieval-based-Voice-Conversion-WebUI/logs/学習モデル名/~.index`ファイルを指定してください．

7. `Conversion`をクリックすると，推論が実行され，変換後音声を再生することが可能になります．