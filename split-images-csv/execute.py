from config import CSV_FILE_PATH, OUTPUT_PATH, ALL_FOLDER_NAMES, FOLDER_NAME_LIST_1, FOLDER_NAME_LIST_2, FOLDER_NAME_LIST_3
import csv
import os

def main():
    if not (ALL_FOLDER_NAMES == {**FOLDER_NAME_LIST_1, **FOLDER_NAME_LIST_2, **FOLDER_NAME_LIST_3}):
        raise ValueError("フォルダリストの分担に不足があります。振り分けミスがないか確認してください。")
    # divide_csv_file(
    #     csv_file_path = CSV_FILE_PATH,
    #     output_path = OUTPUT_PATH,
    #     folder_name_list_1 = FOLDER_NAME_LIST_1,
    #     folder_name_list_2 = FOLDER_NAME_LIST_2,
    #     folder_name_list_3 = FOLDER_NAME_LIST_3
    # )
    divide_csv_file(
        csv_file_path=CSV_FILE_PATH,
        output_path=OUTPUT_PATH,
        folder_name_list=[FOLDER_NAME_LIST_1, FOLDER_NAME_LIST_2, FOLDER_NAME_LIST_3]
    )


# ----- modules -----

def divide_csv_file(csv_file_path, output_path, folder_name_list):
    os.makedirs(output_path, exist_ok=True)
    output_files = {}
    for i, folder in enumerate(folder_name_list):
        output_files[f"splited_images_{i+1}.csv"] = folder
    # output_files = {
    #     "splited_images_1.csv": folder_name_list_1,
    #     "splited_images_2.csv": folder_name_list_2,
    #     "splited_images_3.csv": folder_name_list_3,
    # }
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