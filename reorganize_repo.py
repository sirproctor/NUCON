import os
import shutil

# Define new structure
structure = {
    "docs": ["Constellation_Repo_Safe/constellation-emails/01_intro_manifesto.md",
             "Constellation_Repo_Safe/constellation-emails/08_signal_log.md"],
    "src": [],
    "assets": [],
}

# Create directories
def create_directories():
    for directory in structure.keys():
        if not os.path.exists(directory):
            os.makedirs(directory)

# Move files
def move_files():
    for folder, files in structure.items():
        for file_path in files:
            if os.path.exists(file_path):
                shutil.move(file_path, folder)
                print(f"Moved {file_path} to {folder}")

# Main function
if __name__ == "__main__":
    create_directories()
    move_files()
    print("Repository reorganization complete!")
