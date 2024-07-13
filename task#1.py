import os
import shutil
import argparse

def sort_files_by_extension(src_dir, dest_dir):
    try:
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        for item in os.listdir(src_dir):
            src_path = os.path.join(src_dir, item)
            if os.path.isdir(src_path):
                new_dest_dir = os.path.join(dest_dir, item)
                sort_files_by_extension(src_path, new_dest_dir)
            else:
                file_ext = os.path.splitext(item)[1][1:]  # отримати розширення файлу
                new_dest_dir = os.path.join(dest_dir, file_ext)
                if not os.path.exists(new_dest_dir):
                    os.makedirs(new_dest_dir)
                shutil.copy2(src_path, new_dest_dir)
    except Exception as e:
        print(f"Помилка: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Рекурсивно сортувати файли за розширенням')
    parser.add_argument('src_dir', type=str, help='Шлях до вихідної директорії')
    parser.add_argument('dest_dir', type=str, nargs='?', default='dist', help='Шлях до директорії призначення')
    args = parser.parse_args()

    sort_files_by_extension(args.src_dir, args.dest_dir)
