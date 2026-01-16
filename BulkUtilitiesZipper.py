import tkinter as tk
from tkinter import filedialog
import os
import zipfile

folders_to_zip=[] # Where the folders to zip are saved

def select_folders_to_zip():
    select_folders_to_exist_text="Select a Directory to zip" # Set the initial prompt text
    select_more_folders = True
    initial_dir = None
    while select_more_folders:
        folder_to_zip = filedialog.askdirectory(title=select_folders_to_exist_text, initialdir=initial_dir)
        if folder_to_zip: # If a folder was selected, add it to the list and the user will be prompted again
            folders_to_zip.append(folder_to_zip)

            # Prevents the select window from opening inside the last selected folder
            if initial_dir is None:
                initial_dir = os.path.dirname(folder_to_zip)

            select_folders_to_exist_text="Select another Directory to zip or Cancel to finish" # Change the prompt text for subsequent selections
            print(f"Selected folder to zip: {folder_to_zip}")

        else: # If the user clicks to cancel, they are done selecting folders so break the loop
            select_more_folders = False
            print("Finished selecting folders.")

def create_zip(selected_folder):
    directory_to_save_zip = filedialog.askdirectory(title=f"Select a Directory to save the zip file for '{os.path.basename(selected_folder)}'")
    if directory_to_save_zip: # If a directory was selected to save to
        print(f"Directory to save zip: {directory_to_save_zip}")
        # Zip path is the save location + the name of the folder being zipped
        zip_path = os.path.join(directory_to_save_zip, os.path.basename(selected_folder) + '.zip')
        
        #"with...as" is like saying zip_file=zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) 
        #but it automatically closes the file when done
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file: 
            for root, directories, files in os.walk(selected_folder):
                # Filter out directories starting with '.'
                directories[:] = [directory for directory in directories if not directory.startswith('.')]
                
                for file in files:
                    # Skip files starting with '.'
                    if not file.startswith('.'):
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, selected_folder) # Relative path for files within the zip
                        zip_file.write(file_path, arcname)
        
        print(f"Created zip file: {zip_path}")
    else:
        print("No directory to save to")



# START DOWN HERE
if __name__ == "__main__":
    select_folders_to_zip()

    if len(folders_to_zip) > 0: # Confirm there are folders to zip
        for folder in folders_to_zip: # For every folder that was selected to zip, create its zip
            create_zip(folder)
    else:
        print("No folders were selected to zip.")
