CSV_FILE_PATH = 'split-images-csv/original.csv'
"""
分割したいCSVファイルのパス
"""

OUTPUT_PATH = 'split-images-csv/output'
"""
分割したCSVファイルの出力先パス
"""

ALL_FOLDER_NAMES = {
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

# ----- フォルダリストの振り分け（増やしたり減らしたりできます） ----- 

FOLDER_NAME_LIST_1 = {
    1: 'plan',
    2: 'exterior',
    3: 'map', 
    4: 'neighborhood',
    None: 'unknown',
}
"""
分担１つ目のフォルダリスト
"""

FOLDER_NAME_LIST_2 = {
    5: 'living',
    11: 'living',
    13: 'living',
    14: 'living',
}
"""
分担２つ目のフォルダリスト
"""

FOLDER_NAME_LIST_3 = {
    9: 'other',
    10: 'doorway',
    12: 'kitchen',
    15: 'bathroom',
}
"""
分担３つ目のフォルダリスト
"""

FOLDER_NAME_LIST = [
    {1: 'plan'},
    {2: 'exterior'},
    {3: 'map'},
    {4: 'neighborhood'},
    {5: 'living'},
    {9: 'other'},
    {10: 'doorway'},
    {11: 'living'},
    {12: 'kitchen'},
    {13: 'living'},
    {14: 'living'},
    {15: 'bathroom'},
    {None: 'unknown'},
]