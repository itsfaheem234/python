import os
import shutil


folder = input("enter the folder path you want to organize: ").strip()

if not os.path.exists(folder):
    print("folder not found! ")
else:
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
        "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov"],
        "Music": [".mp3", ".wav", ".flac"],
        "Archives": [".zip", ".rar", ".7z"],
        "Programs": [".py", ".exe", ".msi"]
    }

    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)

        # skip folders
        if os.path.isdir(file_path):
            continue

        # get file extension
        extension = os.path.splitext(file)[1].lower()

        category = "Others"

        for folder_name, extensions in categories.items():
            if extension in extensions:
                category = folder_name
                break

        # create category folder if it doesn't exist
        category_path = os.path.join(folder, category)

        if not os.path.exists(category_path):
            os.makedirs(category_path)

        # move the file
        destination = os.path.join(category_path, file)

        try:
            shutil.move(file_path, destination)
            print(f"moved: {file} → {category}/")

        except shutil.Error:
            print(f"could not move {file}")

    print("\nfile organization complete! ")
