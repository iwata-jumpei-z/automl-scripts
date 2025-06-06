# AutoML Scripts

このプロジェクトは、AutoMLに関連するスクリプトを管理するためのリポジトリです。以下にディレクトリ構造と各スクリプトの使用方法を示します。

## ディレクトリ構造

```
automl_scripts/
├── generate-dataset-csv/
│   └── execute.py
├── import-images/
│   └── execute.py
├── split-images-csv
│   └── execute.py
├── upload-images-to-gcs/
│   └── execute.py
```

## 使用方法（手順に合わせて）

### 1. `split-images-csv/execute.py`
CSVファイルを指定されたフォルダリストに基づいて分割します。分割されたCSVファイルは指定した出力ディレクトリに保存されます。

#### 実行方法
1. `bq-query.sql`を叩いて、実行結果のCSVをダウンロードします。（手動で誰か1人がUI上で行えば良い）
2. `split-images-csv/`にダウンロードしたファイルを格納し、`config.py`内で以下を設定します:
   - `CSV_FILE_PATH`: 処理するCSVファイルのパス
   - `OUTPUT_PATH`: 分割後のCSVファイルの出力先
   - `ALL_FOLDER_NAMES`: 全てのフォルダ名とラベルのマッピング
   - `FOLDER_NAME_LISTS`: 分割するフォルダリスト（リスト形式）
3. スクリプトを実行します:
   ```bash
   python split-images-csv/execute.py
   ```

### 2. `import-images/execute.py`
BigQueryのクエリ結果として得たCSVファイルを処理し、画像をダウンロードしてフォルダに保存します。

#### 実行方法
1. `config.py`で以下の設定を行います:
   - `CSV_FILE_PATH`: 処理するCSVファイルのパス
   - `FOLDER_NAMES`: ラベルごとのフォルダ名のマッピング
   - `IMAGE_EXTENSIONS`: 許可する画像拡張子のリスト
2. スクリプトを実行します:
   ```bash
   python import-images/execute.py
   ```

### 3. `upload-images-to-gcs/execute.py`
ローカルディレクトリ内の画像をGoogle Cloud Storage (GCS) にアップロードします。

#### 実行方法
1. `config.py`で以下の設定を行います:
   - `GCS_BUCKET_NAME`: アップロード先のGCSバケット名
   - `GCS_TRAINING_IMAGE_PATH`: GCS内のベースパス
   - `LOCAL_IMAGES_PATH`: ローカル画像ディレクトリのパス
2. スクリプトを実行します:
   ```bash
   python upload-images-to-gcs/execute.py
   ```

### 4. `generate-dataset-csv/execute.py`
GCS上の特定のフォルダをスキャンし、データセット用のCSVファイルを生成します。

#### 実行方法
1. `config.py`で以下の設定を行います:
   - `BUCKET_NAME`: 対象のGCSバケット名
   - `PREFIX`: スキャンするフォルダのプレフィックス
   - `LABELS`: ラベルのリスト
   - `OUTPUT_CSV`: 出力するCSVファイルのパス
   - `MAX_IMAGES_PER_LABEL`: ラベルごとの最大画像数
2. スクリプトを実行します:
   ```bash
   python generate-dataset-csv/execute.py
   ```

## 注意事項
- 各スクリプトの詳細な設定や挙動については、コード内のコメントを参照してください。
- 必要に応じてGoogle Cloud SDKの認証を行ってください。

