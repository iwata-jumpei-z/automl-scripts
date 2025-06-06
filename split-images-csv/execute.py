from config import CSV_FILE_PATH, OUTPUT_PATH, ALL_FOLDER_NAMES, FOLDER_NAME_LIST
import csv
import os

def main():
    if set(ALL_FOLDER_NAMES.keys()) != set(key for folder in FOLDER_NAME_LIST for key in folder.keys()):
        raise ValueError("フォルダリストの分担に不足があります。振り分けミスがないか確認してください。")
    divide_csv_file(
        csv_file_path=CSV_FILE_PATH,
        output_path=OUTPUT_PATH,
        folder_name_list=FOLDER_NAME_LIST
    )


# ----- modules -----

def divide_csv_file(csv_file_path, output_path, folder_name_list):
    os.makedirs(output_path, exist_ok=True)
    output_files = {f"images_type_{list(folder.keys())[0]}.csv": folder for folder in folder_name_list}
    file_handlers = {filename: open(os.path.join(output_path, filename), mode='w', newline='', encoding='utf-8') for filename in output_files}
    csv_writers = {filename: csv.writer(file) for filename, file in file_handlers.items()}

    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            header = next(reader)
            for writer in csv_writers.values():
                writer.writerow(header)
            for row in reader:
                label = row[1]
                if label.isdigit():
                    label = int(label)
                    for filename, folder_list in output_files.items():
                        if label in folder_list:
                            csv_writers[filename].writerow(row)
                            break
    finally:
        # ファイルを閉じる
        for file in file_handlers.values():
            file.close()


# ----- エントリーポイント -----

if __name__ == "__main__":
    main()