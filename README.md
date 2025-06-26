# AutoML Scripts

このプロジェクトは、AutoML に関連するスクリプトを管理するためのリポジトリです。以下にディレクトリ構造と各スクリプトの使用方法を示します。

## ディレクトリ構造

```
automl_scripts/
├── generate-dataset-csv/
│    ├── config.py
│    └── execute.py
├── import-images/
│    ├── sample.csv
│    ├── config.py
│    └── execute.py
├── import-images-from-gcs/
│    ├── config.py
│    └── execute.py
├── move-all-files-in-gcs/
│    ├── config.py
│    └── execute.py
├── split-images-csv
│    ├── bq-query.sql
│    ├── sample.csv
│    ├── config.py
│    └── execute.py
├── update-solr-data/
│    ├── config.py
│    └── execute.py
└── upload-images-to-gcs/
     ├── config.py
     └── execute.py
```

## 使用方法（手順に合わせて）

### 0. `Google Cloud CLI`

このプロジェクトを使用する前に、Google Cloud CLI を使用して認証を行う必要があります。

```bash
gcloud config set project sumai-sandbox
gcloud auth login
```

#### 注意点

- `sumai-sandbox`プロジェクトが**正しく設定されていることを確認してください**。
- 必要に応じて、`gcloud auth list`を使用して現在の認証状況を確認できます。

### 1. `split-images-csv`

CSV ファイルを config.py で指定されたフォルダリストに基づいて分割します。
分割された CSV ファイルは指定した出力ディレクトリに保存されます。

#### 実行方法

1. `bq-query.sql`を叩いて、実行結果の CSV をダウンロードします。（手動で誰か 1 人が UI 上で行えば良い）
2. `split-images-csv/`にダウンロードした CSV ファイルを格納し、`config.py`内で以下を設定します:
   - `CSV_FILE_PATH`: ダウンロードした CSV ファイルのパス
   - `OUTPUT_PATH`: 分割後の CSV ファイルの出力先
   - `ALL_FOLDER_NAMES`: 全てのフォルダ名とラベルのマッピング
   - `FOLDER_NAME_LISTS`: 分割するフォルダリスト（リスト形式）
3. スクリプトを実行します:
   ```bash
   python split-images-csv/execute.py
   ```

#### 注意点

- 出力する CSV の形式は、bq-query.sql にあるように、global_key, label, URL, building_key の順番で出力されているようにしてください。その形式であることが前提のスクリプトになっています。

### 2. `import-images`

BigQueryでの実行結果として得たCSVファイルを処理し、画像をダウンロードしてフォルダに保存します。

#### 実行方法

1. `config.py`で以下の設定を行います:
   - `CSV_FILE_PATH`: 処理するCSVファイルのパス
   - `BASE_PATH`: 画像保存先のパス
   - `FOLDER_NAMES`: ラベルごとのフォルダ名のマッピング
   - `IMAGE_EXTENSIONS`: 許可する画像拡張子のリスト
2. スクリプトを実行します:
   ```bash
   python import-images/execute.py
   ```

#### 注意点

- CSVファイルの形式は、`global_key, label, URL, building_key`の順番である必要があります。
- ダウンロードされた画像はランダムなファイル名で保存されます。
- 許可される画像拡張子は`.jpg`, `.jpeg`, `.png`です。

### 3. `import-images-from-gcs`

Google Cloud Storage (GCS)から画像をダウンロードし、ローカルフォルダに保存します。

#### 実行方法

1. `config.py`で以下の設定を行います:
   - `BUCKET_NAME`: ダウンロード元の GCS バケット名
   - `LABEL_NAME`: ダウンロード対象のラベル名
   - `FOLDER_PATH`: ダウンロード元の GCS フォルダパス
   - `DOWNLOAD_DIR`: ローカル保存先のディレクトリ
   - `MAX_IMAGES`: ダウンロードする最大画像数
2. スクリプトを実行します:
   ```bash
   python import-images-from-gcs/execute.py
   ```

#### 注意点

- ダウンロードされた画像はランダムなファイル名で保存されます。
- 許可される画像拡張子は`.jpg`, `.jpeg`, `.png`です。

### 4. `upload-images-to-gcs`

ローカルフォルダ内の画像を指定したGoogle Cloud Storage (GCS)バケットにアップロードします。

#### 実行方法

1. `config.py`で以下の設定を行います:
   - `GCS_BACKET_NAME`: アップロード先のGCSバケット名
   - `GCS_TRAINING_IMAGE_PATH`: GCS内での学習データ格納ディレクトリ名
   - `LOCAL_IMAGES_PATH`: アップロードする画像が格納されているローカルパス
2. スクリプトを実行します:
   ```bash
   python upload-images-to-gcs/execute.py
   ```

#### 注意点

- フォルダ構成を保持したままアップロードされます。
- アップロード先のパスは`GCS_TRAINING_IMAGE_PATH`を基準に構成されます。

### 5. `move-all-files-in-gcs`

Google Cloud Storage (GCS)内のファイルを指定したフォルダ間で移動します。

#### 実行方法

1. `config.py`で以下の設定を行います:
   - `SENDER_GCS_BUCKET_NAME`: 移動元のGCSバケット名
   - `SENDER_GCS_FOLDER_PATH`: 移動元のフォルダパス
   - `RECEIVER_GCS_BUCKET_NAME`: 移動先のGCSバケット名
   - `RECEIVER_GCS_FOLDER_PATH`: 移動先のフォルダパス
2. スクリプトを実行します:
   ```bash
   python move-all-files-in-gcs/execute.py
   ```

#### 注意点

- 移動元フォルダ内のすべてのファイルが移動されます。
- `gsutil mv`コマンドを使用してファイルを移動します。

### 6. `generate-dataset-csv`

Google Cloud Storage (GCS)上の指定されたフォルダを参照し、画像データセットの情報をCSV形式で生成します。

#### 実行方法

1. `config.py`で以下の設定を行います:
   - `BUCKET_NAME`: 対象のGCSバケット名
   - `PREFIX`: GCS内での学習データ格納ディレクトリ名
   - `LABELS`: ラベル名のリスト（フォルダ名と一致）
   - `OUTPUT_CSV`: 生成するCSVファイルの保存先
   - `MAX_IMAGES_PER_LABEL`: 1ラベルごとの最大画像数
2. スクリプトを実行します:
   ```bash
   python generate-dataset-csv/execute.py
   ```

#### 注意点

- CSVファイルには画像のパスとラベルが記録されます。
- ファイル名にスペースや日本語が含まれる画像はスキップされます。
- ファイル名の接頭辞に応じて、`training`, `test`, `validation`の区分が自動的に設定されます。

### 7. `update-solr-data`

Solr にデータを更新するためのスクリプトです。

#### 実行方法

1. `config.py`で以下の設定を行います:
   - `GLOBAL_KEYS`: ラベリング対象の物件の `global_key` リスト
   - `LABEL_LIST`: AutoMLラベルをSolrラベル番号に変換する辞書
2. スクリプトを実行します:
   ```bash
   python update-solr-data/execute.py
   ```

#### 注意点

- `GLOBAL_KEYS` に指定された物件のデータを Solr から取得し、AutoML によるラベリングを行います。
- ラベリング結果は `LABEL_LIST` を使用して Solr のラベル番号に変換されます。
- 更新されたデータは Solr に追加されます。
