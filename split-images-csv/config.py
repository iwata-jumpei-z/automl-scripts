CSV_FILE_PATH = 'split-images-csv/original3.csv'
"""
分割したいCSVファイルのパス
"""

OUTPUT_PATH = 'split-images-csv/output3'
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