# GCS上の特定のフォルダを見て、データセット用のCSVファイルを作成するスクリプト
import csv
from google.cloud import storage
from typing import List
import re
from config import BUCKET_NAME, PREFIX, LABELS, OUTPUT_CSV, MAX_IMAGES_PER_LABEL

client = storage.Client()
bucket = client.bucket(BUCKET_NAME)

def main():
    """
    GCS上の指定されたフォルダを見て、データセット用のCSVファイルを作成するスクリプト
    """
    generate_csv(
        output_csv = OUTPUT_CSV,
        labels = LABELS,
        prefix = PREFIX,
        bucket_name = BUCKET_NAME,
        max_images_per_label = MAX_IMAGES_PER_LABEL
    )


# ----- modules -----

def generate_csv(output_csv, labels, prefix, bucket_name, max_images_per_label):
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for label in labels:
            folder_prefix = f"{prefix}/{label}/"
            print(f"Processing folder: {folder_prefix}")
            blobs = bucket.list_blobs(prefix=folder_prefix)
            gcs_paths = [
                f"gs://{bucket_name}/{blob.name}"
                for blob in blobs 
                if blob.name.endswith(('.jpg', '.jpeg', '.png')) and ' ' not in blob.name
            ]
            limited_gcs_paths = gcs_paths[:max_images_per_label]
            for gcs_path in limited_gcs_paths:
                if "(" in gcs_path or ")" in gcs_path or re.search(r'[ぁ-んァ-ン一-龥]', gcs_path):
                    print(f"Skipping path: {gcs_path}")
                    continue
                writer.writerow([gcs_path, label])
    
    print(f"CSVファイルを生成しました: {output_csv}")


# ----- エントリーポイント -----

if __name__ == "__main__":
    main()