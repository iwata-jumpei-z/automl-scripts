import os
from google.cloud import storage
from config import GCS_BACKET_NAME, GCS_TRAINING_IMAGE_PATH, LOCAL_IMAGES_PATH

def main():
    """
    X
    """
    upload_images(
        local_path=LOCAL_IMAGES_PATH,
        gcs_bucket_name=GCS_BACKET_NAME,
        gcs_base_path=GCS_TRAINING_IMAGE_PATH
    )
    

# ----- modules -----

def upload_images(local_path, gcs_bucket_name, gcs_base_path):
        """
        ローカルディレクトリ内の画像をGCSにアップロードする。
        フォルダ構成を保持したままアップロードする。
        """
        client = storage.Client()
        bucket = client.bucket(gcs_bucket_name)

        for root, dirs, files in os.walk(local_path):
            for file in files:
                local_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(local_file_path, local_path)
                gcs_file_path = os.path.join(gcs_base_path, relative_path).replace("\\", "/")
                
                blob = bucket.blob(gcs_file_path)
                blob.upload_from_filename(local_file_path)
                print(f"Uploaded {local_file_path} to gs://{gcs_bucket_name}/{gcs_file_path}")


# ----- エントリーポイント -----

if __name__ == "__main__":
    main()