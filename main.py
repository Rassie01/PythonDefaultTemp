import os

def check_Folder():
    folders = ['folder1', 'folder2', 'folder3']  # Replace with your list of folder names
    
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Created folder: {folder}")
        else:
            print(f"Folder already exists: {folder}")

if __name__ == "__main__":
    check_Folder()
    pass