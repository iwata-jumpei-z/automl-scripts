# AutoML Scripts

このプロジェクトは、AutoMLに関連するスクリプトを管理するためのリポジトリです。以下にディレクトリ構造と各スクリプトの使用方法を示します。

## ディレクトリ構造

```
automl_scripts/
├── generate-csv/
│   └── execute.py
├── import-images/
│   └── execute.py
├── upload-images-to-gcs/
│   └── execute.py
```

## 使用方法

### 1. `generate-csv/execute.py`
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
   python generate-csv/execute.py
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
   - `GCS_BACKET_NAME`: アップロード先のGCSバケット名
   - `GCS_TRAINING_IMAGE_PATH`: GCS内のベースパス
   - `LOCAL_IMAGES_PATH`: ローカル画像ディレクトリのパス
2. スクリプトを実行します:
   ```bash
   python upload-images-to-gcs/execute.py
   ```

## 注意事項
- 各スクリプトの詳細な設定や挙動については、コード内のコメントを参照してください。
- 必要に応じてGoogle Cloud SDKの認証を行ってください。

