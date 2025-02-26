# DLSS4-Extractor
# Copy DLSS Bin to DLL

This is a simple Python script that automates the following tasks:

1. It locates the only file in the directory:
   ```
   C:\ProgramData\NVIDIA\NGX\models\dlss\versions\20316673\files
   ```
2. It copies that file to your Desktop.
3. It renames the copied file to `nvngx_dlss.dll`.

## Requirements

- Python 3.x installed on Windows.
- The directory `C:\ProgramData\NVIDIA\NGX\models\dlss\versions\20316673\files` must exist and contain exactly one file.

## Usage

1. **Clone or download** this repository.

2. Open a command prompt (or PowerShell) and navigate to the repository folder.

3. Run the script by executing:
   ```bash
   python DLSS4-Extractor.py
   ```
   The script will:
   - Check that there is exactly one file in the source directory.
   - Copy that file to your Desktop.
   - Rename the file to `nvngx_dlss.dll`.

4. **Verify** that the file appears on your Desktop.

## Notes

- Ensure you have the necessary permissions to read from `C:\ProgramData\NVIDIA\NGX\models\dlss\versions\20316673\files` and write to your Desktop.
- If the source directory contains more or less than one file, the script will exit with an error message.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.