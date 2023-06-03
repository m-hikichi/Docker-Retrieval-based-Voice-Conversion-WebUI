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

## 音声変換モデルの学習
1. 音声ファイル（`.wav`，`.mp3`など）を`datasets`ディレクトリに配置してください．これらが学習データとなります．

2. retrieval-based-voice-conversion-webui画面で`Train`タブを選択します．

3. `Experiment name`に出力される学習モデルの名前を入力します．

4. `Target sample rate`で音声ファイルのサンプリングレートを指定します．今回は`40k`を選択します．

5. `If the model have pitch guidance`でピッチガイダンスの有無を指定します．ピッチガイダンスとは，音声変換時に音声の高さ（ピッチ）を補正する機能です．パソコンのスペックや目的に応じて選択してください．<br>
    - `true`にすると，ピッチガイダンスが有効になります．音声変換精度が向上しますが，リアルタイム音声変換時にパソコンの負荷が高くなります．
    - `false`に設定するとピッチガイダンスが無効になります．パソコンの負荷が低くなりますが，音声変換精度がやや劣ります．
    - 学習音声ファイルが楽曲の場合は，必ず`true`にしてください．

6. `Model architecture version`でRVCの事前学習モデルのバージョンを指定します．今回は`v1`を選択します．

7. `Threads of CPU, for pitch extraction and dataset processing`でピッチ抽出とデータセット処理に使用するCPUスレッドの数を指定します．

8. `Path to training folder`で学習させるデータセットフォルダのパスを指定します．今回は`/datasets`を入力します．

9. `Select pitch extraction algorithm`でピッチ抽出アルゴリズムの設定を行います．以下の3種類から選べます．<br>
    - `pm`：歌声の処理を高速化するアルゴリズムです．
    - `dio`：高品質の音声を処理するアルゴリズムです．
    - `harvest`：最高の品質で処理するアルゴリズムですが，最も処理が遅くなります．

10. `Save frequency`，`Total training epochs (total_epoch)`，`batch_size`に適切な値を設定します．これらは学習の進捗や結果に影響します．

11. `One-click training.`をクリックして学習を開始します．

## 音声変換モデルの推論
1.  変換したい音声ファイルを`input`ディレクトリに配置します．

2. retrieval-based-voice-conversion-webui画面で`Model Inference`タブを選択します．

3. `Refresh voice list and index path`をクリックして，使用可能な音声変換モデルの一覧を更新します．

4. `Inferencing voice`から使用したい学習済みの音声変換モデルを選択します．

5. `transpose(Input must be integer, represents number of semitones. Example: octave sharp: 12;octave flat: -12)`で音声の高さ（ピッチ）を調整します．整数値で入力してください．12は1オクターブ上げ，-12は1オクターブ下げを意味します．男性から女性に変換する場合は`12`，女性から男性に変換する場合は`-12`を推奨しています．音域が行き過ぎて声が歪んでしまう場合は，ご自身で適切な音域に調整してください．

6. `Enter the path of the audio file to be processed`に変換したい音声ファイルのパスを入力します．例えば，`input`ディレクトリに`test.wav`という名前の音声ファイルを配置した場合は，`/input/test.wav`と入力してください．

7. `Select pitch extraction algorithm`でピッチ抽出アルゴリズムの設定を行います．以下の2種類から選べます．
    - `pm`：抽出は最速だが，音声の品質は低い．
    - `harvest`：品質は向上するが，抽出が最も遅い．
    - ~~`crepe`：品質は最高だが，GPUが必要．~~現在使用できません

8. `Path to the '.index' file in 'logs' directory is auto detected. Pick the matching file from the dropdown`で学習済みの音声変換モデルに対応する`.index`ファイルをドロップダウンから選択します．例えば，学習の際に「Experiment name」（出力される学習モデルの名前）を「ichiro」にした場合，`logs/ichiro/added_~.index`を選ぶようにします．

9. `Resample the audio in post-processing to a different sample rate`にて，後処理で音声を異なるサンプルレートにリサンプリングします．設定を`0`にした場合は，リサンプリングは実行されません．

10. `Conversion`をクリックすると，推論が実行され，変換後音声を再生することが可能になります．