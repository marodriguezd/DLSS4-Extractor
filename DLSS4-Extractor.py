import os
import shutil

def copy_bin_to_dll_on_desktop():
    # Folder where the bin file is located
    source_folder = r"C:\ProgramData\NVIDIA\NGX\models\dlss\versions\20316673\files"
    
    # List all items in that folder
    files = os.listdir(source_folder)
    
    # Assuming there is ONLY one file in the folder, we take it
    if len(files) != 1:
        print("ERROR: Expected exactly one file in the folder, but found:", len(files))
        return
    
    bin_file = files[0]  # The only file
    
    # Full path to the bin file
    source_path = os.path.join(source_folder, bin_file)
    
    # Build the path to the current user's Desktop
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    
    # Final name for the file on the Desktop
    destination = os.path.join(desktop, "nvngx_dlss.dll")
    
    # Copy (and rename) the file
    shutil.copy2(source_path, destination)
    
    print(f"Copied successfully:\n  Source:  {source_path}\n  Destination: {destination}")

if __name__ == "__main__":
    copy_bin_to_dll_on_desktop()
