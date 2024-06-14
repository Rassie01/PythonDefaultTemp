import os
import tkinter as tk
from tkinter import filedialog

def create_file(path, content=""):
    with open(path, 'w') as file:
        file.write(content)

def check_folder(location, project_name):
    # Create project folder
    project_folder = os.path.join(location, project_name)
    if not os.path.exists(project_folder):
        os.makedirs(project_folder)
        print(f"Created project folder: {project_folder}")
    else:
        print(f"Project folder already exists: {project_folder}")

    # Create subfolders and files
    subfolders = ['my_project']
    for subfolder in subfolders:
        folder_path = os.path.join(project_folder, subfolder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {folder_path}")
        else:
            print(f"Folder already exists: {folder_path}")

    # Create files in my_project/ subfolder
    create_file(os.path.join(project_folder, 'my_project', '__init__.py'))
    create_file(os.path.join(project_folder, 'my_project', 'main.py'), 'def main():\n    print("Hello, World!")\n\nif __name__ == "__main__":\n    main()')
    create_file(os.path.join(project_folder, 'my_project', 'module1.py'), 'def function1():\n    return "Function 1 result"')
    create_file(os.path.join(project_folder, 'my_project', 'module2.py'), 'def function2():\n    return "Function 2 result"')

    # Create top-level files
    create_file(os.path.join(project_folder, 'requirements.txt'))
    create_file(os.path.join(project_folder, 'setup.py'), 'from setuptools import setup, find_packages\n\nsetup(\n    name="my_project",\n    version="0.1",\n    packages=find_packages(),\n    install_requires=[\n        # List your project dependencies here\n    ],\n    entry_points={\n        \'console_scripts\': [\n            \'my_project = my_project.main:main\',\n        ],\n    },\n)')
    create_file(os.path.join(project_folder, 'README.md'), '# My Project\n\n## Installation\n\n```bash\npip install -r requirements.txt\n```\n\n## Usage\n\n```bash\npython -m my_project.main\n```\n')

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
