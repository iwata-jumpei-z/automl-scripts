from google.cloud import storage
import os
import random
import string
from config import BUCKET_NAME, LABEL_NAME, FOLDER_PATH, DOWNLOAD_DIR, MAX_IMAGES

def main():
    download_images_from_gcs(
        bucket_name = BUCKET_NAME,
        folder_path = f"{FOLDER_PATH}/{LABEL_NAME}",
        download_dir = f"{DOWNLOAD_DIR}/{LABEL_NAME}",
        max_images = MAX_IMAGES
    )

# ----- modules -----

def download_images_from_gcs(bucket_name, folder_path, download_dir, max_images):
    # GCSクライアントを初期化
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blobs = bucket.list_blobs(prefix=folder_path)

    os.makedirs(download_dir, exist_ok=True)

    count = 0
    for blob in blobs:
        if count >= max_images:
            break
        if blob.name.endswith(('.jpg', '.jpeg', '.png')):
            # ランダムな15文字のファイル名を生成
            _, extension = os.path.splitext(blob.name)  # 元の拡張子を取得
            random_filename = ''.join(random.choices(string.ascii_letters + string.digits, k=15)) + extension
            destination_path = os.path.join(download_dir, random_filename)
            blob.download_to_filename(destination_path)
            print(f"Downloaded: {blob.name} to {destination_path}")
            count += 1

# ----- エントリーポイント -----

if __name__ == "__main__":
    main()
