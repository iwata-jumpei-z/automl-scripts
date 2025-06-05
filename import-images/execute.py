import os
import random
import string
from config import CSV_FILE_PATH, FOLDER_NAMES, IMAGE_EXTENSIONS
import csv
from collections import defaultdict
import requests


def main():
    """
    BigQueryでクエリを叩き、その実行結果として得たCSVファイルを処理する
    """
    make_folders(
        folder_name_array = FOLDER_NAMES.values()
    )
    data = load_csv_data(
        csv_file_path = CSV_FILE_PATH
    )
    download_images_and_store(
        data = data,
        folder_names = FOLDER_NAMES,
        image_extensions = IMAGE_EXTENSIONS
    )

# ----- modules -----

def make_folders(folder_name_array):
    """
    config.pyからフォルダーリストを読み取り、特定のパスにフォルダを作成する。
    もし特定のパスが存在していれば別名を付けて作成する。
    """
    BASE_PATH = 'import-images/images'

    store_path = BASE_PATH
    while os.path.exists(store_path):
        random_suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=3))
        store_path = f"{BASE_PATH}_{random_suffix}"
    os.makedirs(store_path)
    for folder_name in folder_name_array:
        os.makedirs(os.path.join(store_path, folder_name), exist_ok=True)
    print(f"{store_path}に画像フォルダを作成しました。")


def load_csv_data(csv_file_path):
    """
    CSVファイルの読み込みとデータの整形
    global_key,label,URL,building_key
    {type: 'number', urls:['*','*','*']} の形式に変換
    """

    data_dict = defaultdict(list)
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            label = row['label']
            url = row['URL']
            if label and url:
                data_dict[label].append(url)
    formatted_data = [{'type': label, 'urls': urls} for label, urls in data_dict.items()]
    return formatted_data
    
    
def download_images_and_store(data, folder_names, image_extensions):
    """
    画像のダウンロードと画像種別ごとに保存
    """
    
    BASE_PATH = 'import-images/images'

    for item in data:
        type_label = int(item['type'])  # 明示的に整数型にキャスト
        urls = item['urls']
        folder_path = os.path.join(BASE_PATH, folder_names.get(type_label, 'unknown'))

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        for idx, url in enumerate(urls):
            try:
                response = requests.get(url, stream=True)
                response.raise_for_status()

                # ファイル拡張子を決定
                ext = os.path.splitext(url)[-1].lower()
                if ext not in image_extensions:
                    ext = '.jpg'  # デフォルト拡張子

                # ファイル名を生成
                random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=15))
                file_name = f"{random_string}{ext}"  # ランダムな文字列を使用してファイル名を生成
                file_path = os.path.join(folder_path, file_name)

                # 画像を保存
                with open(file_path, 'wb') as file:
                    for chunk in response.iter_content(1024):
                        file.write(chunk)

                print(f"画像を保存しました: {file_path}")

            except requests.RequestException as e:
                print(f"画像のダウンロードに失敗しました: {url} - {e}")

# ----- エントリーポイント -----

if __name__ == "__main__":
    main()