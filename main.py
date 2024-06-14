import os
import tkinter as tk
from tkinter import filedialog

def check_folder(location, project_name):
    # Create project folder
    project_folder = os.path.join(location, project_name)
    if not os.path.exists(project_folder):
        os.makedirs(project_folder)
        print(f"Created project folder: {project_folder}")
    else:
        print(f"Project folder already exists: {project_folder}")

    # Create subfolders
    folders = ['folder1', 'folder2', 'folder3']
    for folder in folders:
        folder_path = os.path.join(project_folder, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {folder_path}")
        else:
            print(f"Folder already exists: {folder_path}")

def select_location():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    location = filedialog.askdirectory(title="Select the location where you want to place the folders")
    return location

if __name__ == "__main__":
    location = select_location()
    if location:
        project_name = input("Enter the project name: ")
        if project_name:
            check_folder(location, project_name)
        else:
            print("Project name cannot be empty.")
    else:
        print("Location selection cancelled.")
