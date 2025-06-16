CSV_FILE_PATH = 'split-images-csv/original4.csv'
"""
読み込むCSVファイルのパス
"""

BASE_PATH = 'import-images/images4'
"""
画像を保存するフォルダパス
"""

FOLDER_NAMES = {
    1: 'plan',
    2: 'exterior',
    3: 'map', 
    4: 'neighborhood',
    5: 'living',
    9: 'other',
    10: 'doorway',
    11: 'living',
    12: 'kitchen',
    13: 'living',
    14: 'living',
    15: 'bathroom',
    None: 'unknown',
}
"""
フォルダの名前リスト（=ラベルリスト）
"""

IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png'}
"""
許可する画像の拡張子を指定する
"""

