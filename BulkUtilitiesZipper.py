import tkinter as tk
from tkinter import filedialog
import os
import shutil

folders_to_zip=[] # Where the folders to zip are saved

def select_folders_to_zip():
    select_folders_to_exist_text="Select a Directory to zip" # Set the initial prompt text
    select_more_folders = True
    while select_more_folders:
        folder_to_zip = filedialog.askdirectory(title=select_folders_to_exist_text)
        if folder_to_zip: # If a folder was selected, add it to the list and the user will be prompted again
            folders_to_zip.append(folder_to_zip)
            select_folders_to_exist_text="Select another Directory to zip or Cancel to finish" # Change the prompt text for subsequent selections
            print(f"Selected folder to zip: {folder_to_zip}")
        else: # If the user clicks to cancel, they are done selecting folders so break the loop
            select_more_folders = False
            print("Finished selecting folders.")

def create_zip(selected_folder):
    directory_to_save_zip = filedialog.askdirectory(title="Select a Directory to save the zip file")
    if directory_to_save_zip: # If a directory was selected to save to
        print(f"Directory to save zip: {directory_to_save_zip}")
        # Zip path is the save location + the name of the folder being zipped
        zip_path = os.path.join(directory_to_save_zip, os.path.basename(selected_folder))
        # Create the zip file
        zip_filename = shutil.make_archive(zip_path, 'zip', selected_folder)
        print(f"Created zip file: {zip_filename}")
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
