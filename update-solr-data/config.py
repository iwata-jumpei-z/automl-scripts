GLOBAL_KEYS = [
    "your_global_key_1",
    "your_global_key_2",
]
"""
画像のAutoMLによるラベリングを行いたい物件のglobal_keyを指定する
"""

LABEL_LIST = {
    'plan': 1,
    'exterior': 2,
    'map': 3,
    'neighborhood': 4,
    'other': 9,
    'doorway': 10,
    'living': 11,
    'kitchen': 12,
    'bathroom': 15,
    'toilet': 16,
    'washroom': 17,
    'storage': 18,
    'equipment': 19,
    'balcony': 20,
    'entrance': 21,
    'parking': 22,
    'bicycle-parking': None,
    'unitbath': None,
    'laundry-space': None,
    'view': None,
    'loft': None,
    'clean-living': None,
    'entryway': None,
    'noimage': None,
    'picture': None,
    'window': None,
    'shoe_shelf': None,
}
"""
AutoMLからのラベリング結果を、Solrに登録する際のラベル番号の変換辞書
"""