BUCKET_NAME = "auto_ml_third_test_storage_20250529"
"""
GCSのバケット名
"""

PREFIX = "data_20250606_devil_number/images"
"""
GCS内での学習データ格納ディレクトリ名
"""

LABELS = [
    "balcony",
    "bathroom",
    "bicycle-parking",
    "clean-living",
    "doorway",
    "entrance",
    "entryway",
    "equipment",
    "exterior",
    "kitchen",
    "laundry-space",
    "living",
    "loft",
    "map",
    "neighborhood",
    "noimage",
    "other",
    "parking",
    "plan",
    "storage",
    "toilet",
    "unitbath",
    "view",
    "washroom", 
    "window",
    "shoe_shelf",
    "picture",
]
"""
GCS内のフォルダ名リスト（=ラベルリスト）
"""

OUTPUT_CSV = "generate-dataset-csv/training_dataset.csv"
"""
生成するCSVファイルの出力パス
"""

MAX_IMAGES_PER_LABEL = 1000
"""
1ラベルごとの最大画像数
"""