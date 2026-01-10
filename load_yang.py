import os

def load_yang_models(folder_path):
    yang_models = {}
    if not os.path.exists(folder_path):
        print(f"Warning: Folder {folder_path} not found.")
        return yang_models

    for filename in os.listdir(folder_path):
        if filename.endswith(".yang.txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                yang_models[filename] = f.read()
    return yang_models

# This ensures the code below ONLY runs if you run this file directly,
# not when you import it into prompt_test.py
if __name__ == "__main__":
    test_folder = "./yang_files"
    results = load_yang_models(test_folder)
    print(f"Loaded {len(results)} models.")

