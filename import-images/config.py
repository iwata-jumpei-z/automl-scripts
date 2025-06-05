CSV_FILE_PATH = 'import-images/sample.csv'
"""
読み込むCSVファイルのパス
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

