import os
import subprocess
from google.cloud import storage
from config import SENDER_GCS_BACKET_NAME, SENDER_GCS_TRAINING_FOLDER_PATH, RECEIVER_GCS_BACKET_NAME, RECEIVER_GCS_TRAINING_FOLDER_PATH

def main():
    """
    X
    """
    move_all_images(
        sender_gcs_backet_name=SENDER_GCS_BACKET_NAME,
        sender_gcs_training_folder_path=SENDER_GCS_TRAINING_FOLDER_PATH,
        receiver_gcs_backet_name=RECEIVER_GCS_BACKET_NAME,
        receiver_gcs_training_folder_path=RECEIVER_GCS_TRAINING_FOLDER_PATH
    )

# ----- modules -----

def move_all_images(sender_gcs_backet_name, sender_gcs_training_folder_path, receiver_gcs_backet_name, receiver_gcs_training_folder_path):
    """
    GCS内のフォルダ間で画像を移動する関数。
    """
    client = storage.Client()
    sender_bucket = client.bucket(sender_gcs_backet_name)
    blobs = sender_bucket.list_blobs(prefix=sender_gcs_training_folder_path)

    for blob in blobs:
        source_url = f"gs://{sender_gcs_backet_name}/{blob.name}"
        destination_url = f"gs://{receiver_gcs_backet_name}/{receiver_gcs_training_folder_path}/{os.path.basename(blob.name)}"
        
        try:
            # gsutil mv コマンドを実行
            subprocess.run(["gsutil", "mv", source_url, destination_url], check=True)
            print(f"Moved: {source_url} -> {destination_url}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to move {source_url}: {e}")

# ----- エントリーポイント -----

if __name__ == "__main__":
    main()