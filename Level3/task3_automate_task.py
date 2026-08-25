"""
Level 3 - Task 3: Automate a Task
A common, genuinely useful automation: organize files in a folder into
subfolders by file type (e.g. all .pdf files go into a "PDF" folder,
all .jpg files go into an "Images" folder, etc).

No extra libraries needed - uses only Python's built-in 'os' and 'shutil'.
"""

import os
import shutil

# Map file extensions to a folder name
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Spreadsheets": [".xlsx", ".csv"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"],
}

def get_category(extension):
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Other"


def organize_folder(folder_path):
    if not os.path.isdir(folder_path):
        print("That folder doesn't exist.")
        return

    moved_count = 0

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip subfolders, only organize actual files
        if os.path.isdir(file_path):
            continue

        _, extension = os.path.splitext(filename)
        category = get_category(extension)

        category_folder = os.path.join(folder_path, category)
        os.makedirs(category_folder, exist_ok=True)

        destination = os.path.join(category_folder, filename)
        shutil.move(file_path, destination)
        moved_count += 1
        print(f"Moved '{filename}' -> {category}/")

    print(f"\nDone! Organized {moved_count} file(s).")


if __name__ == "__main__":
    folder = input("Enter the full path of the folder to organize: ").strip()
    organize_folder(folder)
