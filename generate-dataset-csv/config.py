BUCKET_NAME = "automl-labeling-training-images"
"""
GCSのバケット名
"""

PREFIX = "general"
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
    "shoe-shelf",
    "picture",
    "air-conditioner",
    "delivery-box",
    "elevator",
    "self-locking-door",
    "underfloor-storage",
]
"""
GCS内のフォルダ名リスト（=ラベルリスト）
"""

OUTPUT_CSV = "generate-dataset-csv/training_dataset3.csv"
"""
生成するCSVファイルの出力パス
"""

MAX_IMAGES_PER_LABEL = 1000
"""
1ラベルごとの最大画像数
"""